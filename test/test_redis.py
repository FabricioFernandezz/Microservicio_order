import unittest
import redis

class TestRedis(unittest.TestCase):
    def setUp(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0, password='9697')

    def test_redis_set_get(self):
        self.redis.set('key', 'value')
        value = self.redis.get('key')
        self.assertEqual(value, b'value')

if __name__ == '__main__':
    unittest.main()