# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class InfectedFileParam(object):

    """Implementation of the 'InfectedFileParam' model.

    Specifies the parameters to delete a infected file.

    Attributes:
        entity_id (long|int): Specifies the entity id of the infected file.
        remediation_state (RemediationStateEnum): Specifies the remediation
            state of the file. Remediation State. 'kQuarantine' indicates
            'Quarantine' state of the file. This state blocks the client
            access. The administrator will have to manually delete, rescan or
            unquarantine the file. 'kUnquarantine' indicates 'Unquarantine'
            state of the file. The administrator has manually moved files from
            quarantined to the unquarantined state to allow client access.
            Unquarantined files are not scanned for virus until manually
            reset.
        root_inode_id (long|int): Specifies the root inode id of the file
            system that infected file belongs to.
        view_id (long|int): Specifies the id of the View the infected file
            belongs to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entity_id":'entityId',
        "remediation_state":'remediationState',
        "root_inode_id":'rootInodeId',
        "view_id":'viewId'
    }

    def __init__(self,
                 entity_id=None,
                 remediation_state=None,
                 root_inode_id=None,
                 view_id=None):
        """Constructor for the InfectedFileParam class"""

        # Initialize members of the class
        self.entity_id = entity_id
        self.remediation_state = remediation_state
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
        remediation_state = dictionary.get('remediationState')
        root_inode_id = dictionary.get('rootInodeId')
        view_id = dictionary.get('viewId')

        # Return an object of this model
        return cls(entity_id,
                   remediation_state,
                   root_inode_id,
                   view_id)


