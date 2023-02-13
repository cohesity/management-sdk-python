# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.oracle_session

class OracleHost(object):

    """Implementation of the 'OracleHost' model.

    Specifies information about an Oracle Host.

    Attributes:
        cpu_count (int): Specifies the count of CPU available on the host.
        ip_addresses (list of string): Specifies the IP address of the host.
        ports (list of long|int): Specifies ports available for this host.
        sessions (list of OracleSession): Specifies multiple session
            configurations available for this host.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cpu_count":'cpuCount',
        "ip_addresses":'ipAddresses',
        "ports":'ports',
        "sessions":'sessions'
    }

    def __init__(self,
                 cpu_count=None,
                 ip_addresses=None,
                 ports=None,
                 sessions=None):
        """Constructor for the OracleHost class"""

        # Initialize members of the class
        self.cpu_count = cpu_count
        self.ip_addresses = ip_addresses
        self.ports = ports
        self.sessions = sessions


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
        cpu_count = dictionary.get('cpuCount')
        ip_addresses = dictionary.get('ipAddresses')
        ports = dictionary.get('ports')
        sessions = None
        if dictionary.get('sessions') != None:
            sessions = list()
            for structure in dictionary.get('sessions'):
                sessions.append(cohesity_management_sdk.models.oracle_session.OracleSession.from_dictionary(structure))

        # Return an object of this model
        return cls(cpu_count,
                   ip_addresses,
                   ports,
                   sessions)


