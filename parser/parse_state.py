import pyparsing as pp
from parser.parse_basic_unit import whitespace, id, colon
from parser.parse_exprs import exprs

# STATE关键字
s_key = pp.Keyword("state", caseless=True)

# STATE表达式
state_token = pp.Group(s_key 
                       + whitespace 
                       + id("state") 
                       + colon 
                       + exprs)