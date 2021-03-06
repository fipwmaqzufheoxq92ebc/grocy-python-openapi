"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import grocy
from grocy.api.recipes_api import RecipesApi  # noqa: E501


class TestRecipesApi(unittest.TestCase):
    """RecipesApi unit test stubs"""

    def setUp(self):
        self.api = RecipesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_recipes_fulfillment_get(self):
        """Test case for recipes_fulfillment_get

        Get stock fulfillment information for all recipe  # noqa: E501
        """
        pass

    def test_recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_post(self):
        """Test case for recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_post

        Adds all missing products for the given recipe to the shopping list  # noqa: E501
        """
        pass

    def test_recipes_recipe_id_consume_post(self):
        """Test case for recipes_recipe_id_consume_post

        Consumes all products of the given recipe  # noqa: E501
        """
        pass

    def test_recipes_recipe_id_fulfillment_get(self):
        """Test case for recipes_recipe_id_fulfillment_get

        Get stock fulfillment information for the given recipe  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
