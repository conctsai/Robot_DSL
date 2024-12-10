class RunningEngineError(Exception):
    def __init__(self, message, type):
        self.message = message
        self.type = type
        super().__init__(message)
        
class HistoryOutputNotMatchedError(RunningEngineError):
    def __init__(self, message):
        super().__init__(message, "HistoryOutputNotMatchedError")
        
class NoInputError(RunningEngineError):
    def __init__(self, message):
        super().__init__(message, "NoInputError")
    