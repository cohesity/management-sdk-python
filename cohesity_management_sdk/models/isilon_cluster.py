# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IsilonCluster(object):

    """Implementation of the 'IsilonCluster' model.

    Specifies information about an Isilon Cluster.

    Attributes:
        api_version_str (string): Specifies the API version of an Isilon
            Cluster as string.
        description (string): Specifies the description of an Isilon Cluster.
        guid (string): Specifies a globally unique id of an Isilon Cluster.
        version (string): Specifies the version of an Isilon Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "api_version_str":'apiVersionStr',
        "description":'description',
        "guid":'guid',
        "version":'version'
    }

    def __init__(self,
                 api_version_str=None,
                 description=None,
                 guid=None,
                 version=None):
        """Constructor for the IsilonCluster class"""

        # Initialize members of the class
        self.api_version_str = api_version_str
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
        api_version_str = dictionary.get('apiVersionStr')
        description = dictionary.get('description')
        guid = dictionary.get('guid')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(api_version_str,
                   description,
                   guid,
                   version)


