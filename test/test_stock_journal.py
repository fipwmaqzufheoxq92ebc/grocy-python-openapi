"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import grocy
from grocy.model.stock_transaction_type import StockTransactionType
globals()['StockTransactionType'] = StockTransactionType
from grocy.model.stock_journal import StockJournal


class TestStockJournal(unittest.TestCase):
    """StockJournal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStockJournal(self):
        """Test StockJournal"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StockJournal()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
