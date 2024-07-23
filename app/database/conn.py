import logging
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

from app.conf.config import Config

load_dotenv()

db_client : AsyncIOMotorClient = None

async def get_db() ->AsyncIOMotorClient:
    db_name = Config.app_settings.get("db_name")
    return db_client[db_name]

async def connect_to_db():
    global db_client
    try:
        db_client = AsyncIOMotorClient(
            Config.app_settings.get("mongodb_url"),
            username = Config.app_settings.get("db_username"),
            password = Config.app_settings.get("db_password")
        )
        logging.info('Connected to mongo.')
    except Exception as e:
        logging.exception(f'Could not connect to mongo: {e}')
        raise

async def close_db_connection():
    global db_client
    if db_client is None:
        logging.warning('Connection is None, nothing to close.')
        return
    db_client.close()
    db_client = None
    logging.info('Connection closed')

    


