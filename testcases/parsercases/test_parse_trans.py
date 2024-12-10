from parser.parse_trans import trans_expr
import pytest as ptt

class TestParseTrans:
    @ptt.fixture(params=[
        ('-> state_a', [['state_a']])
    ])
    def stub_input(self, request):
        return request.param
    
    def test_parse(self, stub_input):
        s, expected = stub_input
        result = trans_expr.parseString(s, parse_all=True).as_list()
        assert result == expected