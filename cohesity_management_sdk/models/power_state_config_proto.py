# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PowerStateConfigProto(object):

    """Implementation of the 'PowerStateConfigProto' model.

    TODO: type model description here.

    Attributes:
        power_on (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "power_on":'powerOn'
    }

    def __init__(self,
                 power_on=None):
        """Constructor for the PowerStateConfigProto class"""

        # Initialize members of the class
        self.power_on = power_on


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
        power_on = dictionary.get('powerOn')

        # Return an object of this model
        return cls(power_on)


