# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.sfdc_object
import cohesity_management_sdk.models.sfdc_org


class SfdcProtectionSource(object):

    """Implementation of the 'SfdcProtectionSource' model.

    Specifies an Object representing Salesforce.


    Attributes:

        name (string): Specifies the instance name of the Salesforce entity.
        object_info (SfdcObject): Information of a Salesforce object, only
            valid for an entity of type kObject.
        org_info (SfdcOrg): Information of a Salesforce org, only valid for an
            entity of type kOrg.
        mtype (TypeSfdcProtectionSourceEnum): Specifies the type of the managed
            Object in Salesforce Protection Source. Sfdc related params. 
            Specifies the type of an Salesforce source entity. 'kOrg' indicates
            a Salseforce Org. 'kObject' indicates a object within the
            Salesforce Org.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "object_info":'objectInfo',
        "org_info":'orgInfo',
        "mtype":'type',
    }
    def __init__(self,
                 name=None,
                 object_info=None,
                 org_info=None,
                 mtype=None,
            ):

        """Constructor for the SfdcProtectionSource class"""

        # Initialize members of the class
        self.name = name
        self.object_info = object_info
        self.org_info = org_info
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
        name = dictionary.get('name')
        object_info = cohesity_management_sdk.models.sfdc_object.SfdcObject.from_dictionary(dictionary.get('objectInfo')) if dictionary.get('objectInfo') else None
        org_info = cohesity_management_sdk.models.sfdc_org.SfdcOrg.from_dictionary(dictionary.get('orgInfo')) if dictionary.get('orgInfo') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(
            name,
            object_info,
            org_info,
            mtype
)