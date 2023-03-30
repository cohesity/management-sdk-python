# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AwsKmsConfiguration(object):

    """Implementation of the 'AwsKmsConfiguration' model.

    TODO: type description here.


    Attributes:

        access_key_id (string): Access key id needed to access the cloud
            account. When update cluster config, should encrypte accessKeyId
            with cluster ID.
        auth_method (AuthMethodEnum): Specifies the authentication method to be
            used for API calls. Specifies the authentication method to be used
            for API calls. 'kUseIAMUser' indicates a user based authentication.
            'kUseIAMRole' indicates a role based authentication, used only for
            AWS CE. 'kUseHelios' indicates a Helios based authentication.
        ca_certificate (string): Specify the ca certificate path.
        cmk_alias (string): The string alias of the CMK.
        cmk_arn (string): The Amazon Resource Number of AWS Customer Managed
            Key.
        cmk_key_id (string): AWS keyId, and alias. Only need one of them to
            connect AWS. Alias is better, because keyId maybe rotated by AWS.
            The unique key id of the CMK.
        iam_role_arn (string): Specifies the IAM role which will be used to
            access the security credentials required for API calls.
        region (string): AWS region, e.g. us-east-1, us-west-2, for the AWS
            Glacier service to be used to authenticate resources within this
            region by the configured AWS account.
        secret_access_key (string): Secret access key needed to access the
            cloud account. This is encrypted with the cluster id.
        verify_s_s_l (bool): Specify whether to verify SSL when connect with
            AWS KMS. Default is true.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "access_key_id":'accessKeyId',
        "auth_method":'authMethod',
        "ca_certificate":'caCertificate',
        "cmk_alias":'cmkAlias',
        "cmk_arn":'cmkArn',
        "cmk_key_id":'cmkKeyId',
        "iam_role_arn":'iamRoleArn',
        "region":'region',
        "secret_access_key":'secretAccessKey',
        "verify_s_s_l":'verifySSL',
    }
    def __init__(self,
                 access_key_id=None,
                 auth_method=None,
                 ca_certificate=None,
                 cmk_alias=None,
                 cmk_arn=None,
                 cmk_key_id=None,
                 iam_role_arn=None,
                 region=None,
                 secret_access_key=None,
                 verify_s_s_l=None,
            ):

        """Constructor for the AwsKmsConfiguration class"""

        # Initialize members of the class
        self.access_key_id = access_key_id
        self.auth_method = auth_method
        self.ca_certificate = ca_certificate
        self.cmk_alias = cmk_alias
        self.cmk_arn = cmk_arn
        self.cmk_key_id = cmk_key_id
        self.iam_role_arn = iam_role_arn
        self.region = region
        self.secret_access_key = secret_access_key
        self.verify_s_s_l = verify_s_s_l

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
        auth_method = dictionary.get('authMethod')
        ca_certificate = dictionary.get('caCertificate')
        cmk_alias = dictionary.get('cmkAlias')
        cmk_arn = dictionary.get('cmkArn')
        cmk_key_id = dictionary.get('cmkKeyId')
        iam_role_arn = dictionary.get('iamRoleArn')
        region = dictionary.get('region')
        secret_access_key = dictionary.get('secretAccessKey')
        verify_s_s_l = dictionary.get('verifySSL')

        # Return an object of this model
        return cls(
            access_key_id,
            auth_method,
            ca_certificate,
            cmk_alias,
            cmk_arn,
            cmk_key_id,
            iam_role_arn,
            region,
            secret_access_key,
            verify_s_s_l
)