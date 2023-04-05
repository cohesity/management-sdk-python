# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pre_check_validation


class NodeDeleteResult(object):

    """Implementation of the 'NodeDeleteResult' model.

    NodeDeleteResult specifies response for mark node for removal


    Attributes:

        id (long|int): Id of the node to be marked for deletion.
        mark_node_for_removal (bool): MarkNodeForRemoval indicates if the node
            is marked for removal
        timestamp_secs (long|int): TimestampSecs specifies the last run time of
            the pre-checks execution in Unix epoch timestamp in seconds
        validation_checks (list of PreCheckValidation): ValidationChecks
            specifies list of pre-check validations
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "mark_node_for_removal":'markNodeForRemoval',
        "timestamp_secs":'timestampSecs',
        "validation_checks":'validationChecks',
    }
    def __init__(self,
                 id=None,
                 mark_node_for_removal=None,
                 timestamp_secs=None,
                 validation_checks=None,
            ):

        """Constructor for the NodeDeleteResult class"""

        # Initialize members of the class
        self.id = id
        self.mark_node_for_removal = mark_node_for_removal
        self.timestamp_secs = timestamp_secs
        self.validation_checks = validation_checks

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
        id = dictionary.get('id')
        mark_node_for_removal = dictionary.get('markNodeForRemoval')
        timestamp_secs = dictionary.get('timestampSecs')
        validation_checks = None
        if dictionary.get('validationChecks') != None:
            validation_checks = list()
            for structure in dictionary.get('validationChecks'):
                validation_checks.append(cohesity_management_sdk.models.pre_check_validation.PreCheckValidation.from_dictionary(structure))

        # Return an object of this model
        return cls(
            id,
            mark_node_for_removal,
            timestamp_secs,
            validation_checks
)