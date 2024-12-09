import re

class StringOperation:
    @staticmethod
    def euqal_string(str1, str2):
        return str1 == str2
    
    @staticmethod
    def regex_string(str1, str2):
        return re.fullmatch(str2, str1) is not None
    
    @staticmethod
    def greater_number(str1, str2):
        return float(str1) > float(str2)
    
    @staticmethod
    def less_number(str1, str2):
        return float(str1) < float(str2)
    
    @staticmethod
    def greater_equal_number(str1, str2):
        return float(str1) >= float(str2)
    
    @staticmethod
    def less_equal_number(str1, str2):
        return float(str1) <= float(str2)
    
    @staticmethod
    def not_equal_string(str1, str2):
        return str1 != str2