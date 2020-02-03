# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class ArchivalTarget(object):

    """Implementation of the 'ArchivalTarget' model.

    Message that specifies the details about an archival target (such as
    cloud
    or tape) where backup snapshots may be archived to.

    Attributes:
        name (string): The name of the archival target.
        mtype (int): The type of the archival target.
        vault_id (long|int): The id of the archival vault.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "mtype":'type',
        "vault_id":'vaultId'
    }

    def __init__(self,
                 name=None,
                 mtype=None,
                 vault_id=None):
        """Constructor for the ArchivalTarget class"""

        # Initialize members of the class
        self.name = name
        self.mtype = mtype
        self.vault_id = vault_id


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
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        vault_id = dictionary.get('vaultId')

        # Return an object of this model
        return cls(name,
                   mtype,
                   vault_id)


