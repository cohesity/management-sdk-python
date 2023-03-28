# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.object_meta_annotations_entry
import cohesity_management_sdk.models.object_meta_labels_entry


class ObjectMeta(object):

    """Implementation of the 'ObjectMeta' model.

    TODO: type description here.


    Attributes:

        annotations (list of ObjectMeta_AnnotationsEntry): Annotations added to
            the object.
        labels (list of ObjectMeta_LabelsEntry): A set of key-value pairs,
            capturing the labels of a k8s object.
        name (string): Name must be unique within a namespace. Is required when
            creating resources, although some resources may allow a client to
            request the generation of an appropriate name automatically. Name
            is primarily intended for creation idempotence and configuration
            definition. Cannot be updated.
        namespace (string): Namespace defines the space within each name must
            be unique. An empty namespace is equivalent to the "default"
            namespace, but "default" is the canonical representation. Not all
            objects are required to be scoped to a namespace - the value of
            this field for those objects will be empty.
        uid (string): UUID of the object queried.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "annotations":'annotations',
        "labels":'labels',
        "name":'name',
        "namespace":'namespace',
        "uid":'uid',
    }
    def __init__(self,
                 annotations=None,
                 labels=None,
                 name=None,
                 namespace=None,
                 uid=None,
            ):

        """Constructor for the ObjectMeta class"""

        # Initialize members of the class
        self.annotations = annotations
        self.labels = labels
        self.name = name
        self.namespace = namespace
        self.uid = uid

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
        annotations = None
        if dictionary.get('annotations') != None:
            annotations = list()
            for structure in dictionary.get('annotations'):
                annotations.append(cohesity_management_sdk.models.object_meta_annotations_entry.ObjectMeta_AnnotationsEntry.from_dictionary(structure))
        labels = None
        if dictionary.get('labels') != None:
            labels = list()
            for structure in dictionary.get('labels'):
                labels.append(cohesity_management_sdk.models.object_meta_labels_entry.ObjectMeta_LabelsEntry.from_dictionary(structure))
        name = dictionary.get('name')
        namespace = dictionary.get('namespace')
        uid = dictionary.get('uid')

        # Return an object of this model
        return cls(
            annotations,
            labels,
            name,
            namespace,
            uid
)