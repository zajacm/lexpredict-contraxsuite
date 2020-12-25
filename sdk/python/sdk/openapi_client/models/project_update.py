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


class ProjectUpdate(object):
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
        'pk': 'int',
        'name': 'str',
        'description': 'str',
        'status': 'int',
        'send_email_notification': 'bool',
        'owners': 'list[int]',
        'reviewers': 'list[int]',
        'super_reviewers': 'list[int]',
        'junior_reviewers': 'list[int]',
        'type': 'str',
        'hide_clause_review': 'bool'
    }

    attribute_map = {
        'pk': 'pk',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'send_email_notification': 'send_email_notification',
        'owners': 'owners',
        'reviewers': 'reviewers',
        'super_reviewers': 'super_reviewers',
        'junior_reviewers': 'junior_reviewers',
        'type': 'type',
        'hide_clause_review': 'hide_clause_review'
    }

    def __init__(self, pk=None, name=None, description=None, status=None, send_email_notification=None, owners=None, reviewers=None, super_reviewers=None, junior_reviewers=None, type=None, hide_clause_review=None, local_vars_configuration=None):  # noqa: E501
        """ProjectUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pk = None
        self._name = None
        self._description = None
        self._status = None
        self._send_email_notification = None
        self._owners = None
        self._reviewers = None
        self._super_reviewers = None
        self._junior_reviewers = None
        self._type = None
        self._hide_clause_review = None
        self.discriminator = None

        if pk is not None:
            self.pk = pk
        self.name = name
        self.description = description
        if status is not None:
            self.status = status
        if send_email_notification is not None:
            self.send_email_notification = send_email_notification
        if owners is not None:
            self.owners = owners
        if reviewers is not None:
            self.reviewers = reviewers
        if super_reviewers is not None:
            self.super_reviewers = super_reviewers
        if junior_reviewers is not None:
            self.junior_reviewers = junior_reviewers
        if type is not None:
            self.type = type
        if hide_clause_review is not None:
            self.hide_clause_review = hide_clause_review

    @property
    def pk(self):
        """Gets the pk of this ProjectUpdate.  # noqa: E501


        :return: The pk of this ProjectUpdate.  # noqa: E501
        :rtype: int
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this ProjectUpdate.


        :param pk: The pk of this ProjectUpdate.  # noqa: E501
        :type pk: int
        """

        self._pk = pk

    @property
    def name(self):
        """Gets the name of this ProjectUpdate.  # noqa: E501


        :return: The name of this ProjectUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectUpdate.


        :param name: The name of this ProjectUpdate.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProjectUpdate.  # noqa: E501


        :return: The description of this ProjectUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectUpdate.


        :param description: The description of this ProjectUpdate.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this ProjectUpdate.  # noqa: E501


        :return: The status of this ProjectUpdate.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProjectUpdate.


        :param status: The status of this ProjectUpdate.  # noqa: E501
        :type status: int
        """

        self._status = status

    @property
    def send_email_notification(self):
        """Gets the send_email_notification of this ProjectUpdate.  # noqa: E501


        :return: The send_email_notification of this ProjectUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._send_email_notification

    @send_email_notification.setter
    def send_email_notification(self, send_email_notification):
        """Sets the send_email_notification of this ProjectUpdate.


        :param send_email_notification: The send_email_notification of this ProjectUpdate.  # noqa: E501
        :type send_email_notification: bool
        """

        self._send_email_notification = send_email_notification

    @property
    def owners(self):
        """Gets the owners of this ProjectUpdate.  # noqa: E501


        :return: The owners of this ProjectUpdate.  # noqa: E501
        :rtype: list[int]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this ProjectUpdate.


        :param owners: The owners of this ProjectUpdate.  # noqa: E501
        :type owners: list[int]
        """

        self._owners = owners

    @property
    def reviewers(self):
        """Gets the reviewers of this ProjectUpdate.  # noqa: E501


        :return: The reviewers of this ProjectUpdate.  # noqa: E501
        :rtype: list[int]
        """
        return self._reviewers

    @reviewers.setter
    def reviewers(self, reviewers):
        """Sets the reviewers of this ProjectUpdate.


        :param reviewers: The reviewers of this ProjectUpdate.  # noqa: E501
        :type reviewers: list[int]
        """

        self._reviewers = reviewers

    @property
    def super_reviewers(self):
        """Gets the super_reviewers of this ProjectUpdate.  # noqa: E501


        :return: The super_reviewers of this ProjectUpdate.  # noqa: E501
        :rtype: list[int]
        """
        return self._super_reviewers

    @super_reviewers.setter
    def super_reviewers(self, super_reviewers):
        """Sets the super_reviewers of this ProjectUpdate.


        :param super_reviewers: The super_reviewers of this ProjectUpdate.  # noqa: E501
        :type super_reviewers: list[int]
        """

        self._super_reviewers = super_reviewers

    @property
    def junior_reviewers(self):
        """Gets the junior_reviewers of this ProjectUpdate.  # noqa: E501


        :return: The junior_reviewers of this ProjectUpdate.  # noqa: E501
        :rtype: list[int]
        """
        return self._junior_reviewers

    @junior_reviewers.setter
    def junior_reviewers(self, junior_reviewers):
        """Sets the junior_reviewers of this ProjectUpdate.


        :param junior_reviewers: The junior_reviewers of this ProjectUpdate.  # noqa: E501
        :type junior_reviewers: list[int]
        """

        self._junior_reviewers = junior_reviewers

    @property
    def type(self):
        """Gets the type of this ProjectUpdate.  # noqa: E501


        :return: The type of this ProjectUpdate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProjectUpdate.


        :param type: The type of this ProjectUpdate.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def hide_clause_review(self):
        """Gets the hide_clause_review of this ProjectUpdate.  # noqa: E501


        :return: The hide_clause_review of this ProjectUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._hide_clause_review

    @hide_clause_review.setter
    def hide_clause_review(self, hide_clause_review):
        """Sets the hide_clause_review of this ProjectUpdate.


        :param hide_clause_review: The hide_clause_review of this ProjectUpdate.  # noqa: E501
        :type hide_clause_review: bool
        """

        self._hide_clause_review = hide_clause_review

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
        if not isinstance(other, ProjectUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectUpdate):
            return True

        return self.to_dict() != other.to_dict()