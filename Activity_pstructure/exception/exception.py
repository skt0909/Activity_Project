import sys
from Activity_pstructure.logging import logger

class ActivityException(Exception):
    def __init__(self, error_message, error_details):
        # error_details should be the result of sys.exc_info()
        self.error_message = error_message
        
        # Extract traceback details
        exc_type, exc_value, exc_tb = error_details
        
        # Get the line number where the exception occurred
        self.lineno = exc_tb.tb_lineno
        
        # Get the file name where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        # Return a string with the details about the exception
        return f"Error occurred in python script name [{self.file_name}] line number [{self.lineno}] error message [{str(self.error_message)}]"

if __name__ == '__main__':
    try:
        # Example logging
        logger.logging.info("Starting the program")
        
        # Simulate an error (division by zero)
        a = 1 / 0
        print("This will not be printed", a)
    
    except Exception as e:
        # Raise custom exception with sys.exc_info() to pass traceback details
        raise ActivityException(str(e), sys.exc_info())
