import pyparsing as pp
from parser.parse_basic_unit import whitespace, string, id, arrow

# ASK关键字
a_key = pp.Keyword("ask", caseless=True)

# ASK表达式
ask_expr = pp.Group(a_key 
                    + whitespace
                    + string("ask") 
                    + whitespace
                    + arrow
                    + whitespace
                    + id("save_to"))