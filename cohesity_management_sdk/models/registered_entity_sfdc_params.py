# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.credentials


class RegisteredEntitySfdcParams(object):

    """Implementation of the 'RegisteredEntitySfdcParams' model.

    Contains all params specified by the user while registering a Sfdc source.


    Attributes:

        access_token (string): Token that will be used in subsequent api
            requests.
        api_limit (long|int): Maximum daily api limit
        consumer_key (string): Consumer key from the connected app in Sfdc.
        consumer_secret (string): Consumer secret from the connected app in
            Sfdc.
        credentials (Credentials): Credentials that will be used to log into
            the application environment. Remove this field later.
        endpoint (string): Sfdc instance_url. Rename to instance_url later.
        endpoint_type (int): TODO: Type description here.
        metadata_endpoint_url (string): Metadata endpoint url. All metadata
            requests must be made to this url.
        refresh_token (string): Token that will be used to refresh the access
            token.
        soap_endpoint_url (string): Soap endpoint url. All soap requests must
            be made to this url.
        use_bulk_api (bool): use bulk api if set to true
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "access_token":'accessToken',
        "api_limit":'apiLimit',
        "consumer_key":'consumerKey',
        "consumer_secret":'consumerSecret',
        "credentials":'credentials',
        "endpoint":'endpoint',
        "endpoint_type":'endpointType',
        "metadata_endpoint_url":'metadataEndpointUrl',
        "refresh_token":'refreshToken',
        "soap_endpoint_url":'soapEndpointUrl',
        "use_bulk_api":'useBulkApi',
    }
    def __init__(self,
                 access_token=None,
                 api_limit=None,
                 consumer_key=None,
                 consumer_secret=None,
                 credentials=None,
                 endpoint=None,
                 endpoint_type=None,
                 metadata_endpoint_url=None,
                 refresh_token=None,
                 soap_endpoint_url=None,
                 use_bulk_api=None,
            ):

        """Constructor for the RegisteredEntitySfdcParams class"""

        # Initialize members of the class
        self.access_token = access_token
        self.api_limit = api_limit
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.credentials = credentials
        self.endpoint = endpoint
        self.endpoint_type = endpoint_type
        self.metadata_endpoint_url = metadata_endpoint_url
        self.refresh_token = refresh_token
        self.soap_endpoint_url = soap_endpoint_url
        self.use_bulk_api = use_bulk_api

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
        access_token = dictionary.get('accessToken')
        api_limit = dictionary.get('apiLimit')
        consumer_key = dictionary.get('consumerKey')
        consumer_secret = dictionary.get('consumerSecret')
        credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('credentials')) if dictionary.get('credentials') else None
        endpoint = dictionary.get('endpoint')
        endpoint_type = dictionary.get('endpointType')
        metadata_endpoint_url = dictionary.get('metadataEndpointUrl')
        refresh_token = dictionary.get('refreshToken')
        soap_endpoint_url = dictionary.get('soapEndpointUrl')
        use_bulk_api = dictionary.get('useBulkApi')

        # Return an object of this model
        return cls(
            access_token,
            api_limit,
            consumer_key,
            consumer_secret,
            credentials,
            endpoint,
            endpoint_type,
            metadata_endpoint_url,
            refresh_token,
            soap_endpoint_url,
            use_bulk_api
)