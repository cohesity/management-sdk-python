# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class GoogleCloudCredentials(object):

    """Implementation of the 'GoogleCloudCredentials' model.

    Specifies the cloud credentials to connect to a Google service account.


    Attributes:

        client_email_address (string): Specifies the client email address used
            to access Google Cloud Storage.
        client_private_key (string): Specifies the private key used to access
            Google Cloud Storage that is generated when the service account is
            created.
        project_id (string): Specifies the project id of an existing Google
            Cloud project to store objects.
        tier_type (TierTypeGoogleCloudCredentialsEnum): Specifies the storage
            class of GCP. GoogleTierType specifies the storage class for
            Google. 'kGoogleStandard' indicates a tier type of Google
            properties. 'kGoogleNearline' indicates a tier type of Google
            properties that is not accessed frequently. 'kGoogleColdline'
            indicates a tier type of Google properties that is rarely accessed.
            'kGoogleRegional' indicates a tier type of Google properties that
            stores frequently accessed data in the same region.
            'kGoogleMultiRegional' indicates a tier type of Google properties
            that is frequently accessed ("hot" objects) around the world.
        tiers (list of string): Specifies the list of all tiers for Google
            account.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "client_email_address":'clientEmailAddress',
        "client_private_key":'clientPrivateKey',
        "project_id":'projectId',
        "tier_type":'tierType',
        "tiers":'tiers',
    }
    def __init__(self,
                 client_email_address=None,
                 client_private_key=None,
                 project_id=None,
                 tier_type=None,
                 tiers=None,
            ):

        """Constructor for the GoogleCloudCredentials class"""

        # Initialize members of the class
        self.client_email_address = client_email_address
        self.client_private_key = client_private_key
        self.project_id = project_id
        self.tier_type = tier_type
        self.tiers = tiers

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
        client_email_address = dictionary.get('clientEmailAddress')
        client_private_key = dictionary.get('clientPrivateKey')
        project_id = dictionary.get('projectId')
        tier_type = dictionary.get('tierType')
        tiers = dictionary.get("tiers")

        # Return an object of this model
        return cls(
            client_email_address,
            client_private_key,
            project_id,
            tier_type,
            tiers
)