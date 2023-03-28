# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.kubernetes_label_attribute


class KubernetesProtectionSource(object):

    """Implementation of the 'KubernetesProtectionSource' model.

    Specifies a Protection Source in Kubernetes environment.


    Attributes:

        datamover_image_location (string): Specifies the location of Datamover
            image in private registry.
        description (string): Specifies an optional description of the object.
        distribution (DistributionEnum): Specifies the type of the entity in a
            Kubernetes environment. Determines the K8s distribution.
        init_container_image_location (string): Specifies the location of the
            image for init containers.
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
        velero_aws_plugin_image_location (string): Specifies the location of
            Velero AWS plugin image in private registry.
        velero_image_location (string): Specifies the location of Velero image
            in private registry.
        velero_openshift_plugin_image_location (string): Specifies the location
            of the image for openshift plugin container.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "datamover_image_location":'datamoverImageLocation',
        "description":'description',
        "distribution":'distribution',
        "init_container_image_location":'initContainerImageLocation',
        "label_attributes":'labelAttributes',
        "name":'name',
        "mtype":'type',
        "uuid":'uuid',
        "velero_aws_plugin_image_location":'veleroAwsPluginImageLocation',
        "velero_image_location":'veleroImageLocation',
        "velero_openshift_plugin_image_location":'veleroOpenshiftPluginImageLocation',
    }
    def __init__(self,
                 datamover_image_location=None,
                 description=None,
                 distribution=None,
                 init_container_image_location=None,
                 label_attributes=None,
                 name=None,
                 mtype=None,
                 uuid=None,
                 velero_aws_plugin_image_location=None,
                 velero_image_location=None,
                 velero_openshift_plugin_image_location=None,
            ):

        """Constructor for the KubernetesProtectionSource class"""

        # Initialize members of the class
        self.datamover_image_location = datamover_image_location
        self.description = description
        self.distribution = distribution
        self.init_container_image_location = init_container_image_location
        self.label_attributes = label_attributes
        self.name = name
        self.mtype = mtype
        self.uuid = uuid
        self.velero_aws_plugin_image_location = velero_aws_plugin_image_location
        self.velero_image_location = velero_image_location
        self.velero_openshift_plugin_image_location = velero_openshift_plugin_image_location

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
        datamover_image_location = dictionary.get('datamoverImageLocation')
        description = dictionary.get('description')
        distribution = dictionary.get('distribution')
        init_container_image_location = dictionary.get('initContainerImageLocation')
        label_attributes = None
        if dictionary.get('labelAttributes') != None:
            label_attributes = list()
            for structure in dictionary.get('labelAttributes'):
                label_attributes.append(cohesity_management_sdk.models.kubernetes_label_attribute.KubernetesLabelAttribute.from_dictionary(structure))
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')
        velero_aws_plugin_image_location = dictionary.get('veleroAwsPluginImageLocation')
        velero_image_location = dictionary.get('veleroImageLocation')
        velero_openshift_plugin_image_location = dictionary.get('veleroOpenshiftPluginImageLocation')

        # Return an object of this model
        return cls(
            datamover_image_location,
            description,
            distribution,
            init_container_image_location,
            label_attributes,
            name,
            mtype,
            uuid,
            velero_aws_plugin_image_location,
            velero_image_location,
            velero_openshift_plugin_image_location
)