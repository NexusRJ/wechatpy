# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest

from wechatpy.utils import ObjectDict, check_signature


class UtilityTestCase(unittest.TestCase):

    def test_object_dict(self):
        obj = ObjectDict()
        self.assertTrue(obj.xxx is None)
        obj.xxx = 1
        self.assertEqual(1, obj.xxx)

    def test_check_signature_should_ok(self):
        token = 'test'
        signature = 'f21891de399b4e33a1a93c9a7b8a8fffb5a443ff'
        timestamp = '1410685589'
        nonce = 'test'
        self.assertTrue(check_signature(token, signature, timestamp, nonce))

    def test_check_signature_should_fail(self):
        token = 'test'
        signature = 'f21891de399b4e33a1a93c9a7b8a8fffb5a443fe'
        timestamp = '1410685589'
        nonce = 'test'
        self.assertFalse(check_signature(token, signature, timestamp, nonce))
