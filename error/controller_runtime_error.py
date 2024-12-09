class ControllerRuntimeError(Exception):
    def __init__(self, message, type):
        self.message = message
        self.type = type
        super().__init__(message)
        
class SessionNotFoundError(ControllerRuntimeError):
    def __init__(self, message):
        super().__init__(message, "SessionNotFoundError")
        
class ConfNotFoundError(ControllerRuntimeError):
    def __init__(self, message):
        super().__init__(message, "ConfNotFoundError")