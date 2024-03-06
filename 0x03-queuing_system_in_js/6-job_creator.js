import { createQueue } from 'kue';

const queue = createQueue();

const jobData = {
  phoneNumber: 572117434,
  message: 'kue Notificatin',
};

const job = queue.create('push_notification_code', jobData);

job.save((err) => {
  if(!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});
job.on('failed', () => {
  console.log('Notification job failed');
});
