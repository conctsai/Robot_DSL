from model.dsl_tree import OUT, ASK, TRANS, JUDGE, IF_, ELIF_, ELSE_, CONDITION, DSLTree
from typing import Union
from engine.variable_manager import VariableManager
from engine.message_handler import MessageHandler
from engine.string_operation import StringOperation

class RunningEngine():
    def __init__(self, tree: DSLTree):
        self.tree = tree
        self.vm = VariableManager()
        self.mh = MessageHandler()
        
        # 处理param
        for item in self.tree.param_iter():
            self.vm.set(item.param, item.value)
            
        self.state = 'INITIAL'
        self.op = 0
        
    def run(self):
        while True:
            trans_flag = False
            state = self.tree.get_state(self.state)
            for item in state.expr_iter():
                if not self.exec_expr(item):
                    trans_flag = True
                    break
            if not trans_flag:
                # 如果没有状态转换，结束执行
                break
            
    
    def exec_expr(self, expr: Union[OUT, ASK, TRANS, JUDGE]) -> bool: # 返回是否继续执行
        if isinstance(expr, OUT):
            self.exec_out(expr)
        elif isinstance(expr, ASK):
            self.exec_ask(expr)
        elif isinstance(expr, TRANS):
            self.exec_trans(expr)
            return False
        elif isinstance(expr, JUDGE):
            return self.exec_judge(expr)
        return True
    
    def exec_out(self, item: OUT):
        out = self.vm.format_placeholders(item.get_out())
        self.mh.send(out)
        
    def exec_ask(self, item: ASK):
        ask = self.vm.format_placeholders(item.get_ask())
        self.mh.send(ask)
        self.vm.set(item.get_save_to(), self.mh.recv())
        
    def exec_trans(self, item: TRANS):
        self.state = self.tree.get_state(item.get_trans()).get_state_name()
        
    def exec_judge(self, item: JUDGE) -> bool: # 返回是否继续执行
        if_ = item.get_if()
        if not self.exec_if_or_elif(if_):
            return False
        for elif_ in item.elif_iter():
            if not self.exec_if_or_elif(elif_):
                return False
        if item.has_else():
            if not self.exec_else(item.get_else()):
                return False
        
    def exec_if_or_elif(self, item: Union[IF_, ELIF_]) -> bool: # 返回是否继续执行
        cond = item.get_condition()
        if self.exec_condition(cond):
            for expr in item.expr_iter():
                if not self.exec_expr(expr):
                    return False
        return True

    def exec_else(self, item: ELSE_) -> bool: # 返回是否继续执行
        for expr in item.expr_iter():
            if not self.exec_expr(expr):
                return False
        return True
    
    def exec_condition(self, cond: CONDITION) -> bool: # 返回CONDITION是否成立
        if cond.get_judge() == "==":
            return StringOperation.euqal_string(self.vm.get(cond.get_key()), cond.get_value())
        elif cond.get_judge() == "~=":
            return StringOperation.regex_string(self.vm.get(cond.get_key()), cond.get_value())
        return False