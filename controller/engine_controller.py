from engine.message_handler import MessageHandler
from engine.running_engine import RunningEngine
from model.dsl_tree import DSLTree
from typing import Tuple, List


class EngineController():
    '''
    引擎控制器，用于控制引擎的运行
    '''
    def __init__(self, tree: DSLTree):
        '''
        初始化引擎控制器
        :param tree: DSL树
        '''
        self.mh = MessageHandler()
        self.tree = tree
    
    def get_output(self, input: List[str]) -> Tuple[bool, List[str]]:
        '''
        获取输出
        :param input: 输入
        :return: 是否运行结束，输出
        '''
        try:
            self.mh.reset()
            for item in input:
                self.mh.client_send(item)
            flag = RunningEngine(self.tree, self.mh).run()
            return flag, self.mh.client_recv()
        except Exception as e:
            raise e