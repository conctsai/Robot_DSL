import re

class StringOperation:
    @staticmethod
    def euqal_string(str1, str2):
        '''
        判断两个字符串是否相等
        :param str1: 字符串1
        :param str2: 字符串2
        :return: 是否相等
        '''
        return str1 == str2
    
    @staticmethod
    def regex_string(str1, str2):
        '''
        判断字符串是否匹配正则表达式
        :param str1: 字符串
        :param str2: 正则表达式
        :return: 是否匹配
        '''
        return re.fullmatch(str2, str1) is not None
    
    @staticmethod
    def greater_number(str1, str2):
        '''
        判断数字或字符串的大小，如果是字符串则按照字典序比较
        :param str1: 字符串1
        :param str2: 字符串2
        :return: 是否str1 > str2
        '''
        # 先判断是否为数字
        if not str1.isdigit() or not str2.isdigit():
            return str1 > str2
        return float(str1) > float(str2)
    
    @staticmethod
    def less_number(str1, str2):
        '''
        判断数字或字符串的大小，如果是字符串则按照字典序比较
        :param str1: 字符串1
        :param str2: 字符串2
        :return: 是否str1 < str2
        '''
        if not str1.isdigit() or not str2.isdigit():
            return str1 < str2
        return float(str1) < float(str2)
    
    @staticmethod
    def greater_equal_number(str1, str2):
        '''
        判断数字或字符串的大小，如果是字符串则按照字典序比较
        :param str1: 字符串1
        :param str2: 字符串2
        :return: 是否str1 >= str2
        '''
        if not str1.isdigit() or not str2.isdigit():
            return str1 >= str2
        return float(str1) >= float(str2)
    
    @staticmethod
    def less_equal_number(str1, str2):
        '''
        判断数字或字符串的大小，如果是字符串则按照字典序比较
        :param str1: 字符串1
        :param str2: 字符串2
        :return: 是否str1 <= str2
        '''
        if not str1.isdigit() or not str2.isdigit():
            return str1 <= str2
        return float(str1) <= float(str2)
    
    @staticmethod
    def not_equal_string(str1, str2):
        '''
        判断数字或字符串的大小，如果是字符串则按照字典序比较
        :param str1: 字符串1
        :param str2: 字符串2
        :return: 是否str1 <> str2
        '''
        if not str1.isdigit() or not str2.isdigit():
            return str1 != str2
        return float(str1) != float(str2)