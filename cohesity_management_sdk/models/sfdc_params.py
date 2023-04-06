# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SfdcParams(object):

    """Implementation of the 'SfdcParams' model.

    Specifies an Object containing information about a registered Salesforce
    source.


    Attributes:

        access_token (string): Token that will be used in subsequent api
            requests.
        concurrent_api_requests_limit (long|int): Specifies the maximum number
            of concurrent API requests allowed for salesforce.
        consumer_key (string): Consumer key from the connected app in Sfdc.
        consumer_secret (string): Consumer secret from the connected app in
            Sfdc.
        daily_api_limit (long|int): Maximum daily api limit
        endpoint (string): Sfdc Endpoint URL.
        endpoint_type (EndpointTypeEnum): Specifies the Environment type for
            salesforce. 'PROD' 'SANDBOX' 'OTHER'
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
        "concurrent_api_requests_limit":'concurrentApiRequestsLimit',
        "consumer_key":'consumerKey',
        "consumer_secret":'consumerSecret',
        "daily_api_limit":'dailyApiLimit',
        "endpoint":'endpoint',
        "endpoint_type":'endpointType',
        "metadata_endpoint_url":'metadataEndpointUrl',
        "refresh_token":'refreshToken',
        "soap_endpoint_url":'soapEndpointUrl',
        "use_bulk_api":'useBulkApi',
    }
    def __init__(self,
                 access_token=None,
                 concurrent_api_requests_limit=None,
                 consumer_key=None,
                 consumer_secret=None,
                 daily_api_limit=None,
                 endpoint=None,
                 endpoint_type=None,
                 metadata_endpoint_url=None,
                 refresh_token=None,
                 soap_endpoint_url=None,
                 use_bulk_api=None,
            ):

        """Constructor for the SfdcParams class"""

        # Initialize members of the class
        self.access_token = access_token
        self.concurrent_api_requests_limit = concurrent_api_requests_limit
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.daily_api_limit = daily_api_limit
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
        concurrent_api_requests_limit = dictionary.get('concurrentApiRequestsLimit')
        consumer_key = dictionary.get('consumerKey')
        consumer_secret = dictionary.get('consumerSecret')
        daily_api_limit = dictionary.get('dailyApiLimit')
        endpoint = dictionary.get('endpoint')
        endpoint_type = dictionary.get('endpointType')
        metadata_endpoint_url = dictionary.get('metadataEndpointUrl')
        refresh_token = dictionary.get('refreshToken')
        soap_endpoint_url = dictionary.get('soapEndpointUrl')
        use_bulk_api = dictionary.get('useBulkApi')

        # Return an object of this model
        return cls(
            access_token,
            concurrent_api_requests_limit,
            consumer_key,
            consumer_secret,
            daily_api_limit,
            endpoint,
            endpoint_type,
            metadata_endpoint_url,
            refresh_token,
            soap_endpoint_url,
            use_bulk_api
)