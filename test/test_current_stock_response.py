"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import grocy
from grocy.model.product import Product
globals()['Product'] = Product
from grocy.model.current_stock_response import CurrentStockResponse


class TestCurrentStockResponse(unittest.TestCase):
    """CurrentStockResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCurrentStockResponse(self):
        """Test CurrentStockResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CurrentStockResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
