# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class IsilonCluster(object):

    """Implementation of the 'IsilonCluster' model.

    Specifies information about an Isilon Cluster.

    Attributes:
        api_version (int): Specifies the API version of an Isilon Cluster.
        description (string): Specifies the description of an Isilon Cluster.
        guid (string): Specifies a globally unique id of an Isilon Cluster.
        version (string): Specifies the version of an Isilon Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "api_version":'apiVersion',
        "description":'description',
        "guid":'guid',
        "version":'version'
    }

    def __init__(self,
                 api_version=None,
                 description=None,
                 guid=None,
                 version=None):
        """Constructor for the IsilonCluster class"""

        # Initialize members of the class
        self.api_version = api_version
        self.description = description
        self.guid = guid
        self.version = version


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
        api_version = dictionary.get('apiVersion')
        description = dictionary.get('description')
        guid = dictionary.get('guid')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(api_version,
                   description,
                   guid,
                   version)


