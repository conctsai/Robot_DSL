class ParseError(Exception): # 解析错误
    def __init__(self, message):
        self.message = message
        super().__init__(message)