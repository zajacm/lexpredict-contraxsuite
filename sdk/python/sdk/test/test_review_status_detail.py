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
from openapi_client.models.review_status_detail import ReviewStatusDetail  # noqa: E501
from openapi_client.rest import ApiException

class TestReviewStatusDetail(unittest.TestCase):
    """ReviewStatusDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReviewStatusDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.review_status_detail.ReviewStatusDetail()  # noqa: E501
        if include_optional :
            return ReviewStatusDetail(
                pk = 56, 
                name = '0', 
                code = '0', 
                order = 0, 
                group = 56, 
                group_data = openapi_client.models.review_status_detail_group_data.ReviewStatusDetail_group_data(
                    pk = 56, 
                    name = '0', 
                    code = '0', 
                    order = 0, 
                    is_active = True, ), 
                is_active = True
            )
        else :
            return ReviewStatusDetail(
                name = '0',
                order = 0,
                group_data = openapi_client.models.review_status_detail_group_data.ReviewStatusDetail_group_data(
                    pk = 56, 
                    name = '0', 
                    code = '0', 
                    order = 0, 
                    is_active = True, ),
        )

    def testReviewStatusDetail(self):
        """Test ReviewStatusDetail"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
