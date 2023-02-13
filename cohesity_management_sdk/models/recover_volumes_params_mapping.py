# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RecoverVolumesParamsMapping(object):

    """Implementation of the 'RecoverVolumesParams_Mapping' model.

    TODO: type model description here.

    Attributes:
        dst_guid (string): The destination, pertains to the newly rebuilt
            system.
        src_guid (string): The source, pertains to the original backup.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dst_guid":'dstGuid',
        "src_guid":'srcGuid'
    }

    def __init__(self,
                 dst_guid=None,
                 src_guid=None):
        """Constructor for the RecoverVolumesParamsMapping class"""

        # Initialize members of the class
        self.dst_guid = dst_guid
        self.src_guid = src_guid


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
        dst_guid = dictionary.get('dstGuid')
        src_guid = dictionary.get('srcGuid')

        # Return an object of this model
        return cls(dst_guid,
                   src_guid)


