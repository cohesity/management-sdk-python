# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VcloudDirectorInfo(object):

    """Implementation of the 'VCloudDirectorInfo' model.

    TODO: type model description here.

    Attributes:
        endpoint (string): vCenter endpoint.
        name (string): vCenter name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "endpoint":'endpoint',
        "name":'name'
    }

    def __init__(self,
                 endpoint=None,
                 name=None):
        """Constructor for the VcloudDirectorInfo class"""

        # Initialize members of the class
        self.endpoint = endpoint
        self.name = name


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
        endpoint = dictionary.get('endpoint')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(endpoint,
                   name)


