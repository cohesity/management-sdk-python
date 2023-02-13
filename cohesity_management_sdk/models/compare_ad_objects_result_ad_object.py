# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.compare_ad_objects_result_ad_attribute
import cohesity_management_sdk.models.error_proto

class CompareADObjectsResultADObject(object):

    """Implementation of the 'CompareADObjectsResult_ADObject' model.

    TODO: type model description here.

    Attributes:
        attribute_vec (list of CompareADObjectsResultADAttribute): Array of AD
            attributes of AD object. This will contain distinct attributes
            from source and destination objects.
        dest_guid (string): Object guid from dest_server. If empty, compare
            could not find an AD object corresponding to 'source_guid' even
            after looking up based on source_guid, source DN or source SAM
            account name. The SAM is applicable only for account type
            objects.
        dest_prop_count (int): Number of attributes in destination object
            including system properties compared. This count is useful for
            debugging.
        excluded_prop_count (int): Number of attributes not compared due to
            ADCompareOptionFlags.kExcludeSysProps. This count is useful for
            debugging.
        mismatch_prop_count (int): Number of AD attributes compared based on
            'ADCompareOptionFlagsType' flags and found to be mismatched. If
            this is non-zero, compared objects are different. If this is 0
            ann'dest_guid' is empty, then object is missing.
        object_flags (int): Object result flags of type ADObjectFlags.
        source_guid (string): Object guid from $SourceServer. Guid string with
            or without '{}' braces.
        source_prop_count (int): Number of attributes in source object
            including system properties compared. This count is useful for
            debugging.
        status (ErrorProto): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attribute_vec":'attributeVec',
        "dest_guid":'destGuid',
        "dest_prop_count":'destPropCount',
        "excluded_prop_count":'excludedPropCount',
        "mismatch_prop_count":'mismatchPropCount',
        "object_flags":'objectFlags',
        "source_guid":'sourceGuid',
        "source_prop_count":'sourcePropCount',
        "status":'status'
    }

    def __init__(self,
                 attribute_vec=None,
                 dest_guid=None,
                 dest_prop_count=None,
                 excluded_prop_count=None,
                 mismatch_prop_count=None,
                 object_flags=None,
                 source_guid=None,
                 source_prop_count=None,
                 status=None):
        """Constructor for the CompareADObjectsResultADObject class"""

        # Initialize members of the class
        self.attribute_vec = attribute_vec
        self.dest_guid = dest_guid
        self.dest_prop_count = dest_prop_count
        self.excluded_prop_count = excluded_prop_count
        self.mismatch_prop_count = mismatch_prop_count
        self.object_flags = object_flags
        self.source_guid = source_guid
        self.source_prop_count = source_prop_count
        self.status = status


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
        attribute_vec = None
        if dictionary.get('attributeVec') != None:
            attribute_vec = list()
            for structure in dictionary.get('attributeVec'):
                attribute_vec.append(cohesity_management_sdk.models.compare_ad_objects_result_ad_attribute.CompareADObjectsResultADAttribute.from_dictionary(structure))
        dest_guid = dictionary.get('destGuid')
        dest_prop_count = dictionary.get('destPropCount')
        excluded_prop_count = dictionary.get('excludedPropCount')
        mismatch_prop_count = dictionary.get('mismatchPropCount')
        object_flags = dictionary.get('objectFlags')
        source_guid = dictionary.get('sourceGuid')
        source_prop_count = dictionary.get('sourcePropCount')
        status = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('status')) if dictionary.get('status') else None

        # Return an object of this model
        return cls(attribute_vec,
                   dest_guid,
                   dest_prop_count,
                   excluded_prop_count,
                   mismatch_prop_count,
                   object_flags,
                   source_guid,
                   source_prop_count,
                   status)


