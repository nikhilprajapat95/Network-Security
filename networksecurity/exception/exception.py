import sys

# Custom Exception Class
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        """
        :param error_message: error message in string format
        :param error_details: helper sys module to extract traceback
        """
        # Call the base class constructor
        super().__init__(error_message)
        
        # Get the traceback object
        _, _, exc_tb = error_details.exc_info()
        
        # Safety check: ensure traceback exists before accessing attributes
        if exc_tb is not None:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = "Unknown"
            self.file_name = "Unknown"
            
        self.error_message = error_message

    def __str__(self):
        return f"Error occurred in Python script: [{self.file_name}] at line: [{self.lineno}] error message: [{str(self.error_message)}]"

# Testing the implementation
if __name__ == "__main__":
    try:
        # Simulating an error (Division by Zero)
        a = 1 / 0
    except Exception as e:
        # Raising our custom exception
        raise NetworkSecurityException(e, sys)