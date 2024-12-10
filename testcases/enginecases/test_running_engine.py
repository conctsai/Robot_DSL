from engine.message_handler import MessageHandler
from engine.running_engine import RunningEngine
from model.dsl_tree import serialize
from parser.parsing import parse
import pytest as ptt

class TestRunningEngine:
    
    def test_running_engine_1(self):
        mh = MessageHandler()
        re = RunningEngine(serialize(
            parse.parse_string(
                '''
                PARAM robot = "测试机器人"
                STATE INITIAL:
                    OUT "你好，我是{robot}"
                    ASK "你今年几岁了" -> age
                    IF age < "18":
                        OUT "你还是个小孩子"
                    ELIF age < "40":
                        OUT "你已经是个青年人了"
                    ELSE:
                        OUT "你已经是个老人了"
                    ;
                ''',
                parse_all=True
            ).as_dict()
            ), mh)
        flag = re.run()
        assert flag == False
        assert mh.client_recv() == ["你好，我是测试机器人", "你今年几岁了"]
        mh.reset()
        mh.client_send("17")
        flag = re.run()
        assert flag == True
        assert mh.client_recv() == ["你还是个小孩子"]
        
    def test_running_engine_2(self):
        mh = MessageHandler()
        re = RunningEngine(serialize(
            parse.parse_string(
                '''
                PARAM robot = "测试机器人"
                STATE INITIAL:
                    OUT "你好，我是{robot}"
                    ASK "你今年几岁了" -> age
                    IF age < "18":
                        OUT "你还是个小孩子"
                    ELIF age < "40":
                        OUT "你已经是个青年人了"
                    ELSE:
                        OUT "你已经是个老人了"
                    ;
                ''',
                parse_all=True
            ).as_dict()
            ), mh)
        flag = re.run()
        assert flag == False
        assert mh.client_recv() == ["你好，我是测试机器人", "你今年几岁了"]
        mh.reset()
        mh.client_send("20")
        flag = re.run()
        assert flag == True
        assert mh.client_recv() == ["你已经是个青年人了"]
        
    def test_running_engine_3(self):
        mh = MessageHandler()
        re = RunningEngine(serialize(
            parse.parse_string(
                '''
                PARAM robot = "测试机器人"
                STATE INITIAL:
                    OUT "你好，我是{robot}"
                    ASK "你今年几岁了" -> age
                    IF age < "18":
                        OUT "你还是个小孩子"
                    ELIF age < "40":
                        OUT "你已经是个青年人了"
                    ELSE:
                        OUT "你已经是个老人了"
                    ;
                ''',
                parse_all=True
            ).as_dict()
            ), mh)
        flag = re.run()
        assert flag == False
        assert mh.client_recv() == ["你好，我是测试机器人", "你今年几岁了"]
        mh.reset()
        mh.client_send("50")
        flag = re.run()
        assert flag == True
        assert mh.client_recv() == ["你已经是个老人了"]