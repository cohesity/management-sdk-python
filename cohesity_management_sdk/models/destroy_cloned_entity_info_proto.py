# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.destroy_cloned_entity_info_proto_cloned_entity
import cohesity_management_sdk.models.error_proto

class DestroyClonedEntityInfoProto(object):

    """Implementation of the 'DestroyClonedEntityInfoProto' model.

    Each available extension is listed below along with the location of the
    proto file (relative to magneto/connectors) where it is defined.
    DestroyClonedEntityInfoProto.ClonedEntity extension    Location
    Extension
    ===========================================================================
    ==
    azure::ClonedEntityInfo::azure_cloned_entity_info   azure/azure.proto
    100
    aws::ClonedEntityInfo::aws_cloned_entity_info       aws/aws.proto
    101
    ===========================================================================
    ==

    Attributes:
        cloned_entity (DestroyClonedEntityInfoProtoClonedEntity): TODO: type
            description here.
        cloned_entity_status (int): TODO: type description here.
        destroy_cloned_entity_state (int): The state of the destroy/teardown
            of a cloned entity (i.e, VM).  The following two fields are set by
            the slave in order for the master to find status of the destroy
            operation.
        error (ErrorProto): TODO: type description here.
        full_view_name (string): The full external view name where cloned
            objects are placed.
        mtype (int): The type of environment this destroy cloned entity info
            pertains to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cloned_entity":'clonedEntity',
        "cloned_entity_status":'clonedEntityStatus',
        "destroy_cloned_entity_state":'destroyClonedEntityState',
        "error":'error',
        "full_view_name":'fullViewName',
        "mtype":'type'
    }

    def __init__(self,
                 cloned_entity=None,
                 cloned_entity_status=None,
                 destroy_cloned_entity_state=None,
                 error=None,
                 full_view_name=None,
                 mtype=None):
        """Constructor for the DestroyClonedEntityInfoProto class"""

        # Initialize members of the class
        self.cloned_entity = cloned_entity
        self.cloned_entity_status = cloned_entity_status
        self.destroy_cloned_entity_state = destroy_cloned_entity_state
        self.error = error
        self.full_view_name = full_view_name
        self.mtype = mtype


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
        cloned_entity = cohesity_management_sdk.models.destroy_cloned_entity_info_proto_cloned_entity.DestroyClonedEntityInfoProtoClonedEntity.from_dictionary(dictionary.get('clonedEntity')) if dictionary.get('clonedEntity') else None
        cloned_entity_status = dictionary.get('clonedEntityStatus')
        destroy_cloned_entity_state = dictionary.get('destroyClonedEntityState')
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        full_view_name = dictionary.get('fullViewName')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(cloned_entity,
                   cloned_entity_status,
                   destroy_cloned_entity_state,
                   error,
                   full_view_name,
                   mtype)


