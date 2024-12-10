from parser.parse_state import state_token
import pytest as ptt


class TestParseState:
    @ptt.fixture(params=[
        (
            '''
            STATE INITIAL:
               ASK "你好，我是{robot}，请问我可以怎么称呼您？" -> name
               OUT "你好，{name}，很高兴为您服务！"
               -> HELP
            ''',
            [['state', 'INITIAL', ['ask', '你好，我是{robot}，请问我可以怎么称呼您？', 'name'], ['out', '你好，{name}，很高兴为您服务！'], ['HELP']]]
        )
    ])
    def stub_input(self, request):
        return request.param
    
    def test_parse(self, stub_input):
        s, expected = stub_input
        result = state_token.parse_string(s, parse_all=True).as_list()
        assert result == expected