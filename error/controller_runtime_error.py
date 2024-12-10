class ControllerRuntimeError(Exception): # 控制器运行时错误
    def __init__(self, message, type):
        self.message = message
        self.type = type
        super().__init__(message)
        
class SessionNotFoundError(ControllerRuntimeError): # 会话未找到错误
    def __init__(self, message):
        super().__init__(message, "SessionNotFoundError")
        
class ConfNotFoundError(ControllerRuntimeError): # 配置未找到错误
    def __init__(self, message):
        super().__init__(message, "ConfNotFoundError")