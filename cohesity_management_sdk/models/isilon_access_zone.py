# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class IsilonAccessZone(object):

    """Implementation of the 'IsilonAccessZone' model.

    Specifies information about access zone in an Isilon Cluster.

    Attributes:
        id (long|int): Specifies the id of the access zone.
        name (string): Specifies the name of the access zone.
        path (string): Specifies the path of the access zone in ifs. This
            should include the leading "/ifs/".

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "path":'path'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 path=None):
        """Constructor for the IsilonAccessZone class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.path = path


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
        id = dictionary.get('id')
        name = dictionary.get('name')
        path = dictionary.get('path')

        # Return an object of this model
        return cls(id,
                   name,
                   path)


