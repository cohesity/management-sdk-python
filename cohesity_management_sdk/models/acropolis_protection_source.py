# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.virtual_disk_config


class AcropolisProtectionSource(object):

    """Implementation of the 'AcropolisProtectionSource' model.

    Specifies a Protection Source in Acropolis environment.


    Attributes:

        cluster_uuid (string): Specifies the UUID of the Acropolis cluster
            instance to which this entity belongs to.
        description (string): Specifies a description about the Protection
            Source.
        mount_path (bool): Specifies whether the VM is an agent VM. This is
            applicable to acropolis entity of type kVirtualMachine.
        name (string): Specifies the name of the Acropolis Object.
        ngt_capabilities (list of int): Specifies enabled capabilities for NGT
            on the VM. This is applicable to acropolis entity of type
            kVirtualMachine.
        ngt_enable_status (int): Specifies if NGT is enabled on the VM. This is
            applicable to acropolis entity of type kVirtualMachine.
        ngt_install_status (int): Specified if NGT is installed on the VM. This
            is applicable to acropolis entity of type kVirtualMachine.
        ngt_reachable (bool): Specifies if NGT on the VM is reachable from
            Controller VM. This is applicable to acropolis entity of type
            kVirtualMachine.
        ngt_version (string): Specifies version of NGT installed on the VM.
            This is applicable to acropolis entity of type kVirtualMachine.
        mtype (int): Specifies the type of an Acropolis Protection Source
            Object such as 'kPrismCentral', 'kHost', 'kNetwork', etc.
        uuid (string): Specifies the UUID of the Acropolis Object. This is
            unique within the cluster instance. Together with clusterUuid, this
            entity is unique within the Acropolis environment.
        version (string): Specifies the version of an Acropolis cluster or
            standalone cluster.
        virtual_disks (list of VirtualDiskConfig): Specifies an array of
            virtual disks that are part of the Virtual Machine. This is
            populated for entities of type 'kVirtualMachine'.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_uuid":'clusterUuid',
        "description":'description',
        "mount_path":'mountPath',
        "name":'name',
        "ngt_capabilities":'ngtCapabilities',
        "ngt_enable_status":'ngtEnableStatus',
        "ngt_install_status":'ngtInstallStatus',
        "ngt_reachable":'ngtReachable',
        "ngt_version":'ngtVersion',
        "mtype":'type',
        "uuid":'uuid',
        "version":'version',
        "virtual_disks":'virtualDisks',
    }
    def __init__(self,
                 cluster_uuid=None,
                 description=None,
                 mount_path=None,
                 name=None,
                 ngt_capabilities=None,
                 ngt_enable_status=None,
                 ngt_install_status=None,
                 ngt_reachable=None,
                 ngt_version=None,
                 mtype=None,
                 uuid=None,
                 version=None,
                 virtual_disks=None,
            ):

        """Constructor for the AcropolisProtectionSource class"""

        # Initialize members of the class
        self.cluster_uuid = cluster_uuid
        self.description = description
        self.mount_path = mount_path
        self.name = name
        self.ngt_capabilities = ngt_capabilities
        self.ngt_enable_status = ngt_enable_status
        self.ngt_install_status = ngt_install_status
        self.ngt_reachable = ngt_reachable
        self.ngt_version = ngt_version
        self.mtype = mtype
        self.uuid = uuid
        self.version = version
        self.virtual_disks = virtual_disks

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
        cluster_uuid = dictionary.get('clusterUuid')
        description = dictionary.get('description')
        mount_path = dictionary.get('mountPath')
        name = dictionary.get('name')
        ngt_capabilities = dictionary.get("ngtCapabilities")
        ngt_enable_status = dictionary.get('ngtEnableStatus')
        ngt_install_status = dictionary.get('ngtInstallStatus')
        ngt_reachable = dictionary.get('ngtReachable')
        ngt_version = dictionary.get('ngtVersion')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')
        version = dictionary.get('version')
        virtual_disks = None
        if dictionary.get('virtualDisks') != None:
            virtual_disks = list()
            for structure in dictionary.get('virtualDisks'):
                virtual_disks.append(cohesity_management_sdk.models.virtual_disk_config.VirtualDiskConfig.from_dictionary(structure))

        # Return an object of this model
        return cls(
            cluster_uuid,
            description,
            mount_path,
            name,
            ngt_capabilities,
            ngt_enable_status,
            ngt_install_status,
            ngt_reachable,
            ngt_version,
            mtype,
            uuid,
            version,
            virtual_disks
)