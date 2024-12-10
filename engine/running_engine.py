from model.dsl_tree import OUT, ASK, TRANS, JUDGE, IF_, ELIF_, ELSE_, CONDITION, DSLTree
from typing import Union, Tuple
from engine.variable_manager import VariableManager
from engine.message_handler import MessageHandler
from engine.string_operation import StringOperation
from error.running_engine_error import NoInputError

class RunningEngine():
    def __init__(self, tree: DSLTree, mh: MessageHandler):
        '''
        初始化运行引擎
        :param tree: DSL树
        :param mh: 消息处理器
        '''
        self.tree = tree
        self.vm = VariableManager() # 变量管理器
        self.mh = mh # 消息处理器
        
        # 处理param
        for item in self.tree.param_iter():
            self.vm.set(item.param, item.value) # 加入预先定义的变量
            
        self.state = 'INITIAL' # 初始状态
        
    def run(self) -> bool:
        '''
        运行引擎，当遇到输入时返回，返回值为是否运行结束
        :return: 是否运行结束
        '''
        try:
            while True:
                trans_flag = False
                state = self.tree.get_state(self.state) # 获取当前状态
                for item in state.expr_iter(): # 遍历当前状态的表达式
                    if not self.exec_expr(item): # 执行表达式
                        trans_flag = True
                        break
                if not trans_flag:
                    # 如果没有状态转换，结束执行
                    break
            return True
        except NoInputError as e:
            return False
            
    
    def exec_expr(self, expr: Union[OUT, ASK, TRANS, JUDGE]) -> bool: # 返回是否有状态转换
        '''
        执行表达式
        :param expr: 表达式
        :return: 是否有状态转换
        '''
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
        '''
        执行OUT表达式
        :param item: OUT表达式
        '''
        out = self.vm.format_placeholders(item.get_out())
        self.mh.server_send(out)
        
    def exec_ask(self, item: ASK):
        '''
        执行ASK表达式
        :param item: ASK表达式
        '''
        ask = self.vm.format_placeholders(item.get_ask()) # 格式化ASK表达式
        self.mh.server_send(ask) # 发送ASK表达式
        revmsg = self.mh.server_recv() # 接收用户输入
        if revmsg is None:
            raise NoInputError("No input")
        else:
            self.vm.set(item.get_save_to(), revmsg)
        
    def exec_trans(self, item: TRANS):
        '''
        执行转移表达式
        :param item: 转移表达式
        '''
        self.state = self.tree.get_state(item.get_trans()).get_state_name()
        
    def exec_judge(self, item: JUDGE) -> bool: # 返回有状态转换
        '''
        执行JUDGE表达式
        :param item: JUDGE表达式
        :return: 是否有状态转换
        '''
        if_ = item.get_if()
        exec_flag, judge_flag = self.exec_if_or_elif(if_)
        if not exec_flag:
            return False
        if not judge_flag:
            return True
        for elif_ in item.elif_iter():
            exec_flag, judge_flag = self.exec_if_or_elif(elif_)
            if not exec_flag:
                return False
            if not judge_flag:
                return True
        if item.has_else():
            if not self.exec_else(item.get_else()):
                return False
        return True
        
    def exec_if_or_elif(self, item: Union[IF_, ELIF_]) -> Tuple[bool, bool]: # 第一个返回是否有状态转换，第二个返回是否继续判断
        '''
        执行IF或ELIF表达式
        :param item: IF或ELIF表达式
        :return: 是否有状态转换，是否继续判断
        '''
        cond = item.get_condition()
        if self.exec_condition(cond):
            for expr in item.expr_iter():
                if not self.exec_expr(expr):
                    return False, False # 有状态转换
            return True, False # 没有状态转换，但是不继续判断
        return True, True # 没有状态转换，继续判断

    def exec_else(self, item: ELSE_) -> bool: # 返回是否有状态转换
        '''
        执行ELSE表达式
        :param item: ELSE表达式
        :return: 是否有状态转换
        '''
        for expr in item.expr_iter():
            if not self.exec_expr(expr):
                return False
        return True
    
    def exec_condition(self, cond: CONDITION) -> bool: # 返回CONDITION是否成立
        '''
        判断条件是否成立
        :param cond: 条件
        :return 条件是否成立
        '''
        if cond.get_judge() == "==":
            return StringOperation.euqal_string(self.vm.get(cond.get_key()), cond.get_value())
        elif cond.get_judge() == "~=":
            return StringOperation.regex_string(self.vm.get(cond.get_key()), cond.get_value())
        elif cond.get_judge() == ">":
            return StringOperation.greater_number(self.vm.get(cond.get_key()), cond.get_value())
        elif cond.get_judge() == "<":
            return StringOperation.less_number(self.vm.get(cond.get_key()), cond.get_value())
        elif cond.get_judge() == ">=":
            return StringOperation.greater_equal_number(self.vm.get(cond.get_key()), cond.get_value())
        elif cond.get_judge() == "<=":
            return StringOperation.less_equal_number(self.vm.get(cond.get_key()), cond.get_value())
        elif cond.get_judge() == "<>":
            return StringOperation.not_equal_string(self.vm.get(cond.get_key()), cond.get_value())
        return False