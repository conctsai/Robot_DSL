import pyparsing as pp
from parser.parse_basic_unit import whitespace, id, arrow

# 转移表达式
trans_expr = pp.Group(arrow
                      + whitespace
                      + id("trans"))