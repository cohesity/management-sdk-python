# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class SyslogServer(object):

    """Implementation of the 'SyslogServer' model.

    Specifies the syslog servers configuration to upload Cluster audit logs
    and filer audit logs.

    Attributes:
        address (string): Specifies the IP address or hostname of the syslog
            server.
        is_cluster_auditing_enabled (bool): Specifies if Cluster audit logs
            should be sent to this syslog server. If 'true', Cluster audit
            logs are sent to the syslog server. (default) If 'false', Cluster
            audit logs are not sent to the syslog server. Either cluster audit
            logs or filer audit logs should be enabled.
        is_filer_auditing_enabled (bool): Specifies if filer audit logs should
            be sent to this syslog server. If 'true', filer audit logs are
            sent to the syslog server. (default) If 'false', filer audit logs
            are not sent to the syslog server. Either cluster audit logs or
            filer audit logs should be enabled.
        name (string): Specifies a unique name for the syslog server on the
            Cluster.
        port (int): Specifies the port where the syslog server listens.
        protocol (ProtocolSyslogServerEnum): Specifies the protocol used to
            send the logs. Specifies the protocol used to communicate to a
            server. e.g., kUDP, kTCP.  'kUDP' indicates UDP protocol. 'kTCP'
            indicates TCP protocol.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address":'address',
        "port":'port',
        "protocol":'protocol',
        "is_cluster_auditing_enabled":'isClusterAuditingEnabled',
        "is_filer_auditing_enabled":'isFilerAuditingEnabled',
        "name":'name'
    }

    def __init__(self,
                 address=None,
                 port=None,
                 protocol=None,
                 is_cluster_auditing_enabled=None,
                 is_filer_auditing_enabled=None,
                 name=None):
        """Constructor for the SyslogServer class"""

        # Initialize members of the class
        self.address = address
        self.is_cluster_auditing_enabled = is_cluster_auditing_enabled
        self.is_filer_auditing_enabled = is_filer_auditing_enabled
        self.name = name
        self.port = port
        self.protocol = protocol


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
        address = dictionary.get('address')
        port = dictionary.get('port')
        protocol = dictionary.get('protocol')
        is_cluster_auditing_enabled = dictionary.get('isClusterAuditingEnabled')
        is_filer_auditing_enabled = dictionary.get('isFilerAuditingEnabled')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(address,
                   port,
                   protocol,
                   is_cluster_auditing_enabled,
                   is_filer_auditing_enabled,
                   name)


