# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.tag_attribute

class GcpProtectionSource(object):

    """Implementation of the 'GcpProtectionSource' model.

    Specifies a Protection Source in GCP environment.

    Attributes:
        client_email_address (string): Specifies Client email address
            associated with the service account.
        client_private_key (string): Specifies Client private associated with
            the service account.
        gcp_type (GcpTypeEnum): Specifies the entity type such as 'kIAMUser'
            if the environment is kGCP. Specifies the type of a GCP source
            entity. 'kIAMUser' indicates a unique user within a GCP account.
            'kProject' represents compute resources and storage. 'kRegion'
            indicates a geographical region in the global infrastructure.
            'kAvailabilityZone' indicates an availability zone within a
            region. 'kVirtualMachine' indicates a Virtual Machine running in
            GCP environment. 'kVPC' indicates a virtual private cloud (VPC)
            network within GCP. 'kSubnet' indicates a subnet inside the VPC.
            'kNetworkSecurityGroup' represents a network security group.
            'kInstanceType' represents various machine types. 'kLabel'
            represents a label present on the instances. 'kMetaData'
            represents a custom metadata present on instances. 'kTag'
            represents a network tag on instances. 'kVPCConnector' represents
            a VPC connector used for serverless VPC access.
        host_project_id (string): Specifies the host project id. It is
            populated in entities of type kSubnet if the subnet is part of a
            shared VPC. This contains the ID of host project the subnet
            belongs to. Populated in entities of type kProject if the
            project is a service project in a Shared VPC setup. This contains
            the ID of the host project it is attached to.
        host_type (HostTypeEnum): Specifies the OS type of the Protection
            Source of type 'kVirtualMachine' such as 'kWindows' or 'kLinux'.
            overrideDescription: true 'kLinux' indicates the Linux operating
            system. 'kWindows' indicates the Microsoft Windows operating
            system. 'kAix' indicates the IBM AIX operating system. 'kSolaris'
            indicates the Oracle Solaris operating system. 'kSapHana'
            indicates the Sap Hana database system developed by SAP SE.
            'kOther' indicates the other types of operating system.
        ip_addresses_vm (string): Specifies the IP address of the entity of
            type 'kVirtualMachine'.
        name (string): Specifies the name of the Object set by the Cloud
            Provider. If the provider did not set a name for the object, this
            field is not set.
        owner_id (string): Specifies the owner id of the resource in GCP
            environment. With type, name and ownerId gives a globally unique
            identity to the GCP entity.
        physical_source_id (long|int): Specifies the Protection Source id of
            the registered Physical Host. If the cloud entity is protected
            using a Physical Agent, it must be registered as a physical host.
        project_id (string): Specifies the project Id. For the kIAMUser entity
            this contains the id of the project to be used to deploy proxy
            VMs. For entities of type kVirtualMachine this contains the id of
            the project the virtual machine belongs to.
        region_id (string): Specifies the region Id. For the kIAMUser entity
            this contains the region to be used to deploy proxy VMs. For
            entities of type kVirtualMachine this contains the region the
            virtual machine belongs to.
        resource_id (string): Specifies the unique Id of the resource given by
            the cloud provider.
        restore_task_id (long|int): Specifies the id of the "convert and
            deploy" restore task that created the entity in the cloud.  It is
            required to support the DR-to-cloud usecase where we replicate an
            on-prem entity to a cluster running in cloud, bring it up using
            "convert and deploy" mechanism, protect it using a cloud job that
            uses physical adapter, and convert it back to the on-prem format
            before replication.  Before replicating, we need to update the
            backup task state of the backed up entity using the on-prem entity
            and on-prem entity's parent. The id is used to lookup the restore
            entity that contains details about the on-prem entity.  It is set
            at the time of refreshing the cloud entity hierarchy if all the
            following conditions are met: Name of the current entity matches
            with name of any cloud entity deployed using the "convert and
            deploy" restore task. Restore entity associated with the above
            matched cloud entity has 'failed_over' flag set to true in its
            cloud extension.
        tag_attributes (list of TagAttribute):  Specifies the list of GCP tag
            attributes.
        mtype (TypeGcpProtectionSourceEnum): Specifies the type of an GCP
            Protection Source Object such as 'kIAMUser', 'kProject',
            'kRegion', etc. Specifies the type of a GCP source entity.
            'kIAMUser' indicates a unique user within a GCP account.
            'kProject' represents compute resources and storage. 'kRegion'
            indicates a geographical region in the global infrastructure.
            'kAvailabilityZone' indicates an availability zone within a
            region. 'kVirtualMachine' indicates a Virtual Machine running in
            GCP environment. 'kVPC' indicates a virtual private cloud (VPC)
            network within GCP. 'kSubnet' indicates a subnet inside the VPC.
            'kNetworkSecurityGroup' represents a network security group.
            'kInstanceType' represents various machine types. 'kLabel'
            represents a label present on the instances. 'kMetaData'
            represents a custom metadata present on instances. 'kTag'
            represents a network tag on instances. 'kVPCConnector' represents
            a VPC connector used for serverless VPC access.
        vpc_network (string): Specifies the VPC Network to deploy proxy VMs.
        vpc_subnetwork (string): Specifies the subnetwork to deploy proxy
            VMs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_email_address":'clientEmailAddress',
        "client_private_key":'clientPrivateKey',
        "gcp_type":'gcpType',
        "host_project_id":'hostProjectId',
        "host_type":'hostType',
        "ip_addresses_vm":'ipAddressesVM',
        "name":'name',
        "owner_id":'ownerId',
        "physical_source_id":'physicalSourceId',
        "project_id":'projectId',
        "region_id":'regionId',
        "resource_id":'resourceId',
        "restore_task_id":'restoreTaskId',
        "mtype":'type',
        "tag_attributes":'tagAttributes',
        "vpc_network":'vpcNetwork',
        "vpc_subnetwork":'vpcSubnetwork'
    }

    def __init__(self,
                 client_email_address=None,
                 client_private_key=None,
                 gcp_type=None,
                 host_project_id=None,
                 host_type=None,
                 ip_addresses_vm=None,
                 name=None,
                 owner_id=None,
                 physical_source_id=None,
                 project_id=None,
                 region_id=None,
                 resource_id=None,
                 restore_task_id=None,
                 mtype=None,
                 tag_attributes=None,
                 vpc_network=None,
                 vpc_subnetwork=None):
        """Constructor for the GcpProtectionSource class"""

        # Initialize members of the class
        self.client_email_address = client_email_address
        self.client_private_key = client_private_key
        self.gcp_type = gcp_type
        self.host_project_id = host_project_id
        self.host_type = host_type
        self.ip_addresses_vm = ip_addresses_vm
        self.name = name
        self.owner_id = owner_id
        self.physical_source_id = physical_source_id
        self.project_id = project_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.restore_task_id = restore_task_id
        self.mtype = mtype
        self.tag_attributes = tag_attributes
        self.vpc_network = vpc_network
        self.vpc_subnetwork = vpc_subnetwork


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
        client_email_address = dictionary.get('clientEmailAddress')
        client_private_key = dictionary.get('clientPrivateKey')
        gcp_type = dictionary.get('gcpType')
        host_project_id = dictionary.get('hostProjectId', None)
        host_type = dictionary.get('hostType')
        ip_addresses_vm = dictionary.get('ipAddressesVM')
        name = dictionary.get('name')
        owner_id = dictionary.get('ownerId')
        physical_source_id = dictionary.get('physicalSourceId')
        project_id = dictionary.get('projectId')
        region_id = dictionary.get('regionId')
        resource_id = dictionary.get('resourceId')
        restore_task_id = dictionary.get('restoreTaskId')
        tag_attributes = None
        if dictionary.get('tagAttributes') != None:
            tag_attributes= list()
            for structure in dictionary.get('tagAttributes'):
                tag_attributes.append(cohesity_management_sdk.models.tag_attribute.TagAttribute.from_dictionary(structure))
        mtype = dictionary.get('type')
        vpc_network = dictionary.get('vpcNetwork')
        vpc_subnetwork = dictionary.get('vpcSubnetwork')

        # Return an object of this model
        return cls(client_email_address,
                   client_private_key,
                   gcp_type,
                   host_project_id,
                   host_type,
                   ip_addresses_vm,
                   name,
                   owner_id,
                   physical_source_id,
                   project_id,
                   region_id,
                   resource_id,
                   restore_task_id,
                   mtype,
                   tag_attributes,
                   vpc_network,
                   vpc_subnetwork)


