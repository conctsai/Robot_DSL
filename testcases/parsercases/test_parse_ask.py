import pyparsing as pp
import pytest as ptt
from parser.parse_ask import ask_expr

class TestParseAsk:
    @ptt.fixture
    def stub_input_lowercase(self):
        return 'ask "hello world" -> abc'

    @ptt.fixture
    def stub_input_uppercase(self):
        return 'ASK "hello world" -> abc'
    
    @ptt.fixture
    def stub_input_mixedcase(self):
        return 'aSk "hello world" -> abc'    
    
    def test_parse_ask_with_lowercase(self, stub_input_lowercase):
        result = ask_expr.parseString(stub_input_lowercase, parse_all=True).as_list()
        assert result[0][0] == 'ask'
        assert result[0][1] == 'hello world'
        assert result[0][2] == 'abc'
        
    def test_parse_ask_with_uppercase(self, stub_input_uppercase):
        result = ask_expr.parseString(stub_input_uppercase, parse_all=True).as_list()
        assert result[0][0] == 'ask'
        assert result[0][1] == 'hello world'
        assert result[0][2] == 'abc'
        
    def test_parse_ask_with_mixedcase(self, stub_input_mixedcase):
        result = ask_expr.parseString(stub_input_mixedcase, parse_all=True).as_list()
        assert result[0][0] == 'ask'
        assert result[0][1] == 'hello world'
        assert result[0][2] == 'abc'