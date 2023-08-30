// Connect to redis in node
import redis from 'redis'

const client = redis.createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err.message));
client.on('connect', () => console.log(`Redis client connected to the server`))

// task 1
const setNewSchool = async (schoolName, value) => {
	await client.set(schoolName, value, redis.print)
}

const displaySchoolValue = async (schoolName) => {
	await client.get(schoolName, (err, res) => console.log(res))
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFransico', '100');
displaySchoolValue('HolbertonSanFransico');