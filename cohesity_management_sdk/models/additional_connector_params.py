# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.o365_region_proto

class AdditionalConnectorParams(object):

    """Implementation of the 'AdditionalConnectorParams' model.

    Message that encapsulates the additional connector params to establish a
    connection with a particular environment.

    Attributes:
        o365_region (O365RegionProto): Optional o365_region proto to store the
            region info to be used while making ews/graph api calls in o365
            adapter.
        use_outlook_ews_oauth (bool): Whether OAuth should be used for
            authentication with EWS API (outlook backup), applicable only for
            Exchange Online.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "o365_region": 'o365Region',
        "use_outlook_ews_oauth": 'useOutlookEwsOauth'
    }

    def __init__(self,
                 o365_region=None,
                 use_outlook_ews_oauth=None):
        """Constructor for the AdditionalConnectorParams class"""

        # Initialize members of the class
        self.o365_region = o365_region
        self.use_outlook_ews_oauth = use_outlook_ews_oauth


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
        o365_region = cohesity_management_sdk.models.o365_region_proto.O365RegionProto.from_dictionary(dictionary.get('o365Region', None)) if dictionary.get('o365Region', None) else None
        use_outlook_ews_oauth = dictionary.get('useOutlookEwsOauth', None)

        # Return an object of this model
        return cls(o365_region,
                   use_outlook_ews_oauth)


