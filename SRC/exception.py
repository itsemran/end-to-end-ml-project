import sys 
import logging
#this module provides access to some variables used or maintained by the 
#interpreter and provides functions
#that interact with the Python runtime environment.

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    #it gives us details about error where it occured in which file
    file_name= exc_tb.tb_frame.f_code.co_filename
    error_message="error ocurred in python script name [{0}] line number [{1}] error message[{2}]".format( 
     file_name,exc_tb.tb_lineno,str(error))   
    
    return error_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        # as we are inheriting it from Exception class so for initializing or inherting init 
        self.error_message= error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

#TO CHECK USE

#if __name__=="__main__":
    
#    try:
#        a=1/0
#    except Exception as e:
#        logging.info("Division by Zero")
#        raise CustomException(e, sys )

