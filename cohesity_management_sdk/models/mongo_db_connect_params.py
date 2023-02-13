# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MongoDBConnectParams(object):

    """Implementation of the 'MongoDBConnectParams' model.

    Specifies an Object containing information about a registered mongodb
    source.

    Attributes:
        auth_type (AuthTypeMongoDBConnectParamsEnum): Specifies whether
            authentication is configured on this MongoDB cluster.
            Specifies the type of an MongoDB source entity.
            'SCRAM'
            'LDAP'
            'NONE'
            'KERBEROS'
        authenticating_database_name (string): Specifies the Authenticating
            Database for this MongoDB cluster.
        requires_ssl (bool): Specifies whether connection is allowed through
            SSL only in this cluster.
        secondary_node_tag (string): MongoDB Secondary node tag. Required only
            if 'useSecondaryForBackup' is true. The system will use this to
            identify the secondary nodes for reading backup data.
        seeds (list of string): Specifies the seeds of this MongoDB Cluster.
        use_secondary_for_backup (bool): Set this to true if you want the
            system to peform backups from secondary nodes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auth_type":'authType',
        "authenticating_database_name":'authenticatingDatabaseName',
        "requires_ssl":'requiresSsl',
        "secondary_node_tag":'secondaryNodeTag',
        "seeds":'seeds',
        "use_secondary_for_backup":'useSecondaryForBackup'
    }

    def __init__(self,
                 auth_type=None,
                 authenticating_database_name=None,
                 requires_ssl=None,
                 secondary_node_tag=None,
                 seeds=None,
                 use_secondary_for_backup=None):
        """Constructor for the MongoDBConnectParams class"""

        # Initialize members of the class
        self.auth_type = auth_type
        self.authenticating_database_name = authenticating_database_name
        self.requires_ssl = requires_ssl
        self.secondary_node_tag = secondary_node_tag
        self.seeds = seeds
        self.use_secondary_for_backup = use_secondary_for_backup


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
        auth_type = dictionary.get('authType')
        authenticating_database_name = dictionary.get('authenticatingDatabaseName')
        requires_ssl = dictionary.get('requiresSsl')
        secondary_node_tag = dictionary.get('secondaryNodeTag')
        seeds = dictionary.get('seeds')
        use_secondary_for_backup = dictionary.get('useSecondaryForBackup')

        # Return an object of this model
        return cls(auth_type,
                   authenticating_database_name,
                   requires_ssl,
                   secondary_node_tag,
                   seeds,
                   use_secondary_for_backup)


