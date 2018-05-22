# coding: utf-8

"""
    Cohesity REST API

    This API provides operations for interfacing with the Cohesity Cluster. NOTE: To view the documentation on the responses, click 'Model' next to 'Example Value' and keep clicking to expand the hierarchy.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class AmazonCloudCredentials(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, access_key_id=None, region=None, secret_access_key=None, service_url=None, signature_version=None, use_https=None):
        """
        AmazonCloudCredentials - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_key_id': 'str',
            'region': 'str',
            'secret_access_key': 'str',
            'service_url': 'str',
            'signature_version': 'int',
            'use_https': 'bool'
        }

        self.attribute_map = {
            'access_key_id': 'accessKeyId',
            'region': 'region',
            'secret_access_key': 'secretAccessKey',
            'service_url': 'serviceUrl',
            'signature_version': 'signatureVersion',
            'use_https': 'useHttps'
        }

        self._access_key_id = access_key_id
        self._region = region
        self._secret_access_key = secret_access_key
        self._service_url = service_url
        self._signature_version = signature_version
        self._use_https = use_https

    @property
    def access_key_id(self):
        """
        Gets the access_key_id of this AmazonCloudCredentials.
        Specifies the access key for Amazon service account. See the Cohesity online help for the value to specify for this field based on the current S3 Compatible Vault (External Target) type. For example for Iron Mountain, specify the user name from Iron Mountain for this field.

        :return: The access_key_id of this AmazonCloudCredentials.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """
        Sets the access_key_id of this AmazonCloudCredentials.
        Specifies the access key for Amazon service account. See the Cohesity online help for the value to specify for this field based on the current S3 Compatible Vault (External Target) type. For example for Iron Mountain, specify the user name from Iron Mountain for this field.

        :param access_key_id: The access_key_id of this AmazonCloudCredentials.
        :type: str
        """

        self._access_key_id = access_key_id

    @property
    def region(self):
        """
        Gets the region of this AmazonCloudCredentials.
        Specifies the region to use for the Amazon service account.

        :return: The region of this AmazonCloudCredentials.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this AmazonCloudCredentials.
        Specifies the region to use for the Amazon service account.

        :param region: The region of this AmazonCloudCredentials.
        :type: str
        """

        self._region = region

    @property
    def secret_access_key(self):
        """
        Gets the secret_access_key of this AmazonCloudCredentials.
        Specifies the secret access key for Amazon service account. See the Cohesity online help for the value to specify for this field based on the current S3-compatible Vault (External Target) type.

        :return: The secret_access_key of this AmazonCloudCredentials.
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """
        Sets the secret_access_key of this AmazonCloudCredentials.
        Specifies the secret access key for Amazon service account. See the Cohesity online help for the value to specify for this field based on the current S3-compatible Vault (External Target) type.

        :param secret_access_key: The secret_access_key of this AmazonCloudCredentials.
        :type: str
        """

        self._secret_access_key = secret_access_key

    @property
    def service_url(self):
        """
        Gets the service_url of this AmazonCloudCredentials.
        Specifies the URL (Endpoint) for the service such as s3like.notamazon.com. This field is only significant for S3-compatible cloud services.

        :return: The service_url of this AmazonCloudCredentials.
        :rtype: str
        """
        return self._service_url

    @service_url.setter
    def service_url(self, service_url):
        """
        Sets the service_url of this AmazonCloudCredentials.
        Specifies the URL (Endpoint) for the service such as s3like.notamazon.com. This field is only significant for S3-compatible cloud services.

        :param service_url: The service_url of this AmazonCloudCredentials.
        :type: str
        """

        self._service_url = service_url

    @property
    def signature_version(self):
        """
        Gets the signature_version of this AmazonCloudCredentials.
        Specifies the version of the S3 Compliance. This field must be set to 2 or 4 and the default version is 2. This field is only significant for S3-compatible cloud services. See the Cohesity online help for the supported S3-compatible Vault (External Target) types and the value to specify for this field based on the current S3-compatible Vault (External Target) type.

        :return: The signature_version of this AmazonCloudCredentials.
        :rtype: int
        """
        return self._signature_version

    @signature_version.setter
    def signature_version(self, signature_version):
        """
        Sets the signature_version of this AmazonCloudCredentials.
        Specifies the version of the S3 Compliance. This field must be set to 2 or 4 and the default version is 2. This field is only significant for S3-compatible cloud services. See the Cohesity online help for the supported S3-compatible Vault (External Target) types and the value to specify for this field based on the current S3-compatible Vault (External Target) type.

        :param signature_version: The signature_version of this AmazonCloudCredentials.
        :type: int
        """

        self._signature_version = signature_version

    @property
    def use_https(self):
        """
        Gets the use_https of this AmazonCloudCredentials.
        Specifies whether to use http or https to connect to the service. If true, a secure connection (https) is used. This field is only significant for S3-compatible cloud services.

        :return: The use_https of this AmazonCloudCredentials.
        :rtype: bool
        """
        return self._use_https

    @use_https.setter
    def use_https(self, use_https):
        """
        Sets the use_https of this AmazonCloudCredentials.
        Specifies whether to use http or https to connect to the service. If true, a secure connection (https) is used. This field is only significant for S3-compatible cloud services.

        :param use_https: The use_https of this AmazonCloudCredentials.
        :type: bool
        """

        self._use_https = use_https

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
