import pytest as ptt
from engine.message_handler import MessageHandler
from error.running_engine_error import HistoryOutputNotMatchedError


class TestMessageHandler:

    def test_message_handler(self):
        mh = MessageHandler()
        mh.server_send("hello")
        mh.server_send("world")
        assert mh.server_recv() == None
        assert mh.client_recv() == ["hello", "world"]
        mh.client_send("world")
        mh.reset()
        mh.server_send("hello")
        mh.server_send("world")
        mh.server_send("nihao")
        assert mh.client_recv() == ["nihao"]
        
    def test_message_handler_error(self):
        mh = MessageHandler()
        mh.server_send("hello")
        mh.server_send("world")
        assert mh.server_recv() == None
        assert mh.client_recv() == ["hello", "world"]
        mh.client_send("world")
        mh.reset()
        mh.server_send("hello")
        with ptt.raises(HistoryOutputNotMatchedError):
            mh.client_recv()
            
    def test_message_handler_error_2(self):
        mh = MessageHandler()
        mh.server_send("hello")
        mh.server_send("world")
        assert mh.server_recv() == None
        assert mh.client_recv() == ["hello", "world"]
        mh.client_send("world")
        mh.reset()
        mh.server_send("nihao")
        with ptt.raises(HistoryOutputNotMatchedError):
            mh.client_recv()
            