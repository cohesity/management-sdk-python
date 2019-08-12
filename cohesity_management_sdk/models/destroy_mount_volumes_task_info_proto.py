# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.mount_volumes_info_proto
import cohesity_management_sdk.models.entity_proto

class DestroyMountVolumesTaskInfoProto(object):

    """Implementation of the 'DestroyMountVolumesTaskInfoProto' model.

    TODO: type model description here.

    Attributes:
        error (ErrorProto): TODO: type description here.
        finished (bool): This will be set to true if the task is complete on
            the slave.
        mount_volumes_info_proto (MountVolumesInfoProto): Each available
            extension is listed below along with the location of the proto
            file (relative to magneto/connectors) where it is defined.
            MountVolumesInfoProto extension                     Location
            ===================================================================
            ==========
            vmware::MountVolumesInfoProto::vmware_mount_volumes_info
            vmware/vmware.proto
            ===================================================================
            ==========
        slave_task_start_time_usecs (long|int): This is the timestamp at which
            the slave task started.
        target_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error":'error',
        "finished":'finished',
        "mount_volumes_info_proto":'mountVolumesInfoProto',
        "slave_task_start_time_usecs":'slaveTaskStartTimeUsecs',
        "target_entity":'targetEntity'
    }

    def __init__(self,
                 error=None,
                 finished=None,
                 mount_volumes_info_proto=None,
                 slave_task_start_time_usecs=None,
                 target_entity=None):
        """Constructor for the DestroyMountVolumesTaskInfoProto class"""

        # Initialize members of the class
        self.error = error
        self.finished = finished
        self.mount_volumes_info_proto = mount_volumes_info_proto
        self.slave_task_start_time_usecs = slave_task_start_time_usecs
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
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        finished = dictionary.get('finished')
        mount_volumes_info_proto = cohesity_management_sdk.models.mount_volumes_info_proto.MountVolumesInfoProto.from_dictionary(dictionary.get('mountVolumesInfoProto')) if dictionary.get('mountVolumesInfoProto') else None
        slave_task_start_time_usecs = dictionary.get('slaveTaskStartTimeUsecs')
        target_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetEntity')) if dictionary.get('targetEntity') else None

        # Return an object of this model
        return cls(error,
                   finished,
                   mount_volumes_info_proto,
                   slave_task_start_time_usecs,
                   target_entity)


