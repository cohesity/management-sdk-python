# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NfsConnection(object):

    """Implementation of the 'NfsConnection' model.

    TODO: type description here.


    Attributes:

        client_ip (string): Specifies the Client IP address of the connection.
        node_ip (string): Specifies a Node IP address where the connection
            request is received.
        server_ip (string): Specifies the Server IP address of the connection.
            This could be a VIP, VLAN IP, or node IP on the Cluster.
        view_id (long|int): Specifies the id of the view.
        view_name (string): Specifies the name of the view.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "client_ip":'clientIp',
        "node_ip":'nodeIp',
        "server_ip":'serverIp',
        "view_id":'viewId',
        "view_name":'viewName',
    }
    def __init__(self,
                 client_ip=None,
                 node_ip=None,
                 server_ip=None,
                 view_id=None,
                 view_name=None,
            ):

        """Constructor for the NfsConnection class"""

        # Initialize members of the class
        self.client_ip = client_ip
        self.node_ip = node_ip
        self.server_ip = server_ip
        self.view_id = view_id
        self.view_name = view_name

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
        client_ip = dictionary.get('clientIp')
        node_ip = dictionary.get('nodeIp')
        server_ip = dictionary.get('serverIp')
        view_id = dictionary.get('viewId')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(
            client_ip,
            node_ip,
            server_ip,
            view_id,
            view_name
)