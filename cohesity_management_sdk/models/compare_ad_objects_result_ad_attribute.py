# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.compare_ad_objects_result_ad_attribute_value
import cohesity_management_sdk.models.error_proto


class CompareADObjectsResult_ADAttribute(object):

    """Implementation of the 'CompareADObjectsResult_ADAttribute' model.

    TODO: type description here.


    Attributes:

        attr_flags (int): Object result flags of type ADAttributeFlags.
        dest_value (CompareADObjectsResult_ADAttributeValue): Destination
            attribute value if dest value exists (!ADAttributeFlags.kNotFound)
            and is different from source.
        ldap_name (string): LDAP attribute name.
        same_value (CompareADObjectsResult_ADAttributeValue): if the attribute
            values are same (ADAttributeFlags.kEqual), the value is put here to
            avoid duplication in 'source_value' and 'dest_value'.
        source_value (CompareADObjectsResult_ADAttributeValue): Source
            attribute value if source value exists
            (!ADAttributeFlags.kNotFound) and is different from destination.
        status (ErrorProto): Error status for the attribute compare or value
            access.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "attr_flags":'attrFlags',
        "dest_value":'destValue',
        "ldap_name":'ldapName',
        "same_value":'sameValue',
        "source_value":'sourceValue',
        "status":'status',
    }
    def __init__(self,
                 attr_flags=None,
                 dest_value=None,
                 ldap_name=None,
                 same_value=None,
                 source_value=None,
                 status=None,
            ):

        """Constructor for the CompareADObjectsResult_ADAttribute class"""

        # Initialize members of the class
        self.attr_flags = attr_flags
        self.dest_value = dest_value
        self.ldap_name = ldap_name
        self.same_value = same_value
        self.source_value = source_value
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
        attr_flags = dictionary.get('attrFlags')
        dest_value = cohesity_management_sdk.models.compare_ad_objects_result_ad_attribute_value.CompareADObjectsResult_ADAttributeValue.from_dictionary(dictionary.get('destValue')) if dictionary.get('destValue') else None
        ldap_name = dictionary.get('ldapName')
        same_value = cohesity_management_sdk.models.compare_ad_objects_result_ad_attribute_value.CompareADObjectsResult_ADAttributeValue.from_dictionary(dictionary.get('sameValue')) if dictionary.get('sameValue') else None
        source_value = cohesity_management_sdk.models.compare_ad_objects_result_ad_attribute_value.CompareADObjectsResult_ADAttributeValue.from_dictionary(dictionary.get('sourceValue')) if dictionary.get('sourceValue') else None
        status = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('status')) if dictionary.get('status') else None

        # Return an object of this model
        return cls(
            attr_flags,
            dest_value,
            ldap_name,
            same_value,
            source_value,
            status
)