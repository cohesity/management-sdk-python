# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class KubernetesParams(object):

    """Implementation of the 'KubernetesParams' model.

    Specifies the parameters required to register Application Servers running
    in a Protection Source.


    Attributes:

        datamover_image_location (string): Specifies the location of Datamover
            image in private registry.
        init_container_image_location (string): Specifies the location of the
            image for init containers.
        kubernetes_distribution (KubernetesDistributionEnum): Specifies the
            distribution if the environment is kKubernetes.
            overrideDescription: true
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
        "init_container_image_location":'initContainerImageLocation',
        "kubernetes_distribution":'kubernetesDistribution',
        "velero_aws_plugin_image_location":'veleroAwsPluginImageLocation',
        "velero_image_location":'veleroImageLocation',
        "velero_openshift_plugin_image_location":'veleroOpenshiftPluginImageLocation',
    }
    def __init__(self,
                 datamover_image_location=None,
                 init_container_image_location=None,
                 kubernetes_distribution=None,
                 velero_aws_plugin_image_location=None,
                 velero_image_location=None,
                 velero_openshift_plugin_image_location=None,
            ):

        """Constructor for the KubernetesParams class"""

        # Initialize members of the class
        self.datamover_image_location = datamover_image_location
        self.init_container_image_location = init_container_image_location
        self.kubernetes_distribution = kubernetes_distribution
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
        init_container_image_location = dictionary.get('initContainerImageLocation')
        kubernetes_distribution = dictionary.get('kubernetesDistribution')
        velero_aws_plugin_image_location = dictionary.get('veleroAwsPluginImageLocation')
        velero_image_location = dictionary.get('veleroImageLocation')
        velero_openshift_plugin_image_location = dictionary.get('veleroOpenshiftPluginImageLocation')

        # Return an object of this model
        return cls(
            datamover_image_location,
            init_container_image_location,
            kubernetes_distribution,
            velero_aws_plugin_image_location,
            velero_image_location,
            velero_openshift_plugin_image_location
)