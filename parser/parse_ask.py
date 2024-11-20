import pyparsing as pp
from parser.parse_basic_unit import whitespace, string, id, arrow

a_key = pp.Keyword("ask", caseless=True)

ask_expr = pp.Group(a_key 
                    + whitespace
                    + string("ask") 
                    + whitespace
                    + arrow
                    + whitespace
                    + id("save_to"))