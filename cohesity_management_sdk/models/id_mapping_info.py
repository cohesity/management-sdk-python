# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.user_id_mapping

class IdMappingInfo(object):

    """Implementation of the 'IdMappingInfo' model.

    Specifies the params required to update the user id mapping info of an
    Active Directory.

    Attributes:
        fallback_user_id_mapping_info (UserIdMapping): Specifies how the Unix
            and Windows users are mapped in an Active Directory.
        unix_root_sid (string): Specifies the SID of the Active Directory
            domain user to be mapped to Unix root user.
        user_id_mapping_info (UserIdMapping): Specifies how the Unix and
            Windows users are mapped in an Active Directory.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fallback_user_id_mapping_info":'fallbackUserIdMappingInfo',
        "unix_root_sid":'unixRootSid',
        "user_id_mapping_info":'userIdMappingInfo'
    }

    def __init__(self,
                 fallback_user_id_mapping_info=None,
                 unix_root_sid=None,
                 user_id_mapping_info=None):
        """Constructor for the IdMappingInfo class"""

        # Initialize members of the class
        self.fallback_user_id_mapping_info = fallback_user_id_mapping_info
        self.unix_root_sid = unix_root_sid
        self.user_id_mapping_info = user_id_mapping_info


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
        fallback_user_id_mapping_info = cohesity_management_sdk.models.user_id_mapping.UserIdMapping.from_dictionary(dictionary.get('fallbackUserIdMappingInfo')) if dictionary.get('fallbackUserIdMappingInfo') else None
        unix_root_sid = dictionary.get('unixRootSid')
        user_id_mapping_info = cohesity_management_sdk.models.user_id_mapping.UserIdMapping.from_dictionary(dictionary.get('userIdMappingInfo')) if dictionary.get('userIdMappingInfo') else None

        # Return an object of this model
        return cls(fallback_user_id_mapping_info,
                   unix_root_sid,
                   user_id_mapping_info)


