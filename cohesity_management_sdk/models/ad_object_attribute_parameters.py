# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_ad_guid_pair

class AdObjectAttributeParameters(object):

    """Implementation of the 'AdObjectAttributeParameters' model.

    AdObjectAttributeParameters are AD attribute recovery parameters for one
    or more AD objects

    Attributes:
        ad_guid_pairs (list of RestoreAdGuidPair): Specifies the array of source and
            destination object guid pairs to restore attributes.
        exclude_ldap_properties (list of string): Specifies the array of LDAP
            property names to excluded from 'property_vec'. Excluded property
            name cannot contain wildcard character '*'.  Property names are
            case insensitive.
        ldap_properties (list of string): Specifies the array of LDAP
            property(attribute) names. The name can be standard or custom
            property defined in AD schema partition. The property can contain
            wildcard character '*'. If this array is empty, then '*' is
            assigned, means restore all properties except default system
            excluded properties. Wildcards will be expanded. If 'memberOf'
            property is included, group membership of the objects specified in
            'guid_vec' will be restored. Property that does not exist for an
            object is ignored and no error info is returned for that property.
            Property names are case insensitive.
        merge_multi_val_properties (bool): Specifies the Option to merge
            multi-valued values vs clearing and setting values from the AD
            snapshot. Defaults is to overwrite production AD values from the
            source AD snapshot. When updating group membership (using
            'memberOf' property), setting this option to true will result in
            group membership merge. This is useful in cases where production
            AD has later updates that should not be overridden while restoring
            an attribute.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ad_guid_pairs":'adGuidPairs',
        "exclude_ldap_properties":'excludeLdapProperties',
        "ldap_properties":'ldapProperties',
        "merge_multi_val_properties":'mergeMultiValProperties'
    }

    def __init__(self,
                 ad_guid_pairs=None,
                 exclude_ldap_properties=None,
                 ldap_properties=None,
                 merge_multi_val_properties=None):
        """Constructor for the AdObjectAttributeParameters class"""

        # Initialize members of the class
        self.ad_guid_pairs = ad_guid_pairs
        self.exclude_ldap_properties = exclude_ldap_properties
        self.ldap_properties = ldap_properties
        self.merge_multi_val_properties = merge_multi_val_properties


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
        ad_guid_pairs = None
        if dictionary.get('adGuidPairs') != None:
            ad_guid_pairs = list()
            for structure in dictionary.get('adGuidPairs'):
                ad_guid_pairs.append(cohesity_management_sdk.models.restore_ad_guid_pair.RestoreAdGuidPair.from_dictionary(structure))
        exclude_ldap_properties = dictionary.get('excludeLdapProperties')
        ldap_properties = dictionary.get('ldapProperties')
        merge_multi_val_properties = dictionary.get('mergeMultiValProperties')

        # Return an object of this model
        return cls(ad_guid_pairs,
                   exclude_ldap_properties,
                   ldap_properties,
                   merge_multi_val_properties)


