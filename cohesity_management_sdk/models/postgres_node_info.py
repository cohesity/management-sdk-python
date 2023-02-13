# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PostgresNodeInfo(object):

    """Implementation of the 'PostgresNodeInfo' model.

    Specifies the Node Id, IP and port information to access the postgres
    database.

    Attributes:
        default_password (string): Specifies the default password to access
            the postgres database.
        default_username (string): Specifies the default username to access
            the postgres database.
        node_id (long|int): Specifies the id of the node where postgres
            database is running.
        node_ip (string): Specifies the ip of the node where postgres database
            is running.
        port (int): Specifies the information where postgres database is
            running.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default_password":'defaultPassword',
        "default_username":'defaultUsername',
        "node_id":'nodeId',
        "node_ip":'nodeIp',
        "port":'port'
    }

    def __init__(self,
                 default_password=None,
                 default_username=None,
                 node_id=None,
                 node_ip=None,
                 port=None):
        """Constructor for the PostgresNodeInfo class"""

        # Initialize members of the class
        self.default_password = default_password
        self.default_username = default_username
        self.node_id = node_id
        self.node_ip = node_ip
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
        default_password = dictionary.get('defaultPassword')
        default_username = dictionary.get('defaultUsername')
        node_id = dictionary.get('nodeId')
        node_ip = dictionary.get('nodeIp')
        port = dictionary.get('port')

        # Return an object of this model
        return cls(default_password,
                   default_username,
                   node_id,
                   node_ip,
                   port)


