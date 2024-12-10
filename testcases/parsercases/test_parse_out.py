from parser.parse_out import out_expr
import pytest as ptt

class TestParseOut:
    @ptt.fixture(params=[
        ('OUT "hello world"', [['out', 'hello world']]),
        ('out "hello world"', [['out', 'hello world']]),
        ('oUt "hello world"', [['out', 'hello world']])
    ])
    def stub_input(self, request):
        return request.param
    
    
    def test_parse_out(self, stub_input):
        s, expected = stub_input
        result = out_expr.parseString(s, parse_all=True).as_list()
        assert result == expected