# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class MarkUnmarkForDeleteProjectsRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'all': 'bool',
        'remove_all': 'bool',
        'exclude_document_ids': 'list[int]'
    }

    attribute_map = {
        'all': 'all',
        'remove_all': 'remove_all',
        'exclude_document_ids': 'exclude_document_ids'
    }

    def __init__(self, all=None, remove_all=None, exclude_document_ids=None, local_vars_configuration=None):  # noqa: E501
        """MarkUnmarkForDeleteProjectsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._all = None
        self._remove_all = None
        self._exclude_document_ids = None
        self.discriminator = None

        if all is not None:
            self.all = all
        if remove_all is not None:
            self.remove_all = remove_all
        if exclude_document_ids is not None:
            self.exclude_document_ids = exclude_document_ids

    @property
    def all(self):
        """Gets the all of this MarkUnmarkForDeleteProjectsRequest.  # noqa: E501


        :return: The all of this MarkUnmarkForDeleteProjectsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this MarkUnmarkForDeleteProjectsRequest.


        :param all: The all of this MarkUnmarkForDeleteProjectsRequest.  # noqa: E501
        :type all: bool
        """

        self._all = all

    @property
    def remove_all(self):
        """Gets the remove_all of this MarkUnmarkForDeleteProjectsRequest.  # noqa: E501


        :return: The remove_all of this MarkUnmarkForDeleteProjectsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._remove_all

    @remove_all.setter
    def remove_all(self, remove_all):
        """Sets the remove_all of this MarkUnmarkForDeleteProjectsRequest.


        :param remove_all: The remove_all of this MarkUnmarkForDeleteProjectsRequest.  # noqa: E501
        :type remove_all: bool
        """

        self._remove_all = remove_all

    @property
    def exclude_document_ids(self):
        """Gets the exclude_document_ids of this MarkUnmarkForDeleteProjectsRequest.  # noqa: E501


        :return: The exclude_document_ids of this MarkUnmarkForDeleteProjectsRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._exclude_document_ids

    @exclude_document_ids.setter
    def exclude_document_ids(self, exclude_document_ids):
        """Sets the exclude_document_ids of this MarkUnmarkForDeleteProjectsRequest.


        :param exclude_document_ids: The exclude_document_ids of this MarkUnmarkForDeleteProjectsRequest.  # noqa: E501
        :type exclude_document_ids: list[int]
        """

        self._exclude_document_ids = exclude_document_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MarkUnmarkForDeleteProjectsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarkUnmarkForDeleteProjectsRequest):
            return True

        return self.to_dict() != other.to_dict()
