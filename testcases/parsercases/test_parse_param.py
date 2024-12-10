from parser.parse_param import param_token
import pytest as ptt
import pyparsing as pp

class TestParseParam:
    @ptt.fixture(params=[
        ('param a = "b"', [['param', 'a', 'b']]),
        ('PARAM a = "b"', [['param', 'a', 'b']]),
        ('pArAm a = "b"', [['param', 'a', 'b']]),
        ('param a=\'b\'', pp.exceptions.ParseException)
    ])
    def stub_input(self, request):
        return request.param
    
    
    def test_parse_param(self, stub_input):
        s, expected = stub_input
        if isinstance(expected, list):
            result = param_token.parseString(s, parse_all=True).as_list()
            assert result == expected
        else:
            with ptt.raises(expected):
                param_token.parseString(s, parse_all=True)