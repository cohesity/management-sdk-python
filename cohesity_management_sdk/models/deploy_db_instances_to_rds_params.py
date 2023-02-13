# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.deploy_db_instances_to_rds_params_point_in_time_restore_params

class DeployDBInstancesToRDSParams(object):

    """Implementation of the 'DeployDBInstancesToRDSParams' model.

    Contains RDS specfic options that can be supplied while restoring the RDS
    DB instance.

    Attributes:
        auto_minor_version_upgrade (bool): Whether to enable auto minor
            version upgrade in the restored DB.
        availability_zone (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        copy_tags_to_snapshots (bool): Whether to enable copying of tags to
            snapshots of the DB.
        db_instance_id (string): The DB instance identifier to use for the
            restored DB. This field is required.
        db_option_group (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        db_parameter_group (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        db_port (int): Port to use for the DB in the restored RDS instance.
        iam_db_authentication (bool): Whether to enable IAM authentication for
            the DB.
        multi_az_deployment (bool): Whether this is a multi-az deployment or
            not.
        point_in_time_params
            (DeployDBInstancesToRDSParamsPointInTimeRestoreParams): Message to
            capture details of a point in time that the DB needs to be
            restored to.
        public_accessibility (bool): Whether this DB will be publicly
            accessible or not.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auto_minor_version_upgrade":'autoMinorVersionUpgrade',
        "availability_zone":'availabilityZone',
        "copy_tags_to_snapshots":'copyTagsToSnapshots',
        "db_instance_id":'dbInstanceId',
        "db_option_group":'dbOptionGroup',
        "db_parameter_group":'dbParameterGroup',
        "db_port":'dbPort',
        "iam_db_authentication":'iamDbAuthentication',
        "multi_az_deployment":'multiAzDeployment',
        "point_in_time_params":'pointInTimeParams',
        "public_accessibility":'publicAccessibility'
    }

    def __init__(self,
                 auto_minor_version_upgrade=None,
                 availability_zone=None,
                 copy_tags_to_snapshots=None,
                 db_instance_id=None,
                 db_option_group=None,
                 db_parameter_group=None,
                 db_port=None,
                 iam_db_authentication=None,
                 multi_az_deployment=None,
                 point_in_time_params=None,
                 public_accessibility=None):
        """Constructor for the DeployDBInstancesToRDSParams class"""

        # Initialize members of the class
        self.auto_minor_version_upgrade = auto_minor_version_upgrade
        self.availability_zone = availability_zone
        self.copy_tags_to_snapshots = copy_tags_to_snapshots
        self.db_instance_id = db_instance_id
        self.db_option_group = db_option_group
        self.db_parameter_group = db_parameter_group
        self.db_port = db_port
        self.iam_db_authentication = iam_db_authentication
        self.multi_az_deployment = multi_az_deployment
        self.point_in_time_params = point_in_time_params
        self.public_accessibility = public_accessibility


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
        auto_minor_version_upgrade = dictionary.get('autoMinorVersionUpgrade')
        availability_zone = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('availabilityZone')) if dictionary.get('availabilityZone') else None
        copy_tags_to_snapshots = dictionary.get('copyTagsToSnapshots')
        db_instance_id = dictionary.get('dbInstanceId')
        db_option_group = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('dbOptionGroup')) if dictionary.get('dbOptionGroup') else None
        db_parameter_group = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('dbParameterGroup')) if dictionary.get('dbParameterGroup') else None
        db_port = dictionary.get('dbPort')
        iam_db_authentication = dictionary.get('iamDbAuthentication')
        multi_az_deployment = dictionary.get('multiAzDeployment')
        point_in_time_params = cohesity_management_sdk.models.deploy_db_instances_to_rds_params_point_in_time_restore_params.DeployDBInstancesToRDSParamsPointInTimeRestoreParams.from_dictionary(dictionary.get('pointInTimeParams')) if dictionary.get('pointInTimeParams') else None
        public_accessibility = dictionary.get('publicAccessibility')

        # Return an object of this model
        return cls(auto_minor_version_upgrade,
                   availability_zone,
                   copy_tags_to_snapshots,
                   db_instance_id,
                   db_option_group,
                   db_parameter_group,
                   db_port,
                   iam_db_authentication,
                   multi_az_deployment,
                   point_in_time_params,
                   public_accessibility)


