# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SchedulingPolicyProto_YearlySchedule(object):

    """Implementation of the 'SchedulingPolicyProto_YearlySchedule' model.

    TODO: type description here.


    Attributes:

        day_of_the_year (int): Count of the day on which to perform the backup
            (look above for a more detailed description).
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "day_of_the_year":'dayOfTheYear',
    }
    def __init__(self,
                 day_of_the_year=None,
            ):

        """Constructor for the SchedulingPolicyProto_YearlySchedule class"""

        # Initialize members of the class
        self.day_of_the_year = day_of_the_year

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
        day_of_the_year = dictionary.get('dayOfTheYear')

        # Return an object of this model
        return cls(
            day_of_the_year
)