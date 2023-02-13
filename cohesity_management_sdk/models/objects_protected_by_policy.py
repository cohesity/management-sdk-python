# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.objects_by_env

class ObjectsProtectedByPolicy(object):

    """Implementation of the 'ObjectsProtectedByPolicy' model.

    Objects (e.g. VMs) protected by Policy.

    Attributes:
        objects_protected (list of ObjectsByEnv): Protected Objects.
        policy_id (string): Id of the policy.
        policy_name (string): Name of the policy.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "objects_protected":'objectsProtected',
        "policy_id":'policyId',
        "policy_name":'policyName'
    }

    def __init__(self,
                 objects_protected=None,
                 policy_id=None,
                 policy_name=None):
        """Constructor for the ObjectsProtectedByPolicy class"""

        # Initialize members of the class
        self.objects_protected = objects_protected
        self.policy_id = policy_id
        self.policy_name = policy_name


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
        objects_protected = None
        if dictionary.get('objectsProtected') != None:
            objects_protected = list()
            for structure in dictionary.get('objectsProtected'):
                objects_protected.append(cohesity_management_sdk.models.objects_by_env.ObjectsByEnv.from_dictionary(structure))
        policy_id = dictionary.get('policyId')
        policy_name = dictionary.get('policyName')

        # Return an object of this model
        return cls(objects_protected,
                   policy_id,
                   policy_name)


