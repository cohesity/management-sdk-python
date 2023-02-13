# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ShowSystemLedInfoResult(object):

    """Implementation of the 'ShowSystemLedInfoResult' model.

    Specifies the result returned after a successful request to show system
    LED details.

    Attributes:
        led_info (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "led_info":'ledInfo'
    }

    def __init__(self,
                 led_info=None):
        """Constructor for the ShowSystemLedInfoResult class"""

        # Initialize members of the class
        self.led_info = led_info


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
        led_info = dictionary.get('ledInfo')

        # Return an object of this model
        return cls(led_info)


