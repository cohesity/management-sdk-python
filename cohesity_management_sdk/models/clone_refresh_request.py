# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_object_details
import cohesity_management_sdk.models.vlan_parameters

class CloneRefreshRequest(object):

    """Implementation of the 'CloneRefreshRequest' model.

    Specifies the settings for creating a new clone refresh task.

    Attributes:
        clone_task_id (long|int): Specifies the ID of the clone task. This is
            required to determine the details of the clone to be refreshed as
            clone task contains the details of the clone.
        continue_on_error (bool): Specifies if the Restore Task should
            continue when some operations on some objects fail. If true, the
            Cohesity Cluster ignores intermittent errors and restores as many
            objects as possible.
        name (string): Specifies the name of the Restore Task. This field must
            be set and must be a unique name.
        new_parent_id (long|int): Specify a new registered parent Protection
            Source. If specified the selected objects are cloned or recovered
            to this new Protection Source. If not specified, objects are
            cloned or recovered to the original Protection Source that was
            managing them.
        objects (list of RestoreObjectDetails): Array of Objects.  Specifies a
            list of Protection Source objects or Protection Job objects (with
            specified Protection Source objects).
        refresh_time_secs (long|int): Specifies a point in time (unix epoch)
            to which the database needs to be refreshed. This helps granular
            refresh of the database. If this is set, relevant archive logs
            (redo logs) will also be re-played to match with the specified
            time. For this, the log backup should be enabled in the backup
            policy. If this is not set, then only the incremental backup data
            will be used to refresh the target database.
        source_database_id (long|int): Specifies the ID of the source database
            in the backup job snapshot. This is the entity ID of the database,
            which needs to be used as a source during the refresh process.
        vlan_parameters (VlanParameters): Specifies VLAN parameters for the
            restore operation.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "clone_task_id":'cloneTaskId',
        "continue_on_error":'continueOnError',
        "new_parent_id":'newParentId',
        "objects":'objects',
        "refresh_time_secs":'refreshTimeSecs',
        "source_database_id":'sourceDatabaseId',
        "vlan_parameters":'vlanParameters'
    }

    def __init__(self,
                 name=None,
                 clone_task_id=None,
                 continue_on_error=None,
                 new_parent_id=None,
                 objects=None,
                 refresh_time_secs=None,
                 source_database_id=None,
                 vlan_parameters=None):
        """Constructor for the CloneRefreshRequest class"""

        # Initialize members of the class
        self.clone_task_id = clone_task_id
        self.continue_on_error = continue_on_error
        self.name = name
        self.new_parent_id = new_parent_id
        self.objects = objects
        self.refresh_time_secs = refresh_time_secs
        self.source_database_id = source_database_id
        self.vlan_parameters = vlan_parameters


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
        name = dictionary.get('name')
        clone_task_id = dictionary.get('cloneTaskId')
        continue_on_error = dictionary.get('continueOnError')
        new_parent_id = dictionary.get('newParentId')
        objects = None
        if dictionary.get('objects') != None:
            objects = list()
            for structure in dictionary.get('objects'):
                objects.append(cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(structure))
        refresh_time_secs = dictionary.get('refreshTimeSecs')
        source_database_id = dictionary.get('sourceDatabaseId')
        vlan_parameters = cohesity_management_sdk.models.vlan_parameters.VlanParameters.from_dictionary(dictionary.get('vlanParameters')) if dictionary.get('vlanParameters') else None

        # Return an object of this model
        return cls(name,
                   clone_task_id,
                   continue_on_error,
                   new_parent_id,
                   objects,
                   refresh_time_secs,
                   source_database_id,
                   vlan_parameters)


