# mongo_db_client.py (MongoDB Client Setup)
import sys
import pymongo  # type: ignore
import certifi
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.constants import DATABASE_NAME, MONGODB_URL  # Import necessary constants

# Define MongoDB client with SSL certificate verification
ca = certifi.where()

class MongoDBClient:
    """
    MongoDBClient is used to establish a connection to the MongoDB database and access the specified database.

    On Failure: raises a USvisaException.
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            # Initialize MongoDB client only once
            if MongoDBClient.client is None:
                if MONGODB_URL is None:
                    raise Exception("MONGODB_URL environment variable is not set.")
                MongoDBClient.client = pymongo.MongoClient(MONGODB_URL, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise USvisaException(e, sys)
