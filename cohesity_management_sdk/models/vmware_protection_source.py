# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.agent_information
import cohesity_management_sdk.models.datastore_info
import cohesity_management_sdk.models.ip_details
import cohesity_management_sdk.models.vmware_object_id
import cohesity_management_sdk.models.tag_attribute
import cohesity_management_sdk.models.vcloud_director_info
import cohesity_management_sdk.models.virtual_disk_info
import cohesity_management_sdk.models.vmware_cdp_protection_source_info
import cohesity_management_sdk.models.vm_linking_info

class VmwareProtectionSource(object):

    """Implementation of the 'VMwareProtectionSource' model.

    Specifies a Protection Source in a VMware environment.

    Attributes:
        agent_id (long|int): Specifies the id of the persistent agent.
        agents (list of AgentInformation): Specifies the list of agent
            information on the Virtual Machine. This is set only if the
            Virtual Machine has persistent agent.
        cdp_info (VMwareCdpProtectionSourceInfo): This field contains the
            details about Continuous Data Protection (CDP) of the Protection
            Source.
        connection_state (ConnectionStateEnum): Specifies the connection state
            of the Object and are only valid for ESXi hosts ('kHostSystem') or
            Virtual Machines ('kVirtualMachine'). These enums are equivalent
            to the connection states documented in VMware's reference
            documentation. Examples of Cohesity connection states include
            'kConnected', 'kDisconnected', 'kInacccessible', etc. 'kConnected'
            indicates that server has access to virtual machine.
            'kDisconnected' indicates that server is currently disconnected to
            virtual machine. 'kInaccessible' indicates that one or more
            configuration files are inacccessible. 'kInvalid' indicates that
            virtual machine configuration is invalid. 'kOrphaned' indicates
            that virtual machine is no longer registered on the host it is
            associated with. 'kNotResponding' indicates that virtual machine
            is failed to response due to external issues such as network
            connectivity, hostd not running etc.
        datastore_info (DatastoreInfo): TODO: type description here.
        folder_type (FolderTypeEnum): Specifies the folder type for the
            'kFolder' Object. 'kVMFolder' indicates folder can hold VMs or
            vApps. 'kHostFolder' indicates folder can hold hosts and compute
            resources. 'kDatastoreFolder' indicates folder can hold datastores
            and storage pods. 'kNetworkFolder' indicates folder can hold
            networks and switches. 'kRootFolder' indicates folder can hold
            datacenters.
        has_persistent_agent (bool): Set to true if a persistent agent is
            running on the Virtual Machine. This is populated for entities of
            type 'kVirtualMachine'.
        host_type (HostTypeVmwareProtectionSourceEnum): Specifies the host
            type for the 'kVirtualMachine' Object. 'kLinux' indicates the
            Linux operating system. 'kWindows' indicates the Microsoft Windows
            operating system. 'kAix' indicates the IBM AIX operating system.
            'kSolaris' indicates the Oracle Solaris operating system.
            'kSapHana' indicates the Sap Hana database system developed by SAP
            SE. 'kOther' indicates the other types of operating system.
        id (VmwareObjectId): Specifies a unique Protection Source id across
            Cohesity Clusters. It is derived from the id of the VMware
            Protection Source.
        ip_details (IpDetails): This field can be used to capture IP Addresses
            for entities that have it.
        is_vm_template (bool): IsTemplate specifies if the VM is a template or
            not.
        is_vmc_entity (bool): This field is used for indicating that
            registered vmware source is a VMC (VMware Cloud) environment.
        name (string): Specifies a human readable name of the Protection
            Source.
        tag_attributes (list of TagAttribute): Specifies the optional list of
            VM Tag attributes associated with this Object.
        tools_running_status (ToolsRunningStatusEnum): Specifies the status of
            VMware Tools for the guest OS on the VM. This is only valid for
            the 'kVirtualMachine' type. 'kGuestToolsRunning' means the VMware
            tools are running on the guest OS. 'kGuestToolsNotRunning' means
            the VMware tools are not running on the guest OS. 'kUnknown' means
            the state of the VMware tools on the guest OS is not known.
            'kGuestToolsExecutingScripts' means the guest OS is currently
            executing scripts using VMware tools.
        mtype (TypeVmwareProtectionSourceEnum): Specifies the type of managed
            Object in a VMware Protection Source. Examples of VMware Objects
            include 'kVCenter', 'kFolder', 'kDatacenter', 'kResourcePool',
            'kDatastore', 'kVirtualMachine', etc. 'kVCenter' indicates the
            vCenter entity in a VMware protection source type. 'kFolder
            indicates the folder entity (of any kind) in a VMware protection
            source type. 'kDatacenter' indicates the datacenter entity in a
            VMware protection source type. 'kComputeResource' indicates the
            physical compute resource entity in a VMware protection source
            type. 'kResourcePool' indicates the set of physical resourses
            within a compute resource or cloudcompute resource. 'kDataStore'
            indicates the datastore entity in a VMware protection source type.
            'kHostSystem' indicates the ESXi host entity in a VMware
            protection source type. 'kVirtualMachine' indicates the virtual
            machine entity in a VMware protection source type. 'kVirtualApp'
            indicates the virtual app entity in a VMware protection source
            type. 'kStandaloneHost' indicates the standalone ESXi host entity
            (not managed by vCenter) in a VMware protection source type.
            'kStoragePod' indicates the storage pod entity in a VMware
            protection source type. 'kNetwork' indicates the standard vSwitch
            in a VMware protection source type. 'kDistributedVirtualPortgroup'
            indicates a distributed vSwitch port group in a VMware protection
            source type. 'kTagCategory' indicates a tag category entity in a
            VMware protection source type. 'kTag' indocates a tag entity in a
            VMware protection source type. 'kOpaqueNetwork' indicates a opaque
            network which is created and managed by an entity outside of
            vSphere. 'kVCloudDirector' indicates a vCloud director entity in a
            VMware protection source type. 'kOrganization' indicates an
            Organization under a vCD in a VMware protection source type.
            'kVirtualDatacenter' indicates a virtual datacenter entity in a
            VMware protection source type. 'kCatalog' indocates a VCD catalog
            entity in a VMware protection source type. 'kOrgMetadata'
            indicates an VCD organization metadata in a VMware protection
            source type. 'kStoragePolicy' indicates a storage policy
            associated with the vApp in a VMware protection source type.
        vcloud_director_info (list of VcloudDirectorInfo): Specifies an array
            of vCenters to be registered
        version (string): For vCenter and ESXi, this will show the software
            version. For VMs, this will show the hardware version.
        virtual_disks (list of VirtualDiskInfo): Specifies an array of virtual
            disks that are part of the Virtual Machine. This is populated for
            entities of type 'kVirtualMachine'.
        vm_linking_info (VmLinkingInfo): This field contains information about
            a VM that has been migrated from another vCenter. This is only
            valid for the 'kVirtualMachine' type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "agent_id":'agentId',
        "agents":'agents',
        "cdp_info":'cdpInfo',
        "connection_state":'connectionState',
        "datastore_info":'datastoreInfo',
        "folder_type":'folderType',
        "has_persistent_agent":'hasPersistentAgent',
        "host_type":'hostType',
        "id":'id',
        "ip_details":'ipDetails',
        "is_vm_template":'isVmTemplate',
        "is_vmc_entity":'isVmcEntity',
        "name":'name',
        "tag_attributes":'tagAttributes',
        "tools_running_status":'toolsRunningStatus',
        "mtype":'type',
        "vcloud_director_info":'vCloudDirectorInfo',
        "version":'version',
        "virtual_disks":'virtualDisks',
        "vm_linking_info":'vmLinkingInfo'
    }

    def __init__(self,
                 agent_id=None,
                 agents=None,
                 cdp_info=None,
                 connection_state=None,
                 datastore_info=None,
                 folder_type=None,
                 has_persistent_agent=None,
                 host_type=None,
                 id=None,
                 ip_details=None,
                 is_vm_template=None,
                 is_vmc_entity=None,
                 name=None,
                 tag_attributes=None,
                 tools_running_status=None,
                 mtype=None,
                 vcloud_director_info=None,
                 version=None,
                 virtual_disks=None,
                 vm_linking_info=None):
        """Constructor for the VmwareProtectionSource class"""

        # Initialize members of the class
        self.agent_id = agent_id
        self.agents = agents
        self.cdp_info = cdp_info
        self.connection_state = connection_state
        self.datastore_info = datastore_info
        self.folder_type = folder_type
        self.has_persistent_agent = has_persistent_agent
        self.host_type = host_type
        self.id = id
        self.ip_details = ip_details
        self.is_vm_template = is_vm_template
        self.is_vmc_entity = is_vmc_entity
        self.name = name
        self.tag_attributes = tag_attributes
        self.tools_running_status = tools_running_status
        self.mtype = mtype
        self.vcloud_director_info = vcloud_director_info
        self.version = version
        self.virtual_disks = virtual_disks
        self.vm_linking_info = vm_linking_info


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
        agent_id = dictionary.get('agentId')
        agents = None
        if dictionary.get('agents') != None:
            agents = list()
            for structure in dictionary.get('agents'):
                agents.append(cohesity_management_sdk.models.agent_information.AgentInformation.from_dictionary(structure))
        cdp_info = cohesity_management_sdk.models.vmware_cdp_protection_source_info.VMwareCdpProtectionSourceInfo.from_dictionary(dictionary.get('cdpInfo')) if dictionary.get('cdpInfo') else None
        connection_state = dictionary.get('connectionState')
        datastore_info = cohesity_management_sdk.models.datastore_info.DatastoreInfo.from_dictionary(dictionary.get('datastoreInfo')) if dictionary.get('datastoreInfo') else None
        folder_type = dictionary.get('folderType')
        has_persistent_agent = dictionary.get('hasPersistentAgent')
        host_type = dictionary.get('hostType')
        id = cohesity_management_sdk.models.vmware_object_id.VmwareObjectId.from_dictionary(dictionary.get('id')) if dictionary.get('id') else None
        ip_details = cohesity_management_sdk.models.ip_details.IpDetails.from_dictionary(dictionary.get('ipDetails')) if dictionary.get('ipDetails') else None
        is_vm_template = dictionary.get('isVmTemplate')
        is_vmc_entity = dictionary.get('isVmcEntity')
        name = dictionary.get('name')
        tag_attributes = None
        if dictionary.get('tagAttributes') != None:
            tag_attributes = list()
            for structure in dictionary.get('tagAttributes'):
                tag_attributes.append(cohesity_management_sdk.models.tag_attribute.TagAttribute.from_dictionary(structure))
        tools_running_status = dictionary.get('toolsRunningStatus')
        mtype = dictionary.get('type')
        vcloud_director_info = None
        if dictionary.get('vCloudDirectorInfo') != None:
            vcloud_director_info = list()
            for structure in dictionary.get('vCloudDirectorInfo'):
                vcloud_director_info.append(cohesity_management_sdk.models.vcloud_director_info.VcloudDirectorInfo.from_dictionary(structure))
        version = dictionary.get('version')
        virtual_disks = None
        if dictionary.get('virtualDisks') != None:
            virtual_disks = list()
            for structure in dictionary.get('virtualDisks'):
                virtual_disks.append(cohesity_management_sdk.models.virtual_disk_info.VirtualDiskInfo.from_dictionary(structure))
        vm_linking_info = cohesity_management_sdk.models.vm_linking_info.VmLinkingInfo.from_dictionary(dictionary.get('vmLinkingInfo')) if dictionary.get('vmLinkingInfo') else None

        # Return an object of this model
        return cls(agent_id,
                   agents,
                   cdp_info,
                   connection_state,
                   datastore_info,
                   folder_type,
                   has_persistent_agent,
                   host_type,
                   id,
                   ip_details,
                   is_vm_template,
                   is_vmc_entity,
                   name,
                   tag_attributes,
                   tools_running_status,
                   mtype,
                   vcloud_director_info,
                   version,
                   virtual_disks,
                   vm_linking_info)


