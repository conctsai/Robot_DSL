class RunningEngineError(Exception): # 运行引擎错误
    def __init__(self, message, type):
        self.message = message
        self.type = type
        super().__init__(message)
        
class HistoryOutputNotMatchedError(RunningEngineError): # 历史输出不匹配错误
    def __init__(self, message):
        super().__init__(message, "HistoryOutputNotMatchedError")
        
class NoInputError(RunningEngineError): # 无输入错误
    def __init__(self, message):
        super().__init__(message, "NoInputError")
    