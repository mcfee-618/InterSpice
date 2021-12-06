import redis
from InterSpice.settings import REDIS_CONFIG

redis_pool = redis.ConnectionPool(**REDIS_CONFIG)


def get_redis_connection():
    redis_conn = redis.Redis(connection_pool=redis_pool)
    return redis_conn