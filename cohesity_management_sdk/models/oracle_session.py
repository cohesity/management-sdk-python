# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class OracleSession(object):

    """Implementation of the 'OracleSession' model.

    Specifies information about session configuration for an Oracle host.

    Attributes:
        location (string): Location is the path where Oracle is installed.
        system_identifier (string): SystemIdentifier is the unique Oracle
            System Identifier for the DB instance.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "location":'location',
        "system_identifier":'systemIdentifier'
    }

    def __init__(self,
                 location=None,
                 system_identifier=None):
        """Constructor for the OracleSession class"""

        # Initialize members of the class
        self.location = location
        self.system_identifier = system_identifier


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
        location = dictionary.get('location')
        system_identifier = dictionary.get('systemIdentifier')

        # Return an object of this model
        return cls(location,
                   system_identifier)


