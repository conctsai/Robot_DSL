import pyparsing as pp
import model.dsl_tree as dsl_tree
from parser.parse_param import param_token
from parser.parse_state import state_token
from error.parse_error import ParseError

# DSL语法
parse = pp.ZeroOrMore(param_token | state_token)("DSLTree")

# 忽略注释
parse = parse.ignore(pp.pythonStyleComment)

def parse_file(file) -> dsl_tree.DSLTree:
    '''
    解析DSL文件
    输入：文件路径
    输出：DSL树
    '''
    try:
        result = parse.parse_file(file, parseAll=True).as_dict()
    except pp.exceptions.ParseException as e:
        raise ParseError(e)
    # print(result)
    result = dsl_tree.serialize(result)
    return result