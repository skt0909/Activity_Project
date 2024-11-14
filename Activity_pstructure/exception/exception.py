import sys
from Activity_pstructure.logging import logger
class ActivityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message  # Initialize the exception with error, message, and details
        _,_,exc_tb = error_details.exc_info()

        # Store the line number and file name where the exception occurred
        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return  "Error occurred in Python script name [{0}] at line number [{1}] error message [{2}]".format(self.file_name, self.line_number,str(self.error_message))
    
# Example usage
    """
try:
    raise ValueError("This is a test error")
except ValueError as e:
    exception = ActivityException(str(e), sys)
    print(exception)

    """