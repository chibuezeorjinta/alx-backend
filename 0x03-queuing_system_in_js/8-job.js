function createPushNotificationsJobs(jobs, queue) {
	if (!Array.isArray(jobs)) {
		throw new Error('Jobs is not an array');
	}
	jobs.forEach((job) => {
		const mainjob = queue.create('push_notification_code_3', job).save((err) => {
			if (!err) console.log(`Notification job created: ${mainjob.id}`)
		});

		mainjob.on('complete', () => console.log(`Notification job ${mainjob.id} completed`));
		mainjob.on('failed', (err) => console.log(`Notification job ${mainjob.id} failed: ${err}`));
		mainjob.on('progress', (progress) => console.log(`Notification job ${mainjob.id} ${progress}% complete`));
	})
}

export default createPushNotificationsJobs;