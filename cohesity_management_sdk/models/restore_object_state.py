# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.request_error

class RestoreObjectState(object):

    """Implementation of the 'RestoreObjectState' model.

    Specifies the state of an individual object in a Restore Task.

    Attributes:
        error (RequestError): Details about the Error.
        object_status (ObjectStatusEnum): Specifies the status of an object
            during a Restore Task. 'kFilesCloned' indicates that the cloning
            has completed. 'kFetchedEntityInfo' indicates that information
            about the object was fetched from the primary source. 'kVMCreated'
            indicates that the new VM was created. 'kRelocationStarted'
            indicates that restoring to a different resource pool has started.
            'kFinished' indicates that the Restore Task has finished. Whether
            it was successful or not is indicated by the error code that that
            is stored with the Restore Task. 'kAborted' indicates that the
            Restore Task was aborted before trying to restore this object.
            This can happen if the Restore Task encounters a global error. For
            example during a 'kCloneVMs' Restore Task, the datastore could not
            be mounted. The entire Restore Task is aborted before trying to
            create VMs on the primary source. 'kDataCopyStarted' indicates
            that the disk copy is started. 'kInProgress' captures a generic
            in-progress state and can be used by restore operations that don't
            track individual states.
        resource_pool_id (long|int): Specifies the id of the Resource Pool
            that the restored object is attached to. For a 'kRecoverVMs'
            Restore Task, an object can be recovered back to its original
            resource pool. This means while recovering a set of objects, this
            field can reference different resource pools. For a 'kCloneVMs'
            Restore Task, all objects are attached to the same resource pool.
            However, this field will still be populated. NOTE: This field may
            not be populated if the restore of the object fails.
        restored_object_id (long|int): Specifies the Id of the recovered or
            cloned object. NOTE: For a Restore Task that is recovering or
            cloning an object in the VMware environment, after the VM is
            created it is storage vMotioned to its primary datastore. If
            storage vMotion fails, the Cohesity Cluster marks the recovery
            task as failed. However, this field is still populated with the id
            of the recovered VM. This id can be used later to clean up the VM
            from primary environment (i.e, the vCenter Server).
        source_object_id (long|int): Specifies the Protection Source id of the
            object to be recovered or cloned.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error":'error',
        "object_status":'objectStatus',
        "resource_pool_id":'resourcePoolId',
        "restored_object_id":'restoredObjectId',
        "source_object_id":'sourceObjectId'
    }

    def __init__(self,
                 error=None,
                 object_status=None,
                 resource_pool_id=None,
                 restored_object_id=None,
                 source_object_id=None):
        """Constructor for the RestoreObjectState class"""

        # Initialize members of the class
        self.error = error
        self.object_status = object_status
        self.resource_pool_id = resource_pool_id
        self.restored_object_id = restored_object_id
        self.source_object_id = source_object_id


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
        error = cohesity_management_sdk.models.request_error.RequestError.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        object_status = dictionary.get('objectStatus')
        resource_pool_id = dictionary.get('resourcePoolId')
        restored_object_id = dictionary.get('restoredObjectId')
        source_object_id = dictionary.get('sourceObjectId')

        # Return an object of this model
        return cls(error,
                   object_status,
                   resource_pool_id,
                   restored_object_id,
                   source_object_id)


