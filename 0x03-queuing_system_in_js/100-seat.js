import express from 'express';
import kue from 'kue';
import { promisify } from 'util';
import Redic from 'redic';

const app = express();
const port = 1245;

const redisClient = new Redic();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

const initialNumberOfSeats = 50;
await setAsync('available_seats', initialNumberOfSeats);

let reservationEnabled = true;

const queue = kue.createQueue();

async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  return await getAsync('available_seats');
}

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat');

  job.save(async (err) => {
    if (!err) {
      res.json({ status: 'Reservation in process' });
    } else {
      res.json({ status: 'Reservation failed' });
    }
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();
    const newSeats = currentSeats - 1;

    await reserveSeat(newSeats);

    if (newSeats === 0) {
      reservationEnabled = false;
    }

    if (newSeats >= 0) {
      done();
      console.log(`Seat reservation job ${job.id} completed`);
    } else {
      done(new Error('Not enough seats available'));
      console.log(`Seat reservation job ${job.id} failed: Not enough seats available`);
    }
  });
});

app.listen(port)
