"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import grocy
from grocy.model.inline_object17 import InlineObject17


class TestInlineObject17(unittest.TestCase):
    """InlineObject17 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineObject17(self):
        """Test InlineObject17"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InlineObject17()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()