// Connect to redis in node
import redis from 'redis'

const client = redis.createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err.message));
client.on('connect', () => console.log(`Redis client connected to the server`))

// Publish from server

const CHANNEL = 'holberton school channel';

function publishMessage(message, time) {
	setTimeout(async () => {
		console.log(`About to send ${message}`)
		await client.publish(CHANNEL, message)
	}, time)
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);