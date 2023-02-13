# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_aws_ebs
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_azure_disk
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_azure_file
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_cephfs
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_cinder
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_config_map
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_csi
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_downward_api
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_empty_dir
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_ephemeral_volume_source
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_fc
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_flex
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_flocker
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_gce_persistent_disk
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_gluster_fs
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_host_path
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_iscsi
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_local
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_nfs
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_pvc
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_photon_persistent_disk
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_portworx
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_projected
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_quobyte
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_rbd
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_scale_io
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_config_map
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_storage_os
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_vsphere_virtual_disk

class PodInfo_PodSpec_VolumeInfo(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo' model.

    Contains information about volumes of different types that can be
    mounted to a pod. Reference:
    https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.19/

    Attributes:
        aws_elastic_block_store (PodInfo_PodSpec_VolumeInfo_AWS_EBS): Below
            fields determine type of volume.
        azure_disk (PodInfo_PodSpec_VolumeInfo_AzureDisk): TODO: Type
            description here.
        azure_file (PodInfo_PodSpec_VolumeInfo_AzureFile): TODO: Type
            description here.
        cephfs (PodInfo_PodSpec_VolumeInfo_Cephfs): TODO: Type description
            here.
        cinder (PodInfo_PodSpec_VolumeInfo_Cinder): TODO: Type description
            here.
        config_map (PodInfo_PodSpec_VolumeInfo_ConfigMap): TODO: Type description
            here.
        csi (PodInfo_PodSpec_VolumeInfo_CSI): TODO: Type description here.
        downward_api (PodInfo_PodSpec_VolumeInfo_DownwardAPI): TODO: Type
            description here.
        empty_dir (PodInfo_PodSpec_VolumeInfo_EmptyDir): TODO: Type
            description here.
        ephemeral (PodInfo_PodSpec_VolumeInfo_EphemeralVolumeSource): TODO:
            Type description here.
        fc (PodInfo_PodSpec_VolumeInfo_FC): TODO: Type description here.
        flex_volume (PodInfo_PodSpec_VolumeInfo_Flex): TODO: Type description here.
        flocker (PodInfo_PodSpec_VolumeInfo_Flocker): TODO: Type description here.
        gce_persistent_disk (PodInfo_PodSpec_VolumeInfo_GcePersistentDisk): 
            TODO: Type description here.
        glusterfs (PodInfo_PodSpec_VolumeInfo_GlusterFs): TODO: Type description
            here.
        host_path (PodInfo_PodSpec_VolumeInfo_HostPath): TODO: Type description
            here.
        iscsi (PodInfo_PodSpec_VolumeInfo_ISCSI): TODO: Type description here.
        local (PodInfo_PodSpec_VolumeInfo_Local): TODO: Type description here.
        name (string): Name of the volume.
        nfs (PodInfo_PodSpec_VolumeInfo_NFS): TODO: Type
            description here.
        persistent_volume_claim (PodInfo_PodSpec_VolumeInfo_PVC): TODO: Type
            description here.
        photon_persistent_disk (PodInfo_PodSpec_VolumeInfo_PhotonPersistentDisk): TODO:
            Type description here.
        portworx_volume (PodInfo_PodSpec_VolumeInfo_Portworx):TODO: 
        Type description here.
        projected (PodInfo_PodSpec_VolumeInfo_Projected): TODO:
            Type description here.
        quobyte (PodInfo_PodSpec_VolumeInfo_Quobyte): TODO:
            Type description here.
        rbd (PodInfo_PodSpec_VolumeInfo_RBD): TODO: Type
            description here.
        scale_io (PodInfo_PodSpec_VolumeInfo_ScaleIO): TODO: Type
            description here.
        secret (PodInfo_PodSpec_VolumeInfo_ConfigMap): TODO: Type
            description here.
        storageos (PodInfo_PodSpec_VolumeInfo_StorageOS):
            TODO: Type description here.
        vsphere_volume (PodInfo_PodSpec_VolumeInfo_VsphereVirtualDisk):
            TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_elastic_block_store":'awsElasticBlockStore',
        "azure_disk":'azureDisk',
        "azure_file":'azureFile',
        "cephfs":'cephfs',
        "cinder":'cinder',
        "config_map":'configMap',
        "csi":'csi',
        "downward_api":'downwardApi',
        "empty_dir":'emptyDir',
        "ephemeral":'ephemeral',
        "fc":'fc',
        "flex_volume":'flexVolume',
        "flocker":'flocker',
        "gce_persistent_disk":'gcePersistentDisk',
        "glusterfs":'glusterfs',
        "host_path":'hostPath',
        "iscsi":'iscsi',
        "local":'local',
        "name":'name',
        "nfs":'nfs',
        "persistent_volume_claim":'persistentVolumeClaim',
        "photon_persistent_disk":'photonPersistentDisk',
        "portworx_volume":'portworxVolume',
        "projected":'projected',
        "quobyte":'quobyte',
        "rbd":'rbd',
        "scale_io":'scaleIo',
        "secret":'secret',
        "storageos":'storageos',
        "vsphere_volume":'vsphereVolume'
    }

    def __init__(self,
                 aws_elastic_block_store=None,
                 azure_disk=None,
                 azure_file=None,
                 cephfs=None,
                 cinder=None,
                 config_map=None,
                 csi=None,
                 downward_api=None,
                 empty_dir=None,
                 ephemeral=None,
                 fc=None,
                 flex_volume=None,
                 flocker=None,
                 gce_persistent_disk=None,
                 glusterfs=None,
                 host_path=None,
                 iscsi=None,
                 local=None,
                 name=None,
                 nfs=None,
                 persistent_volume_claim=None,
                 photon_persistent_disk=None,
                 portworx_volume=None,
                 projected=None,
                 quobyte=None,
                 rbd=None,
                 scale_io=None,
                 secret=None,
                 storageos=None,
                 vsphere_volume=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo class"""

        # Initialize members of the class
        self.aws_elastic_block_store = aws_elastic_block_store
        self.azure_disk = azure_disk
        self.azure_file = azure_file
        self.cephfs = cephfs
        self.cinder = cinder
        self.config_map = config_map
        self.csi = csi
        self.downward_api = downward_api
        self.empty_dir = empty_dir
        self.ephemeral = ephemeral
        self.fc = fc
        self.flex_volume = flex_volume
        self.flocker = flocker
        self.gce_persistent_disk = gce_persistent_disk
        self.glusterfs = glusterfs
        self.host_path = host_path
        self.iscsi = iscsi
        self.local = local
        self.name = name
        self.nfs = nfs
        self.persistent_volume_claim = persistent_volume_claim
        self.photon_persistent_disk = photon_persistent_disk
        self.portworx_volume = portworx_volume
        self.projected = projected
        self.quobyte = quobyte
        self.rbd = rbd
        self.scale_io = scale_io
        self.secret = secret
        self.storageos = storageos
        self.vsphere_volume = vsphere_volume


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
        aws_elastic_block_store = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_aws_ebs.PodInfo_PodSpec_VolumeInfo_AWS_EBS.from_dictionary(dictionary.get('awsElasticBlockStore')) if dictionary.get('awsElasticBlockStore') else None
        azure_disk = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_azure_disk.PodInfo_PodSpec_VolumeInfo_AzureDisk.from_dictionary(dictionary.get('azureDisk')) if dictionary.get('azureDisk') else None
        azure_file = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_azure_file.PodInfo_PodSpec_VolumeInfo_AzureFile.from_dictionary(dictionary.get('azureFile')) if dictionary.get('azureFile') else None
        cephfs = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_cephfs.PodInfo_PodSpec_VolumeInfo_Cephfs.from_dictionary(dictionary.get('cephfs')) if dictionary.get('cephfs') else None
        cinder = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_cinder.PodInfo_PodSpec_VolumeInfo_Cinder.from_dictionary(dictionary.get('cinder')) if dictionary.get('cinder') else None
        config_map =  cohesity_management_sdk.models.pod_info_pod_spec_volume_info_config_map.PodInfo_PodSpec_VolumeInfo_ConfigMap.from_dictionary(dictionary.get('configMap')) if dictionary.get('configMap') else None
        csi = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_csi.PodInfo_PodSpec_VolumeInfo_CSI.from_dictionary(dictionary.get('csi')) if dictionary.get('csi') else None
        downward_api = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_downward_api.PodInfo_PodSpec_VolumeInfo_DownwardAPI.from_dictionary(dictionary.get('downwardApi')) if dictionary.get('downwardApi') else None
        empty_dir = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_empty_dir.PodInfo_PodSpec_VolumeInfo_EmptyDir.from_dictionary(dictionary.get('emptyDir')) if dictionary.get('emptyDir') else None
        ephemeral = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_ephemeral_volume_source.PodInfo_PodSpec_VolumeInfo_EphemeralVolumeSource.from_dictionary(dictionary.get('ephemeral')) if dictionary.get('ephemeral') else None
        fc = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_fc.PodInfo_PodSpec_VolumeInfo_FC.from_dictionary(dictionary.get('fc')) if dictionary.get('fc') else None
        flex_volume = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_flex.PodInfo_PodSpec_VolumeInfo_Flex.from_dictionary(dictionary.get('flexVolume')) if dictionary.get('flexVolume') else None
        flocker = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_flocker.PodInfo_PodSpec_VolumeInfo_Flocker.from_dictionary(dictionary.get('flocker')) if dictionary.get('flocker') else None
        gce_persistent_disk = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_gce_persistent_disk.PodInfo_PodSpec_VolumeInfo_GcePersistentDisk.from_dictionary(dictionary.get('gcePersistentDisk')) if dictionary.get('gcePersistentDisk') else None
        glusterfs = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_gluster_fs.PodInfo_PodSpec_VolumeInfo_GlusterFs.from_dictionary(dictionary.get('glusterfs')) if dictionary.get('glusterfs') else None
        host_path = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_host_path.PodInfo_PodSpec_VolumeInfo_HostPath.from_dictionary(dictionary.get('hostPath')) if dictionary.get('hostPath') else None
        iscsi = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_iscsi.PodInfo_PodSpec_VolumeInfo_ISCSI.from_dictionary(dictionary.get('iscsi')) if dictionary.get('iscsi') else None
        local = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_local.PodInfo_PodSpec_VolumeInfo_Local.from_dictionary(dictionary.get('local')) if dictionary.get('local') else None
        name = dictionary.get('name')
        nfs = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_nfs.PodInfo_PodSpec_VolumeInfo_NFS.from_dictionary(dictionary.get('nfs')) if dictionary.get('nfs') else None
        persistent_volume_claim = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_pvc.PodInfo_PodSpec_VolumeInfo_PVC.from_dictionary(dictionary.get('persistentVolumeClaim')) if dictionary.get('persistentVolumeClaim') else None
        photon_persistent_disk = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_photon_persistent_disk.PodInfo_PodSpec_VolumeInfo_PhotonPersistentDisk.from_dictionary(dictionary.get('photonPersistentDisk')) if dictionary.get('photonPersistentDisk') else None
        portworx_volume =  cohesity_management_sdk.models.pod_info_pod_spec_volume_info_portworx.PodInfo_PodSpec_VolumeInfo_Portworx.from_dictionary(dictionary.get('portworxVolume')) if dictionary.get('portworxVolume') else None
        projected = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_projected.PodInfo_PodSpec_VolumeInfo_Projected.from_dictionary(dictionary.get('projected')) if dictionary.get('projected') else None
        quobyte = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_quobyte.PodInfo_PodSpec_VolumeInfo_Quobyte.from_dictionary(dictionary.get('quobyte')) if dictionary.get('quobyte') else None
        rbd = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_rbd.PodInfo_PodSpec_VolumeInfo_RBD.from_dictionary(dictionary.get('rbd')) if dictionary.get('rbd') else None
        scale_io = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_scale_io.PodInfo_PodSpec_VolumeInfo_ScaleIO.from_dictionary(dictionary.get('scaleIo')) if dictionary.get('scaleIo') else None
        secret = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_config_map.PodInfo_PodSpec_VolumeInfo_ConfigMap.from_dictionary(dictionary.get('secret')) if dictionary.get('secret') else None
        storageos = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_storage_os.PodInfo_PodSpec_VolumeInfo_StorageOS.from_dictionary(dictionary.get('storageos')) if dictionary.get('storageos') else None
        vsphere_volume = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_vsphere_virtual_disk.PodInfo_PodSpec_VolumeInfo_VsphereVirtualDisk.from_dictionary(dictionary.get('vsphereVolume')) if dictionary.get('vsphereVolume') else None
        

        # Return an object of this model
        return cls(aws_elastic_block_store,
                   azure_disk,
                   azure_file,
                   cephfs,
                   cinder,
                   config_map,
                   csi,
                   downward_api,
                   empty_dir,
                   ephemeral,
                   fc,
                   flex_volume,
                   flocker,
                   gce_persistent_disk,
                   glusterfs,
                   host_path,
                   iscsi,
                   local,
                   name,
                   nfs,
                   persistent_volume_claim,
                   photon_persistent_disk,
                   portworx_volume,
                   projected,
                   quobyte,
                   rbd,
                   scale_io,
                   secret,
                   storageos,
                   vsphere_volume)


