# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.acropolis_restore_parameters
import cohesity_management_sdk.models.application_restore_parameters
import cohesity_management_sdk.models.universal_id
import cohesity_management_sdk.models.update_view_param
import cohesity_management_sdk.models.deploy_vms_to_cloud
import cohesity_management_sdk.models.request_error
import cohesity_management_sdk.models.hyperv_restore_parameters
import cohesity_management_sdk.models.mount_volumes_state
import cohesity_management_sdk.models.restore_object_details
import cohesity_management_sdk.models.one_drive_restore_parameters
import cohesity_management_sdk.models.outlook_restore_parameters
import cohesity_management_sdk.models.restore_object_state
import cohesity_management_sdk.models.virtual_disk_recover_task_state
import cohesity_management_sdk.models.vlan_parameters
import cohesity_management_sdk.models.vmware_restore_parameters

class RestoreTask(object):

    """Implementation of the 'RestoreTask' model.

    Specifies information about a Restore Task.

    Attributes:
        acropolis_parameters (AcropolisRestoreParameters): This field defines
            the Acropolis specific params for restore tasks of type
            kRecoverVMs.
        application_parameters (ApplicationRestoreParameters): Specifies the
            information regarding the application restore parameters.
        archive_task_uid (UniversalId): Specifies the uid of the Restore Task
            that retrieves objects from an archive. This field is only
            populated when objects must be retrieved from an archive before
            being restored. This field is deprecated. deprecated:true
        archive_task_uids (list of UniversalId): Specifies the uids of the
            Restore Task that retrieves objects from an archive. This field is
            only populated when objects must be retrieved from an archive
            before being restored. overrideDescription:true
        clone_view_parameters (UpdateViewParam): Specifies the View settings
            used when cloning a View.
        continue_on_error (bool): Specifies if the Restore Task should
            continue when some operations on some objects fail. If true, the
            Cohesity Cluster ignores intermittent errors and restores as many
            objects as possible.
        datastore_id (long|int): Specifies the datastore where the object's
            files are recovered to. This field is populated when objects are
            recovered to a different resource pool or to a different parent
            source. This field is not populated when objects are recovered to
            their original datastore locations in the original parent source.
        deploy_vms_to_cloud (DeployVmsToCloud): Specifies the details about
            deploying vms to specific clouds where backup may be stored and
            converted.
        end_time_usecs (long|int): Specifies the end time of the Restore Task
            as a Unix epoch Timestamp (in microseconds). This field is only
            populated if the Restore Task completes.
        error (RequestError): Specifies the error reported by the Restore Task
            (if any) after the Task has finished.
        full_view_name (string): Specifies the full name of a View.
        hyperv_parameters (HypervRestoreParameters): Specifies information
            needed when restoring VMs in HyperV enviroment. This field defines
            the HyperV specific params for restore tasks of type kRecoverVMs.
        id (long|int): Specifies the id of the Restore Task assigned by
            Cohesity Cluster.
        mount_volumes_state (MountVolumesState): Specifies the states of
            mounting all the volumes onto a mount target for a 'kRecoverVMs'
            Restore Task.
        name (string, required ): Specifies the name of the Restore Task. This
            field must be set and must be a unique name.
        new_parent_id (long|int): Specify a new registered parent Protection
            Source. If specified the selected objects are cloned or recovered
            to this new Protection Source. If not specified, objects are
            cloned or recovered to the original Protection Source that was
            managing them.
        objects (list of RestoreObjectDetails): Array of Objects.  Specifies a
            list of Protection Source objects or Protection Job objects (with
            specified Protection Source objects).
        one_drive_parameters (OneDriveRestoreParameters): Specifies
            information needed for recovering Drive(s) & Drive items.
        outlook_parameters (OutlookRestoreParameters): Specifies information
            needed for recovering Mailboxes in O365Outlook environment.
        restore_object_state (list of RestoreObjectState): Array of Object
            States.  Specifies the states of all the objects for the
            'kRecoverVMs' and 'kCloneVMs' Restore Tasks.
        start_time_usecs (long|int): Specifies the start time for the Restore
            Task as a Unix epoch Timestamp (in microseconds).
        status (StatusRestoreTaskEnum): Specifies the overall status of the
            Restore Task. 'kReadyToSchedule' indicates the Restore Task is
            waiting to be scheduled. 'kProgressMonitorCreated' indicates the
            progress monitor for the Restore Task has been created.
            'kRetrievedFromArchive' indicates that the objects to restore have
            been retrieved from the specified archive. A Task will only ever
            transition to this state if a retrieval is necessary. 'kAdmitted'
            indicates the task has been admitted. After a task has been
            admitted, its status does not move back to 'kReadyToSchedule'
            state even if it is rescheduled. 'kInProgress' indicates that the
            Restore Task is in progress. 'kFinishingProgressMonitor' indicates
            that the Restore Task is finishing its progress monitoring.
            'kFinished' indicates that the Restore Task has finished. The
            status indicating success or failure is found in the error code
            that is stored with the Restore Task. 'kInternalViewCreated'
            indicates that internal view for the task has been created.
            'kZipFileRequested' indicates that request has been sent to create
            zip files for the files to be downloaded. This state is only going
            to be present for kDownloadFiles Task. 'kCancelled' indicates that
            task or jb has been cancelled.
        target_view_created (bool): Is true if a new View was created by a
            'kCloneVMs' Restore Task. This field is only set for a 'kCloneVMs'
            Restore Task.
        mtype (TypeRestoreTaskEnum): Specifies the type of Restore Task.
            'kRecoverVMs' specifies a Restore Task that recovers VMs.
            'kCloneVMs' specifies a Restore Task that clones VMs. 'kCloneView'
            specifies a Restore Task that clones a View. 'kMountVolumes'
            specifies a Restore Task that mounts volumes. 'kRestoreFiles'
            specifies a Restore Task that recovers files and folders.
            'kRecoverApp' specifies a Restore Task that recovers app.
            'kCloneApp' specifies a Restore Task that clone app.
            'kRecoverSanVolume' specifies a Restore Task that recovers SAN
            volumes. 'kConvertAndDeployVMs' specifies a Restore Task that
            converts and deploy VMs to a target environment.
            'kMountFileVolume' specifies a Restore Task that mounts a file
            volume. 'kSystem' specifies a Restore Task that recovers a system.
            'kRecoverVolumes' specifies a Restore Task that recovers volumes
            via the physical agent. 'kDeployVolumes' specifies a Restore Task
            that deployes volumes to a target environment. 'kDownloadFiles'
            specifies a Restore Task that downloads the requested files and
            folders in zip format. 'kRecoverEmails' specifies a Restore Task
            that recovers the mailbox/email items. 'kRecoverDisks' specifies a
            Restore Task that recovers the virtual disks. 'kRecoverNamespaces'
            specifies a Restore Task that recovers Kubernetes namespaces.
            'kCloneVMsToView' specifies a Restore Task that clones VMs into a
            View.
        username (string): Specifies the Cohesity user who requested this
            Restore Task.
        view_box_id (long|int): Specifies the id of the Domain (View Box)
            where the View is stored.
        virtual_disk_restore_state (VirtualDiskRecoverTaskState): Specifies
            the complete information about a recover virtual disk task state.
        vlan_parameters (VlanParameters): Specifies VLAN parameters for the
            restore operation.
        vmware_parameters (VmwareRestoreParameters): Specifies the information
            required for recovering or cloning VmWare VMs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "acropolis_parameters":'acropolisParameters',
        "application_parameters":'applicationParameters',
        "archive_task_uid":'archiveTaskUid',
        "archive_task_uids":'archiveTaskUids',
        "clone_view_parameters":'cloneViewParameters',
        "continue_on_error":'continueOnError',
        "datastore_id":'datastoreId',
        "deploy_vms_to_cloud":'deployVmsToCloud',
        "end_time_usecs":'endTimeUsecs',
        "error":'error',
        "full_view_name":'fullViewName',
        "hyperv_parameters":'hypervParameters',
        "id":'id',
        "mount_volumes_state":'mountVolumesState',
        "new_parent_id":'newParentId',
        "objects":'objects',
        "one_drive_parameters":'oneDriveParameters',
        "outlook_parameters":'outlookParameters',
        "restore_object_state":'restoreObjectState',
        "start_time_usecs":'startTimeUsecs',
        "status":'status',
        "target_view_created":'targetViewCreated',
        "mtype":'type',
        "username":'username',
        "view_box_id":'viewBoxId',
        "virtual_disk_restore_state":'virtualDiskRestoreState',
        "vlan_parameters":'vlanParameters',
        "vmware_parameters":'vmwareParameters'
    }

    def __init__(self,
                 name=None,
                 acropolis_parameters=None,
                 application_parameters=None,
                 archive_task_uid=None,
                 archive_task_uids=None,
                 clone_view_parameters=None,
                 continue_on_error=None,
                 datastore_id=None,
                 deploy_vms_to_cloud=None,
                 end_time_usecs=None,
                 error=None,
                 full_view_name=None,
                 hyperv_parameters=None,
                 id=None,
                 mount_volumes_state=None,
                 new_parent_id=None,
                 objects=None,
                 one_drive_parameters=None,
                 outlook_parameters=None,
                 restore_object_state=None,
                 start_time_usecs=None,
                 status=None,
                 target_view_created=None,
                 mtype=None,
                 username=None,
                 view_box_id=None,
                 virtual_disk_restore_state=None,
                 vlan_parameters=None,
                 vmware_parameters=None):
        """Constructor for the RestoreTask class"""

        # Initialize members of the class
        self.acropolis_parameters = acropolis_parameters
        self.application_parameters = application_parameters
        self.archive_task_uid = archive_task_uid
        self.archive_task_uids = archive_task_uids
        self.clone_view_parameters = clone_view_parameters
        self.continue_on_error = continue_on_error
        self.datastore_id = datastore_id
        self.deploy_vms_to_cloud = deploy_vms_to_cloud
        self.end_time_usecs = end_time_usecs
        self.error = error
        self.full_view_name = full_view_name
        self.hyperv_parameters = hyperv_parameters
        self.id = id
        self.mount_volumes_state = mount_volumes_state
        self.name = name
        self.new_parent_id = new_parent_id
        self.objects = objects
        self.one_drive_parameters = one_drive_parameters
        self.outlook_parameters = outlook_parameters
        self.restore_object_state = restore_object_state
        self.start_time_usecs = start_time_usecs
        self.status = status
        self.target_view_created = target_view_created
        self.mtype = mtype
        self.username = username
        self.view_box_id = view_box_id
        self.virtual_disk_restore_state = virtual_disk_restore_state
        self.vlan_parameters = vlan_parameters
        self.vmware_parameters = vmware_parameters


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
        acropolis_parameters = cohesity_management_sdk.models.acropolis_restore_parameters.AcropolisRestoreParameters.from_dictionary(dictionary.get('acropolisParameters')) if dictionary.get('acropolisParameters') else None
        application_parameters = cohesity_management_sdk.models.application_restore_parameters.ApplicationRestoreParameters.from_dictionary(dictionary.get('applicationParameters')) if dictionary.get('applicationParameters') else None
        archive_task_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('archiveTaskUid')) if dictionary.get('archiveTaskUid') else None
        archive_task_uids = None
        if dictionary.get('archiveTaskUids') != None:
            archive_task_uids = list()
            for structure in dictionary.get('archiveTaskUids'):
                archive_task_uids.append(cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(structure))
        clone_view_parameters = cohesity_management_sdk.models.update_view_param.UpdateViewParam.from_dictionary(dictionary.get('cloneViewParameters')) if dictionary.get('cloneViewParameters') else None
        continue_on_error = dictionary.get('continueOnError')
        datastore_id = dictionary.get('datastoreId')
        deploy_vms_to_cloud = cohesity_management_sdk.models.deploy_vms_to_cloud.DeployVmsToCloud.from_dictionary(dictionary.get('deployVmsToCloud')) if dictionary.get('deployVmsToCloud') else None
        end_time_usecs = dictionary.get('endTimeUsecs')
        error = cohesity_management_sdk.models.request_error.RequestError.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        full_view_name = dictionary.get('fullViewName')
        hyperv_parameters = cohesity_management_sdk.models.hyperv_restore_parameters.HypervRestoreParameters.from_dictionary(dictionary.get('hypervParameters')) if dictionary.get('hypervParameters') else None
        id = dictionary.get('id')
        mount_volumes_state = cohesity_management_sdk.models.mount_volumes_state.MountVolumesState.from_dictionary(dictionary.get('mountVolumesState')) if dictionary.get('mountVolumesState') else None
        new_parent_id = dictionary.get('newParentId')
        objects = None
        if dictionary.get('objects') != None:
            objects = list()
            for structure in dictionary.get('objects'):
                objects.append(cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(structure))
        one_drive_parameters = cohesity_management_sdk.models.one_drive_restore_parameters.OneDriveRestoreParameters.from_dictionary(dictionary.get('oneDriveParameters')) if dictionary.get('oneDriveParameters') else None
        outlook_parameters = cohesity_management_sdk.models.outlook_restore_parameters.OutlookRestoreParameters.from_dictionary(dictionary.get('outlookParameters')) if dictionary.get('outlookParameters') else None
        restore_object_state = None
        if dictionary.get('restoreObjectState') != None:
            restore_object_state = list()
            for structure in dictionary.get('restoreObjectState'):
                restore_object_state.append(cohesity_management_sdk.models.restore_object_state.RestoreObjectState.from_dictionary(structure))
        start_time_usecs = dictionary.get('startTimeUsecs')
        status = dictionary.get('status')
        target_view_created = dictionary.get('targetViewCreated')
        mtype = dictionary.get('type')
        username = dictionary.get('username')
        view_box_id = dictionary.get('viewBoxId')
        virtual_disk_restore_state = cohesity_management_sdk.models.virtual_disk_recover_task_state.VirtualDiskRecoverTaskState.from_dictionary(dictionary.get('virtualDiskRestoreState')) if dictionary.get('virtualDiskRestoreState') else None
        vlan_parameters = cohesity_management_sdk.models.vlan_parameters.VlanParameters.from_dictionary(dictionary.get('vlanParameters')) if dictionary.get('vlanParameters') else None
        vmware_parameters = cohesity_management_sdk.models.vmware_restore_parameters.VmwareRestoreParameters.from_dictionary(dictionary.get('vmwareParameters')) if dictionary.get('vmwareParameters') else None

        # Return an object of this model
        return cls(name,
                   acropolis_parameters,
                   application_parameters,
                   archive_task_uid,
                   archive_task_uids,
                   clone_view_parameters,
                   continue_on_error,
                   datastore_id,
                   deploy_vms_to_cloud,
                   end_time_usecs,
                   error,
                   full_view_name,
                   hyperv_parameters,
                   id,
                   mount_volumes_state,
                   new_parent_id,
                   objects,
                   one_drive_parameters,
                   outlook_parameters,
                   restore_object_state,
                   start_time_usecs,
                   status,
                   target_view_created,
                   mtype,
                   username,
                   view_box_id,
                   virtual_disk_restore_state,
                   vlan_parameters,
                   vmware_parameters)


