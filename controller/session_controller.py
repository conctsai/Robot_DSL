from controller.engine_controller import EngineController
from controller.conf_controller import ConfController
from typing import List, Mapping
from error.controller_runtime_error import ConfNotFoundError, SessionNotFoundError
from error.parse_error import ParseError

class SessionController:
    '''
    会话控制器，用于管理会话
    '''
    def __init__(self):
        self.session_engine_map: Mapping[int, EngineController] = {}
        self.session_count = 1
        self.conf_controller = ConfController()
        
    def create_session(self, conf_name: str):
        '''
        创建会话
        :param conf_name: 配置文件名
        :return: 会话ID
        '''
        session_id = self.session_count
        self.session_count += 1
        try:
            self.session_engine_map[session_id] = EngineController(self.conf_controller.get_dsl_tree(conf_name))
        except Exception as e:
            raise e
        return session_id
    
    def close_session(self, session_id: int):
        '''
        关闭会话
        :param session_id: 会话ID
        '''
        if session_id in self.session_engine_map:
            del self.session_engine_map[session_id]
        else:
            raise SessionNotFoundError(f"Session {session_id} not found")
    
    def get_output(self, session_id: int, input: List[str]):
        '''
        获取输出
        :param session_id: 会话ID
        :param input: 输入
        :return: 输出
        '''
        if session_id in self.session_engine_map:
            return self.session_engine_map[session_id].get_output(input)
        else:
            raise SessionNotFoundError(f"Session {session_id} not found")