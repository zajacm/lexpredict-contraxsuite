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
from openapi_client.models.text_unit_classification import TextUnitClassification  # noqa: E501
from openapi_client.rest import ApiException

class TestTextUnitClassification(unittest.TestCase):
    """TextUnitClassification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TextUnitClassification
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.text_unit_classification.TextUnitClassification()  # noqa: E501
        if include_optional :
            return TextUnitClassification(
                pk = 56, 
                text_unit__document__pk = '0', 
                text_unit__document__name = '0', 
                text_unit__document__document_type = '0', 
                text_unit__document__description = '0', 
                text_unit__pk = '0', 
                text_unit__unit_type = '0', 
                text_unit__language = '0', 
                class_name = '0', 
                class_value = '0', 
                user__username = '0', 
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return TextUnitClassification(
                class_name = '0',
                class_value = '0',
        )

    def testTextUnitClassification(self):
        """Test TextUnitClassification"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
