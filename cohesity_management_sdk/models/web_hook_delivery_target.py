# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class WebHookDeliveryTarget(object):

    """Implementation of the 'WebHookDeliveryTarget' model.

    WebHookDeliveryTarget
    Specifies the external api url to hit along with the related options for
    it.

    Attributes:
        curl_options (string): Specifies curl options used to invoke external
            api url defined above.
        external_api_url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "curl_options":'curlOptions',
        "external_api_url":'externalApiUrl'
    }

    def __init__(self,
                 curl_options=None,
                 external_api_url=None):
        """Constructor for the WebHookDeliveryTarget class"""

        # Initialize members of the class
        self.curl_options = curl_options
        self.external_api_url = external_api_url


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
        curl_options = dictionary.get('curlOptions')
        external_api_url = dictionary.get('externalApiUrl')

        # Return an object of this model
        return cls(curl_options,
                   external_api_url)


