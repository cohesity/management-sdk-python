# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AuroraClusterInfo(object):

    """Implementation of the 'AuroraClusterInfo' model.

    TODO: type description here.


    Attributes:

        aws_region (string): Aws region of the Aurora DB cluster and S3 bucket.
        db_user_name (string): Database user for managing the databases on the
            Aurora cluster. This user will have exclusive access on all the
            databases created for the protection group and recovery for a
            particular tenant.
        host_name (string): Contains the host name of the Aurora cluster. This
            is the writer end point of the Aurora cluster.
        kms_key_arn (string): Contains the kms encryption key used for
            encryption of data on the Aurora cluster.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "aws_region":'awsRegion',
        "db_user_name":'dbUserName',
        "host_name":'hostName',
        "kms_key_arn":'kmsKeyArn',
    }
    def __init__(self,
                 aws_region=None,
                 db_user_name=None,
                 host_name=None,
                 kms_key_arn=None,
            ):

        """Constructor for the AuroraClusterInfo class"""

        # Initialize members of the class
        self.aws_region = aws_region
        self.db_user_name = db_user_name
        self.host_name = host_name
        self.kms_key_arn = kms_key_arn

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
        aws_region = dictionary.get('awsRegion')
        db_user_name = dictionary.get('dbUserName')
        host_name = dictionary.get('hostName')
        kms_key_arn = dictionary.get('kmsKeyArn')

        # Return an object of this model
        return cls(
            aws_region,
            db_user_name,
            host_name,
            kms_key_arn
)