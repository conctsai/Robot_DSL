import pytest as ptt
from engine.message_handler import MessageHandler

class TestMessageHandler:
    def test(self):
        mh = MessageHandler()
        mh.server_send("hello")
        mh.server_send("world")
        assert mh.server_recv() == None
        assert mh.client_recv() == ["hello", "world"]
        mh.client_send("world")
        mh.reset()
        mh.server_send("hello")
        mh.server_send("world")
        assert mh.client_recv() == []