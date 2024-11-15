import os 
import json
import sys
import certifi

import pandas as pd
import numpy as np
import pymongo
from Activity_pstructure.exception.exception import ActivityException
from Activity_pstructure.logging.logger import logging

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

##Certifi
ca = certifi.where() 

class ActivityDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise ActivityException(e,sys)

    def cv_to_json_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values()) ##Tranpose Dataset to A:1,B:2 format 
            return records
            pass
        except Exception as e:
            raise ActivityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            self.database =  self.mongo_client[self.database]
            self.collection =  self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise ActivityException(e,sys)

if __name__=='__main__':
    FILE_PATH = "Activity_Data\ActivityData.csv"
    DATABASE="SDB"
    Collection="ActivityData"
    activityobj=ActivityDataExtract()
    records=activityobj.cv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records = activityobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)