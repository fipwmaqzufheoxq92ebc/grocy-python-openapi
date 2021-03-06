"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import grocy
from grocy.api.current_user_api import CurrentUserApi  # noqa: E501


class TestCurrentUserApi(unittest.TestCase):
    """CurrentUserApi unit test stubs"""

    def setUp(self):
        self.api = CurrentUserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_get(self):
        """Test case for user_get

        Returns the currently authenticated user  # noqa: E501
        """
        pass

    def test_user_settings_get(self):
        """Test case for user_settings_get

        Returns all settings of the currently logged in user  # noqa: E501
        """
        pass

    def test_user_settings_setting_key_delete(self):
        """Test case for user_settings_setting_key_delete

        Deletes the given setting of the currently logged in user  # noqa: E501
        """
        pass

    def test_user_settings_setting_key_get(self):
        """Test case for user_settings_setting_key_get

        Returns the given setting of the currently logged in user  # noqa: E501
        """
        pass

    def test_user_settings_setting_key_put(self):
        """Test case for user_settings_setting_key_put

        Sets the given setting of the currently logged in user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
