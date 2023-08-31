// Connect to redis in node
import redis from 'redis'

const client = redis.createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err.message));
client.on('connect', () => console.log(`Redis client connected to the server`))

// Subscribe to a channel

const CHANNEL = 'holberton school channel';

client.subscribe(CHANNEL);

client.on('message', (channel, message) => {
  if (channel === CHANNEL) console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe(CHANNEL);
    client.quit();
  }
});
