# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AwsKmsUpdateParams(object):

    """Implementation of the 'AwsKmsUpdateParams' model.

    AwsKmsUpdateParams to define AWS KMS config.

    Attributes:
        access_key_id (string): Access key id needed to access the cloud
            account. When update cluster config, should encrypte accessKeyId
            with cluster ID.
        ca_certificate_path (string): Specify the ca certificate path.
        iam_role_arn (string): Specifies the IAM role which will be used to
            access the security credentials required for API calls.
        secret_access_key (string): Secret access key needed to access the
            cloud account. This is encrypted with the cluster id.
        verify_ssl (bool): Specify whether to verify SSL when connect with AWS
            KMS. Default is true.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_key_id":'accessKeyId',
        "ca_certificate_path":'caCertificatePath',
        "iam_role_arn":'iamRoleArn',
        "secret_access_key":'secretAccessKey',
        "verify_ssl":'verifySSL'
    }

    def __init__(self,
                 access_key_id=None,
                 ca_certificate_path=None,
                 iam_role_arn=None,
                 secret_access_key=None,
                 verify_ssl=None):
        """Constructor for the AwsKmsUpdateParams class"""

        # Initialize members of the class
        self.access_key_id = access_key_id
        self.ca_certificate_path = ca_certificate_path
        self.iam_role_arn = iam_role_arn
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
        ca_certificate_path = dictionary.get('caCertificatePath')
        iam_role_arn = dictionary.get('iamRoleArn')
        secret_access_key = dictionary.get('secretAccessKey')
        verify_ssl = dictionary.get('verifySSL')

        # Return an object of this model
        return cls(access_key_id,
                   ca_certificate_path,
                   iam_role_arn,
                   secret_access_key,
                   verify_ssl)


