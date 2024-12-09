class DSLRuntimeError(Exception):
    def __init__(self, message, type):
        self.message = message
        self.type = type
        super().__init__(message)
        
class VariableNotDefinedError(DSLRuntimeError):
    def __init__(self, message):
        super().__init__(message, "VariableNotDefinedError")
        
class NoStateDefinedError(DSLRuntimeError):
    def __init__(self, message):
        super().__init__(message, "NoStateDefinedError")
        
class NoInitialStateError(DSLRuntimeError):
    def __init__(self, message):
        super().__init__(message, "NoInitialStateError")
        
class NoStateMatchedError(DSLRuntimeError):
    def __init__(self, message):
        super().__init__(message, "NoStateMatchedError")
        
