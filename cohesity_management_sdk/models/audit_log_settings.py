# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AuditLogSettings(object):

    """Implementation of the 'AuditLogSettings' model.

    AuditLogSettings specifies struct with audt log configuration. Make these
    settings in such a way that zero values are cluster default when bb is not
    present.

    Attributes:
        read_logging (bool): ReadLogging specifies whether read logs needs to
            be captured.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "read_logging":'readLogging'
    }

    def __init__(self,
                 read_logging=None):
        """Constructor for the AuditLogSettings class"""

        # Initialize members of the class
        self.read_logging = read_logging


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
        read_logging = dictionary.get('readLogging')

        # Return an object of this model
        return cls(read_logging)


