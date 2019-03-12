# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class RPOSchedule(object):

    """Implementation of the 'RPO Schedule.' model.

    Specifies an RPO Schedule.

    Attributes:
        rpo_inteval_minutes (long|int): If this field is set, then at any
            point, a recovery point should be available not older than the
            given interval minutes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rpo_inteval_minutes":'rpoIntevalMinutes'
    }

    def __init__(self,
                 rpo_inteval_minutes=None):
        """Constructor for the RPOSchedule class"""

        # Initialize members of the class
        self.rpo_inteval_minutes = rpo_inteval_minutes


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
        rpo_inteval_minutes = dictionary.get('rpoIntevalMinutes')

        # Return an object of this model
        return cls(rpo_inteval_minutes)


