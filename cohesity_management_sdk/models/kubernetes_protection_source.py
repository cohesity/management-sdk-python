# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.kubernetes_label_attribute

class KubernetesProtectionSource(object):

    """Implementation of the 'KubernetesProtectionSource' model.

    Specifies a Protection Source in Kubernetes environment.

    Attributes:
        description (string): Specifies an optional description of the
            object.
        label_attributes (list of KubernetesLabelAttribute): Specifies the list
            of label attributes of this source.
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
        "label_attributes":'labelAttributes',
        "name":'name',
        "mtype":'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 description=None,
                 label_attributes=None,
                 name=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the KubernetesProtectionSource class"""

        # Initialize members of the class
        self.description = description
        self.label_attributes = label_attributes
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
        label_attributes = None
        if dictionary.get('labelAttributes') != None:
            label_attributes = list()
            for structure in dictionary.get('labelAttributes'):
                label_attributes.append(cohesity_management_sdk.models.kubernetes_label_attribute.KubernetesLabelAttribute.from_dictionary(structure))
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(description,
                   label_attributes,
                   name,
                   mtype,
                   uuid)


