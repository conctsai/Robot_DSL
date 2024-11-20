from parser.parse_param import param_token
import pytest as ptt
import pyparsing as pp

class TestParseParam:
    def test_parse_param_with_lowercase(self):
        s = 'param a = "b"'
        result = param_token.parseString(s, parse_all=True).as_list()
        assert result[0][0] == 'param'
        assert result[0][1] == 'a'
        assert result[0][2] == 'b'
        
    def test_parse_param_with_uppercase(self):
        s = 'PARAM a = "b"'
        result = param_token.parseString(s, parse_all=True).as_list()
        assert result[0][0] == 'param'
        assert result[0][1] == 'a'
        assert result[0][2] == 'b'
        
    def test_parse_param_with_mixedcase(self):
        s = "pArAm a = 'b'"
        result = param_token.parseString(s, parse_all=True).as_list()
        assert result[0][0] == 'param'
        assert result[0][1] == 'a'
        assert result[0][2] == 'b'
        
    def test_parse_param_with_no_separator(self):
        s = "param a='b'"
        with ptt.raises(pp.exceptions.ParseException):
            param_token.parseString(s, parse_all=True)