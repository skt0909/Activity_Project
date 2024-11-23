from Activity_pstructure.exception.exception import ActivityException
from Activity_pstructure.logging.logger import logging
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from Activity_pstructure.logging.logger import logging
from Activity_pstructure.exception.exception import ActivityException
from Activity_pstructure.logging.logger import logging
from sklearn.compose import ColumnTransformer
from Activity_pstructure.entity.artifact_entity import DataTransformationConfig
from Activity_pstructure.utils.main_utils.utils import save_object
from sklearn.preprocessing import StandardScaler
import os,sys
import numpy as np 
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

class DataTransformation:
    try:
        def __init__(self):
            self.data_transformation_config=DataTransformationConfig()
    
        def get_data_transformer_object(self):
            # Define numerical pipeline
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),  # Fill missing numerical values with median
                    ("scaler", StandardScaler())  # Scale numerical values
                ]
            )
            logging.info("Numerical pipeline created: Imputation and scaling")

            # Combine the numerical pipeline in a ColumnTransformer
            preprocessor = ColumnTransformer(
                [
                ("num_pipeline", num_pipeline)  # Apply numerical pipeline to numerical columns
                ]
            )
            logging.info("Preprocessor object created with ColumnTransformer for numerical features")

            return preprocessor
    except Exception as e:
            raise ActivityException(e, sys)
    
    def initiate_data_transformation(self, train_file_path, test_file_path):
        try:
            # Read train and test data
            train_df = pd.read_csv(train_file_path)
            test_df = pd.read_csv(test_file_path)
            logging.info("Read train and test completed")

            # Obtain preprocessing object
            logging.info("Obtaining preprocessing object")
            target_column_name = "calories"
        
            # Separate input and target features
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]
            logging.info("Applying preprocessing object")
        
            # Preprocessing object (StandardScaler example)
            preprocessing_obj = StandardScaler()
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # Combine processed input features with target features
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info("Saved preprocessing object")
            
            # Save the preprocessing object
            save_object(
            file_path=self.data_transformation_config.preprocessor_obj_file_path,
            obj=preprocessing_obj
            )
        
            # Return as a dictionary,
            return {
                "train_arr": train_arr,
                "test_arr": test_arr,
                "preprocessor_obj_file_path": self.data_transformation_config.preprocessor_obj_file_path
            }

        except Exception as e:
            raise ActivityException(e, sys)
    
    '''
    def initiate_data_transformation(self,train_file_path,test_file_path):
            try:
                 train_df=pd.read_csv(train_file_path)
                 test_df=pd.read_csv(test_file_path)
                 logging.info("Read train,test completed")
                 logging.info("Obtaining preprossing object")

                 preprocessing_obj=self.get_data_transformer_object
                 target_column_name="calories"
            
                 input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
                 target_feature_train_df=train_df[target_column_name]

                 input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
                 target_feature_test_df=test_df[target_column_name]
                 logging.info( f"Applying preprocessing Object")

                 preprocessing_obj = StandardScaler()
                 input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
                 input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

                 train_arr = np.c_[
                     input_feature_train_arr,np.array(target_feature_train_df)
                 ]
                 test_arr = np.c_[
                     input_feature_test_arr,np.array(target_feature_test_df)
                 ]
                 logging.info("Saved preprocessing object")

                 save_object(
                      file_path=self.data_transformation_config.preprocessor_obj_file_path,
                      obj=preprocessing_obj
                 )
                 return{
                      train_arr,
                      test_arr,
                      self.data_transformation_config.preprocessor_obj_file_path
                 }
            except Exception as e:
                raise ActivityException(e,sys)
       '''         
            
