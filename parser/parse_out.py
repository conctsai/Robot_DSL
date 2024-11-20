import pyparsing as pp
from parser.parse_basic_unit import whitespace, string

o_key = pp.Keyword("out", caseless=True)

out_expr = pp.Group(o_key 
                    + whitespace 
                    + string("out"))