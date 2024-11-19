import os
import json
import sys
import pandas as pd
import numpy as np


"Constant variable for training pipeline" 
TARGET_COLUMN = "calories" 
PIPELINE_NAME: str = "Activity_pipeline" 
ARTIFACT_DIR: str = "Artifacts" 
FILE_NAME: str = "ActivityData.csv" 

TRAIN_FILE_NAME: str = "train.csv" 
TEST_FILE_NAME: str = "test.csv"


"Data Ingestion VAR NAME"

DATA_INGESTION_COLLECTION_NAME: str = "ActivityData" 
DATA_INGESTION_DATABASE_NAME: str = "SDB" 
DATA_INGESTION_DIR_NAME: str = "data_ingestion" 
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store" 
DATA_INGESTION_INGESTED_DIR: str = "ingested" 
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

"Data Vaildation VAR NAME"

DATA_VALIDATION_DIR_NAME: str = "data_validation" 
DATA_VALIDATION_VALID_DIR: str = "validated" 
DATA_VALIDATION_INVALID_DIR: str = "invalid" 
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report" 
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report. yam1"

SCHEMA_FILE_PATH =os.path.join("Data_schema", "schema.yaml")