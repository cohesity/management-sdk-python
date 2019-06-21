# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class TagAttribute(object):

    """Implementation of the 'TagAttribute' model.

    Specifies a VMware tag.

    Attributes:
        id (long|int): Specifies the Coheisty id of the VM tag.
        name (string): Specifies the VMware name of the VM tag.
        uuid (string): Specifies the VMware Universally Unique Identifier
            (UUID) of the VM tag.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "uuid":'uuid'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 uuid=None):
        """Constructor for the TagAttribute class"""

        # Initialize members of the class
        self.id = id
        self.name = name
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
        id = dictionary.get('id')
        name = dictionary.get('name')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(id,
                   name,
                   uuid)


