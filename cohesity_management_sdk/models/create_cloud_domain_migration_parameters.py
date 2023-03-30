# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CreateCloudDomainMigrationParameters(object):

    """Implementation of the 'CreateCloudDomainMigrationParameters' model.

    CreateCloudDomainMigrationParameters represents the parameters needed to
    schedule the cloud domain migration.


    Attributes:

        cloud_domain_id (long|int): Specifies the Id of a specific cloud domain
            present inside the vault, that needs to be migrated. If not set,
            all cloud domains found in the vault or under the
            'domain_namespace' specified in CADConfig will be migrated.
        is_cad_mode (bool): Specifies if the migration mode is CAD or not.
        migration_uid (string): Specifies the Unique identifier of the domain
            migration request and can be used to query the status of the
            migration.
        vault_id (long|int): Specifies Id of the vault.
        view_box_id (long|int): Specifies the id of the viewbox for the request
            in case migration mode is Incremental Forever. Not set for CAD mode
            migration.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_domain_id":'cloudDomainId',
        "is_cad_mode":'isCadMode',
        "migration_uid":'migrationUid',
        "vault_id":'vaultId',
        "view_box_id":'viewBoxId',
    }
    def __init__(self,
                 cloud_domain_id=None,
                 is_cad_mode=None,
                 migration_uid=None,
                 vault_id=None,
                 view_box_id=None,
            ):

        """Constructor for the CreateCloudDomainMigrationParameters class"""

        # Initialize members of the class
        self.cloud_domain_id = cloud_domain_id
        self.is_cad_mode = is_cad_mode
        self.migration_uid = migration_uid
        self.vault_id = vault_id
        self.view_box_id = view_box_id

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
        cloud_domain_id = dictionary.get('cloudDomainId')
        is_cad_mode = dictionary.get('isCadMode')
        migration_uid = dictionary.get('migrationUid')
        vault_id = dictionary.get('vaultId')
        view_box_id = dictionary.get('viewBoxId')

        # Return an object of this model
        return cls(
            cloud_domain_id,
            is_cad_mode,
            migration_uid,
            vault_id,
            view_box_id
)