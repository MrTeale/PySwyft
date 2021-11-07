"""Exceptions"""

class PySwyftError(Exception):
    """Generic Error Class
        
    In case of HTTP response codes >= 400 this class can be used
    to raise an exception representing that error.
    """
    def __init__(self, code, message):
        self.code = code
        self.message = message

        super(PySwyftError, self).__init__(message)