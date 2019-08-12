# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class DeliveryRuleProtoDeliveryTarget(object):

    """Implementation of the 'DeliveryRuleProto_DeliveryTarget' model.

    Delivery targets for the notifications. For now only email delivery is
    supported. In future, we can potentially add other delivery targets such
    as paging, SMS, etc.

    Attributes:
        email_address (string): List of email addresses to send
            notifications.
        external_api_curl_options (string): Specifies the curl options used to
            invoke above rest external api.
        external_api_url (string): Specifies the external api to be invoked
            when an alert matching this rule is raised.
        locale (string): Locale for the delivery target.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email_address":'emailAddress',
        "external_api_curl_options":'externalApiCurlOptions',
        "external_api_url":'externalApiUrl',
        "locale":'locale'
    }

    def __init__(self,
                 email_address=None,
                 external_api_curl_options=None,
                 external_api_url=None,
                 locale=None):
        """Constructor for the DeliveryRuleProtoDeliveryTarget class"""

        # Initialize members of the class
        self.email_address = email_address
        self.external_api_curl_options = external_api_curl_options
        self.external_api_url = external_api_url
        self.locale = locale


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
        email_address = dictionary.get('emailAddress')
        external_api_curl_options = dictionary.get('externalApiCurlOptions')
        external_api_url = dictionary.get('externalApiUrl')
        locale = dictionary.get('locale')

        # Return an object of this model
        return cls(email_address,
                   external_api_curl_options,
                   external_api_url,
                   locale)


