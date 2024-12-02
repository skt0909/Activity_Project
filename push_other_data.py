import os, sys
import json
import pandas as pd
import pymongo
from Activity_pstructure.exception.exception import ActivityException
from Activity_pstructure.logging.logger import logging


from dotenv import load_dotenv
load_dotenv()

# MongoDB connection 
MONGO_DB_URL = os.getenv('MONGO_DB_URL')

class DummyDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise ActivityException(e, sys)
        
    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise ActivityException(e, sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            # Connect to MongoDB
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]  # Access the database
            self.collection = self.database[self.collection]  # Access the collection

            # Insert records into MongoDB
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise ActivityException(e, sys)

# Main program to load dummy data and insert it into MongoDB
if __name__ == '__main__':
    FILE_PATH = "D:\ActivityP\Activity_Dummy_Data\Activity_Dummy_data\Activity_D_Data.csv"  # Ensure this is a valid CSV file
    DATABASE = "DDB"  # New database name
    COLLECTION = "DummyData"  # New collection name
    activity_obj = DummyDataExtract()

    try:
        # Convert CSV to JSON records
        records = activity_obj.csv_to_json_convertor(file_path=FILE_PATH)
        print(f"Records: {records}")  # Debugging step to see what records look like

        # Insert records into MongoDB
        no_of_records = activity_obj.insert_data_mongodb(records, DATABASE, COLLECTION)
        print(f"Number of records inserted: {no_of_records}")

    except ActivityException as e:
        logging.error(f"Error occurred: {str(e)}")
        print(f"Error occurred: {str(e)}")
