import pyparsing as pp
from parser.parse_basic_unit import whitespace, string

# OUT关键字
o_key = pp.Keyword("out", caseless=True)

# OUT表达式
out_expr = pp.Group(o_key 
                    + whitespace 
                    + string("out"))