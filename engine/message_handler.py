from typing import Union, List
from error.running_engine_error import HistoryOutputNotMatchedError

# 发送消息的类
class MessageHandler():
    '''
    用于处理消息的类
    '''
    def __init__(self):
        self.history_input = []
        self.history_input_index = 0
        self.history_output = []
        self.output = []
    
    def server_send(self, message):
        '''
        服务端发送消息
        :param message: 消息
        '''
        self.output.append(message)
        
    def server_recv(self) -> Union[str, None]:
        '''
        服务端接收消息
        :param message: 消息
        :return: 消息
        '''
        if self.history_input_index >= len(self.history_input):
            return None
        else:
            self.history_input_index += 1
            return self.history_input[self.history_input_index - 1]
        
    def reset(self):
        '''
        重置状态
        '''
        self.history_input_index = 0
        self.history_output = self.output
        self.output = []
        
    def client_send(self, message):
        '''
        客户端发送消息
        :param message: 消息
        '''
        self.history_input.append(message)
        
    def client_recv(self) -> List[str]:
        '''
        客户端接收消息
        :return: 消息
        '''
        # 先匹配history_output和output前面的部分
        for index, _ in enumerate(self.history_output):
            try:
                assert self.history_output[index] == self.output[index]
            except Exception:
                raise HistoryOutputNotMatchedError("History output not matched")
        return self.output[len(self.history_output):]
    
# 具体流程：服务器端server_send发送消息后，到server_recv接收消息，此时会返回None
# 执行引擎退出，此时需要先调用client_recv获取服务端发送的消息
# 若为空，则说明执行引擎已经执行完毕
# 若不为空，则说明服务端发送了消息，此时需要调用client_send发送消息
# 最后调用reset重置状态