# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class OracleDatabaseNode(object):

    """Implementation of the 'OracleDatabaseNode' model.

    Oracle Database Node.
    Specifies database node required for the backup and restore.

    Attributes:
        channel_count (int): Specifies the number of channels user wants for
            the backup/recovery of this node.
        node (string): Specifies the ip of the database node.
        port (long|int): Specifies the port on which user wants to run the
            backup/recovery.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "channel_count":'channelCount',
        "node":'node',
        "port":'port'
    }

    def __init__(self,
                 channel_count=None,
                 node=None,
                 port=None):
        """Constructor for the OracleDatabaseNode class"""

        # Initialize members of the class
        self.channel_count = channel_count
        self.node = node
        self.port = port


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
        channel_count = dictionary.get('channelCount')
        node = dictionary.get('node')
        port = dictionary.get('port')

        # Return an object of this model
        return cls(channel_count,
                   node,
                   port)


