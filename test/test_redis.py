import unittest
import redis
import os
import time
from dotenv import load_dotenv

class TestRedis(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.redis = redis.Redis(
            host=os.getenv("REDIS_HOST"), 
            port=os.getenv("REDIS_PORT"), 
            db=os.getenv("REDIS_DB"), 
            password=os.getenv('REDIS_PASSWORD'))
        self.redis.flushdb()

    def tearDown(self):
        self.redis.flushdb()

    def test_redis_connection(self):
        print("\n--- Testing the Redis Connection ---")
        self.assertIsNotNone(self.redis)

    def test_redis_set(self):
        print("\n--- Testing the Redis Set ---")
        self.redis.set('key', 'value')
        self.assertEqual(self.redis.get('key').decode('utf-8'), 'value')

    def test_redis_expire(self):
        print("\n--- Testing the Redis Expire ---")
        self.redis.set('key', 'value', ex=1)
        time.sleep(2)
        self.assertIsNone(self.redis.get('key'))

    def test_redis_delete(self):
        print("\n--- Testing the Redis Delete ---")
        self.redis.set('key', 'value')
        self.redis.delete('key')

if __name__ == '__main__':
    unittest.main()