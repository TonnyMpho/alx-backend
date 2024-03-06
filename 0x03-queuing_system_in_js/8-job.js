//10. Writing the job creation function

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const notificationJob = queue.create('push_notification_code_3', jobData);

    notificationJob.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${notificationJob.id}`);
      }
    });

    notificationJob.on('complete', () => {
      console.log(`Notification job ${notificationJob.id} completed`);
    });

    notificationJob.on('failed', (err) => {
      console.log(`Notification job ${notificationJob.id} failed: ${err}`);
    });

    notificationJob.on('progress', (progress) => {
      console.log(`Notification job ${notificationJob.id} ${progress}% complete`);
    });
  });
}

module.exports = createPushNotificationsJobs;
