import sys
from Activity_pstructure.logging import logger

class ActivityException(Exception):
    def __init__(self, error_message, error_details):
        """
        Custom exception class for detailed error reporting.
        
        :param error_message: The error message to be displayed.
        :param error_details: A tuple returned by sys.exc_info(), containing (exc_type, exc_value, exc_tb).
        """
        self.error_message = error_message

        # Ensure error_details is unpacked correctly
        exc_type, exc_value, exc_tb = error_details
        self.lineno = exc_tb.tb_lineno if exc_tb else None
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"

    def __str__(self):
        return (f"Error occurred in python script: [{self.file_name}] "
                f"at line number [{self.lineno}] "
                f"with error message: [{self.error_message}]")

if __name__ == "__main__":
    try:
        # Example logging
        logger.logging.info("Starting the program")

        # Simulate an error (division by zero)
        a = 1 / 0
        print("This will not be printed", a)

    except Exception as e:
        # Raise custom exception with sys.exc_info() to pass traceback details
        raise ActivityException(str(e), sys.exc_info())
