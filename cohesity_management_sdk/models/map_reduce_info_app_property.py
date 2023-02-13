# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MapReduceInfo_AppProperty(object):

    """Implementation of the 'MapReduceInfo_AppProperty' model.

    AppProperty message encapsulates properties that are same across all run
    instances of an app.

    Attributes:
        csv_header (string): csv_header should be tab separated
            column names.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "csv_header":'csvHeader'
    }

    def __init__(self,
                 csv_header=None):
        """Constructor for the MapReduceInfo_AppProperty class"""

        # Initialize members of the class
        self.csv_header = csv_header


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
        csv_header = dictionary.get('csvHeader')

        # Return an object of this model
        return cls(csv_header)


