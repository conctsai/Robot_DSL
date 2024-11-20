import pyparsing as pp
from parser.parse_basic_unit import whitespace, id, colon
from parser.parse_exprs import exprs

s_key = pp.Keyword("state", caseless=True)
state_token = pp.Group(s_key 
                       + whitespace 
                       + id("state") 
                       + colon 
                       + exprs)