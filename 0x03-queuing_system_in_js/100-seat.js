import redis from 'redis'
import { promisify } from 'util';
import express from 'express';

const client = redis.createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err.message));
client.on('connect', () => console.log(`Redis client connected to the server`))
const redisGet = promisify(client.get);

const KEY = 'available_seats';

function reserveSeat(number) {
	client.set(KEY, number, redis.print);
}

async function getCurrentAvailableSeats(KEY) {
	const availSeats = await redisGet(KEY);
	return availSeats;
}

let reservationEnabled = true;

const queue = require('kue').createQueue;

// express ======================================
const app = new express();
const port = 1245;

app.listen(port, () => {
	console.log(`app listening at http://localhost:${port}`);
});

reserveSeat(50);

app.get('/available_seats', async (req, res) => {
	const seatNum = await getCurrentAvailableSeats(KEY);
	return res.json({"numberOfAvailableSeats": seatNum});
});

app.get('/reserve_seat', async (req, res) => {
	if (reservationEnabled === false) {
		return res.json({ "status": "Reservation are blocked" });
	} else {
		const newjob = queue.create('reserve_seat').save((err) => {
			if (!err) {
				return res.json({ "status": "Reservation in process" });
			}else {
				return res.json({ "status": "Reservation failed" });
			}
		});

		newjob.on('complete', () => console.log(`Seat reservation job ${newjob.id} completed`));
		newjob.on('failed', (err) => console.log(`Seat reservation job ${newjob.id} failed: ${err}`))
	}
});

app.get('/process', async (req, res) => {
	queue.process('reserve_seat', done, async (job, done) => {
		let currentfree = await getCurrentAvailableSeats(KEY);
		currentfree = Number(currentfree) - 1;
		if (currentfree >= 0) {
			if (currentfree === 0) {
				reservationEnabled = false;
			}
			reserveSeat(currentfree);
			return done();
		}else {
			return done(new Error('Not enough seats available'))
		}
	}).then(() => res.json({ "status": "Queue processing" }));
})
