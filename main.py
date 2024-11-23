from Activity_pstructure.components.data_injestion import DataIngestion
from Activity_pstructure.components.data_validation import DataValidation
from Activity_pstructure.exception.exception import ActivityException
from Activity_pstructure.logging.logger import logging
from Activity_pstructure.entity.config_entity import DataIngestionConfig, DataValidationConfig
from Activity_pstructure.entity.config_entity import TrainingPipelineConfig
from Activity_pstructure.components.data_transformation import DataTransformation, DataTransformationConfig
import sys

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion= DataIngestion(dataingestionconfig)
        logging.info("Initiate Data Ingestion")

        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")

        print(data_ingestion_artifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(data_ingestion_artifact,data_validation_config)
        logging.info("Initiate Data Ingestion")

        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(" data_validation_artifact")

        train_data_path = data_ingestion_artifact.train_file_path
        test_data_path = data_ingestion_artifact.test_file_path

        data_transformation = DataTransformation()
        data_transformation_artifact = data_transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )
        logging.info("Data Transformation Completed")
    except Exception as e:
        raise ActivityException(e,sys)