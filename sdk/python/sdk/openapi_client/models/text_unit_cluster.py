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


class TextUnitCluster(object):
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
        'cluster_id': 'int',
        'name': 'str',
        'self_name': 'str',
        'description': 'str',
        'cluster_by': 'str',
        'using': 'str',
        'created_date': 'datetime',
        'text_unit_count': 'str',
        'text_unit_data': 'str'
    }

    attribute_map = {
        'pk': 'pk',
        'cluster_id': 'cluster_id',
        'name': 'name',
        'self_name': 'self_name',
        'description': 'description',
        'cluster_by': 'cluster_by',
        'using': 'using',
        'created_date': 'created_date',
        'text_unit_count': 'text_unit_count',
        'text_unit_data': 'text_unit_data'
    }

    def __init__(self, pk=None, cluster_id=None, name=None, self_name=None, description=None, cluster_by=None, using=None, created_date=None, text_unit_count=None, text_unit_data=None, local_vars_configuration=None):  # noqa: E501
        """TextUnitCluster - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pk = None
        self._cluster_id = None
        self._name = None
        self._self_name = None
        self._description = None
        self._cluster_by = None
        self._using = None
        self._created_date = None
        self._text_unit_count = None
        self._text_unit_data = None
        self.discriminator = None

        if pk is not None:
            self.pk = pk
        if cluster_id is not None:
            self.cluster_id = cluster_id
        self.name = name
        self.self_name = self_name
        self.description = description
        self.cluster_by = cluster_by
        self.using = using
        if created_date is not None:
            self.created_date = created_date
        if text_unit_count is not None:
            self.text_unit_count = text_unit_count
        if text_unit_data is not None:
            self.text_unit_data = text_unit_data

    @property
    def pk(self):
        """Gets the pk of this TextUnitCluster.  # noqa: E501


        :return: The pk of this TextUnitCluster.  # noqa: E501
        :rtype: int
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this TextUnitCluster.


        :param pk: The pk of this TextUnitCluster.  # noqa: E501
        :type pk: int
        """

        self._pk = pk

    @property
    def cluster_id(self):
        """Gets the cluster_id of this TextUnitCluster.  # noqa: E501


        :return: The cluster_id of this TextUnitCluster.  # noqa: E501
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this TextUnitCluster.


        :param cluster_id: The cluster_id of this TextUnitCluster.  # noqa: E501
        :type cluster_id: int
        """
        if (self.local_vars_configuration.client_side_validation and
                cluster_id is not None and cluster_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cluster_id is not None and cluster_id < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def name(self):
        """Gets the name of this TextUnitCluster.  # noqa: E501


        :return: The name of this TextUnitCluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TextUnitCluster.


        :param name: The name of this TextUnitCluster.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 300):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `300`")  # noqa: E501

        self._name = name

    @property
    def self_name(self):
        """Gets the self_name of this TextUnitCluster.  # noqa: E501


        :return: The self_name of this TextUnitCluster.  # noqa: E501
        :rtype: str
        """
        return self._self_name

    @self_name.setter
    def self_name(self, self_name):
        """Sets the self_name of this TextUnitCluster.


        :param self_name: The self_name of this TextUnitCluster.  # noqa: E501
        :type self_name: str
        """
        if self.local_vars_configuration.client_side_validation and self_name is None:  # noqa: E501
            raise ValueError("Invalid value for `self_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                self_name is not None and len(self_name) > 200):
            raise ValueError("Invalid value for `self_name`, length must be less than or equal to `200`")  # noqa: E501

        self._self_name = self_name

    @property
    def description(self):
        """Gets the description of this TextUnitCluster.  # noqa: E501


        :return: The description of this TextUnitCluster.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TextUnitCluster.


        :param description: The description of this TextUnitCluster.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 300):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `300`")  # noqa: E501

        self._description = description

    @property
    def cluster_by(self):
        """Gets the cluster_by of this TextUnitCluster.  # noqa: E501


        :return: The cluster_by of this TextUnitCluster.  # noqa: E501
        :rtype: str
        """
        return self._cluster_by

    @cluster_by.setter
    def cluster_by(self, cluster_by):
        """Sets the cluster_by of this TextUnitCluster.


        :param cluster_by: The cluster_by of this TextUnitCluster.  # noqa: E501
        :type cluster_by: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_by is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_by`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cluster_by is not None and len(cluster_by) > 100):
            raise ValueError("Invalid value for `cluster_by`, length must be less than or equal to `100`")  # noqa: E501

        self._cluster_by = cluster_by

    @property
    def using(self):
        """Gets the using of this TextUnitCluster.  # noqa: E501


        :return: The using of this TextUnitCluster.  # noqa: E501
        :rtype: str
        """
        return self._using

    @using.setter
    def using(self, using):
        """Sets the using of this TextUnitCluster.


        :param using: The using of this TextUnitCluster.  # noqa: E501
        :type using: str
        """
        if self.local_vars_configuration.client_side_validation and using is None:  # noqa: E501
            raise ValueError("Invalid value for `using`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                using is not None and len(using) > 20):
            raise ValueError("Invalid value for `using`, length must be less than or equal to `20`")  # noqa: E501

        self._using = using

    @property
    def created_date(self):
        """Gets the created_date of this TextUnitCluster.  # noqa: E501


        :return: The created_date of this TextUnitCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this TextUnitCluster.


        :param created_date: The created_date of this TextUnitCluster.  # noqa: E501
        :type created_date: datetime
        """

        self._created_date = created_date

    @property
    def text_unit_count(self):
        """Gets the text_unit_count of this TextUnitCluster.  # noqa: E501


        :return: The text_unit_count of this TextUnitCluster.  # noqa: E501
        :rtype: str
        """
        return self._text_unit_count

    @text_unit_count.setter
    def text_unit_count(self, text_unit_count):
        """Sets the text_unit_count of this TextUnitCluster.


        :param text_unit_count: The text_unit_count of this TextUnitCluster.  # noqa: E501
        :type text_unit_count: str
        """

        self._text_unit_count = text_unit_count

    @property
    def text_unit_data(self):
        """Gets the text_unit_data of this TextUnitCluster.  # noqa: E501


        :return: The text_unit_data of this TextUnitCluster.  # noqa: E501
        :rtype: str
        """
        return self._text_unit_data

    @text_unit_data.setter
    def text_unit_data(self, text_unit_data):
        """Sets the text_unit_data of this TextUnitCluster.


        :param text_unit_data: The text_unit_data of this TextUnitCluster.  # noqa: E501
        :type text_unit_data: str
        """

        self._text_unit_data = text_unit_data

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
        if not isinstance(other, TextUnitCluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextUnitCluster):
            return True

        return self.to_dict() != other.to_dict()