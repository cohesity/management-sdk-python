# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.object_meta
import cohesity_management_sdk.models.pvc_info_pvc_spec

class PVCInfo(object):

    """Implementation of the 'PVCInfo' model.

    Message that encapsulates information about a PVC. We only extract relevant
    information from a larger response sent by Kubernetes.

    Attributes:
        api_version (string): APIVersion defines the versioned schema of this
            representation of anobject. Servers should convert recognized
            schemas to the latest internal value, and may reject unrecognized
            values.
        kind (string): Kind is a string value representing the REST resource
            this object represents. Servers may infer this from the endpoint
            the client submits requests to.
        metadata (ObjectMeta): Metadata if any.
        spec (PVCInfo_PVCSpec): Specifies the IPMI Username.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "api_version":'apiVersion',
        "kind":'kind',
        "metadata":'metadata',
        "spec":'spec'
    }

    def __init__(self,
                 api_version=None,
                 kind=None,
                 metadata=None,
                 spec=None):
        """Constructor for the PVCInfo class"""

        # Initialize members of the class
        self.api_version = api_version
        self.kind = kind
        self.metadata = metadata
        self.spec = spec


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
        api_version = dictionary.get('apiVersion')
        kind = dictionary.get('kind')
        metadata = cohesity_management_sdk.models.object_meta.ObjectMeta.from_dictionary(dictionary.get('metadata')) if dictionary.get('metadata') else None
        spec = cohesity_management_sdk.models.pvc_info_pvc_spec.PVCInfo_PVCSpec.from_dictionary(dictionary.get('spec')) if dictionary.get('spec') else None

        # Return an object of this model
        return cls(api_version,
                   kind,
                   metadata,
                   spec)


