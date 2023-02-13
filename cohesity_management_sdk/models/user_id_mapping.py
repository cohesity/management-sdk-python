# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.centrify_zone
import cohesity_management_sdk.models.custom_unix_id_attributes
import cohesity_management_sdk.models.fixed_unix_id_mapping

class UserIdMapping(object):

    """Implementation of the 'UserIdMapping' model.

    Specifies how the Unix and Windows users are mapped in an Active
    Directory.

    Attributes:
        centrify_zone_mapping (CentrifyZone): Specifies the properties
            associated to a Centrify zone of an Active Directory domain.
        custom_attributes_mapping (CustomUnixIdAttributes): Specifies the
            custom attributes when mapping type is set to 'kCustomAttributes'.
            It defines the attribute names to derive the mapping for a user of
            an Active Directory domain.
        fixed_mapping (FixedUnixIdMapping): Specifies the fields when mapping
            type is set to 'kFixed'. It maps all Active Directory users of a
            domain to a fixed Unix uid, and gid.
        mtype (TypeUserIdMappingEnum): Specifies the mapping type used. 'kRid'
            indicates the kRid mapping type. 'kRfc2307' indicates the kRfc2307
            mapping type. 'kSfu30' indicates the kSfu30 mapping type.
            'kCentrify' indicates the mapping type to refer to a centrify
            zone. 'kFixed' indicates the mapping from all Active Directory
            users to a fixed Unix uid, and gid. 'kCustomAttributes' indicates
            the mapping to derive from custom attributes defined in an AD
            domain. 'kLdapProvider' indicates the Active Directory to LDAP
            provider mapping.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "centrify_zone_mapping":'centrifyZoneMapping',
        "custom_attributes_mapping":'customAttributesMapping',
        "fixed_mapping":'fixedMapping',
        "mtype":'type'
    }

    def __init__(self,
                 centrify_zone_mapping=None,
                 custom_attributes_mapping=None,
                 fixed_mapping=None,
                 mtype=None):
        """Constructor for the UserIdMapping class"""

        # Initialize members of the class
        self.centrify_zone_mapping = centrify_zone_mapping
        self.custom_attributes_mapping = custom_attributes_mapping
        self.fixed_mapping = fixed_mapping
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
        centrify_zone_mapping = cohesity_management_sdk.models.centrify_zone.CentrifyZone.from_dictionary(dictionary.get('centrifyZoneMapping')) if dictionary.get('centrifyZoneMapping') else None
        custom_attributes_mapping = cohesity_management_sdk.models.custom_unix_id_attributes.CustomUnixIdAttributes.from_dictionary(dictionary.get('customAttributesMapping')) if dictionary.get('customAttributesMapping') else None
        fixed_mapping = cohesity_management_sdk.models.fixed_unix_id_mapping.FixedUnixIdMapping.from_dictionary(dictionary.get('fixedMapping')) if dictionary.get('fixedMapping') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(centrify_zone_mapping,
                   custom_attributes_mapping,
                   fixed_mapping,
                   mtype)


