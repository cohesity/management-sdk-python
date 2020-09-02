# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class AwsKmsConfiguration(object):

    """Implementation of the 'AwsKmsConfiguration' model.

    AwsKmsConfiguration to define AWS KMS config.

    Attributes:
        access_key_id (string): Access key id needed to access the cloud
            account. When update cluster config, should encrypte
            accessKeyId with cluster ID.
        ca_certificate (string): Specify the ca certificate path.
        cmk_alias (string): The string alias of the CMK.
        cmk_arn (string): The Amazon Resource Number of AWS Customer Managed
            Key.
        cmk_key_id (string): AWS keyId, and alias.
            Only need one of them to connect AWS.
            Alias is better, because keyId maybe rotated by AWS.
            The unique key id of the CMK.
        region (string): AWS region, e.g. us-east-1, us-west-2, for the AWS
            Glacier service to be used to authenticate resources within this
            region by the configured AWS account.
        secret_access_key (string): Secret access key needed to access the
            cloud account. This is encrypted with the cluster id.
        verify_ssl (bool): Specify whether to verify SSL when connect with
            AWS KMS. Default is true.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_key_id":'accessKeyId',
        "ca_certificate":'caCertificate',
        "cmk_alias":'cmkAlias',
        "cmk_arn":'cmkArn',
        "cmk_key_id":'cmkKeyId',
        "region":'region',
        "secret_access_key":'secretAccessKey',
        "verify_ssl":'verifySSL'
    }

    def __init__(self,
                 access_key_id=None,
                 ca_certificate=None,
                 cmk_alias=None,
                 cmk_arn=None,
                 cmk_key_id=None,
                 region=None,
                 secret_access_key=None,
                 verify_ssl=None):
        """Constructor for the AwsKmsConfiguration class"""

        # Initialize members of the class
        self.access_key_id = access_key_id
        self.ca_certificate = ca_certificate
        self.cmk_alias = cmk_alias
        self.cmk_arn = cmk_arn
        self.cmk_key_id = cmk_key_id
        self.region = region
        self.secret_access_key = secret_access_key
        self.verify_ssl = verify_ssl


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        access_key_id = dictionary.get('accessKeyId')
        ca_certificate = dictionary.get('caCertificate')
        cmk_alias = dictionary.get('cmkAlias')
        cmk_arn = dictionary.get('cmkArn')
        cmk_key_id = dictionary.get('cmkKeyId')
        region = dictionary.get('region')
        secret_access_key = dictionary.get('secretAccessKey')
        verify_ssl = dictionary.get('verifySSL')

        # Return an object of this model
        return cls(access_key_id,
                   ca_certificate,
                   cmk_alias,
                   cmk_arn,
                   cmk_key_id,
                   region,
                   secret_access_key,
                   verify_ssl)


