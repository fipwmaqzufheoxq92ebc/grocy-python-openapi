"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import grocy
from grocy.model.inline_response200_grocy_version import InlineResponse200GrocyVersion
globals()['InlineResponse200GrocyVersion'] = InlineResponse200GrocyVersion
from grocy.model.inline_response200 import InlineResponse200


class TestInlineResponse200(unittest.TestCase):
    """InlineResponse200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponse200(self):
        """Test InlineResponse200"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InlineResponse200()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
