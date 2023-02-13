# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.mount_volumes_hyperv_params
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.mount_volumes_vmware_params

class MountVolumesParams(object):

    """Implementation of the 'MountVolumesParams' model.

    TODO: type model description here.

    Attributes:
        hyperv_params (MountVolumesHypervParams): TODO: type description
            here.
        readonly_mount (bool): Allows the caller to force the Agent to perform
            a read-only mount. This is not usually required and we want to
            give customers the ability to mutate this mount for test/dev
            purposes.
        target_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        vmware_params (MountVolumesVmwareParams): TODO: type description
            here.
        volume_name_vec (list of string): Optional names of volumes that need
            to be mounted. The names here correspond to the volume names
            obtained by Iris from Yoda as part of VMVolumeInfo call. NOTE: If
            this is not specified then all volumes that are part of the server
            will be mounted on the target entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hyperv_params":'hypervParams',
        "readonly_mount":'readonlyMount',
        "target_entity":'targetEntity',
        "vmware_params":'vmwareParams',
        "volume_name_vec":'volumeNameVec'
    }

    def __init__(self,
                 hyperv_params=None,
                 readonly_mount=None,
                 target_entity=None,
                 vmware_params=None,
                 volume_name_vec=None):
        """Constructor for the MountVolumesParams class"""

        # Initialize members of the class
        self.hyperv_params = hyperv_params
        self.readonly_mount = readonly_mount
        self.target_entity = target_entity
        self.vmware_params = vmware_params
        self.volume_name_vec = volume_name_vec


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
        hyperv_params = cohesity_management_sdk.models.mount_volumes_hyperv_params.MountVolumesHypervParams.from_dictionary(dictionary.get('hypervParams')) if dictionary.get('hypervParams') else None
        readonly_mount = dictionary.get('readonlyMount')
        target_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetEntity')) if dictionary.get('targetEntity') else None
        vmware_params = cohesity_management_sdk.models.mount_volumes_vmware_params.MountVolumesVmwareParams.from_dictionary(dictionary.get('vmwareParams')) if dictionary.get('vmwareParams') else None
        volume_name_vec = dictionary.get('volumeNameVec')

        # Return an object of this model
        return cls(hyperv_params,
                   readonly_mount,
                   target_entity,
                   vmware_params,
                   volume_name_vec)


