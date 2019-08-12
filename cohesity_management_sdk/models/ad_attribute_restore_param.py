# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.ad_guid_pair_ad_attribute_restore_param

class ADAttributeRestoreParam(object):

    """Implementation of the 'ADAttributeRestoreParam' model.

    TODO: type model description here.

    Attributes:
        excluded_property_vec (list of string): Array of LDAP property names
            to excluded from 'property_vec'. Excluded property name cannot
            contain wildcard character '*'.  Property names are case
            insensitive.
        guidpair_vec (list of ADGuidPairADAttributeRestoreParam): Array of
            source and destination object guid pairs to restore attributes.
            Pair source guid refers to guid in AD snapshot in source_server
            endpoint. Destination guid refers to guid in production AD. If
            destination guid is empty, then source guid in AD snapshot should
            exist in production AD.
        option_flags (int): Attribute restore option flags of type
            ADAttributeOptionFlags.
        property_vec (list of string): Array of LDAP property(attribute)
            names. The name can be standard or custom property defined in AD
            schema partition. The property can contain wildcard character '*'.
            If this array is empty, then '*' is assigned, means restore all
            properties except default system excluded properties. Wildcards
            will be expanded. If 'memberOf' property is included, group
            membership of the objects specified in 'guid_vec' will be
            restored. Property that does not exist for an object is ignored
            and no error info is returned for that property. Property names
            are case insensitive. Caller may check the
            ADAttributeFlags.kSystem obtained during object compare to exclude
            system properties.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "excluded_property_vec":'excludedPropertyVec',
        "guidpair_vec":'guidpairVec',
        "option_flags":'optionFlags',
        "property_vec":'propertyVec'
    }

    def __init__(self,
                 excluded_property_vec=None,
                 guidpair_vec=None,
                 option_flags=None,
                 property_vec=None):
        """Constructor for the ADAttributeRestoreParam class"""

        # Initialize members of the class
        self.excluded_property_vec = excluded_property_vec
        self.guidpair_vec = guidpair_vec
        self.option_flags = option_flags
        self.property_vec = property_vec


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
        excluded_property_vec = dictionary.get('excludedPropertyVec')
        guidpair_vec = None
        if dictionary.get('guidpairVec') != None:
            guidpair_vec = list()
            for structure in dictionary.get('guidpairVec'):
                guidpair_vec.append(cohesity_management_sdk.models.ad_guid_pair_ad_attribute_restore_param.ADGuidPairADAttributeRestoreParam.from_dictionary(structure))
        option_flags = dictionary.get('optionFlags')
        property_vec = dictionary.get('propertyVec')

        # Return an object of this model
        return cls(excluded_property_vec,
                   guidpair_vec,
                   option_flags,
                   property_vec)


