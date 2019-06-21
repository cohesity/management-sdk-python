# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class IsilonCluster(object):

    """Implementation of the 'IsilonCluster' model.

    Specifies information about an Isilon Cluster.

    Attributes:
        description (string): Specifies the description of an Isilon Cluster.
        guid (string): Specifies a globally unique id of an Isilon Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "guid":'guid'
    }

    def __init__(self,
                 description=None,
                 guid=None):
        """Constructor for the IsilonCluster class"""

        # Initialize members of the class
        self.description = description
        self.guid = guid


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
        description = dictionary.get('description')
        guid = dictionary.get('guid')

        # Return an object of this model
        return cls(description,
                   guid)


