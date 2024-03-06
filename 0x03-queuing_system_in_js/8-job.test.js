import { assert } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue({ redis: { createClientFactory: () => kue.redis.createClient() }, testMode: true });
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    const invalidJobs = 'notAnArray';
    assert.throws(() => createPushNotificationsJobs(invalidJobs, queue), 'Jobs is not an array');
  });

  it('should create Kue jobs for each job in the array', () => {
    const jobs = [
      {
        phoneNumber: '1234567890',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '9876543210',
        message: 'This is the code 5678 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    assert.equal(queue.testMode.jobs.length, jobs.length);

    assert.equal(queue.testMode.jobs[0].type, 'push_notification_code_3');
    assert.equal(queue.testMode.jobs[1].type, 'push_notification_code_3');
  });

});
