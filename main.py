from Activity_pstructure.components.data_injestion import DataIngestion
from Activity_pstructure.components.data_validation import DataValidation
from Activity_pstructure.exception.exception import ActivityException
from Activity_pstructure.logging.logger import logging
from Activity_pstructure.entity.config_entity import DataIngestionConfig, DataValidationConfig
from Activity_pstructure.entity.config_entity import TrainingPipelineConfig
from Activity_pstructure.components.data_transformation import DataTransformation, DataTransformationConfig
from Activity_pstructure.components.model_trainer import ModelTrainer, ModelTrainerConfig
import sys
"""
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
        
        
        train_arr,test_arr=data_transformation_artifact = data_transformation.initiate_data_transformation(
            train_data_path, test_data_path
        }
      
        logging.info("Data Transformation Completed")

        modeltrainer=ModelTrainer()
        print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
        

    except Exception as e:
        raise ActivityException(e,sys)
"""
if __name__ == "__main__":
    try:
        # Setup configurations and objects
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate Data Ingestion")

        # Start Data Ingestion process
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")

        print(data_ingestion_artifact)

        # Data Validation Process
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)
        logging.info("Initiate Data Validation")

        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)

        # Get train and test data paths
        train_data_path = data_ingestion_artifact.train_file_path
        test_data_path = data_ingestion_artifact.test_file_path

        # Data Transformation Process
        data_transformation = DataTransformation()
        data_transformation_artifact = data_transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )

        # Access train_arr and test_arr from the returned dictionary
        train_arr = data_transformation_artifact["train_arr"]
        test_arr = data_transformation_artifact["test_arr"]

        logging.info("Data Transformation Completed")

        # Model Training Process
        modeltrainer = ModelTrainer()
        print(modeltrainer.initiate_model_trainer(train_arr, test_arr))

    except Exception as e:
        raise ActivityException(e, sys)
