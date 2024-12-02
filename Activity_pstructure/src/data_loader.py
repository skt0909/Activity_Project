from Activity_pstructure.exception.exception import ActivityException
import sys
import pymongo
from dotenv import load_dotenv
import os

def fetch_data_from_mongo():
    try:
        load_dotenv()  # Load environment variables from .env
        MONGO_DB_URL = os.getenv('MONGO_DB_URL')  # MongoDB URL from .env file
        
        # Connect to MongoDB
        mongo_client = pymongo.MongoClient(MONGO_DB_URL)
        dummy_collection = mongo_client['DDB']['DummyData']

        documents = list(dummy_collection.find().limit(1)) 

        return documents
    
        
    except Exception as e:
        raise ActivityException(str(e), sys.exc_info())  