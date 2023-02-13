# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.acropolis_restore_parameters
import cohesity_management_sdk.models.deploy_vms_to_cloud
import cohesity_management_sdk.models.hyperv_restore_parameters
import cohesity_management_sdk.models.kubernetes_restore_parameters
import cohesity_management_sdk.models.mount_volumes_parameters
import cohesity_management_sdk.models.restore_object_details
import cohesity_management_sdk.models.one_drive_restore_parameters
import cohesity_management_sdk.models.outlook_restore_parameters
import cohesity_management_sdk.models.public_folders_restore_parameters
import cohesity_management_sdk.models.update_view_param
import cohesity_management_sdk.models.virtual_disk_restore_parameters
import cohesity_management_sdk.models.vlan_parameters
import cohesity_management_sdk.models.vmware_restore_parameters
import cohesity_management_sdk.models.share_point_restore_parameters

class RecoverTaskRequest(object):

    """Implementation of the 'RecoverTaskRequest' model.

    Create a Restore Task Request for recovering VMs or mounting volumes to
    mount points.

    Attributes:
        public_folders_parameters (PublicFoldersRestoreParameters): Specifies
            additional parameters for 'kRecoverO365PublicFolders' restore
            objects.
        acropolis_parameters (AcropolisRestoreParameters): This field defines
            the Acropolis specific params for restore tasks of type
            kRecoverVMs.
        continue_on_error (bool): Specifies if the Restore Task should
            continue when some operations on some objects fail. If true, the
            Cohesity Cluster ignores intermittent errors and restores as many
            objects as possible.
        deploy_vms_to_cloud (DeployVmsToCloud): Specifies the details about
            deploying vms to specific clouds where backup may be stored and
            converted.
        glacier_retrieval_type (GlacierRetrievalTypeEnum): Specifies the way
            data needs to be retrieved from the external target. This
            information will be filled in by Iris and Magneto will pass it
            along to the Icebox as it is to support bulk retrieval from
            Glacier. Specifies the type of Restore Task.  'kStandard'
            specifies retrievals that allow to access any of your archives
            within several hours. Standard retrievals typically complete
            within 3–5 hours.This is the default option for retrieval requests
            that do not specify the retrieval option. 'kBulk' specifies
            retrievals that are Glacier’s lowest-cost retrieval option, which
            can be use to retrieve large amounts, even petabytes, of data
            inexpensively in a day. Bulk retrieval typically complete within
            5–12 hours. 'kExpedited' specifies retrievals that allows to
            quickly access your data when occasional urgent requests for a
            subset of archives are required. For all but the largest archives
            (250 MB+), data accessed using Expedited retrievals are typically
            made available within 1–5 minutes.
        hyperv_parameters (HypervRestoreParameters): Specifies information
            needed when restoring VMs in HyperV enviroment. This field defines
            the HyperV specific params for restore tasks of type kRecoverVMs.
        kubernetes_parameters (KubernetesRestoreParameters): Specifies the
            information required for recovering kubernetes entities.
        mount_parameters (MountVolumesParameters): Specifies the information
            required for mounting volumes. Only required for Restore Tasks of
            type 'kMountVolumes'. At a minimum, the targetSourceId must be
            specified for 'kMountVolumes' Restore Tasks. If only
            targetSourceId is specified, all disks are attached but may not be
            mounted. The mount target must be registered on the Cohesity
            Cluster. If the mount target is a VM, VMware Tools must be
            installed. If the mount target is a physical server, a Cohesity
            Agent must be be installed. See the Cohesity Dashboard help
            documentation for details. In the username and password fields,
            specify the credentials to access the mount target.
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
        one_drive_parameters (OneDriveRestoreParameters): Specifies
            information needed for recovering Drive(s) & Drive items.
        outlook_parameters (OutlookRestoreParameters): Specifies information
            needed for recovering Mailboxes in O365Outlook environment.
        restore_view_parameters (UpdateViewParam): Specifies the settings that
            define a View.
        share_point_parameters (SharePointRestoreParameters): Specifies
            additional parameters for 'kRecoverSites' restore objects.
        mtype (TypeRecoverTaskRequestEnum): Specifies the type of Restore Task
            such as 'kRecoverVMs' or 'kMountVolumes'. 'kRecoverVMs' specifies
            a Restore Task that recovers VMs. 'kMountVolumes' specifies a
            Restore Task that mounts volumes to mount points.
            'kRecoverNamespaces' specifies a Restore Task that recovers
            Kubernetes namespaces. 'kMountFileVolume' specifies a Restore Task
            that mounts a file volume.
        view_name (string): Specifie target view into which the objects are to
            be cloned when doing recovery for NAS.
        virtual_disk_restore_parameters (VirtualDiskRestoreParameters):
            Specifies the parameters to recover virtual disks of a vm.
        vlan_parameters (VlanParameters): Specifies VLAN parameters for the
            restore operation.
        vmware_parameters (VmwareRestoreParameters): Specifies the information
            required for recovering or cloning VmWare VMs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "mtype":'type',
        "public_folders_parameters":'PublicFoldersParameters',
        "acropolis_parameters":'acropolisParameters',
        "continue_on_error":'continueOnError',
        "deploy_vms_to_cloud":'deployVmsToCloud',
        "glacier_retrieval_type":'glacierRetrievalType',
        "hyperv_parameters":'hypervParameters',
        "kubernetes_parameters":'kubernetesParameters',
        "mount_parameters":'mountParameters',
        "new_parent_id":'newParentId',
        "objects":'objects',
        "one_drive_parameters":'oneDriveParameters',
        "outlook_parameters":'outlookParameters',
        "restore_view_parameters":'restoreViewParameters',
        "share_point_parameters":'sharePointParameters',
        "view_name":'viewName',
        "virtual_disk_restore_parameters":'virtualDiskRestoreParameters',
        "vlan_parameters":'vlanParameters',
        "vmware_parameters":'vmwareParameters'
    }

    def __init__(self,
                 name=None,
                 mtype=None,
                 public_folders_parameters=None,
                 acropolis_parameters=None,
                 continue_on_error=None,
                 deploy_vms_to_cloud=None,
                 glacier_retrieval_type=None,
                 hyperv_parameters=None,
                 kubernetes_parameters=None,
                 mount_parameters=None,
                 new_parent_id=None,
                 objects=None,
                 one_drive_parameters=None,
                 outlook_parameters=None,
                 restore_view_parameters=None,
                 share_point_parameters=None,
                 view_name=None,
                 virtual_disk_restore_parameters=None,
                 vlan_parameters=None,
                 vmware_parameters=None):
        """Constructor for the RecoverTaskRequest class"""

        # Initialize members of the class
        self.public_folders_parameters = public_folders_parameters
        self.acropolis_parameters = acropolis_parameters
        self.continue_on_error = continue_on_error
        self.deploy_vms_to_cloud = deploy_vms_to_cloud
        self.glacier_retrieval_type = glacier_retrieval_type
        self.hyperv_parameters = hyperv_parameters
        self.kubernetes_parameters = kubernetes_parameters
        self.mount_parameters = mount_parameters
        self.name = name
        self.new_parent_id = new_parent_id
        self.objects = objects
        self.one_drive_parameters = one_drive_parameters
        self.outlook_parameters = outlook_parameters
        self.restore_view_parameters = restore_view_parameters
        self.share_point_parameters = share_point_parameters
        self.mtype = mtype
        self.view_name = view_name
        self.virtual_disk_restore_parameters = virtual_disk_restore_parameters
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
        mtype = dictionary.get('type')
        public_folders_parameters = cohesity_management_sdk.models.public_folders_restore_parameters.PublicFoldersRestoreParameters.from_dictionary(dictionary.get('PublicFoldersParameters')) if dictionary.get('PublicFoldersParameters') else None
        acropolis_parameters = cohesity_management_sdk.models.acropolis_restore_parameters.AcropolisRestoreParameters.from_dictionary(dictionary.get('acropolisParameters')) if dictionary.get('acropolisParameters') else None
        continue_on_error = dictionary.get('continueOnError')
        deploy_vms_to_cloud = cohesity_management_sdk.models.deploy_vms_to_cloud.DeployVmsToCloud.from_dictionary(dictionary.get('deployVmsToCloud')) if dictionary.get('deployVmsToCloud') else None
        glacier_retrieval_type = dictionary.get('glacierRetrievalType')
        hyperv_parameters = cohesity_management_sdk.models.hyperv_restore_parameters.HypervRestoreParameters.from_dictionary(dictionary.get('hypervParameters')) if dictionary.get('hypervParameters') else None
        kubernetes_parameters = cohesity_management_sdk.models.kubernetes_restore_parameters.KubernetesRestoreParameters.from_dictionary(dictionary.get('kubernetesParameters')) if dictionary.get('kubernetesParameters') else None
        mount_parameters = cohesity_management_sdk.models.mount_volumes_parameters.MountVolumesParameters.from_dictionary(dictionary.get('mountParameters')) if dictionary.get('mountParameters') else None
        new_parent_id = dictionary.get('newParentId')
        objects = None
        if dictionary.get('objects') != None:
            objects = list()
            for structure in dictionary.get('objects'):
                objects.append(cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(structure))
        one_drive_parameters = cohesity_management_sdk.models.one_drive_restore_parameters.OneDriveRestoreParameters.from_dictionary(dictionary.get('oneDriveParameters')) if dictionary.get('oneDriveParameters') else None
        outlook_parameters = cohesity_management_sdk.models.outlook_restore_parameters.OutlookRestoreParameters.from_dictionary(dictionary.get('outlookParameters')) if dictionary.get('outlookParameters') else None
        restore_view_parameters = cohesity_management_sdk.models.update_view_param.UpdateViewParam.from_dictionary(dictionary.get('restoreViewParameters')) if dictionary.get('restoreViewParameters') else None
        share_point_parameters = cohesity_management_sdk.models.share_point_restore_parameters.SharePointRestoreParameters.from_dictionary(dictionary.get('sharePointParameters')) if dictionary.get('sharePointParameters') else None
        view_name = dictionary.get('viewName')
        virtual_disk_restore_parameters = cohesity_management_sdk.models.virtual_disk_restore_parameters.VirtualDiskRestoreParameters.from_dictionary(dictionary.get('virtualDiskRestoreParameters')) if dictionary.get('virtualDiskRestoreParameters') else None
        vlan_parameters = cohesity_management_sdk.models.vlan_parameters.VlanParameters.from_dictionary(dictionary.get('vlanParameters')) if dictionary.get('vlanParameters') else None
        vmware_parameters = cohesity_management_sdk.models.vmware_restore_parameters.VmwareRestoreParameters.from_dictionary(dictionary.get('vmwareParameters')) if dictionary.get('vmwareParameters') else None

        # Return an object of this model
        return cls(name,
                   mtype,
                   public_folders_parameters,
                   acropolis_parameters,
                   continue_on_error,
                   deploy_vms_to_cloud,
                   glacier_retrieval_type,
                   hyperv_parameters,
                   kubernetes_parameters,
                   mount_parameters,
                   new_parent_id,
                   objects,
                   one_drive_parameters,
                   outlook_parameters,
                   restore_view_parameters,
                   share_point_parameters,
                   view_name,
                   virtual_disk_restore_parameters,
                   vlan_parameters,
                   vmware_parameters)


