# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_services_to_connector_ids_map_entry
import cohesity_management_sdk.models.label_attributes_info


class Entity(object):

    """Implementation of the 'Entity' model.

    Message encapsulating a Kubernetes entity


    Attributes:

        datamover_image_location (string): Location of the datamover image
            specified by the user.
        description (string): This is a general description that could be set
            for some entities.
        distribution (int): K8s distribution. This will only be applicable to
            kCluster entities.
        init_container_image_location (string): Location of the init container
            image specified by the user.
        label_attributes_vec (list of LabelAttributesInfo): Label attributes
            vector contains info about the label nodes corresponding to the
            current entity's labels. TODO(jhwang): Make it applicable to
            non-kNamespace type entities also.
        name (string): A human readable name for the object.
        namespace (string): Namespace of object, if applicable. For a PV, this
            field stores the namespace of the PVC which is bound to the PV.
        pvc_name (string): Name of the PVC which is bound to the PV. Applicable
            only to 'kPersistentVolume' type entity.
        services_to_connector_ids_map (list of
            Entity_ServicesToConnectorIdsMapEntry): A mapping from datamover
            services to corresponding unique connector_params IDs. This will be
            generated during registration and updated during refresh.
            Applicable only for 'kCluster' type entities.
        mtype (int): The type of entity this proto refers to.
        uuid (string): The UUID of the object.
        velero_aws_plugin_image_location (string): Location of the Velero AWS
            plugin image specified by the user.
        velero_image_location (string): Location of the Velero image specified
            by the user.
        velero_openshift_plugin_image_location (string): Location of the Velero
            Openshift plugin image specified by the user.
        version (string): Kubernetes cluster version.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "datamover_image_location":'datamoverImageLocation',
        "description":'description',
        "distribution":'distribution',
        "init_container_image_location":'initContainerImageLocation',
        "label_attributes_vec":'labelAttributesVec',
        "name":'name',
        "namespace":'namespace',
        "pvc_name":'pvcName',
        "services_to_connector_ids_map":'servicesToConnectorIdsMap',
        "mtype":'type',
        "uuid":'uuid',
        "velero_aws_plugin_image_location":'veleroAwsPluginImageLocation',
        "velero_image_location":'veleroImageLocation',
        "velero_openshift_plugin_image_location":'veleroOpenshiftPluginImageLocation',
        "version":'version',
    }
    def __init__(self,
                 datamover_image_location=None,
                 description=None,
                 distribution=None,
                 init_container_image_location=None,
                 label_attributes_vec=None,
                 name=None,
                 namespace=None,
                 pvc_name=None,
                 services_to_connector_ids_map=None,
                 mtype=None,
                 uuid=None,
                 velero_aws_plugin_image_location=None,
                 velero_image_location=None,
                 velero_openshift_plugin_image_location=None,
                 version=None,
            ):

        """Constructor for the Entity class"""

        # Initialize members of the class
        self.datamover_image_location = datamover_image_location
        self.description = description
        self.distribution = distribution
        self.init_container_image_location = init_container_image_location
        self.label_attributes_vec = label_attributes_vec
        self.name = name
        self.namespace = namespace
        self.pvc_name = pvc_name
        self.services_to_connector_ids_map = services_to_connector_ids_map
        self.mtype = mtype
        self.uuid = uuid
        self.velero_aws_plugin_image_location = velero_aws_plugin_image_location
        self.velero_image_location = velero_image_location
        self.velero_openshift_plugin_image_location = velero_openshift_plugin_image_location
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
        datamover_image_location = dictionary.get('datamoverImageLocation')
        description = dictionary.get('description')
        distribution = dictionary.get('distribution')
        init_container_image_location = dictionary.get('initContainerImageLocation')
        label_attributes_vec = None
        if dictionary.get('labelAttributesVec') != None:
            label_attributes_vec = list()
            for structure in dictionary.get('labelAttributesVec'):
                label_attributes_vec.append(cohesity_management_sdk.models.label_attributes_info.LabelAttributesInfo.from_dictionary(structure))
        name = dictionary.get('name')
        namespace = dictionary.get('namespace')
        pvc_name = dictionary.get('pvcName')
        services_to_connector_ids_map = None
        if dictionary.get('servicesToConnectorIdsMap') != None:
            services_to_connector_ids_map = list()
            for structure in dictionary.get('servicesToConnectorIdsMap'):
                services_to_connector_ids_map.append(cohesity_management_sdk.models.entity_services_to_connector_ids_map_entry.Entity_ServicesToConnectorIdsMapEntry.from_dictionary(structure))
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')
        velero_aws_plugin_image_location = dictionary.get('veleroAwsPluginImageLocation')
        velero_image_location = dictionary.get('veleroImageLocation')
        velero_openshift_plugin_image_location = dictionary.get('veleroOpenshiftPluginImageLocation')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(
            datamover_image_location,
            description,
            distribution,
            init_container_image_location,
            label_attributes_vec,
            name,
            namespace,
            pvc_name,
            services_to_connector_ids_map,
            mtype,
            uuid,
            velero_aws_plugin_image_location,
            velero_image_location,
            velero_openshift_plugin_image_location,
            version
)