# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.agent_information
import cohesity_management_sdk.models.hyperv_datastore
import cohesity_management_sdk.models.tag_attribute
import cohesity_management_sdk.models.hyperv_virtual_machine

class HypervProtectionSource(object):

    """Implementation of the 'HypervProtectionSource' model.

    Specifies a Protection Source in HyperV environment.

    Attributes:
        agents (list of AgentInformation): Array of Agents on the Physical
            Protection Source.  Specifiles the agents running on the HyperV
            Protection Source and the status information.
        backup_type (BackupTypeEnum): Specifies the type of backup supported
            by the VM. 'kRctBackup', 'kVssBackup' Specifies the type of an
            HyperV datastore object. 'kRctBackup' indicates backup is done
            using RCT/checkpoints. 'kVssBackup' indicates backup is done using
            VSS.
        build_number (string): Specifies the build number for HyperV SCVMM
            Servers.
        cluster_name (string): Specifies the cluster name for 'kHostCluster'
            objects.
        datastore_info (HypervDatastore): Specifies information about a
            Datastore Object in HyperV environment.
        description (string): Specifies a description about the Protection
            Source.
        host_type (HostTypeHypervProtectionSourceEnum): Specifies host OS type
            for 'kVirtualMachine' objects. 'kLinux' indicates the Linux
            operating system. 'kWindows' indicates the Microsoft Windows
            operating system. 'kAix' indicates the IBM AIX operating system.
            'kSolaris' indicates the Oracle Solaris operating system.
            'kSapHana' indicates the Sap Hana database system developed by SAP
            SE. 'kOther' indicates the other types of operating system.
        hyperv_uuid (string): Specifies the UUID for 'kVirtualMachine' HyperV
            objects.
        name (string): Specifies the name of the HyperV Object.
        tag_attributes (list of TagAttribute): Specifies the list of VM Tag
            attributes associated with this Object.
        mtype (TypeHypervProtectionSourceEnum): Specifies the type of an
            HyperV Protection Source Object such as 'kSCVMMServer',
            'kStandaloneHost', 'kNetwork', etc. overrideDescription: true
            Specifies the type of an HyperV Protection Source. 'kSCVMMServer'
            indicates a collection of root folders clusters. 'kStandaloneHost'
            indicates a single Nutanix cluster. 'kStandaloneCluster' indicates
            a single Nutanix cluster. 'kHostGroup' indicates a Nutanix cluster
            managed by a Prism Central. 'kHypervHost' indicates an HyperV
            host. 'kHostCluster' indicates a Nutanix cluster managed by a
            Prism Central. 'kVirtualMachine' indicates a Virtual Machine.
            'kNetwork' indicates a Virtual Machine network object.
            'kDatastore' represents a storage container object. 'kTag'
            indicates a tag type object. 'kCustomProperty' indicates a custom
            property including tag type.
        uuid (string): Specifies the UUID of the Object. This is unique within
            the HyperV environment.
        vm_info (HypervVirtualMachine): Specifies information about a
            VirtualMachine Object in HyperV environment.
        windows_version (string): Specifies the windows version for HyperV
            hosts.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "agents":'agents',
        "backup_type":'backupType',
        "build_number":'buildNumber',
        "cluster_name":'clusterName',
        "datastore_info":'datastoreInfo',
        "description":'description',
        "host_type":'hostType',
        "hyperv_uuid":'hypervUuid',
        "name":'name',
        "tag_attributes":'tagAttributes',
        "mtype":'type',
        "uuid":'uuid',
        "vm_info":'vmInfo',
        "windows_version":'windowsVersion'
    }

    def __init__(self,
                 agents=None,
                 backup_type=None,
                 build_number=None,
                 cluster_name=None,
                 datastore_info=None,
                 description=None,
                 host_type=None,
                 hyperv_uuid=None,
                 name=None,
                 tag_attributes=None,
                 mtype=None,
                 uuid=None,
                 vm_info=None,
                 windows_version=None):
        """Constructor for the HypervProtectionSource class"""

        # Initialize members of the class
        self.agents = agents
        self.backup_type = backup_type
        self.build_number = build_number
        self.cluster_name = cluster_name
        self.datastore_info = datastore_info
        self.description = description
        self.host_type = host_type
        self.hyperv_uuid = hyperv_uuid
        self.name = name
        self.tag_attributes = tag_attributes
        self.mtype = mtype
        self.uuid = uuid
        self.vm_info = vm_info
        self.windows_version = windows_version


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
        agents = None
        if dictionary.get('agents') != None:
            agents = list()
            for structure in dictionary.get('agents'):
                agents.append(cohesity_management_sdk.models.agent_information.AgentInformation.from_dictionary(structure))
        backup_type = dictionary.get('backupType')
        build_number = dictionary.get('buildNumber', None)
        cluster_name = dictionary.get('clusterName')
        datastore_info = cohesity_management_sdk.models.hyperv_datastore.HypervDatastore.from_dictionary(dictionary.get('datastoreInfo')) if dictionary.get('datastoreInfo') else None
        description = dictionary.get('description')
        host_type = dictionary.get('hostType')
        hyperv_uuid = dictionary.get('hypervUuid')
        name = dictionary.get('name')
        tag_attributes = None
        if dictionary.get('tagAttributes') != None:
            tag_attributes = list()
            for structure in dictionary.get('tagAttributes'):
                tag_attributes.append(cohesity_management_sdk.models.tag_attribute.TagAttribute.from_dictionary(structure))
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')
        vm_info = cohesity_management_sdk.models.hyperv_virtual_machine.HypervVirtualMachine.from_dictionary(dictionary.get('vmInfo')) if dictionary.get('vmInfo') else None
        windows_version = dictionary.get('windowsVersion', None)

        # Return an object of this model
        return cls(agents,
                   backup_type,
                   build_number,
                   cluster_name,
                   datastore_info,
                   description,
                   host_type,
                   hyperv_uuid,
                   name,
                   tag_attributes,
                   mtype,
                   uuid,
                   vm_info,
                   windows_version)


