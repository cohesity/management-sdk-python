# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.recover_volumes_params_mapping


class RecoverVolumesParams(object):

    """Implementation of the 'RecoverVolumesParams' model.

    TODO: type description here.


    Attributes:

        force_unmount_volume (bool): Whether volume would be dismounted first
            during LockVolume failure
        mapping_vec (list of RecoverVolumesParams_Mapping): Contains the volume
            mapping data that defines the restore task.
        target_entity (EntityProto): Target entity where the volumes are being
            mounted.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "force_unmount_volume":'forceUnmountVolume',
        "mapping_vec":'mappingVec',
        "target_entity":'targetEntity',
    }
    def __init__(self,
                 force_unmount_volume=None,
                 mapping_vec=None,
                 target_entity=None,
            ):

        """Constructor for the RecoverVolumesParams class"""

        # Initialize members of the class
        self.force_unmount_volume = force_unmount_volume
        self.mapping_vec = mapping_vec
        self.target_entity = target_entity

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
        force_unmount_volume = dictionary.get('forceUnmountVolume')
        mapping_vec = None
        if dictionary.get('mappingVec') != None:
            mapping_vec = list()
            for structure in dictionary.get('mappingVec'):
                mapping_vec.append(cohesity_management_sdk.models.recover_volumes_params_mapping.RecoverVolumesParams_Mapping.from_dictionary(structure))
        target_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetEntity')) if dictionary.get('targetEntity') else None

        # Return an object of this model
        return cls(
            force_unmount_volume,
            mapping_vec,
            target_entity
)