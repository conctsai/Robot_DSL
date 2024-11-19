import re

class StringOperation:
    @staticmethod
    def euqal_string(str1, str2):
        return str1 == str2
    
    @staticmethod
    def regex_string(str1, str2):
        return re.fullmatch(str2, str1) is not None