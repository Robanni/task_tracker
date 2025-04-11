import redis

from settings import Settings 


settings = Settings()

def get_redis_connection()->redis.Redis:
    return redis.Redis(
        host=settings.REDIS_HOST, 
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD
        )

def set_tracker_count():
    redis = get_redis_connection()
    redis.set("tracker_count",1)