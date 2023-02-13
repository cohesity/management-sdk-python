# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VaultDeleteParams(object):

    """Implementation of the 'VaultDeleteParams' model.

    VaultDeleteParams represents the parameters needed to delete a specific
    vault.

    Attributes:
        force_delete (bool): Specifies whether to force delete the vault. If
            the flag is set to true, the RemovalState of the vault is changed
            to 'kMarkedForRemoval' and Eventually vault is removed from cluster
            config and archived metadata from scribe is removed without
            necessarily deleting the associated archived data.
        id (int|long): Specifies an id that identifies the Vault.
        include_marked_for_removal (bool): Specifies if Vaults that are marked
            for removal should be returned.
        retry (bool): Specifies whether to retry a request after failure.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "force_delete":'forceDelete',
        "id":'id',
        "include_marked_for_removal":'includeMarkedForRemoval',
        "retry":'retry'
    }

    def __init__(self,
                 force_delete=None,
                 id=None,
                 include_marked_for_removal=None,
                 retry=None):
        """Constructor for the VaultDeleteParams class"""

        # Initialize members of the class
        self.force_delete = force_delete
        self.id = id
        self.include_marked_for_removal = include_marked_for_removal
        self.retry = retry


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
        force_delete = dictionary.get('forceDelete')
        id = dictionary.get('id')
        include_marked_for_removal = dictionary.get('includeMarkedForRemoval')
        retry = dictionary.get('retry')

        # Return an object of this model
        return cls(force_delete,
                   id,
                   include_marked_for_removal,
                   retry)


