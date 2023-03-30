# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SchedulingPolicyProtoRPOSchedule(object):

    """Implementation of the 'SchedulingPolicyProto_RPOSchedule' model.

    TODO: type model description here.

    Attributes:
        rpo_interval_mins (long|int): If this field is set, then at any point,
            a recovery point should be available not older than the given
            interval mins.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rpo_interval_mins":'rpoIntervalMins'
    }

    def __init__(self,
                 rpo_interval_mins=None):
        """Constructor for the SchedulingPolicyProtoRPOSchedule class"""

        # Initialize members of the class
        self.rpo_interval_mins = rpo_interval_mins


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
        rpo_interval_mins = dictionary.get('rpoIntervalMins')

        # Return an object of this model
        return cls(rpo_interval_mins)


