import pyparsing as pp

id = pp.Word(pp.alphas + "_", 
             pp.alphanums + "_") # 标识符

equals = pp.Suppress("=") # 等号

whitespace = pp.Suppress(pp.White()) # 空白符

colon = pp.Suppress(":") # 冒号

comma = pp.Suppress(";") # 分号
arrow = pp.Suppress("->") # 箭头
equal = pp.Literal("==") # 等于
reg = pp.Literal("~=") # 正则匹配

string = pp.QuotedString(quoteChar="'", esc_char="\\") | pp.QuotedString(quoteChar='"', esc_char="\\") # 字符串