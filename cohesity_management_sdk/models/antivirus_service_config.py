# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AntivirusServiceConfig(object):

    """Implementation of the 'AntivirusServiceConfig' model.

    Specifies configuration settings for antivirus service provider.

    Attributes:
        description (string): Specifies the description of the Antivirus
            service. This could be any additional information admin might
            associate with the Antivirus service.
        icap_uri (string): Specifies the ICAP uri for this Antivirus service.
            It is of the form icap://<ip-address>[:<port>]/<service>
        tag (string): Specifies the tag of antivirus service. This is
            service-specific "cookie" sent from Antivirus server to clients
            that represents a service's current state. This tag validates that
            previous Antivirus server responses can still be considered fresh
            by an Antivirus client that may be caching them. If a change on
            the AV server invalidates previous responses, the AV server can
            invalidate portions of the Antivirus client's cache by changing
            its service tag.
        tag_id (long|int): Specifies the tag Id of antivirus service.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "icap_uri":'icapUri',
        "description":'description',
        "tag":'tag',
        "tag_id":'tagId'
    }

    def __init__(self,
                 icap_uri=None,
                 description=None,
                 tag=None,
                 tag_id=None):
        """Constructor for the AntivirusServiceConfig class"""

        # Initialize members of the class
        self.description = description
        self.icap_uri = icap_uri
        self.tag = tag
        self.tag_id = tag_id


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
        tag = dictionary.get('tag')
        tag_id = dictionary.get('tagId')

        # Return an object of this model
        return cls(icap_uri,
                   description,
                   tag,
                   tag_id)


