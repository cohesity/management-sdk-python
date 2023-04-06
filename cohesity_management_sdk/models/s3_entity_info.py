# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class S3EntityInfo(object):

    """Implementation of the 'S3EntityInfo' model.

    Specifies S3 specific information about an S3 Entity.


    Attributes:

        create_time_msecs (long|int): Specifies the creation time of the
            entity.
        versioning (VersioningEnum): Specifies the Versioning state of S3
            bucket. Specifies the versioning state of S3 bucket. 'kUnversioned'
            implies versioning is not enabled. 'kEnabled' implies versioning is
            enabled. 'kSuspended' versioning is suspended.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "create_time_msecs":'createTimeMsecs',
        "versioning":'versioning',
    }
    def __init__(self,
                 create_time_msecs=None,
                 versioning=None,
            ):

        """Constructor for the S3EntityInfo class"""

        # Initialize members of the class
        self.create_time_msecs = create_time_msecs
        self.versioning = versioning

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
        create_time_msecs = dictionary.get('createTimeMsecs')
        versioning = dictionary.get('versioning')

        # Return an object of this model
        return cls(
            create_time_msecs,
            versioning
)