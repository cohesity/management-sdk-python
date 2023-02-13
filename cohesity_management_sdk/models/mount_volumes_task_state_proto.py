# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.mount_volumes_info_proto
import cohesity_management_sdk.models.mount_volumes_params

class MountVolumesTaskStateProto(object):

    """Implementation of the 'MountVolumesTaskStateProto' model.

    TODO: type model description here.

    Attributes:
        full_nas_path (string): Contains the SMB/NFS path of the share we
            expose to clients. The share contains the files pertinent to the
            original backup run type.
        host_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        mount_info (MountVolumesInfoProto): Each available extension is listed
            below along with the location of the proto file (relative to
            magneto/connectors) where it is defined.  MountVolumesInfoProto
            extension                     Location
            ===================================================================
            ==========
            vmware::MountVolumesInfoProto::vmware_mount_volumes_info
            vmware/vmware.proto
            ===================================================================
            ==========
        mount_params (MountVolumesParams): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "full_nas_path":'fullNasPath',
        "host_entity":'hostEntity',
        "mount_info":'mountInfo',
        "mount_params":'mountParams'
    }

    def __init__(self,
                 full_nas_path=None,
                 host_entity=None,
                 mount_info=None,
                 mount_params=None):
        """Constructor for the MountVolumesTaskStateProto class"""

        # Initialize members of the class
        self.full_nas_path = full_nas_path
        self.host_entity = host_entity
        self.mount_info = mount_info
        self.mount_params = mount_params


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
        full_nas_path = dictionary.get('fullNasPath')
        host_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('hostEntity')) if dictionary.get('hostEntity') else None
        mount_info = cohesity_management_sdk.models.mount_volumes_info_proto.MountVolumesInfoProto.from_dictionary(dictionary.get('mountInfo')) if dictionary.get('mountInfo') else None
        mount_params = cohesity_management_sdk.models.mount_volumes_params.MountVolumesParams.from_dictionary(dictionary.get('mountParams')) if dictionary.get('mountParams') else None

        # Return an object of this model
        return cls(full_nas_path,
                   host_entity,
                   mount_info,
                   mount_params)


