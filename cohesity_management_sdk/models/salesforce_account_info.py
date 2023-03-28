# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SalesforceAccountInfo(object):

    """Implementation of the 'SalesforceAccountInfo' model.

    Salesforce Account Information of a Helios user.


    Attributes:

        account_id (string): Specifies the Account Id assigned by Salesforce.
        helios_access_grant_status (string): Specifies the status of helios
            access.
        is_d_gaa_s_user (bool): Specifies whether user is a DGaaS licensed
            user.
        is_d_maa_s_user (bool): Specifies whether user is a DMaaS licensed
            user.
        is_draa_s_user (bool): Specifies whether user is a DRaaS licensed user.
        is_r_paa_s_user (bool): Specifies whether user is a RPaaS licensed
            user.
        is_sales_user (bool): Specifies whether user is a Sales person from
            Cohesity.
        is_support_user (bool): Specifies whether user is a support person from
            Cohesity.
        user_id (string): Specifies the User Id assigned by Salesforce.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "account_id":'accountId',
        "helios_access_grant_status":'heliosAccessGrantStatus',
        "is_d_gaa_s_user":'isDGaaSUser',
        "is_d_maa_s_user":'isDMaaSUser',
        "is_draa_s_user":'isDRaaSUser',
        "is_r_paa_s_user":'isRPaaSUser',
        "is_sales_user":'isSalesUser',
        "is_support_user":'isSupportUser',
        "user_id":'userId',
    }
    def __init__(self,
                 account_id=None,
                 helios_access_grant_status=None,
                 is_d_gaa_s_user=None,
                 is_d_maa_s_user=None,
                 is_draa_s_user=None,
                 is_r_paa_s_user=None,
                 is_sales_user=None,
                 is_support_user=None,
                 user_id=None,
            ):

        """Constructor for the SalesforceAccountInfo class"""

        # Initialize members of the class
        self.account_id = account_id
        self.helios_access_grant_status = helios_access_grant_status
        self.is_d_gaa_s_user = is_d_gaa_s_user
        self.is_d_maa_s_user = is_d_maa_s_user
        self.is_draa_s_user = is_draa_s_user
        self.is_r_paa_s_user = is_r_paa_s_user
        self.is_sales_user = is_sales_user
        self.is_support_user = is_support_user
        self.user_id = user_id

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
        account_id = dictionary.get('accountId')
        helios_access_grant_status = dictionary.get('heliosAccessGrantStatus')
        is_d_gaa_s_user = dictionary.get('isDGaaSUser')
        is_d_maa_s_user = dictionary.get('isDMaaSUser')
        is_draa_s_user = dictionary.get('isDRaaSUser')
        is_r_paa_s_user = dictionary.get('isRPaaSUser')
        is_sales_user = dictionary.get('isSalesUser')
        is_support_user = dictionary.get('isSupportUser')
        user_id = dictionary.get('userId')

        # Return an object of this model
        return cls(
            account_id,
            helios_access_grant_status,
            is_d_gaa_s_user,
            is_d_maa_s_user,
            is_draa_s_user,
            is_r_paa_s_user,
            is_sales_user,
            is_support_user,
            user_id
)