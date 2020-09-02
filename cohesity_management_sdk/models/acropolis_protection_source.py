# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class AcropolisProtectionSource(object):

    """Implementation of the 'AcropolisProtectionSource' model.

    Specifies a Protection Source in Acropolis environment.

    Attributes:
        cluster_uuid (string): Specifies the UUID of the Acropolis cluster
            instance to which this entity belongs to.
        description (string): Specifies a description about the Protection
            Source.
        mount_path (bool): Specifies whether the the VM is an agent VM. This
            is applicable to acropolis entity of type kVirtualMachine.
        name (string): Specifies the name of the Acropolis Object.
        mtype (TypeEnum): Specifies the type of an Acropolis Protection Source
            Object such as 'kPrismCentral', 'kHost', 'kNetwork', etc.
            Specifies the type of an Acropolis source entity. 'kPrismCentral'
            indicates a collection of multiple Nutanix clusters.
            'kStandaloneCluster' indicates a single Nutanix cluster.
            'kCluster' indicates a Nutanix cluster managed by a Prism
            Central. 'kHost' indicates an Acropolis host. 'kVirtualMachine'
            indicates a Virtual Machine. 'kNetwork' indicates a Virtual
            Machine network object. 'kStorageContainer' represents a storage
            container object.
        uuid (string): Specifies the UUID of the Acropolis Object. This is
            unique within the cluster instance. Together with clusterUuid,
            this entity is unique within the Acropolis environment.
        version (string, optional): Specifies the version of an Acropolis
            cluster or standalone cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_uuid":'clusterUuid',
        "description":'description',
        "mount_path":'mountPath',
        "name":'name',
        "mtype":'type',
        "uuid":'uuid',
        "version":'version'
    }

    def __init__(self,
                 cluster_uuid=None,
                 description=None,
                 mount_path=None,
                 name=None,
                 mtype=None,
                 uuid=None,
                 version=None):
        """Constructor for the AcropolisProtectionSource class"""

        # Initialize members of the class
        self.cluster_uuid = cluster_uuid
        self.description = description
        self.mount_path = mount_path
        self.name = name
        self.mtype = mtype
        self.uuid = uuid
        self.version = version


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
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(cluster_uuid,
                   description,
                   mount_path,
                   name,
                   mtype,
                   uuid,
                   version)


