from engine.message_handler import MessageHandler
from engine.running_engine import RunningEngine
from model.dsl_tree import DSLTree
from typing import Tuple, List


class EngineController():
    def __init__(self, tree: DSLTree):
        self.mh = MessageHandler()
        self.tree = tree
    
    def get_output(self, input: List[str]) -> Tuple[bool, List[str]]:
        try:
            self.mh.reset()
            for item in input:
                self.mh.client_send(item)
            flag = RunningEngine(self.tree, self.mh).run()
            return flag, self.mh.client_recv()
        except Exception as e:
            raise e