from pydantic import BaseModel, model_validator, ConfigDict
from typing import List, Union, Optional
from error.dsl_runtime_error import NoStateDefinedError, NoInitialStateError, NoStateMatchedError

class ConfigedBaseModel(BaseModel):
    model_config = ConfigDict(extra='forbid')

class PARAM(ConfigedBaseModel):
    param: str
    value: str
    
class OUT(ConfigedBaseModel):
    out: str
    
    def get_out(self):
        return self.out
    
class ASK(ConfigedBaseModel):
    ask: str
    save_to: str
    
    def get_ask(self):
        return self.ask
    
    def get_save_to(self):
        return self.save_to
    
class TRANS(ConfigedBaseModel):
    trans: str
    
    def get_trans(self):
        return self.trans
    
class JUDGE(ConfigedBaseModel):
    if_: 'IF_'
    elif_: List['ELIF_']
    else_: Optional['ELSE_'] = None
    
    def get_if(self) -> 'IF_':
        return self.if_

    def get_elif(self) -> List['ELIF_']:
        return self.elif_
    
    def get_else(self) -> Optional['ELSE_']:
        return self.else_
    
    def has_else(self) -> bool:
        return self.else_ is not None
    
    def elif_iter(self):
        for item in self.elif_:
            yield item
    
class CONDITION(ConfigedBaseModel):
    key: str
    judge: str
    value: str
    
    def get_key(self):
        return self.key
    
    def get_judge(self):
        return self.judge
    
    def get_value(self):
        return self.value
    
class judge_statement(ConfigedBaseModel):
    condition: CONDITION
    exprs: List[Union[OUT, ASK, TRANS, JUDGE]]
    
    def get_condition(self):
        return self.condition
    
    def expr_iter(self):
        for item in self.exprs:
            yield item
    
class IF_(judge_statement):
    pass
    
class ELIF_(judge_statement):
    pass

class ELSE_(ConfigedBaseModel):
    exprs: List[Union[OUT, ASK, TRANS, JUDGE]]
    
    def expr_iter(self):
        for item in self.exprs:
            yield item
    
class STATE(ConfigedBaseModel):
    state: str
    exprs: List[Union[OUT, ASK, TRANS, JUDGE]]
    
    def expr_iter(self):
        for item in self.exprs:
            yield item
    
    def get_state_name(self) -> str:
        return self.state
    
class DSLTree(ConfigedBaseModel):
    DSLTree: List[Union[PARAM, STATE]]
    
    def has_param(self):
        return any([isinstance(item, PARAM) for item in self.DSLTree])
    
    def has_state(self):
        return any([isinstance(item, STATE) for item in self.DSLTree])
    
    def param_iter(self): # param迭代器
        for item in self.DSLTree:
            if isinstance(item, PARAM):
                yield item

    def state_iter(self): # state迭代器
        for item in self.DSLTree:
            if isinstance(item, STATE):
                yield item
                
    def get_state(self, state_name: str) -> STATE:
        # state大小写不敏感
        for state in self.state_iter():
            if state.state.lower() == state_name.lower():
                return state
        raise NoStateMatchedError("state {} not matched".format(state_name))

    @model_validator(mode='after')
    def check_state(self):
        if not self.has_state():
            raise NoStateDefinedError("No state defined")
        # 判断是否有名为initial（大小写不敏感）的state，如果没有，抛出NoInitialStateError
        if not any([state.state.lower() == "initial" for state in self.state_iter()]):
            raise NoInitialStateError("No initial state defined")
        return self

def serialize(dic: dict) -> DSLTree:
    return DSLTree.model_validate(dic)