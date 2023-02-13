# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FilteringPolicyProto(object):

    """Implementation of the 'FilteringPolicyProto' model.

    Proto to encapsulate the filtering policy for backup objects like files
    or
    directories. If an object is not matched by any of the 'allow_filters',
    it
    will be excluded in the backup. If an object is matched by one of the
    'deny_filters', it will always be excluded in the backup. Basically
    'deny_filters' overwrite 'allow_filters' if they both match the same
    object.
    Currently we only support two kinds of filter: prefix which always starts
    with '/', or postfix which always starts with '*' (cannot be "*" only).
    We
    don't support regular expression right now.
    A concrete example is:
    Allow filters: "/"
    Deny filters: "/tmp", "*.mp4"
    Using such a policy will include everything under the root directory
    except
    the /tmp directory and all the mp4 files.

    Attributes:
        allow_filters (list of string): List of filters to allow matched
            objects for backup.
        deny_filters (list of string): List of filters to deny matched objects
            for backup.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allow_filters":'allowFilters',
        "deny_filters":'denyFilters'
    }

    def __init__(self,
                 allow_filters=None,
                 deny_filters=None):
        """Constructor for the FilteringPolicyProto class"""

        # Initialize members of the class
        self.allow_filters = allow_filters
        self.deny_filters = deny_filters


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
        allow_filters = dictionary.get('allowFilters')
        deny_filters = dictionary.get('denyFilters')

        # Return an object of this model
        return cls(allow_filters,
                   deny_filters)


