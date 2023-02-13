# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.destroy_cloned_entity_info_proto

class DestroyClonedVMTaskInfoProto(object):

    """Implementation of the 'DestroyClonedVMTaskInfoProto' model.

    Each available extension is listed below along with the location of the
    proto file (relative to magneto/connectors) where it is defined.
    DestroyClonedVMTaskInfoProto extension          Location
    Extension
    ===========================================================================
    ==
    vmware::DestroyClonedTaskInfo::
    vmware_destroy_cloned_vm_task_info            vmware/vmware.proto    100
    hyperv::DestroyClonedTaskInfo::
    hyperv_destroy_cloned_vm_task_info            hyperv/hyperv.proto    101
    ===========================================================================
    ==

    Attributes:
        datastore_not_unmounted_reason (string): If datastore was not
            unmounted, this field contains the reason for the same.
        datastore_unmounted (bool): Whether the datastore corresponding to the
            clone view was unmounted from primary environment.
        destroy_cloned_entity_info_vec (list of DestroyClonedEntityInfoProto):
            Vector of all cloned entities that this destroy task will
            teardown.
        mtype (int): The type of environment this destroy clone task info
            pertains to.
        view_deleted (bool): Whether the clone view was deleted by the destroy
            task.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "datastore_not_unmounted_reason":'datastoreNotUnmountedReason',
        "datastore_unmounted":'datastoreUnmounted',
        "destroy_cloned_entity_info_vec":'destroyClonedEntityInfoVec',
        "mtype":'type',
        "view_deleted":'viewDeleted'
    }

    def __init__(self,
                 datastore_not_unmounted_reason=None,
                 datastore_unmounted=None,
                 destroy_cloned_entity_info_vec=None,
                 mtype=None,
                 view_deleted=None):
        """Constructor for the DestroyClonedVMTaskInfoProto class"""

        # Initialize members of the class
        self.datastore_not_unmounted_reason = datastore_not_unmounted_reason
        self.datastore_unmounted = datastore_unmounted
        self.destroy_cloned_entity_info_vec = destroy_cloned_entity_info_vec
        self.mtype = mtype
        self.view_deleted = view_deleted


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
        datastore_not_unmounted_reason = dictionary.get('datastoreNotUnmountedReason')
        datastore_unmounted = dictionary.get('datastoreUnmounted')
        destroy_cloned_entity_info_vec = None
        if dictionary.get('destroyClonedEntityInfoVec') != None:
            destroy_cloned_entity_info_vec = list()
            for structure in dictionary.get('destroyClonedEntityInfoVec'):
                destroy_cloned_entity_info_vec.append(cohesity_management_sdk.models.destroy_cloned_entity_info_proto.DestroyClonedEntityInfoProto.from_dictionary(structure))
        mtype = dictionary.get('type')
        view_deleted = dictionary.get('viewDeleted')

        # Return an object of this model
        return cls(datastore_not_unmounted_reason,
                   datastore_unmounted,
                   destroy_cloned_entity_info_vec,
                   mtype,
                   view_deleted)


