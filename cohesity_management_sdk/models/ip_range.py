# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IpRange(object):

    """Implementation of the 'IpRange' model.

    IP Range for range of vip address addition.

    Attributes:
        end_ip (string): Optional End IP of the range If not specified, EndIp
            is same as StartIp
        start_ip (string): Start IP of the range

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_ip": 'endIp',
        "start_ip": 'startIp'
    }

    def __init__(self,
                 end_ip=None,
                 start_ip=None):
        """Constructor for the IpRange class"""

        # Initialize members of the class
        self.end_ip = end_ip
        self.start_ip = start_ip


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
        end_ip = dictionary.get('endIp', None)
        start_ip = dictionary.get('startIp', None)

        # Return an object of this model
        return cls(end_ip,
                   start_ip)


