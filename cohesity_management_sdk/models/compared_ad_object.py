# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_attribute

class ComparedADObject(object):

    """Implementation of the 'ComparedADObject' model.

    Represents the details about an AD object and its properties.
    The attributes of the AD Object contain the information about whether
    they are equal on both Snapshot AD and Production AD as well as value of
    attribute on both Production and Snapshot AD.

    Attributes:
        ad_attributes (list of AdAttribute): Specifies the list of AD
            attributes for the AD object.
        ad_object_flags (list of AdObjectFlagEnum): Specifies the flags
            related to this AD Object. 'kEqual' indicates all the attributes
            of the AD Object on the Snapshot and Production are equal.
            'kNotEqual' indicates atleast one of the attribute of the AD
            Object on the Snapshot and Production AD are not equal.
            'kRestorePasswordRequired' indicates the AD Object is of 'User'
            object class type. when restoring this object from Snapshot AD to
            Priduction AD, a password is required. 'kMovedOnDestination'
            indicates the object has moved to another container or OU in
            production AD compared to AD snapshot. In this case, the
            distinguishedName will be different for these objects
            'kDestinationNotFound' indicates the object corresponding to
            dest_guid specified is missing from Production AD. Caller should
            check this flag and empty 'dest_guid' first to find out
            destination is missing. 'kDisableSupported' indicates the enable
            and disable is supported on the AD Object. AD Objects of type
            'User' and 'Computers' support this operation.
        destination_guid (string): Specifies the guid of the object in the
            Production AD which is equivalent to the one in the Snapshot AD.
        error_message (string): Specifies the error message while fetching the
            AD object.
        mismatch_attr_count (int): Specifies the number of attributes of AD
            Object mismatched on the Snapshot and Production AD.
        source_guid (string): Specifies the guid of the AD object in the
            Snapshot AD.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ad_attributes":'adAttributes',
        "ad_object_flags":'adObjectFlags',
        "destination_guid":'destinationGuid',
        "error_message":'errorMessage',
        "mismatch_attr_count":'mismatchAttrCount',
        "source_guid":'sourceGuid'
    }

    def __init__(self,
                 ad_attributes=None,
                 ad_object_flags=None,
                 destination_guid=None,
                 error_message=None,
                 mismatch_attr_count=None,
                 source_guid=None):
        """Constructor for the ComparedADObject class"""

        # Initialize members of the class
        self.ad_attributes = ad_attributes
        self.ad_object_flags = ad_object_flags
        self.destination_guid = destination_guid
        self.error_message = error_message
        self.mismatch_attr_count = mismatch_attr_count
        self.source_guid = source_guid


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
        ad_attributes = None
        if dictionary.get('adAttributes') != None:
            ad_attributes = list()
            for structure in dictionary.get('adAttributes'):
                ad_attributes.append(cohesity_management_sdk.models.ad_attribute.AdAttribute.from_dictionary(structure))
        ad_object_flags = dictionary.get('adObjectFlags')
        destination_guid = dictionary.get('destinationGuid')
        error_message = dictionary.get('errorMessage')
        mismatch_attr_count = dictionary.get('mismatchAttrCount')
        source_guid = dictionary.get('sourceGuid')

        # Return an object of this model
        return cls(ad_attributes,
                   ad_object_flags,
                   destination_guid,
                   error_message,
                   mismatch_attr_count,
                   source_guid)


