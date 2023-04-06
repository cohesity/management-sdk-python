# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto


class RestoreS3Params_NewLocationParams(object):

    """Implementation of the 'RestoreS3Params_NewLocationParams' model.

    Message specifying new location details, should be set only when
    is_original_location is false.


    Attributes:

        object_prefix (string): Object prefix for the recovered objects. E.g.
            "/", "/a/b".
        region (EntityProto): Target Region in which recovery should happen.
        s3_bucket (EntityProto): Target S3 bucket where recovery should happen.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "object_prefix":'objectPrefix',
        "region":'region',
        "s3_bucket":'s3Bucket',
    }
    def __init__(self,
                 object_prefix=None,
                 region=None,
                 s3_bucket=None,
            ):

        """Constructor for the RestoreS3Params_NewLocationParams class"""

        # Initialize members of the class
        self.object_prefix = object_prefix
        self.region = region
        self.s3_bucket = s3_bucket

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
        object_prefix = dictionary.get('objectPrefix')
        region = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('region')) if dictionary.get('region') else None
        s3_bucket = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('s3Bucket')) if dictionary.get('s3Bucket') else None

        # Return an object of this model
        return cls(
            object_prefix,
            region,
            s3_bucket
)