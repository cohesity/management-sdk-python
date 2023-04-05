# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.c_2_s_access_portal


class AmazonCloudCredentials(object):

    """Implementation of the 'AmazonCloudCredentials' model.

    Specifies the cloud credentials to connect to a Amazon service account.
    Glacier, S3, and S3-compatible clouds all use these credentials.


    Attributes:

        is_lambda_based_g_c_enabled (bool): Specifies whether this vault
            supports AWS Lambda based GC. A Lambda function needs to be
            deployed in the customer's AWS environment or the IAM user should
            have permissions to create one.
        access_key_id (string): Specifies the access key for Amazon service
            account. See the Cohesity online help for the value to specify for
            this field based on the current S3 Compatible Vault (External
            Target) type. For example for Iron Mountain, specify the user name
            from Iron Mountain for this field.
        auth_method (AuthMethodEnum): Specifies the auth method used for the
            request See the Cohesity online help for the value to specify for
            this field based on the current S3-compatible Vault (External
            Target) type. Specifies the authentication method to be used for
            API calls. 'kUseIAMUser' indicates a user based authentication.
            'kUseIAMRole' indicates a role based authentication, used only for
            AWS CE. 'kUseHelios' indicates a Helios based authentication.
        c_2_s_access_portal (C2SAccessPortal): Specifies the C2S Access Portal
            (CAP) which is used to get the aws credentials in Amazon Commercial
            Cloud Service(C2S).
        credential_blob (string): Specifies the credential blob to authenticate
            with credential endpoint.
        credential_endpoint (string): Specifies the credential process that
            generates the security token.
        iam_role_arn (string): Specifies the iam role arn Amazon service
            account. See the Cohesity online help for the value to specify for
            this field based on the current S3-compatible Vault (External
            Target) type.
        read_only_iam_role_arn (string): Specifies a read-only iam role arn
            Amazon service account. See the Cohesity online help for the value
            to specify for this field based on the current S3-compatible Vault
            (External Target) type.
        region (string): Specifies the region to use for the Amazon service
            account.
        secret_access_key (string): Specifies the secret access key for Amazon
            service account. See the Cohesity online help for the value to
            specify for this field based on the current S3-compatible Vault
            (External Target) type.
        service_url (string): Specifies the URL (Endpoint) for the service such
            as s3like.notamazon.com. This field is only significant for
            S3-compatible cloud services.
        signature_version (int): Specifies the version of the S3 Compliance.
            This field must be set to 2 or 4 and the default version is 2. This
            field is only significant for S3-compatible cloud services. See the
            Cohesity online help for the supported S3-compatible Vault
            (External Target) types and the value to specify for this field
            based on the current S3-compatible Vault (External Target) type.
        tier_type (TierTypeAmazonCloudCredentialsEnum): Specifies the storage
            class of AWS. AmazonTierType specifies the storage class for AWS.
            'kAmazonS3Standard' indicates a tier type of Amazon properties that
            is accessed frequently. 'kAmazonS3StandardIA' indicates a tier type
            of Amazon properties that is accessed less frequently, but requires
            rapid access when needed. 'kAmazonGlacier' indicates a tier type of
            Amazon properties that is accessed rarely. 'kAmazonS3OneZoneIA'
            indicates a tier type of Amazon properties for long-lived, but less
            frequently accessed data. 'kAmazonS3IntelligentTiering' indicates a
            tier type of Amazon properties for data with unknown or changing
            access patterns. 'kAmazonS3Glacier' indicates a tier type of Amazon
            properties for data that provides secure, durable object storage
            for long-term data retention and digital preservation. It provides
            three options for access to archives, from a few minutes to several
            hours. 'kAmazonS3GlacierDeepArchive' indicates a tier type of
            Amazon properties for data that provides secure, durable object
            storage for long-term data retention and digital preservation. It
            provides two access options ranging from 12 to 48 hours.
        tiers (list of string): Specifies the list of all tiers for Amazon
            account.
        use_https (bool): Specifies whether to use http or https to connect to
            the service. If true, a secure connection (https) is used. This
            field is only significant for S3-compatible cloud services.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_lambda_based_g_c_enabled":'IsLambdaBasedGCEnabled',
        "access_key_id":'accessKeyId',
        "auth_method":'authMethod',
        "c_2_s_access_portal":'c2sAccessPortal',
        "credential_blob":'credentialBlob',
        "credential_endpoint":'credentialEndpoint',
        "iam_role_arn":'iamRoleArn',
        "read_only_iam_role_arn":'readOnlyIamRoleArn',
        "region":'region',
        "secret_access_key":'secretAccessKey',
        "service_url":'serviceUrl',
        "signature_version":'signatureVersion',
        "tier_type":'tierType',
        "tiers":'tiers',
        "use_https":'useHttps',
    }
    def __init__(self,
                 is_lambda_based_g_c_enabled=None,
                 access_key_id=None,
                 auth_method=None,
                 c_2_s_access_portal=None,
                 credential_blob=None,
                 credential_endpoint=None,
                 iam_role_arn=None,
                 read_only_iam_role_arn=None,
                 region=None,
                 secret_access_key=None,
                 service_url=None,
                 signature_version=None,
                 tier_type=None,
                 tiers=None,
                 use_https=None,
            ):

        """Constructor for the AmazonCloudCredentials class"""

        # Initialize members of the class
        self.is_lambda_based_g_c_enabled = is_lambda_based_g_c_enabled
        self.access_key_id = access_key_id
        self.auth_method = auth_method
        self.c_2_s_access_portal = c_2_s_access_portal
        self.credential_blob = credential_blob
        self.credential_endpoint = credential_endpoint
        self.iam_role_arn = iam_role_arn
        self.read_only_iam_role_arn = read_only_iam_role_arn
        self.region = region
        self.secret_access_key = secret_access_key
        self.service_url = service_url
        self.signature_version = signature_version
        self.tier_type = tier_type
        self.tiers = tiers
        self.use_https = use_https

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
        is_lambda_based_g_c_enabled = dictionary.get('IsLambdaBasedGCEnabled')
        access_key_id = dictionary.get('accessKeyId')
        auth_method = dictionary.get('authMethod')
        c_2_s_access_portal = cohesity_management_sdk.models.c_2_s_access_portal.C2SAccessPortal.from_dictionary(dictionary.get('c2sAccessPortal')) if dictionary.get('c2sAccessPortal') else None
        credential_blob = dictionary.get('credentialBlob')
        credential_endpoint = dictionary.get('credentialEndpoint')
        iam_role_arn = dictionary.get('iamRoleArn')
        read_only_iam_role_arn = dictionary.get('readOnlyIamRoleArn')
        region = dictionary.get('region')
        secret_access_key = dictionary.get('secretAccessKey')
        service_url = dictionary.get('serviceUrl')
        signature_version = dictionary.get('signatureVersion')
        tier_type = dictionary.get('tierType')
        tiers = dictionary.get("tiers")
        use_https = dictionary.get('useHttps')

        # Return an object of this model
        return cls(
            is_lambda_based_g_c_enabled,
            access_key_id,
            auth_method,
            c_2_s_access_portal,
            credential_blob,
            credential_endpoint,
            iam_role_arn,
            read_only_iam_role_arn,
            region,
            secret_access_key,
            service_url,
            signature_version,
            tier_type,
            tiers,
            use_https
)