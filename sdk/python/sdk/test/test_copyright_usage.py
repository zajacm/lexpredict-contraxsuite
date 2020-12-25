# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.copyright_usage import CopyrightUsage  # noqa: E501
from openapi_client.rest import ApiException

class TestCopyrightUsage(unittest.TestCase):
    """CopyrightUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CopyrightUsage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.copyright_usage.CopyrightUsage()  # noqa: E501
        if include_optional :
            return CopyrightUsage(
                copyright_str = '0', 
                count = -2147483648, 
                pk = 56, 
                text_unit__pk = '0', 
                text_unit__unit_type = '0', 
                text_unit__location_start = '0', 
                text_unit__location_end = '0', 
                text_unit__document__pk = '0', 
                text_unit__document__name = '0', 
                text_unit__document__description = '0', 
                text_unit__document__document_type = '0'
            )
        else :
            return CopyrightUsage(
                copyright_str = '0',
        )

    def testCopyrightUsage(self):
        """Test CopyrightUsage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()