#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase



class TestPermissions(TestCase):

    def setUp(self):
        pass

    def test_something(self):
        from model_events.permissions import is_message_allowed
        from model_events.utils import allow_all
        assert is_message_allowed == allow_all

    def tearDown(self):
        pass
