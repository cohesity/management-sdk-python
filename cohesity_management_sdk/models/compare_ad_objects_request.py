# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.guid_pair

class CompareAdObjectsRequest(object):

    """Implementation of the 'CompareAdObjectsRequest' model.

    Specifies the request to compare AD objects from Snapshot and Production
    AD.

    Attributes:
        restore_task_id (long|int): Specifies the Restore Task Id
            corresponding to which we need to compare the AD objects.
        allow_empty_dest_guids (bool): Specifies the option to get object
            attributes from Snapshot AD when destination guid is missing in
            GuidPair. This helps to show attributes of AD object from Snapshot
            AD when the object is missing in Production AD.
        exclude_sys_attributes (bool): Specifies the option to exclude AD
            system attributes when comparing two AD object attributes. If the
            objects have same guid, most of the system attributes would
            match.If the AD object was recovered through a restore, then many
            system attributes will be different. Default compares all
            attributes.
        filter_null_value_attributes (bool): Specifies the option to not
            return attributes where source and destination values are null
            values. This reduces noise of the properties in the objects
            returned.
        filter_same_value_attributes (bool): Specifies the option to not
            return attributes where source and destination values are same.
            Use this flag to return only values that are different.
        guid_pairs (list of GuidPair): Specifies the GuidPair of the AD
            Objects which we want to compare from both Snapshot and Production
            AD.
        quick_compare (bool): Specifies the option to do quick compare of
            specified guid between Snapshot AD and Production AD. If at least
            one attribute mismatch is found, comparison stops and returns with
            AdObjectFlag kNotEqual.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "restore_task_id":'RestoreTaskId',
        "guid_pairs":'guidPairs',
        "allow_empty_dest_guids":'allowEmptyDestGuids',
        "exclude_sys_attributes":'excludeSysAttributes',
        "filter_null_value_attributes":'filterNullValueAttributes',
        "filter_same_value_attributes":'filterSameValueAttributes',
        "quick_compare":'quickCompare'
    }

    def __init__(self,
                 restore_task_id=None,
                 guid_pairs=None,
                 allow_empty_dest_guids=None,
                 exclude_sys_attributes=None,
                 filter_null_value_attributes=None,
                 filter_same_value_attributes=None,
                 quick_compare=None):
        """Constructor for the CompareAdObjectsRequest class"""

        # Initialize members of the class
        self.restore_task_id = restore_task_id
        self.allow_empty_dest_guids = allow_empty_dest_guids
        self.exclude_sys_attributes = exclude_sys_attributes
        self.filter_null_value_attributes = filter_null_value_attributes
        self.filter_same_value_attributes = filter_same_value_attributes
        self.guid_pairs = guid_pairs
        self.quick_compare = quick_compare


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
        restore_task_id = dictionary.get('RestoreTaskId')
        guid_pairs = None
        if dictionary.get('guidPairs') != None:
            guid_pairs = list()
            for structure in dictionary.get('guidPairs'):
                guid_pairs.append(cohesity_management_sdk.models.guid_pair.GuidPair.from_dictionary(structure))
        allow_empty_dest_guids = dictionary.get('allowEmptyDestGuids')
        exclude_sys_attributes = dictionary.get('excludeSysAttributes')
        filter_null_value_attributes = dictionary.get('filterNullValueAttributes')
        filter_same_value_attributes = dictionary.get('filterSameValueAttributes')
        quick_compare = dictionary.get('quickCompare')

        # Return an object of this model
        return cls(restore_task_id,
                   guid_pairs,
                   allow_empty_dest_guids,
                   exclude_sys_attributes,
                   filter_null_value_attributes,
                   filter_same_value_attributes,
                   quick_compare)


