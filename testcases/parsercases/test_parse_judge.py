from parser.parse_exprs import if_expr
import pytest as ptt
import pyparsing as pp

class TestParseJudge:
    @ptt.fixture(params=[
        (
            '''IF a == "12":
                  OUT "1"
               ;
            ''',
            [[['if', ['a', '==', '12'], ['out', '1']]]]
        ),
        (
            '''IF a == "12":
                  OUT "1"
               ELIF a == "13":
                  OUT "2"
               ;
            ''',
            [[['if', ['a', '==', '12'], ['out', '1']], ['elif', ['a', '==', '13'], ['out', '2']]]]
        ),
        (
            '''IF a == "12":
                  OUT "1"
               ELIF a == "13":
                  OUT "2"
               ELSE:
                  OUT "3"
               ;
            ''',
            [[['if', ['a', '==', '12'], ['out', '1']], ['elif', ['a', '==', '13'], ['out', '2']], ['else', ['out', '3']]]]
        ),
        (
            '''IF a == "12":
                  IF b == "13":
                     OUT "1"
                  ELSE:
                     OUT "2"
                  ;
               ;
            ''',
            [[['if', ['a', '==', '12'], [['if', ['b', '==', '13'], ['out', '1']], ['else', ['out', '2']]]]]]
        )
    ])
    def stub_input(self, request):
        return request.param
    
    def test_parse_judge(self, stub_input):
        s, expected = stub_input
        if isinstance(expected, list):
            result = if_expr.parseString(s, parse_all=True).as_list()
            assert result == expected
        else:
            with ptt.raises(expected):
                if_expr.parseString(s, parse_all=True)