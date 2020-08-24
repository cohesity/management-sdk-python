# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class HBaseConnectParams(object):

    """Implementation of the 'HBaseConnectParams' model.

    Specifies an Object containing information about a registered HBase
    source.

    Attributes:
        root_data_directory (string): Specifies the HBase data root directory.
        zookeeper_quorum (list of string): Specifies the HBase zookeeper
            quorum.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "root_data_directory":'rootDataDirectory',
        "zookeeper_quorum":'zookeeperQuorum'
    }

    def __init__(self,
                 root_data_directory=None,
                 zookeeper_quorum=None):
        """Constructor for the HBaseConnectParams class"""

        # Initialize members of the class
        self.root_data_directory = root_data_directory
        self.zookeeper_quorum = zookeeper_quorum


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
        root_data_directory = dictionary.get('rootDataDirectory')
        zookeeper_quorum = dictionary.get('zookeeperQuorum')

        # Return an object of this model
        return cls(root_data_directory,
                   zookeeper_quorum)


