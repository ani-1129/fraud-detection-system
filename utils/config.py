"""
Configuration Management for Fraud Detection System
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Database and Application Configuration"""
    
    # PostgreSQL Configuration
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'fraud_detection')
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'your_password')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
    
    # Redis Configuration
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))
    
    # Application Configuration
    APP_NAME = os.getenv('APP_NAME', 'Fraud Detection System')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    
    # Database Connection String
    @property
    def database_url(self):
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

# Create global config instance
config = Config()
