# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class NtpSettingsConfig(object):

    """Implementation of the 'NtpSettingsConfig' model.

    TODO: type model description here.

    Attributes:
        ntp_servers_internal (bool): Flag to specify if the NTP servers are on
            internal network or not.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ntp_servers_internal":'ntpServersInternal'
    }

    def __init__(self,
                 ntp_servers_internal=None):
        """Constructor for the NtpSettingsConfig class"""

        # Initialize members of the class
        self.ntp_servers_internal = ntp_servers_internal


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
        ntp_servers_internal = dictionary.get('ntpServersInternal')

        # Return an object of this model
        return cls(ntp_servers_internal)


