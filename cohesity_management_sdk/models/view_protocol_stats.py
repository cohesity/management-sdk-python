# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ViewProtocolStats(object):

    """Implementation of the 'ViewProtocolStats' model.

    Specifies the View Protocol stats.

    Attributes:
        protocols (list of ProtocolViewProtocolStatsEnum): Specifies the
            protocols supported on these Views.
        size_bytes (long|int): Specifies the size of all the Views in bytes
            which are using the specified protocol.
        view_count (long|int): Specifies the number of Views which are using
            the specified protocol.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protocols":'protocols',
        "size_bytes":'sizeBytes',
        "view_count":'viewCount'
    }

    def __init__(self,
                 protocols=None,
                 size_bytes=None,
                 view_count=None):
        """Constructor for the ViewProtocolStats class"""

        # Initialize members of the class
        self.protocols = protocols
        self.size_bytes = size_bytes
        self.view_count = view_count


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
        protocols = dictionary.get('protocols')
        size_bytes = dictionary.get('sizeBytes')
        view_count = dictionary.get('viewCount')

        # Return an object of this model
        return cls(protocols,
                   size_bytes,
                   view_count)


