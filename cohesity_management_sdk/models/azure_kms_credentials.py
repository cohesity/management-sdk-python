# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AzureKmsCredentials(object):

    """Implementation of the 'AzureKmsCredentials' model.

    TODO: type description here.


    Attributes:

        client_id (string): Specifies the client id assigned to the cluster.
        client_secret_key (string): Specifies the Secret access key needed to
            access the cloud account.
        microsoft_auth_method (MicrosoftAuthMethodEnum): Specifies
            Authentication method to be used for API calls. 'kAzureAuthNone'
            indicates no authentication. 'kAzureClientSecret' indicates a
            client authentication. 'kAzureManagedIdentity' indicates a Azure
            based authentication.
        tenant_id (string): Specifies the tenant id assigned to the cluster.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "client_id":'clientId',
        "client_secret_key":'clientSecretKey',
        "microsoft_auth_method":'microsoftAuthMethod',
        "tenant_id":'tenantId',
    }
    def __init__(self,
                 client_id=None,
                 client_secret_key=None,
                 microsoft_auth_method=None,
                 tenant_id=None,
            ):

        """Constructor for the AzureKmsCredentials class"""

        # Initialize members of the class
        self.client_id = client_id
        self.client_secret_key = client_secret_key
        self.microsoft_auth_method = microsoft_auth_method
        self.tenant_id = tenant_id

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
        client_id = dictionary.get('clientId')
        client_secret_key = dictionary.get('clientSecretKey')
        microsoft_auth_method = dictionary.get('microsoftAuthMethod')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(
            client_id,
            client_secret_key,
            microsoft_auth_method,
            tenant_id
)