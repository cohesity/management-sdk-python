# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GcpCredentials(object):

    """Implementation of the 'GcpCredentials' model.

    Specifies the credentials to authenticate with Google Cloud Platform.

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
        project_id (string): Specifies Id of the project associated with
            Google cloud account.
        vpc_network (string): Specifies the VPC Network to deploy proxy VMs.
        vpc_subnetwork (string): Specifies the subnetwork to deploy proxy
            VMs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_email_address":'clientEmailAddress',
        "client_private_key":'clientPrivateKey',
        "gcp_type":'gcpType',
        "project_id":'projectId',
        "vpc_network":'vpcNetwork',
        "vpc_subnetwork":'vpcSubnetwork'
    }

    def __init__(self,
                 client_email_address=None,
                 client_private_key=None,
                 gcp_type=None,
                 project_id=None,
                 vpc_network=None,
                 vpc_subnetwork=None):
        """Constructor for the GcpCredentials class"""

        # Initialize members of the class
        self.client_email_address = client_email_address
        self.client_private_key = client_private_key
        self.gcp_type = gcp_type
        self.project_id = project_id
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
        project_id = dictionary.get('projectId')
        vpc_network = dictionary.get('vpcNetwork')
        vpc_subnetwork = dictionary.get('vpcSubnetwork')

        # Return an object of this model
        return cls(client_email_address,
                   client_private_key,
                   gcp_type,
                   project_id,
                   vpc_network,
                   vpc_subnetwork)


