#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from channels.tests import ChannelTestCase
from channels import Channel
from model_events.consumers import ws_message, ws_add, ws_disconnect
from model_events.messaging import notify


class TestConsumers(ChannelTestCase):

    def test_ping_pong(self):
        Channel("websocket.receive").send({"text": "PING"})
        reply = Channel("reply")
        msg = self.get_next_message("websocket.receive", require=True)
        msg.reply_channel = reply
        ws_message(msg)
        msg = self.get_next_message("reply")
        assert msg['text'] == "PONG"


    def test_message(self):
        Channel("websocket.receive").send({"text": "hello world"})
        reply = Channel("reply")
        msg = self.get_next_message("websocket.receive", require=True)
        msg.reply_channel = reply
        ws_message(msg)

    def test_group(self):
        Channel("websocket.connect").send({"text": ""})
        reply = Channel("reply")
        msg = self.get_next_message("websocket.connect", require=True)
        msg.reply_channel = reply
        msg['path'] = '/admin/ws'
        ws_add(msg)
        notify("test")
        msg = self.get_next_message("reply", require=True)
        assert json.loads(msg["text"])["payload"] == "test"
        Channel("websocket.disconnect").send({"text": ""})
        msg = self.get_next_message("websocket.disconnect", require=True)
        msg.reply_channel = reply
        ws_disconnect(msg)
        notify("test")
        msg = self.get_next_message("reply")
        assert msg == None
