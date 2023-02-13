# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto

class BackupJobProtoBackupSource(object):

    """Implementation of the 'BackupJobProto_BackupSource' model.

    TODO: type model description here.

    Attributes:
        entities (list of EntityProto): Source entities. NOTE: Multiple
            sources can be specified here for non-leaf-level entities in the
            hierarchy. The sources obtained after expanding these will be
            intersected among each other to form the final set of sources.
            e.g. this can be used to backup only those VMs that have both the
            tags 'SQL' and '3hrs'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entities":'entities'
    }

    def __init__(self,
                 entities=None):
        """Constructor for the BackupJobProtoBackupSource class"""

        # Initialize members of the class
        self.entities = entities


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
        entities = None
        if dictionary.get('entities') != None:
            entities = list()
            for structure in dictionary.get('entities'):
                entities.append(cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(structure))

        # Return an object of this model
        return cls(entities)


