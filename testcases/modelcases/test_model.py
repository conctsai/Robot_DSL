from model.dsl_tree import serialize
from parser.parsing import parse
from error.dsl_runtime_error import NoStateDefinedError, NoInitialStateError
import pytest as ptt

class TestModel:
    
    @ptt.fixture(params=[
        (
            parse.parse_string(
                '''
                STATE INITIAL:
                    ASK "你好，我是{robot}，请问我可以怎么称呼您？" -> name
                    OUT "你好，{name}，很高兴为您服务！"
                    -> HELP

                STATE HELP:
                    ASK "请问有什么可以帮助您的？(天气/温度/灯光/安全/清扫)" -> task

                    IF task == "天气":
                        -> WEATHER_UPDATE
                    ELIF task == "温度":
                        -> TEMPERATURE_CONTROL
                    ELIF task == "灯光":
                        -> LIGHT_CONTROL
                    ELIF task == "安全":
                        -> SECURITY_CHECK
                    ELSE:
                        -> CLEANING_CONTROL
                    ;
                ''', parse_all=True
            ).as_dict(),
            "DSLTree=[STATE(state='INITIAL', exprs=[ASK(ask='你好，我是{robot}，请问我可以怎么称呼您？', save_to='name'), OUT(out='你好，{name}，很高兴为您服务！'), TRANS(trans='HELP')]), STATE(state='HELP', exprs=[ASK(ask='请问有什么可以帮助您的？(天气/温度/灯光/安全/清扫)', save_to='task'), JUDGE(if_=IF_(condition=CONDITION(key='task', judge='==', value='天气'), exprs=[TRANS(trans='WEATHER_UPDATE')]), elif_=[ELIF_(condition=CONDITION(key='task', judge='==', value='温度'), exprs=[TRANS(trans='TEMPERATURE_CONTROL')]), ELIF_(condition=CONDITION(key='task', judge='==', value='灯光'), exprs=[TRANS(trans='LIGHT_CONTROL')]), ELIF_(condition=CONDITION(key='task', judge='==', value='安全'), exprs=[TRANS(trans='SECURITY_CHECK')])], else_=ELSE_(exprs=[TRANS(trans='CLEANING_CONTROL')]))])]"
        ),
        (
            parse.parse_string(
                '''
                    STATE HELP:
                    ASK "请问有什么可以帮助您的？(天气/温度/灯光/安全/清扫)" -> task

                    IF task == "天气":
                        -> WEATHER_UPDATE
                    ELIF task == "温度":
                        -> TEMPERATURE_CONTROL
                    ELIF task == "灯光":
                        -> LIGHT_CONTROL
                    ELIF task == "安全":
                        -> SECURITY_CHECK
                    ELSE:
                        -> CLEANING_CONTROL
                    ;
                ''', parse_all=True
            ).as_dict(),
            NoInitialStateError
        ),
        (
            parse.parse_string(
                '''
                   OUT "123"
                '''
            ).as_dict(),
            NoStateDefinedError
        )
    ])
    def stub_input(self, request):
        return request.param
    
    
    def test_model(self, stub_input):
        s, expected = stub_input
        if isinstance(expected, str):
            result = serialize(s).__str__()
            assert result == expected
        else:
            with ptt.raises(expected):
                serialize(s)