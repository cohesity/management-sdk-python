# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CouchbaseBucket(object):

    """Implementation of the 'CouchbaseBucket' model.

    Specifies an Object containing information about a couchbase Bucket.

    Attributes:
    bucket_type (string): Type of this bucket.
    document_count (int|long): Number of documents in this bucket.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bucket_type":'bucketType',
        "document_count":'documentCount'
    }

    def __init__(self,
                 bucket_type=None,
                 document_count=None):
        """Constructor for the CouchbaseBucket class"""

        # Initialize members of the class
        self.bucket_type = bucket_type
        self.document_count = document_count


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
        bucket_type = dictionary.get('bucketType')
        document_count = dictionary.get('documentCount')

        # Return an object of this model
        return cls(bucket_type,
                   document_count)


