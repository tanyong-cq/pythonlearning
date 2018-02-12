#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
baidu translate api test.
'''

import unittest
import transapi
import json

class TestTransapi(unittest.TestCase):
    """Test baidu translate api"""

    def test_transapi(self):
        result = transapi.translate('Rate used to calculate the difference between amounts based on the base currency and the reporting currency.')
        print('src=[%s]' % (result['trans_result'][0]['src']))
        print('dst=[%s]' % (result['trans_result'][0]['dst']))
        self.assertIsNotNone(result['trans_result'][0]['dst'])

if __name__ == '__main__':
    unittest.main()
