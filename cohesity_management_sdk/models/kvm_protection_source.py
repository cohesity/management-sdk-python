# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class KvmProtectionSource(object):

    """Implementation of the 'KvmProtectionSource' model.

    Specifies a Protection Source in KVM environment.

    Attributes:
        agent_error (string): Specifies a message when the agent cannot be
            reached.
        agent_id (long|int): Specifies the ID of the Agent with which this KVM
            entity is associated when the entity represents a Delegate host or
            KVM host.
        cluster_id (string): Specifies the cluster ID for 'kCluster' objects.
        datacenter_id (string): Specifies the ID of the 'kDatacenter'
            objects.
        description (string): Specifies a description about the Protection
            Source.
        name (string): Specifies the name of the KVM entity.
        network_id (string): Specifies the network ID to which Vnic is
            attached.
        mtype (TypeKvmProtectionSourceEnum): Specifies the type of KVM
            Protection Source entities such as 'kDatacenter', 'kCluster',
            'kVirtualMachine', etc. Specifies the type of an KVM source
            entity. 'kOVirtManager' indicates the root entity registered with
            Cohesity cluster. 'kStandaloneHost' indicates a host registered
            with Cohesity cluster. 'kDatacenter' indicates a KVM datacenter
            managed by the OVirt manager. 'kCluster' indicates a KVM cluster
            managed by the OVirt manager. 'kHost' indicates a host within the
            KVM environment. 'kVirtualMachine' indicates a virtual machine in
            the KVM enironment. 'kNetwork' represents a network used by the
            virtual machine entity. 'kStorageDomain' represents a storage
            domain in the KVM environment. 'kVNicProfile' represents a VNic
            profile.
        uuid (string): Specifies the UUID of the Object. This is unique within
            the KVM environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "agent_error":'agentError',
        "agent_id":'agentId',
        "cluster_id":'clusterId',
        "datacenter_id":'datacenterId',
        "description":'description',
        "name":'name',
        "network_id":'networkId',
        "mtype":'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 agent_error=None,
                 agent_id=None,
                 cluster_id=None,
                 datacenter_id=None,
                 description=None,
                 name=None,
                 network_id=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the KvmProtectionSource class"""

        # Initialize members of the class
        self.agent_error = agent_error
        self.agent_id = agent_id
        self.cluster_id = cluster_id
        self.datacenter_id = datacenter_id
        self.description = description
        self.name = name
        self.network_id = network_id
        self.mtype = mtype
        self.uuid = uuid


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
        agent_error = dictionary.get('agentError')
        agent_id = dictionary.get('agentId')
        cluster_id = dictionary.get('clusterId')
        datacenter_id = dictionary.get('datacenterId')
        description = dictionary.get('description')
        name = dictionary.get('name')
        network_id = dictionary.get('networkId')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(agent_error,
                   agent_id,
                   cluster_id,
                   datacenter_id,
                   description,
                   name,
                   network_id,
                   mtype,
                   uuid)


