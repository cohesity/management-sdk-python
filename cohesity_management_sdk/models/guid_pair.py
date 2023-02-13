# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GuidPair(object):

    """Implementation of the 'GuidPair' model.

    Represents the guid pair of an AD Object.

    Attributes:
        dest_guid (string): Specifies the guid of an AD object in the
            Production AD.
        source_guid (string): Specifies the guid of an AD object in the
            Snapshot AD.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dest_guid":'destGuid',
        "source_guid":'sourceGuid'
    }

    def __init__(self,
                 dest_guid=None,
                 source_guid=None):
        """Constructor for the GuidPair class"""

        # Initialize members of the class
        self.dest_guid = dest_guid
        self.source_guid = source_guid


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
        dest_guid = dictionary.get('destGuid')
        source_guid = dictionary.get('sourceGuid')

        # Return an object of this model
        return cls(dest_guid,
                   source_guid)


