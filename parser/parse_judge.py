import pyparsing as pp
from parser.parse_basic_unit import whitespace, string, id, reg, equal, colon, gt, lt, ge, le, ne

exprs = pp.Forward()

i_key = pp.Keyword("if", caseless=True)
ei_key = pp.Keyword("elif", caseless=True)
el_key = pp.Keyword("else", caseless=True)

condition = pp.Group(id("key") + 
                     whitespace + 
                     (equal 
                      | reg
                      | ge
                      | le
                      | ne
                      | gt
                      | lt)("judge")
                     + whitespace 
                     + string("value"))("condition")

if_token = pp.Group(i_key 
                    + whitespace
                    + condition 
                    + colon 
                    + exprs)("if_")

elif_token = pp.Group(ei_key 
                      + whitespace 
                      + condition
                      + colon 
                      + exprs)

else_token = pp.Group(el_key
                      + colon
                      + exprs)("else_")