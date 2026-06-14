"""
Retry Logic with Tenacity for Database/API Calls
"""
from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed,
    retry_if_exception_type
)
import psycopg2
from psycopg2 import OperationalError
import redis
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Retry decorator for database connections
@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2),
    retry=retry_if_exception_type((OperationalError, psycopg2.DatabaseError))
)
def connect_to_database():
    """Connect to PostgreSQL with retry logic"""
    from config import config
    
    try:
        connection = psycopg2.connect(
            host=config.POSTGRES_HOST,
            port=config.POSTGRES_PORT,
            database=config.POSTGRES_DB,
            user=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD
        )
        logger.info("✓ Successfully connected to PostgreSQL")
        return connection
    except Exception as e:
        logger.error(f"✗ Database connection failed: {e}")
        raise e

# Retry decorator for Redis connections
@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2),
    retry=retry_if_exception_type(redis.RedisError)
)
def connect_to_redis():
    """Connect to Redis with retry logic"""
    from config import config
    
    try:
        client = redis.Redis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            decode_responses=True
        )
        client.ping()
        logger.info("✓ Successfully connected to Redis")
        return client
    except Exception as e:
        logger.error(f"✗ Redis connection failed: {e}")
        raise e
