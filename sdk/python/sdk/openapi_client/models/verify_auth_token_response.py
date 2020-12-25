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


class VerifyAuthTokenResponse(object):
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
        'key': 'str',
        'user_name': 'str',
        'release_version': 'str',
        'user': 'ProjectDetailOwnersData'
    }

    attribute_map = {
        'key': 'key',
        'user_name': 'user_name',
        'release_version': 'release_version',
        'user': 'user'
    }

    def __init__(self, key=None, user_name=None, release_version=None, user=None, local_vars_configuration=None):  # noqa: E501
        """VerifyAuthTokenResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._user_name = None
        self._release_version = None
        self._user = None
        self.discriminator = None

        self.key = key
        self.user_name = user_name
        self.release_version = release_version
        self.user = user

    @property
    def key(self):
        """Gets the key of this VerifyAuthTokenResponse.  # noqa: E501


        :return: The key of this VerifyAuthTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this VerifyAuthTokenResponse.


        :param key: The key of this VerifyAuthTokenResponse.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def user_name(self):
        """Gets the user_name of this VerifyAuthTokenResponse.  # noqa: E501


        :return: The user_name of this VerifyAuthTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this VerifyAuthTokenResponse.


        :param user_name: The user_name of this VerifyAuthTokenResponse.  # noqa: E501
        :type user_name: str
        """
        if self.local_vars_configuration.client_side_validation and user_name is None:  # noqa: E501
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

    @property
    def release_version(self):
        """Gets the release_version of this VerifyAuthTokenResponse.  # noqa: E501


        :return: The release_version of this VerifyAuthTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        """Sets the release_version of this VerifyAuthTokenResponse.


        :param release_version: The release_version of this VerifyAuthTokenResponse.  # noqa: E501
        :type release_version: str
        """
        if self.local_vars_configuration.client_side_validation and release_version is None:  # noqa: E501
            raise ValueError("Invalid value for `release_version`, must not be `None`")  # noqa: E501

        self._release_version = release_version

    @property
    def user(self):
        """Gets the user of this VerifyAuthTokenResponse.  # noqa: E501


        :return: The user of this VerifyAuthTokenResponse.  # noqa: E501
        :rtype: ProjectDetailOwnersData
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this VerifyAuthTokenResponse.


        :param user: The user of this VerifyAuthTokenResponse.  # noqa: E501
        :type user: ProjectDetailOwnersData
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if not isinstance(other, VerifyAuthTokenResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VerifyAuthTokenResponse):
            return True

        return self.to_dict() != other.to_dict()