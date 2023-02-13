# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AbortIncompleteMultipartUploadAction(object):

    """Implementation of the 'AbortIncompleteMultipartUploadAction' model.

    Attributes:
        days_after_initiation (long|int): Specifies the number of days after which
            to abort an incomplete multipart upload.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "days_after_initiation":'daysAfterInitiation'
    }

    def __init__(self,
                 days_after_initiation=None):
        """Constructor for the AbortIncompleteMultipartUploadAction class"""

        # Initialize members of the class
        self.days_after_initiation = days_after_initiation


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
        days_after_initiation = dictionary.get('daysAfterInitiation')

        # Return an object of this model
        return cls(days_after_initiation)


