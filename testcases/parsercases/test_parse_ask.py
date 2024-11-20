import pyparsing as pp
import pytest as ptt
from parser.parse_ask import ask_expr


class TestParseAsk:
    def test_parse_ask_with_lowercase(self):
        s = 'ask "hello world" -> abc'
        result = ask_expr.parseString(s, parse_all=True).as_list()
        assert result[0][0] == 'ask'
        assert result[0][1] == 'hello world'
        assert result[0][2] == 'abc'
        
    def test_parse_ask_with_uppercase(self):
        s = 'ASK "hello world" -> abc'
        result = ask_expr.parseString(s, parse_all=True).as_list()
        assert result[0][0] == 'ask'
        assert result[0][1] == 'hello world'
        assert result[0][2] == 'abc'
        
    def test_parse_ask_with_mixedcase(self):
        s = 'aSk "hello world" -> abc'
        result = ask_expr.parseString(s, parse_all=True).as_list()
        assert result[0][0] == 'ask'
        assert result[0][1] == 'hello world'
        assert result[0][2] == 'abc'