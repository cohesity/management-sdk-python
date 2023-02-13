# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VmwareObjectId(object):

    """Implementation of the 'VMwareObjectId' model.

    Specifies a unique Protection Source id across Cohesity Clusters.
    It is derived from the id of the VMware Protection Source.

    Attributes:
        mor_item (string): Specifies the Managed Object Reference Item.
        mor_type (string): Specifies the Managed Object Reference Type.
        uuid (string): Specifies a Universally Unique Identifier (UUID) of a
            VMware Object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mor_item":'morItem',
        "mor_type":'morType',
        "uuid":'uuid'
    }

    def __init__(self,
                 mor_item=None,
                 mor_type=None,
                 uuid=None):
        """Constructor for the VmwareObjectId class"""

        # Initialize members of the class
        self.mor_item = mor_item
        self.mor_type = mor_type
        self.uuid = uuid


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
        mor_item = dictionary.get('morItem')
        mor_type = dictionary.get('morType')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(mor_item,
                   mor_type,
                   uuid)


