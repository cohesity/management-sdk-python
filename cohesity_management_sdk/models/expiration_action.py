# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

class ExpirationAction(object):

    """Implementation of the 'ExpirationAction' model.

    Attributes:
        date_usecs (long|int): Timestamp in usecs for the date the object is
            subject to the rule.
        days (long|int): Lifetime in days, of the objects that are subject to
            the rule.
        expired_object_delete_marker (bool): Indicates whether Amazon S3 will
            remove a delete marker with no noncurrent versions. If set, the
            delete marker will be expired.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "date_usecs":'dateUsecs',
        "days":'days',
        "expired_object_delete_marker":'expiredObjectDeleteMarker'
    }

    def __init__(self,
                 date_usecs=None,
                 days=None,
                 expired_object_delete_marker=None):
        """Constructor for the ExpirationAction class"""

        # Initialize members of the class
        self.date_usecs = date_usecs
        self.days = days
        self.expired_object_delete_marker = expired_object_delete_marker


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
        date_usecs = dictionary.get('dateUsecs')
        days = dictionary.get('days')
        expired_object_delete_marker = dictionary.get('expiredObjectDeleteMarker')

        # Return an object of this model
        return cls(date_usecs,
                   days,
                   expired_object_delete_marker)


