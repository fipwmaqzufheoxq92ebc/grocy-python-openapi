"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import grocy
from grocy.api.files_api import FilesApi  # noqa: E501


class TestFilesApi(unittest.TestCase):
    """FilesApi unit test stubs"""

    def setUp(self):
        self.api = FilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_files_group_file_name_delete(self):
        """Test case for files_group_file_name_delete

        Deletes the given file  # noqa: E501
        """
        pass

    def test_files_group_file_name_get(self):
        """Test case for files_group_file_name_get

        Serves the given file  # noqa: E501
        """
        pass

    def test_files_group_file_name_put(self):
        """Test case for files_group_file_name_put

        Uploads a single file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
