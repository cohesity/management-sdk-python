# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.attribute_value

class AdAttribute(object):

    """Implementation of the 'AdAttribute' model.

    Represnts the information about the AD attribute of the object.
    It also contains information regarding whether it is system attribute
    and whether the attribute is equal on both Snapshot and Production
    AD.

    Attributes:
        ad_attribute_flags (list of AdAttributeFlagEnum): Specifies the flags
            related to the attribute of the AD object. 'kEqual' indicates the
            attribute value of AD object from Snapshot and Production AD are
            equal. 'kNotEqual' indicates the attribute value of AD object from
            Snapshot and Production AD are not equal. 'kNotFound' indicates
            attribute of the AD object is missing from both Snapshot and
            Production AD. 'kSystem' indicates this is system attribute. This
            can only be updated by the AD internal component. 'kMultiValue'
            indicates that the attribute is mutli-value attribute. This
            attribute supports mutli-value merge during attribute restore
            operation.
        destination_value (AttributeValue): Represents the information about
            the values of attribute of the ADObject.
        error_message (string): Specifies the error message regarding the
            attribute
        name (string): Specifies the name of the attribute of the AD object.
        same_value (AttributeValue): Represents the information about the
            values of attribute of the ADObject.
        source_value (AttributeValue): Represents the information about the
            values of attribute of the ADObject.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ad_attribute_flags":'adAttributeFlags',
        "destination_value":'destinationValue',
        "error_message":'errorMessage',
        "name":'name',
        "same_value":'sameValue',
        "source_value":'sourceValue'
    }

    def __init__(self,
                 ad_attribute_flags=None,
                 destination_value=None,
                 error_message=None,
                 name=None,
                 same_value=None,
                 source_value=None):
        """Constructor for the AdAttribute class"""

        # Initialize members of the class
        self.ad_attribute_flags = ad_attribute_flags
        self.destination_value = destination_value
        self.error_message = error_message
        self.name = name
        self.same_value = same_value
        self.source_value = source_value


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
        ad_attribute_flags = dictionary.get('adAttributeFlags')
        destination_value = cohesity_management_sdk.models.attribute_value.AttributeValue.from_dictionary(dictionary.get('destinationValue')) if dictionary.get('destinationValue') else None
        error_message = dictionary.get('errorMessage')
        name = dictionary.get('name')
        same_value = cohesity_management_sdk.models.attribute_value.AttributeValue.from_dictionary(dictionary.get('sameValue')) if dictionary.get('sameValue') else None
        source_value = cohesity_management_sdk.models.attribute_value.AttributeValue.from_dictionary(dictionary.get('sourceValue')) if dictionary.get('sourceValue') else None

        # Return an object of this model
        return cls(ad_attribute_flags,
                   destination_value,
                   error_message,
                   name,
                   same_value,
                   source_value)


