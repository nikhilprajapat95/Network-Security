import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            self.client = pymongo.MongoClient(MONGO_DB_URL)
            logging.info("MongoDB client created successfully.")
        except Exception as e:
            logging.error(f"Failed to create MongoDB client: {e}")
            raise NetworkSecurityException(e, sys)

    def get_data_as_dataframe(self, database_name: str, collection_name: str) -> pd.DataFrame:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def cv_to_json(self, file_path: str) -> str:
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = json.loads(data.T.to_json()).values()
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self,records ,database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == "__main__":
    FILE_PATH = "Network Security/Network_Data/networkData.csv"
    DATABASE = "Network_Security"
    COLLECTION = "Network_Data"
    networkobj=NetworkDataExtract()
    records = networkobj.csv_to_json(file_path=FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records=records, database=DATABASE, collection=COLLECTION)
    print(no_of_records)