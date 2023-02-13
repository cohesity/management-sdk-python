# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.lifecycle_rule

class LifecycleConfigProto(object):

    """Implementation of the 'LifecycleConfigProto' model.

    Protobuf that describes the lifecycle configuration that is used to manage
    the lifecycle of objects in a bucket.

    Attributes:
        rules (list of LifecycleRule): Specifies lifecycle configuration rules
            for an Amazon S3 bucket. A maximum of 1000 rules can be specified.
        version_id (long|int): Specifies the uniq monotonically increasing
            version for lifecycle configuration.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rules": 'rules',
        "version_id": 'versionId'
    }

    def __init__(self,
                 rules=None,
                 version_id=None):
        """Constructor for the LifecycleConfigProto class"""

        # Initialize members of the class
        self.rules = rules
        self.version_id = version_id


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
        rules = None
        if dictionary.get('rules', None) != None:
            rules= list()
            for structure in dictionary.get('rules'):
                rules.append(cohesity_management_sdk.models.lifecycle_rule.LifecycleRule.from_dictionary(structure))
        version_id = dictionary.get('versionId', None)

        # Return an object of this model
        return cls(rules,
                   version_id)


