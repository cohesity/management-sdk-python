# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ObjectReference(object):

    """Implementation of the 'ObjectReference' model.

    ObjectReference contains enough information to let you inspect or modify the
    referred object.

    Attributes:
        api_group (string): API group make it easier to extend the Kubernetes
            API. The API group is specified in a REST path and in the
            apiVersion field.
        api_version (string): APIVersion defines the versioned schema of this
            representation of an object. Servers should convert recognized
            schemas to the latest internal value, and may reject unrecognized
            values.
        kind (string): Kind is a string value representing the REST resource
            this object represents. Servers may infer this from the endpoint
            the client submits requests to.
        namespace (string): Namespace of the referent.
        name (string): Name of the referent.
        resource_version (string): Specific resourceVersion to which this
            reference is made, if any.
        uid (string): UID of the referent.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "api_group": 'apiGroup',
        "api_version": 'apiVersion',
        "kind": 'kind',
        "namespace":'namespace',
        "name":'name',
        "resource_version":'resourceVersion',
        "uid":'uid'
    }

    def __init__(self,
                 api_group=None,
                 api_version=None,
                 kind=None,
                 namespace=None,
                 name=None,
                 resource_version=None,
                 uid=None
                 ):
        """Constructor for the ObjectReference class"""

        # Initialize members of the class
        self.api_group = api_group
        self.api_version = api_version
        self.kind = kind
        self.namespace = namespace
        self.name = name
        self.resource_version = resource_version
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
        api_group = dictionary.get('apiGroup')
        api_version = dictionary.get('apiVersion')
        kind = dictionary.get('kind')
        namespace = dictionary.get('namespace')
        name = dictionary.get('name')
        resource_version = dictionary.get('resourceVersion')
        uid = dictionary.get('uid')

        # Return an object of this model
        return cls(api_group,
                   api_version,
                   kind,
                   namespace,
                   name,
                   resource_version,
                   uid)


