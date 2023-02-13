# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CouchbaseBackupJobParams(object):

    """Implementation of the 'CouchbaseBackupJobParams' model.

    Contains any additional couchbase environment specific backup params at
    the
    job level.

    Attributes:

    """

    # Create a mapping from Model property names to API property names
    _names = {
    }

    def __init__(self):
        """Constructor for the CouchbaseBackupJobParams class"""

        # Initialize members of the class
        pass


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
        # TODO: add description here.

        # Return an object of this model
        return cls()


