# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.c_2_s_access_portal

class AmazonCloudCredentials(object):

    """Implementation of the 'AmazonCloudCredentials' model.

    Specifies the cloud credentials to connect to a Amazon
    service account. Glacier, S3, and S3-compatible clouds all use these
    credentials.

    Attributes:
        access_key_id (string): Specifies the access key for Amazon service
            account. See the Cohesity online help for the value to specify for
            this field based on the current S3 Compatible Vault (External
            Target) type. For example for Iron Mountain, specify the user name
            from Iron Mountain for this field.
        c_2_s_access_portal (C2SAccessPortal): Specifies information required
            to connect to CAP to get AWS credentials. C2SAccessPortal(CAP) is
            AWS commercial cloud service access portal.
        region (string): Specifies the region to use for the Amazon service
            account.
        secret_access_key (string): Specifies the secret access key for Amazon
            service account. See the Cohesity online help for the value to
            specify for this field based on the current S3-compatible Vault
            (External Target) type.
        service_url (string): Specifies the URL (Endpoint) for the service
            such as s3like.notamazon.com. This field is only significant for
            S3-compatible cloud services.
        signature_version (int): Specifies the version of the S3 Compliance.
            This field must be set to 2 or 4 and the default version is 2.
            This field is only significant for S3-compatible cloud services.
            See the Cohesity online help for the supported S3-compatible Vault
            (External Target) types and the value to specify for this field
            based on the current S3-compatible Vault (External Target) type.
        tier_type (TierTypeEnum): Specifies the storage class of AWS.
            AmazonTierType specifies the storage class for AWS.
            'kAmazonS3Standard' indicates a tier type of Amazon properties
            that is accessed frequently. 'kAmazonS3StandardIA' indicates a
            tier type of Amazon properties that is accessed less frequently,
            but requires rapid access when needed. 'kAmazonGlacier' indicates
            a tier type of Amazon properties that is accessed rarely.
            'kAmazonS3OneZoneIA' indicates a tier type of Amazon properties
            for long-lived, but less frequently accessed data.
            'kAmazonS3IntelligentTiering' indicates a tier type of Amazon
            properties for data with unknown or changing access patterns.
            'kAmazonS3GlacierDeepArchive' indicates a tier type of Amazon
            properties for data that provides secure, durable object storage
            for long-term data retention and digital preservation.
        use_https (bool): Specifies whether to use http or https to connect to
            the service. If true, a secure connection (https) is used. This
            field is only significant for S3-compatible cloud services.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_key_id":'accessKeyId',
        "c_2_s_access_portal":'c2sAccessPortal',
        "region":'region',
        "secret_access_key":'secretAccessKey',
        "service_url":'serviceUrl',
        "signature_version":'signatureVersion',
        "tier_type":'tierType',
        "use_https":'useHttps'
    }

    def __init__(self,
                 access_key_id=None,
                 c_2_s_access_portal=None,
                 region=None,
                 secret_access_key=None,
                 service_url=None,
                 signature_version=None,
                 tier_type=None,
                 use_https=None):
        """Constructor for the AmazonCloudCredentials class"""

        # Initialize members of the class
        self.access_key_id = access_key_id
        self.c_2_s_access_portal = c_2_s_access_portal
        self.region = region
        self.secret_access_key = secret_access_key
        self.service_url = service_url
        self.signature_version = signature_version
        self.tier_type = tier_type
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
        access_key_id = dictionary.get('accessKeyId')
        c_2_s_access_portal = cohesity_management_sdk.models.c_2_s_access_portal.C2SAccessPortal.from_dictionary(dictionary.get('c2sAccessPortal')) if dictionary.get('c2sAccessPortal') else None
        region = dictionary.get('region')
        secret_access_key = dictionary.get('secretAccessKey')
        service_url = dictionary.get('serviceUrl')
        signature_version = dictionary.get('signatureVersion')
        tier_type = dictionary.get('tierType')
        use_https = dictionary.get('useHttps')

        # Return an object of this model
        return cls(access_key_id,
                   c_2_s_access_portal,
                   region,
                   secret_access_key,
                   service_url,
                   signature_version,
                   tier_type,
                   use_https)


