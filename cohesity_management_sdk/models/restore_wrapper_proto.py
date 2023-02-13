# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.destroy_cloned_task_state_proto
import cohesity_management_sdk.models.restore_wrapper_proto
import cohesity_management_sdk.models.perform_restore_task_state_proto
import cohesity_management_sdk.models.perform_restore_job_state_proto

class RestoreWrapperProto(object):

    """Implementation of the 'RestoreWrapperProto' model.

    If this message is a checkpoint record in WAL-logging or if this message
    is
    used to send restore task info back to the user, it will contain the info
    of
    the restore job/task and the list of all destroy tasks (only when the
    record
    is for a restore task of type clone) associated with it. If this message
    is
    delta record, it will contain the state mutation for one of individual
    restore job, restore task and individual destroy task.

    Attributes:
        destroy_cloned_task_state_vec (list of DestroyClonedTaskStateProto):
            For a restore task of type 'Clone', this field contains the info
            of the destroy task(s).
        owner_restore_wrapper_proto (RestoreWrapperProto): TODO: type
            description here.
        perform_refresh_task_state_vec (list of PerformRestoreTaskStateProto):
            Contains information of the refresh tasks for a clone
        perform_restore_job_state (PerformRestoreJobStateProto): Proto to
            define the persistent information of a wrapper restore job that
            spawns multiple child restore tasks.
        perform_restore_task_state (PerformRestoreTaskStateProto): TODO: type
            description here.
        restore_sub_task_wrapper_proto_vec (list of object): If this restore
            has sub tasks, the following field will get populated with the
            wrapper proto of all of its sub-tasks.  Note that this field is
            only populated for Iris in response to 'GetRestoreTasksArg' RPC.
            It is not persisted in Magneto's WAL.  List of environments that
            use this field: kSQL : Used for multi-stage SQL restore that
            supports a hot-standy.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "destroy_cloned_task_state_vec":'destroyClonedTaskStateVec',
        "owner_restore_wrapper_proto":'ownerRestoreWrapperProto',
        "perform_refresh_task_state_vec":'performRefreshTaskStateVec',
        "perform_restore_job_state":'performRestoreJobState',
        "perform_restore_task_state":'performRestoreTaskState',
        "restore_sub_task_wrapper_proto_vec":'restoreSubTaskWrapperProtoVec'
    }

    def __init__(self,
                 destroy_cloned_task_state_vec=None,
                 owner_restore_wrapper_proto=None,
                 perform_refresh_task_state_vec=None,
                 perform_restore_job_state=None,
                 perform_restore_task_state=None,
                 restore_sub_task_wrapper_proto_vec=None):
        """Constructor for the RestoreWrapperProto class"""

        # Initialize members of the class
        self.destroy_cloned_task_state_vec = destroy_cloned_task_state_vec
        self.owner_restore_wrapper_proto = owner_restore_wrapper_proto
        self.perform_refresh_task_state_vec = perform_refresh_task_state_vec
        self.perform_restore_job_state = perform_restore_job_state
        self.perform_restore_task_state = perform_restore_task_state
        self.restore_sub_task_wrapper_proto_vec = restore_sub_task_wrapper_proto_vec


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
        destroy_cloned_task_state_vec = None
        if dictionary.get('destroyClonedTaskStateVec') != None:
            destroy_cloned_task_state_vec = list()
            for structure in dictionary.get('destroyClonedTaskStateVec'):
                destroy_cloned_task_state_vec.append(cohesity_management_sdk.models.destroy_cloned_task_state_proto.DestroyClonedTaskStateProto.from_dictionary(structure))
        owner_restore_wrapper_proto = cohesity_management_sdk.models.restore_wrapper_proto.RestoreWrapperProto.from_dictionary(dictionary.get('ownerRestoreWrapperProto')) if dictionary.get('ownerRestoreWrapperProto') else None
        perform_refresh_task_state_vec = None
        if dictionary.get('performRefreshTaskStateVec') != None:
            perform_refresh_task_state_vec = list()
            for structure in dictionary.get('performRefreshTaskStateVec'):
                perform_refresh_task_state_vec.append(cohesity_management_sdk.models.perform_restore_task_state_proto.PerformRestoreTaskStateProto.from_dictionary(structure))
        perform_restore_job_state = cohesity_management_sdk.models.perform_restore_job_state_proto.PerformRestoreJobStateProto.from_dictionary(dictionary.get('performRestoreJobState')) if dictionary.get('performRestoreJobState') else None
        perform_restore_task_state = cohesity_management_sdk.models.perform_restore_task_state_proto.PerformRestoreTaskStateProto.from_dictionary(dictionary.get('performRestoreTaskState')) if dictionary.get('performRestoreTaskState') else None
        restore_sub_task_wrapper_proto_vec = dictionary.get('restoreSubTaskWrapperProtoVec')

        # Return an object of this model
        return cls(destroy_cloned_task_state_vec,
                   owner_restore_wrapper_proto,
                   perform_refresh_task_state_vec,
                   perform_restore_job_state,
                   perform_restore_task_state,
                   restore_sub_task_wrapper_proto_vec)


