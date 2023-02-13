# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RdsParams(object):

    """Implementation of the 'RdsParams' model.

    Specifies rds params for the restore operation.

    Attributes:
        availability_zone_id (long|int): Entity representing the availability
            zone to use while restoring the DB.
        db_instance_id (string): The DB instance identifier to use for the
            restored DB. This field is required.
        db_option_group_id (long|int): Entity representing the RDS option
            group to use while restoring the DB.
        db_parameter_group_id (long|int): Entity representing the RDS
            parameter group to use while restoring the DB.
        db_port (int): Port to use for the DB in the restored RDS instance.
        enable_auto_minor_version_upgrade (bool): Whether to enable auto minor
            version upgrade in the restored DB.
        enable_copy_tags_to_snapshots (bool): Whether to enable copying of
            tags to snapshots of the DB.
        enable_db_authentication (bool): Whether to enable IAM authentication
            for the DB.
        enable_public_accessibility (bool): Whether this DB will be publicly
            accessible or not.
        is_multi_az_deployment (bool): Whether this is a multi-az deployment
            or not.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "db_instance_id":'dbInstanceId',
        "availability_zone_id":'availabilityZoneId',
        "db_option_group_id":'dbOptionGroupId',
        "db_parameter_group_id":'dbParameterGroupId',
        "db_port":'dbPort',
        "enable_auto_minor_version_upgrade":'enableAutoMinorVersionUpgrade',
        "enable_copy_tags_to_snapshots":'enableCopyTagsToSnapshots',
        "enable_db_authentication":'enableDbAuthentication',
        "enable_public_accessibility":'enablePublicAccessibility',
        "is_multi_az_deployment":'isMultiAzDeployment'
    }

    def __init__(self,
                 db_instance_id=None,
                 availability_zone_id=None,
                 db_option_group_id=None,
                 db_parameter_group_id=None,
                 db_port=None,
                 enable_auto_minor_version_upgrade=None,
                 enable_copy_tags_to_snapshots=None,
                 enable_db_authentication=None,
                 enable_public_accessibility=None,
                 is_multi_az_deployment=None):
        """Constructor for the RdsParams class"""

        # Initialize members of the class
        self.availability_zone_id = availability_zone_id
        self.db_instance_id = db_instance_id
        self.db_option_group_id = db_option_group_id
        self.db_parameter_group_id = db_parameter_group_id
        self.db_port = db_port
        self.enable_auto_minor_version_upgrade = enable_auto_minor_version_upgrade
        self.enable_copy_tags_to_snapshots = enable_copy_tags_to_snapshots
        self.enable_db_authentication = enable_db_authentication
        self.enable_public_accessibility = enable_public_accessibility
        self.is_multi_az_deployment = is_multi_az_deployment


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
        db_instance_id = dictionary.get('dbInstanceId')
        availability_zone_id = dictionary.get('availabilityZoneId')
        db_option_group_id = dictionary.get('dbOptionGroupId')
        db_parameter_group_id = dictionary.get('dbParameterGroupId')
        db_port = dictionary.get('dbPort')
        enable_auto_minor_version_upgrade = dictionary.get('enableAutoMinorVersionUpgrade')
        enable_copy_tags_to_snapshots = dictionary.get('enableCopyTagsToSnapshots')
        enable_db_authentication = dictionary.get('enableDbAuthentication')
        enable_public_accessibility = dictionary.get('enablePublicAccessibility')
        is_multi_az_deployment = dictionary.get('isMultiAzDeployment')

        # Return an object of this model
        return cls(db_instance_id,
                   availability_zone_id,
                   db_option_group_id,
                   db_parameter_group_id,
                   db_port,
                   enable_auto_minor_version_upgrade,
                   enable_copy_tags_to_snapshots,
                   enable_db_authentication,
                   enable_public_accessibility,
                   is_multi_az_deployment)


