import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

const asyncGet = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const value = await asyncGet(schoolName);
    console.log(value)
  } catch (err) {
    console.log(err)
  }
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
