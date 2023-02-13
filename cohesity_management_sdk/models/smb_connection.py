# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SmbConnection(object):

    """Implementation of the 'SmbConnection' model.

    TODO: type model description here.

    Attributes:
        client_ip (string): Specifies the Client IP address of the
            connection.
        domain_name (string): Domain name of the corresponding user.
        node_ip (string): Specifies a Node IP address where the connection
            request is received.
        path (string): Mount path.
        server_ip (string): Specifies the Server IP address of the connection.
            This could be a VIP, VLAN IP, or node IP on the Cluster.
        session_id (long|int): Session id.
        sids (list of string): List of SIDs in the SMB session token.
        user_name (string): User name used to login for this session.
        view_id (long|int): Specifies the id of the view.
        view_name (string): Specifies the name of the view.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_ip":'clientIp',
        "domain_name":'domainName',
        "node_ip":'nodeIp',
        "path":'path',
        "server_ip":'serverIp',
        "session_id":'sessionId',
        "sids":'sids',
        "user_name":'userName',
        "view_id":'viewId',
        "view_name":'viewName'
    }

    def __init__(self,
                 client_ip=None,
                 domain_name=None,
                 node_ip=None,
                 path=None,
                 server_ip=None,
                 session_id=None,
                 sids=None,
                 user_name=None,
                 view_id=None,
                 view_name=None):
        """Constructor for the SmbConnection class"""

        # Initialize members of the class
        self.client_ip = client_ip
        self.domain_name = domain_name
        self.node_ip = node_ip
        self.path = path
        self.server_ip = server_ip
        self.session_id = session_id
        self.sids = sids
        self.user_name = user_name
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
        domain_name = dictionary.get('domainName')
        node_ip = dictionary.get('nodeIp')
        path = dictionary.get('path')
        server_ip = dictionary.get('serverIp')
        session_id = dictionary.get('sessionId')
        sids = dictionary.get('sids')
        user_name = dictionary.get('userName')
        view_id = dictionary.get('viewId')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(client_ip,
                   domain_name,
                   node_ip,
                   path,
                   server_ip,
                   session_id,
                   sids,
                   user_name,
                   view_id,
                   view_name)


