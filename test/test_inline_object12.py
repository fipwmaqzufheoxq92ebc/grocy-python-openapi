"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import grocy
from grocy.model.inline_object12 import InlineObject12


class TestInlineObject12(unittest.TestCase):
    """InlineObject12 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineObject12(self):
        """Test InlineObject12"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InlineObject12()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
