# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.file_restore_info
import cohesity_management_sdk.models.restore_object_details

class RestoreSourceSummaryByObjectTypeElement(object):

    """Implementation of the 'RestoreSourceSummaryByObjectTypeElement' model.

    RestoreSourceSummaryByObjectTypeElement represents a recover/clone summary
    for a single object type.

    Attributes:
        datastore_id (long|int): Specifies the datastore where the object's
            files are recovered to.
            This field is populated when objects are recovered to a different
            resource pool or to a different parent source.
            This field is not populated when objects are recovered to their
            original datastore locations in the original parent source.
        file_restore_info (list of FileRestoreInfo): Specifies a list of
            restore information of files.
        name (string): Specifies the name of the Restore Task. This field must
            be set and must be a unique name.
        objects (list of RestoreObjectDetails): Array of Objects.
          Specifies a list of Protection Source objects or Protection Job objects
          (with specified Protection Source objects).
        protection_source_name (string): The protection source name.
        start_time_usecs (long|int): Specifies the start time of the Restore
            Task as a Unix epoch Timestamp (in microseconds).
        mtype (TypeRestoreSourceSummaryByObjectTypeElementEnum): Specify the
            object type to filter with. Specifies the type of Restore Task.

            'kRecoverVMs' specifies a Restore Task that recovers VMs.
            'kCloneVMs' specifies a Restore Task that clones VMs.
            'kCloneView' specifies a Restore Task that clones a View.
            'kMountVolumes' specifies a Restore Task that mounts volumes.
            'kRestoreFiles' specifies a Restore Task that recovers files and
            folders.
            'kRecoverApp' specifies a Restore Task that recovers app.
            'kCloneApp' specifies a Restore Task that clone app.
            'kRecoverSanVolume' specifies a Restore Task that recovers SAN
            volumes.
            'kConvertAndDeployVMs' specifies a Restore Task that converts and
            deploy VMs to a target environment.
            'kMountFileVolume' specifies a Restore Task that mounts a file
            volume.
            'kSystem' specifies a Restore Task that recovers a system.
            'kRecoverVolumes' specifies a Restore Task that recovers volumes
            via the physical agent.
            'kDeployVolumes' specifies a Restore Task that deploys volumes to
            a target environment.
            'kDownloadFiles' specifies a Restore Task that downloads the
            requested files and folders in zip format.
            'kRecoverEmails' specifies a Restore Task that recovers the
            mailbox/email items.
            'kConvertToPst' specifies a PST conversion task for selected
            mailbox/email items.
            'kRecoverDisks' specifies a Restore Task that recovers the
            virtual disks.
            'kRecoverNamespaces' specifies a Restore Task that recovers
            Kubernetes namespaces.
            'kCloneVMsToView' specifies a Restore Task that clones VMs into a
            View.
        username (string): Specifies the Cohesity user who requested this
            Restore Task.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "datastore_id":'datastoreId',
        "file_restore_info":'fileRestoreInfo',
        "name":'name',
        "objects":'objects',
        "protection_source_name":'protectionSourceName',
        "start_time_usecs":'startTimeUsecs',
        "mtype":'type',
        "username":'username'
    }

    def __init__(self,
                 datastore_id=None,
                 file_restore_info=None,
                 name=None,
                 objects=None,
                 protection_source_name=None,
                 start_time_usecs=None,
                 mtype=None,
                 username=None):
        """Constructor for the RestoreSourceSummaryByObjectTypeElement class"""

        # Initialize members of the class
        self.datastore_id = datastore_id
        self.file_restore_info = file_restore_info
        self.name = name
        self.objects = objects
        self.protection_source_name = protection_source_name
        self.start_time_usecs = start_time_usecs
        self.mtype = mtype
        self.username = username


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
        datastore_id = dictionary.get('datastoreId')
        file_restore_info = None
        if dictionary.get('fileRestoreInfo') != None:
            file_restore_info = list()
            for structure in dictionary.get('fileRestoreInfo'):
                file_restore_info.append(cohesity_management_sdk.models.file_restore_info.FileRestoreInfo.from_dictionary(structure))
        name = dictionary.get('name')
        objects = None
        if dictionary.get('objects') != None:
            objects = list()
            for structure in dictionary.get('objects'):
                objects.append(cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(structure))
        protection_source_name = dictionary.get('protectionSourceName')
        start_time_usecs = dictionary.get('startTimeUsecs')
        mtype = dictionary.get('type')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(datastore_id,
                   file_restore_info,
                   name,
                   objects,
                   protection_source_name,
                   start_time_usecs,
                   mtype,
                   username)


