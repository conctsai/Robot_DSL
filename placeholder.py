import pyparsing as pp

pp.ParserElement.setDefaultWhitespaceChars("\n") # 禁用默认忽略的空白字符，忽略换行符

string = pp.QuotedString(quoteChar="'", esc_char="\\") | pp.QuotedString(quoteChar='"', esc_char="\\")
placeholder = pp.Regex(r"\{[a-zA-Z_][a-zA-Z0-9_]*\}")
str_with_placeholder = pp.Combine(string + pp.ZeroOrMore(placeholder)("placeholder"))

print(placeholder.parse_string("{world}"))