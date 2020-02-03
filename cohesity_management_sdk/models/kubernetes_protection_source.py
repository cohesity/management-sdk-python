# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class KubernetesProtectionSource(object):

    """Implementation of the 'KubernetesProtectionSource' model.

    Specifies a Protection Source in Kubernetes environment.

    Attributes:
        description (string): Specifies an optional description of the
            object.
        name (string): Specifies a unique name of the Protection Source.
        mtype (TypeKubernetesProtectionSourceEnum): Specifies the type of the
            entity in a Kubernetes environment. Specifies the type of a
            Kubernetes Protection Source. 'kCluster' indicates a Kubernetes
            Cluster. 'kNamespace' indicates a namespace in a Kubernetes
            Cluster. 'kService' indicates a service running on a Kubernetes
            Cluster.
        uuid (string): Specifies the UUID of the object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "name":'name',
        "mtype":'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 description=None,
                 name=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the KubernetesProtectionSource class"""

        # Initialize members of the class
        self.description = description
        self.name = name
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
        description = dictionary.get('description')
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(description,
                   name,
                   mtype,
                   uuid)


