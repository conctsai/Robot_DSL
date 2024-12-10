class DSLRuntimeError(Exception): # 执行引擎运行时错误
    def __init__(self, message, type):
        self.message = message
        self.type = type
        super().__init__(message)
        
class VariableNotDefinedError(DSLRuntimeError): # 变量未定义错误
    def __init__(self, message): 
        super().__init__(message, "VariableNotDefinedError")
        
class NoStateDefinedError(DSLRuntimeError): # 未定义状态错误
    def __init__(self, message):
        super().__init__(message, "NoStateDefinedError")
        
class NoInitialStateError(DSLRuntimeError): # 未定义初始状态错误
    def __init__(self, message):
        super().__init__(message, "NoInitialStateError")
        
class NoStateMatchedError(DSLRuntimeError): # 未匹配状态错误
    def __init__(self, message):
        super().__init__(message, "NoStateMatchedError")