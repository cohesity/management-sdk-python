# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class InfectedFileId(object):

    """Implementation of the 'InfectedFileId' model.

    Specifies the infected file Identifier. A file is identified with three
    Ids
    mentioned in the InfectedFileId definition.

    Attributes:
        entity_id (long|int): Specifies the entity id of the infected file.
        root_inode_id (long|int): Specifies the root inode id of the file
            system that infected file belongs to.
        view_id (long|int): Specifies the id of the View the infected file
            belongs to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entity_id":'entityId',
        "root_inode_id":'rootInodeId',
        "view_id":'viewId'
    }

    def __init__(self,
                 entity_id=None,
                 root_inode_id=None,
                 view_id=None):
        """Constructor for the InfectedFileId class"""

        # Initialize members of the class
        self.entity_id = entity_id
        self.root_inode_id = root_inode_id
        self.view_id = view_id


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
        entity_id = dictionary.get('entityId')
        root_inode_id = dictionary.get('rootInodeId')
        view_id = dictionary.get('viewId')

        # Return an object of this model
        return cls(entity_id,
                   root_inode_id,
                   view_id)


