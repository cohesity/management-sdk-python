# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.smb_active_open

class SmbActiveSession(object):

    """Implementation of the 'SmbActiveSession' model.

    Specifies an active session and its opens.

    Attributes:
        active_opens (list of SmbActiveOpen): Specifies the list of active
            opens of the file in this session.
        client_ip (string): Specifies the IP address from which the file is
            still open.
        domain (string): Specifies the domain of the user.
        server_ip (string): Specifies the IP address of the server where the
            file exists.
        session_id (long|int): Specifies the id of the session.
        username (string): Specifies the username who keeps the file open.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "active_opens":'activeOpens',
        "client_ip":'clientIp',
        "domain":'domain',
        "server_ip":'serverIp',
        "session_id":'sessionId',
        "username":'username'
    }

    def __init__(self,
                 active_opens=None,
                 client_ip=None,
                 domain=None,
                 server_ip=None,
                 session_id=None,
                 username=None):
        """Constructor for the SmbActiveSession class"""

        # Initialize members of the class
        self.active_opens = active_opens
        self.client_ip = client_ip
        self.domain = domain
        self.server_ip = server_ip
        self.session_id = session_id
        self.username = username


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
        active_opens = None
        if dictionary.get('activeOpens') != None:
            active_opens = list()
            for structure in dictionary.get('activeOpens'):
                active_opens.append(cohesity_management_sdk.models.smb_active_open.SmbActiveOpen.from_dictionary(structure))
        client_ip = dictionary.get('clientIp')
        domain = dictionary.get('domain')
        server_ip = dictionary.get('serverIp')
        session_id = dictionary.get('sessionId')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(active_opens,
                   client_ip,
                   domain,
                   server_ip,
                   session_id,
                   username)


