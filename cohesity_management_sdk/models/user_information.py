# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.key_value_pair
import cohesity_management_sdk.models.cluster_config_proto_sid

class UserInformation(object):

    """Implementation of the 'UserInformation' model.

    A message to encapsulate information about the user who made the request.
    Request should be filtered by these fields if specified so that only the
    objects that the user is permissioned for are returned. If both sid_vec &
    tenant_id are specified then an intersection of respective results should
    be returned.

    Attributes:
        include_subtenant_objects (bool): Whether objects owned by subtenants
            should be returned. This would require a prefix search with the
            passed tenant_id. All tenants are considered sub-tenants of the
            admin. For GET requests, if tenant id is empty(admin user is
            querying) and if this flag is false, we will only return untagged
            objects. If it is true, we will return everything.
        pulse_attribute_vec (list of KeyValuePair): Specifies the KeyValuePair
            that client (eg. Iris) wants to persist along with the
            corresponding (soon-to-be-created) Pulse task for the current
            action. Eg. pulse_attribute_vec can drive user notifications by
            associating a Pulse Task with user SID and later Pulse can be
            searched by client specified Sid to get all finished tasks for the
            logged in user.
        sid_vec (list of ClusterConfigProtoSID): If specified, only the
            objects associated with these SIDs should be returned.
        tenant_id_vec (list of string): If specified, only the objects
            associated with this tenant should be returned. A given tenant ID
            is always a prefix of the ids of its subtenants. Eg. if tenant_id
            of cluster admin is empty string then it will be a prefix match
            for all the tenants on the cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "include_subtenant_objects":'includeSubtenantObjects',
        "pulse_attribute_vec":'pulseAttributeVec',
        "sid_vec":'sidVec',
        "tenant_id_vec":'tenantIdVec'
    }

    def __init__(self,
                 include_subtenant_objects=None,
                 pulse_attribute_vec=None,
                 sid_vec=None,
                 tenant_id_vec=None):
        """Constructor for the UserInformation class"""

        # Initialize members of the class
        self.include_subtenant_objects = include_subtenant_objects
        self.pulse_attribute_vec = pulse_attribute_vec
        self.sid_vec = sid_vec
        self.tenant_id_vec = tenant_id_vec


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
        include_subtenant_objects = dictionary.get('includeSubtenantObjects')
        pulse_attribute_vec = None
        if dictionary.get('pulseAttributeVec') != None:
            pulse_attribute_vec = list()
            for structure in dictionary.get('pulseAttributeVec'):
                pulse_attribute_vec.append(cohesity_management_sdk.models.key_value_pair.KeyValuePair.from_dictionary(structure))
        sid_vec = None
        if dictionary.get('sidVec') != None:
            sid_vec = list()
            for structure in dictionary.get('sidVec'):
                sid_vec.append(cohesity_management_sdk.models.cluster_config_proto_sid.ClusterConfigProtoSID.from_dictionary(structure))
        tenant_id_vec = dictionary.get('tenantIdVec')

        # Return an object of this model
        return cls(include_subtenant_objects,
                   pulse_attribute_vec,
                   sid_vec,
                   tenant_id_vec)


