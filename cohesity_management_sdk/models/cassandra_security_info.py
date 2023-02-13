# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CassandraSecurityInfo(object):

    """Implementation of the 'CassandraSecurityInfo' model.

    Specifies an Object containing information on Cassandra security.

    Attributes:
        cassandra_auth_required (bool): Is Cassandra authentication
            required ?
        cassandra_auth_type (CassandraAuthTypeEnum): Cassandra Authentication
            type.
            Enum: [PASSWORD KERBEROS LDAP]
            Specifies the Cassandra auth type.
            'PASSWORD'
            'KERBEROS'
            'LDAP'
        cassandra_authorizer (string): Cassandra Authenticator/Authorizer.
        client_encryption (bool): Is Client Encryption enabled for this
            cluster ?
        dse_authorization (bool): Is DSE Authorization enabled for this
            cluster ?
        server_encryption_req_client_auth (bool): Is 'Server encryption
            request client authentication' enabled for this cluster ?
        server_internode_encryption_type (string): '''Server internal node
            Encryption'' type for this cluster.'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cassandra_auth_required": 'cassandraAuthRequired',
        "cassandra_auth_type": 'cassandraAuthType',
        "cassandra_authorizer": 'cassandraAuthorizer',
        "client_encryption": 'clientEncryption',
        "dse_authorization":'dseAuthorization',
        "server_encryption_req_client_auth":'serverEncryptionReqClientAuth',
        "server_internode_encryption_type":'serverInternodeEncryptionType'
    }

    def __init__(self,
                 cassandra_auth_required=None,
                 cassandra_auth_type=None,
                 cassandra_authorizer=None,
                 client_encryption=None,
                 dse_authorization=None,
                 server_encryption_req_client_auth=None,
                 server_internode_encryption_type=None):
        """Constructor for the CassandraSecurityInfo class"""

        # Initialize members of the class
        self.cassandra_auth_required = cassandra_auth_required
        self.cassandra_auth_type = cassandra_auth_type
        self.cassandra_authorizer = cassandra_authorizer
        self.client_encryption = client_encryption
        self.dse_authorization = dse_authorization
        self.server_encryption_req_client_auth = server_encryption_req_client_auth
        self.server_internode_encryption_type = server_internode_encryption_type

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
        cassandra_auth_required = dictionary.get('cassandraAuthRequired')
        cassandra_auth_type = dictionary.get('cassandraAuthType')
        cassandra_authorizer = dictionary.get('cassandraAuthorizer')
        client_encryption = dictionary.get('clientEncryption')
        dse_authorization = dictionary.get('dseAuthorization')
        server_encryption_req_client_auth = dictionary.get('serverEncryptionReqClientAuth')
        server_internode_encryption_type = dictionary.get('serverInternodeEncryptionType')

        # Return an object of this model
        return cls(cassandra_auth_required,
                   cassandra_auth_type,
                   cassandra_authorizer,
                   client_encryption,
                   dse_authorization,
                   server_encryption_req_client_auth,
                   server_internode_encryption_type)


