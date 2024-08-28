import { createClient } from 'redis';

createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

/* createClient()
  .on('error', (err) => console.log(`Redis client not connected to server: ${err.message}`))
  .on('connect', () => console.log('Redis client connected to the server')); */
