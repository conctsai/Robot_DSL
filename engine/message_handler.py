# 发送消息的类
class MessageHandler():
    def __init__(self):
        pass
    
    def send(self, message):
        print(message)
        
    def recv(self) -> str:
        return input()