import pyparsing as pp
from parser.parse_ask import ask_expr
from parser.parse_out import out_expr
from parser.parse_trans import trans_expr
from parser.parse_judge import if_token, elif_token, else_token, exprs
from parser.parse_basic_unit import comma

# IF表达式的前向声明
if_expr = pp.Forward()

# 表达式
exprs <<= pp.ZeroOrMore(out_expr 
                      | ask_expr 
                      | trans_expr 
                      | if_expr)("exprs")


# IF表达式
if_expr <<= pp.Group(if_token 
                     + pp.ZeroOrMore(elif_token)("elif_") 
                     + pp.Optional(else_token) 
                     + comma)