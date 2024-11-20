import pyparsing as pp
from parser.parse_basic_unit import id, equals, whitespace, string

p_key = pp.Keyword("param", caseless=True)

param_token = pp.Group(p_key 
                       + whitespace 
                       + id("param") 
                       + whitespace 
                       + equals 
                       + whitespace 
                       + string("value"))
