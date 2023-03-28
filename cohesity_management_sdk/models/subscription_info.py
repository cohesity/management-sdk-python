# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.data_governance_info
import cohesity_management_sdk.models.data_protect_info
import cohesity_management_sdk.models.ransomware_info
import cohesity_management_sdk.models.site_continuity_info


class SubscriptionInfo(object):

    """Implementation of the 'SubscriptionInfo' model.

    Extends this to have Helios, DRaaS and DSaaS.


    Attributes:

        data_governance (DataGovernanceInfo): Specifies whether data governance
            subscription was/is enabled for account.
        data_protect (DataProtectInfo): Specifies whether data protect
            subscription was subscribed for account.
        ransomware (RansomwareInfo): Specifies whether ransomware subscription
            was/is enabled for account.
        site_continuity (SiteContinuityInfo): Specifies whether site continuity
            subscription was/is enabled for account.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "data_governance":'dataGovernance',
        "data_protect":'dataProtect',
        "ransomware":'ransomware',
        "site_continuity":'siteContinuity',
    }
    def __init__(self,
                 data_governance=None,
                 data_protect=None,
                 ransomware=None,
                 site_continuity=None,
            ):

        """Constructor for the SubscriptionInfo class"""

        # Initialize members of the class
        self.data_governance = data_governance
        self.data_protect = data_protect
        self.ransomware = ransomware
        self.site_continuity = site_continuity

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
        data_governance = cohesity_management_sdk.models.data_governance_info.DataGovernanceInfo.from_dictionary(dictionary.get('dataGovernance')) if dictionary.get('dataGovernance') else None
        data_protect = cohesity_management_sdk.models.data_protect_info.DataProtectInfo.from_dictionary(dictionary.get('dataProtect')) if dictionary.get('dataProtect') else None
        ransomware = cohesity_management_sdk.models.ransomware_info.RansomwareInfo.from_dictionary(dictionary.get('ransomware')) if dictionary.get('ransomware') else None
        site_continuity = cohesity_management_sdk.models.site_continuity_info.SiteContinuityInfo.from_dictionary(dictionary.get('siteContinuity')) if dictionary.get('siteContinuity') else None

        # Return an object of this model
        return cls(
            data_governance,
            data_protect,
            ransomware,
            site_continuity
)