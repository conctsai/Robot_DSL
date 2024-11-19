from pydantic import BaseModel, model_validator, ValidationError, RootModel
from typing import List, Union, Dict, Optional

dic = {'DSLTree': [{'param': 'a', 'value': '123'}, {'state': 'a', 'exprs': [{'out': '123123'}, {'ask': '123', 'save_to': 'as'}, {'if_': {'condition': {'key': 'a', 'judge': '==', 'value': '123'}, 'exprs': [{'out': '123123'}, {'trans': 'as'}]}, 'elif_': {'condition': {'key': 'b', 'judge': '==', 'value': '23'}, 'exprs': [{'ask': 'qwe', 'save_to': 'as'}, {'trans': 'll'}]}}]}]}

class PARAM(BaseModel):
    param: str
    value: str
    
class OUT(BaseModel):
    out: str
    
class ASK(BaseModel):
    ask: str
    save_to: str
    
class TRANS(BaseModel):
    trans: str
    
class JUDGE(BaseModel):
    if_: 'IF_'
    elif_: Optional['ELIF_'] = None
    else_: Optional['ELSE_'] = None
    
class CONDITION(BaseModel):
    key: str
    judge: str
    value: str
    
class IF_(BaseModel):
    condition: CONDITION
    exprs: List[Union[OUT, ASK, TRANS, JUDGE]]
    
class ELIF_(BaseModel):
    condition: CONDITION
    exprs: List[Union[OUT, ASK, TRANS, JUDGE]]

class ELSE_(BaseModel):
    exprs: List[Union[OUT, ASK, TRANS, JUDGE]]
    
class STATE(BaseModel):
    state: str
    exprs: List[Union[OUT, ASK, TRANS, JUDGE]]
    
class DSLTree(BaseModel):
    DSLTree: List[Union[PARAM, STATE]]
    
def serialize(dic: dict) -> DSLTree:
    return DSLTree.model_validate(dic)