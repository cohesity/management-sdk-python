# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.connector_params
import cohesity_management_sdk.models.restore_vlan_params
import cohesity_management_sdk.models.user_information

class RestoreTaskStateBaseProto(object):

    """Implementation of the 'RestoreTaskStateBaseProto' model.

    TODO: type model description here.

    Attributes:
        cancellation_requested (bool): Whether this task has a pending
            cancellation request.
        end_time_usecs (long|int): If the restore task has finished, this
            field contains the end time for the task.
        error (ErrorProto): TODO: type description here.
        is_internal (bool): Whether the restore task is internal. This is
            currently used by standby restore tasks.
        name (string): The name of the restore task.
        parent_source_connection_params (ConnectorParams): Message that
            encapsulates the various params required to establish a connection
            with a particular environment.
        public_status (int): Iris-facing task state. This field is stamped
            during the export.
        refresh_status (int): Status of the refresh task.
        restore_vlan_params (RestoreVlanParams): TODO: type description here.
        scheduled_constituent_id (long|int): Constituent id (and the gandalf
            session id) where this task has been scheduled. If -1, the task is
            not running at any slave. It's possible that the task was
            previously scheduled, but is now being re-scheduled.
        scheduled_gandalf_session_id (long|int): TODO: type description here.
        start_time_usecs (long|int): The start time for this restore task.
        status (int): Status of the restore task.
        task_id (long|int): A globally unique id for this task.
        total_logical_size_bytes (long|int): Logical size of this restore
            task. This is the amount of data that needs to be transferred to
            restore the entity.
        total_physical_size_bytes (long|int): Physical size of this restore
            task. This is the amount of data that was actually transferred to
            restore the entity.
        mtype (int): The type of restore being performed.
        user (string): The user who requested this restore task.
        user_info (UserInformation): A message to encapsulate information
            about the user who made the request. Request should be filtered by
            these fields if specified so that only the objects that the user
            is permissioned for are returned. If both sid_vec & tenant_id are
            specified then an intersection of respective results should be
            returned.
        user_messages (list of string): Messages displayed to the user for
            this task (if any). Only valid if the status of the task is
            kFinished. This is used for informing the user with additional
            details when there is not an error.
        warnings (list of ErrorProto): The warnings encountered by this task
            (if any) during its execution.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cancellation_requested":'cancellationRequested',
        "end_time_usecs":'endTimeUsecs',
        "error":'error',
        "is_internal":'isInternal',
        "name":'name',
        "parent_source_connection_params":'parentSourceConnectionParams',
        "public_status":'publicStatus',
        "refresh_status":'refreshStatus',
        "restore_vlan_params":'restoreVlanParams',
        "scheduled_constituent_id":'scheduledConstituentId',
        "scheduled_gandalf_session_id":'scheduledGandalfSessionId',
        "start_time_usecs":'startTimeUsecs',
        "status":'status',
        "task_id":'taskId',
        "total_logical_size_bytes":'totalLogicalSizeBytes',
        "total_physical_size_bytes":'totalPhysicalSizeBytes',
        "mtype":'type',
        "user":'user',
        "user_info":'userInfo',
        "user_messages":'userMessages',
        "warnings":'warnings'
    }

    def __init__(self,
                 cancellation_requested=None,
                 end_time_usecs=None,
                 error=None,
                 is_internal=None,
                 name=None,
                 parent_source_connection_params=None,
                 public_status=None,
                 refresh_status=None,
                 restore_vlan_params=None,
                 scheduled_constituent_id=None,
                 scheduled_gandalf_session_id=None,
                 start_time_usecs=None,
                 status=None,
                 task_id=None,
                 total_logical_size_bytes=None,
                 total_physical_size_bytes=None,
                 mtype=None,
                 user=None,
                 user_info=None,
                 user_messages=None,
                 warnings=None):
        """Constructor for the RestoreTaskStateBaseProto class"""

        # Initialize members of the class
        self.cancellation_requested = cancellation_requested
        self.end_time_usecs = end_time_usecs
        self.error = error
        self.is_internal = is_internal
        self.name = name
        self.parent_source_connection_params = parent_source_connection_params
        self.public_status = public_status
        self.refresh_status = refresh_status
        self.restore_vlan_params = restore_vlan_params
        self.scheduled_constituent_id = scheduled_constituent_id
        self.scheduled_gandalf_session_id = scheduled_gandalf_session_id
        self.start_time_usecs = start_time_usecs
        self.status = status
        self.task_id = task_id
        self.total_logical_size_bytes = total_logical_size_bytes
        self.total_physical_size_bytes = total_physical_size_bytes
        self.mtype = mtype
        self.user = user
        self.user_info = user_info
        self.user_messages = user_messages
        self.warnings = warnings


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
        cancellation_requested = dictionary.get('cancellationRequested')
        end_time_usecs = dictionary.get('endTimeUsecs')
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        is_internal = dictionary.get('isInternal')
        name = dictionary.get('name')
        parent_source_connection_params = cohesity_management_sdk.models.connector_params.ConnectorParams.from_dictionary(dictionary.get('parentSourceConnectionParams')) if dictionary.get('parentSourceConnectionParams') else None
        public_status = dictionary.get('publicStatus')
        refresh_status = dictionary.get('refreshStatus')
        restore_vlan_params = cohesity_management_sdk.models.restore_vlan_params.RestoreVlanParams.from_dictionary(dictionary.get('restoreVlanParams')) if dictionary.get('restoreVlanParams') else None
        scheduled_constituent_id = dictionary.get('scheduledConstituentId')
        scheduled_gandalf_session_id = dictionary.get('scheduledGandalfSessionId')
        start_time_usecs = dictionary.get('startTimeUsecs')
        status = dictionary.get('status')
        task_id = dictionary.get('taskId')
        total_logical_size_bytes = dictionary.get('totalLogicalSizeBytes')
        total_physical_size_bytes = dictionary.get('totalPhysicalSizeBytes')
        mtype = dictionary.get('type')
        user = dictionary.get('user')
        user_info = cohesity_management_sdk.models.user_information.UserInformation.from_dictionary(dictionary.get('userInfo')) if dictionary.get('userInfo') else None
        user_messages = dictionary.get('userMessages')
        warnings = None
        if dictionary.get('warnings') != None:
            warnings = list()
            for structure in dictionary.get('warnings'):
                warnings.append(cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(structure))

        # Return an object of this model
        return cls(cancellation_requested,
                   end_time_usecs,
                   error,
                   is_internal,
                   name,
                   parent_source_connection_params,
                   public_status,
                   refresh_status,
                   restore_vlan_params,
                   scheduled_constituent_id,
                   scheduled_gandalf_session_id,
                   start_time_usecs,
                   status,
                   task_id,
                   total_logical_size_bytes,
                   total_physical_size_bytes,
                   mtype,
                   user,
                   user_info,
                   user_messages,
                   warnings)


