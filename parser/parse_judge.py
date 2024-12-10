import pyparsing as pp
from parser.parse_basic_unit import whitespace, string, id, reg, equal, colon, gt, lt, ge, le, ne

# 表达式的前向声明
exprs = pp.Forward()

i_key = pp.Keyword("if", caseless=True) # if关键字
ei_key = pp.Keyword("elif", caseless=True) # elif关键字
el_key = pp.Keyword("else", caseless=True) # else关键字


# 条件判断
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

# IF表达式
if_token = pp.Group(i_key 
                    + whitespace
                    + condition 
                    + colon 
                    + exprs)("if_")

# ELIF表达式
elif_token = pp.Group(ei_key 
                      + whitespace 
                      + condition
                      + colon 
                      + exprs)

# ELSE表达式
else_token = pp.Group(el_key
                      + colon
                      + exprs)("else_")