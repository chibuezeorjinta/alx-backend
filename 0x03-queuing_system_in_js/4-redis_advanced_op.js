// Connect to redis in node
import redis from 'redis'


const client = redis.createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err.message));
client.on('connect', () => console.log(`Redis client connected to the server`))

// // task 2
// const setNewSchool = async (schoolName, value) => {
// 	await client.set(schoolName, value, redis.print)
// }


// const redisGet = promisify(client.get());

// const displaySchoolValue = async (schoolName) => {
// 	await redisGet(schoolName).then((res) => console.log(res))
// }

// displaySchoolValue('Holberton');
// setNewSchool('HolbertonSanFransico', '100');
// displaySchoolValue('HolbertonSanFransico');

// task 4
const hashkey = 'HolbertonSchools';
const hashstuff = async (hashkey) => {
	const fieldList = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris']
	const valueList = [50, 80,20,20,40,2]

	for (let i = 0; i < fieldList.length; i++) {
		await client.hset(hashkey, fieldList[i], valueList[i], redis.print)
	}

	await client.hgetall(hashkey, (_, res) => console.log(res))
}

hashstuff(hashkey)
