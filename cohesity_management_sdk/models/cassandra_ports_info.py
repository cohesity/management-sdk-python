# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CassandraPortsInfo(object):

    """Implementation of the 'CassandraPortsInfo' model.

    Specifies an Object containing information on various Cassandra ports.

    Attributes:
        jmx_port (int): Specifies the Cassandra JMX port.
        native_transport_port (int): Specifies the port for the CQL native
            transport.
        rpc_port (int): Specifies the Remote Procedure Call (RPC) port for
            general mechanism for client-server applications.
        ssl_storage_port (string):  Specifies the SSL port for encrypted
            communication.
        storage_port (int): Specifies the attributes and the latest
            statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "jmx_port":'jmxPort',
        "native_transport_port":'nativeTransportPort',
        "rpc_port":'rpcPort',
        "ssl_storage_port":'sslStoragePort',
        "storage_port":'storagePort'
    }

    def __init__(self,
                 jmx_port=None,
                 native_transport_port=None,
                 rpc_port=None,
                 ssl_storage_port=None,
                 storage_port=None):
        """Constructor for the CassandraPortsInfo class"""

        # Initialize members of the class
        self.jmx_port = jmx_port
        self.native_transport_port = native_transport_port
        self.rpc_port = rpc_port
        self.ssl_storage_port = ssl_storage_port
        self.storage_port = storage_port


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
        jmx_port = dictionary.get('jmxPort')
        native_transport_port = dictionary.get('nativeTransportPort')
        rpc_port = dictionary.get('rpcPort')
        ssl_storage_port = dictionary.get('sslStoragePort')
        storage_port = dictionary.get('storagePort')

        # Return an object of this model
        return cls(jmx_port,
                   native_transport_port,
                   rpc_port,
                   ssl_storage_port,
                   storage_port)

