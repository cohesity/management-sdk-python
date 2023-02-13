# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ExternallyTriggeredSbtParameters(object):

    """Implementation of the 'ExternallyTriggeredSbtParameters' model.

    Attributes:
        catalog_view (string): Specifies the catalog view associated with this job.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "catalog_view":'catalogView'
    }

    def __init__(self,
                 catalog_view=None):
        """Constructor for the ExternallyTriggeredSbtParameters class"""

        # Initialize members of the class
        self.catalog_view = catalog_view


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
        catalog_view = dictionary.get('catalogView')

        # Return an object of this model
        return cls(catalog_view)


