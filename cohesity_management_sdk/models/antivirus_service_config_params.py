# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AntivirusServiceConfigParams(object):

    """Implementation of the 'AntivirusServiceConfigParams' model.

    Specifies the parameters for an Antivirus service provider.

    Attributes:
        description (string): Specifies the description of the Antivirus
            service. This could be any additional information admin might
            associate with the Antivirus service.
        icap_uri (string): Specifies the ICAP uri for this Antivirus service.
            It is of the form icap://<ip-address>[:<port>]/<service>

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "icap_uri":'icapUri',
        "description":'description'
    }

    def __init__(self,
                 icap_uri=None,
                 description=None):
        """Constructor for the AntivirusServiceConfigParams class"""

        # Initialize members of the class
        self.description = description
        self.icap_uri = icap_uri


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
        icap_uri = dictionary.get('icapUri')
        description = dictionary.get('description')

        # Return an object of this model
        return cls(icap_uri,
                   description)


