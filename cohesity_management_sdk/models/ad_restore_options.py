# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_object_attribute_parameters
import cohesity_management_sdk.models.ad_object_restore_parameters

class AdRestoreOptions(object):

    """Implementation of the 'AdRestoreOptions' model.

    AdRestoreOptions are the AD specific options for the restore task being
    updated

    Attributes:
        object_attribute_parameters (AdObjectAttributeParameters):
            AdObjectAttributeParameters are AD attribute recovery parameters
            for one or more AD objects
        object_parameters (AdObjectRestoreParameters):
            AdObjectRestoreParameters are the parameters to restore AD objects
            from recycle bin or from a mounted AD snapshot database.
        mtype (TypeAdRestoreOptionsEnum): Specifies the AD restore request
            type. Specifies the action type of AD restore.  'kNone' specifies
            no special behaviour. 'kObjects' specifies the user action to
            restore AD objects from a mounted AD snapshot database.
            'kObjectAttributes' specifies the user action to restore
            attributes of an AD object from a mounted AD snapshot database.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "object_attribute_parameters":'objectAttributeParameters',
        "object_parameters":'objectParameters',
        "mtype":'type'
    }

    def __init__(self,
                 object_attribute_parameters=None,
                 object_parameters=None,
                 mtype=None):
        """Constructor for the AdRestoreOptions class"""

        # Initialize members of the class
        self.object_attribute_parameters = object_attribute_parameters
        self.object_parameters = object_parameters
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
        object_attribute_parameters = cohesity_management_sdk.models.ad_object_attribute_parameters.AdObjectAttributeParameters.from_dictionary(dictionary.get('objectAttributeParameters')) if dictionary.get('objectAttributeParameters') else None
        object_parameters = cohesity_management_sdk.models.ad_object_restore_parameters.AdObjectRestoreParameters.from_dictionary(dictionary.get('objectParameters')) if dictionary.get('objectParameters') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(object_attribute_parameters,
                   object_parameters,
                   mtype)


