import pyparsing as pp
from parser.parse_basic_unit import id, equals, whitespace, string

# PARAM关键字
p_key = pp.Keyword("param", caseless=True)

# PARAM表达式
param_token = pp.Group(p_key 
                       + whitespace 
                       + id("param") 
                       + whitespace 
                       + equals 
                       + whitespace 
                       + string("value"))
