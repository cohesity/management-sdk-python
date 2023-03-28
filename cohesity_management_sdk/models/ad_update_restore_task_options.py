# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_attribute_restore_param
import cohesity_management_sdk.models.ad_object_restore_param


class ADUpdateRestoreTaskOptions(object):

    """Implementation of the 'ADUpdateRestoreTaskOptions' model.

    TODO: type description here.


    Attributes:

        object_attributes_param (ADAttributeRestoreParam): Object attributes
            restore params with the list of attributes to be restored. This is
            set only when type is kObjectAttributes.
        object_param (ADObjectRestoreParam): Object restore params with info
            about objects to be restored. This is set only when type is
            kObjects.
        mtype (int): Specifies the AD restore request type.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "object_attributes_param":'objectAttributesParam',
        "object_param":'objectParam',
        "mtype":'type',
    }
    def __init__(self,
                 object_attributes_param=None,
                 object_param=None,
                 mtype=None,
            ):

        """Constructor for the ADUpdateRestoreTaskOptions class"""

        # Initialize members of the class
        self.object_attributes_param = object_attributes_param
        self.object_param = object_param
        self.mtype = mtype

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
        object_attributes_param = cohesity_management_sdk.models.ad_attribute_restore_param.ADAttributeRestoreParam.from_dictionary(dictionary.get('objectAttributesParam')) if dictionary.get('objectAttributesParam') else None
        object_param = cohesity_management_sdk.models.ad_object_restore_param.ADObjectRestoreParam.from_dictionary(dictionary.get('objectParam')) if dictionary.get('objectParam') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(
            object_attributes_param,
            object_param,
            mtype
)