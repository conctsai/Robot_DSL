import pyparsing as pp
import model.dsl_tree as dsl_tree
from parser.parse_param import param_token
from parser.parse_state import state_token

parse = pp.ZeroOrMore(param_token | state_token)("DSLTree")
parse = parse.ignore(pp.pythonStyleComment)

def parse_file(file) -> dsl_tree.DSLTree:
    result = parse.parse_file(file, parseAll=True).as_dict()
    # print(result)
    result = dsl_tree.serialize(result)
    return result