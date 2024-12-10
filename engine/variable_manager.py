from error.dsl_runtime_error import VariableNotDefinedError
from typing import Mapping

class VariableManager:
    def __init__(self):
        self.variables: Mapping[str, str] = {}
        
    def set(self, key: str, value: str):
        '''
        设置变量
        :param key: 变量名
        :param value: 变量值
        '''
        self.variables[key] = value
        
    def get(self, key: str) -> str:
        '''
        获取变量，如果变量不存在则抛出异常
        :param key: 变量名
        :return: 变量值
        '''
        if key in self.variables:
            return self.variables[key]
        else:
            raise VariableNotDefinedError("Variable {} not defined".format(key))
        
    def format_placeholders(self, string: str):
        '''
        格式化字符串中的占位符，如果变量不存在则抛出异常
        :param string: 字符串
        :return: 格式化后的字符串
        '''
        try:
            return string.format(**self.variables)
        except KeyError as e:
            raise VariableNotDefinedError("Variable {} not defined".format(str(e)))
        except Exception as e:
            raise e
    
    def __str__(self):
        return str(self.variables)
    