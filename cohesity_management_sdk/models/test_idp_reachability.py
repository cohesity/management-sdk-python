# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TestIdpReachability(object):

    """Implementation of the 'TestIdpReachability' model.

    Specifies the parameters to test the reachability of an IdP.

    Attributes:
        issuer_id (string): Specifies the IdP provided Issuer ID for the app.
        sso_url (string): Specifies the SSO URL of the IdP service for the
            customer. This is the URL given by IdP when the customer created
            an account. Customers may use this for several clusters that are
            registered with on IdP site.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "issuer_id":'issuerId',
        "sso_url":'ssoUrl'
    }

    def __init__(self,
                 issuer_id=None,
                 sso_url=None):
        """Constructor for the TestIdpReachability class"""

        # Initialize members of the class
        self.issuer_id = issuer_id
        self.sso_url = sso_url


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
        issuer_id = dictionary.get('issuerId')
        sso_url = dictionary.get('ssoUrl')

        # Return an object of this model
        return cls(issuer_id,
                   sso_url)


