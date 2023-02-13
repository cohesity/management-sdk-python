# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ExchangeDAGProtectionPreference(object):

    """Implementation of the 'ExchangeDAGProtectionPreference' model.

    Specifies the information about the preference order while choosing
    between which database copy of the database which is part of DAG should
    be protected.

    Attributes:
        passive_copy_preference_server_guid_list (list of string): Specifies
            the preference order of the exchange servers from which passive
            database copies should be protected. The preference order is
            descending which indicates that passive database copy in the first
            server in the list gets the highest preference.
        passive_only (bool): Specifies that only passive database copies should
            be protected if this is set to true.
            If this is set to false, both active and passive database copies
            can be protected.
        use_user_specified_passive_preference_order (bool): Specifies to use
            the user specified preference order of exchange servers from which
            the passive database copies should be protected if this is set to
            true.

            Every copy of an Exchange database in a DAG is assigned an
            activation preference number. This number is used by the system as
            part of the passive database activation process.
            If this bool flag is set to false, the reverse order of activation
        is used while choosing between passive copies.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "passive_copy_preference_server_guid_list":'passiveCopyPreferenceServerGuidList',
        "passive_only":'passiveOnly',
        "use_user_specified_passive_preference_order":'useUserSpecifiedPassivePreferenceOrder'
    }

    def __init__(self,
                 passive_copy_preference_server_guid_list=None,
                 passive_only=None,
                 use_user_specified_passive_preference_order=None):
        """Constructor for the ExchangeDAGProtectionPreference class"""

        # Initialize members of the class
        self.passive_copy_preference_server_guid_list = passive_copy_preference_server_guid_list
        self.passive_only = passive_only
        self.use_user_specified_passive_preference_order = use_user_specified_passive_preference_order


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
        passive_copy_preference_server_guid_list = dictionary.get('passiveCopyPreferenceServerGuidList')
        passive_only = dictionary.get('passiveOnly')
        use_user_specified_passive_preference_order = dictionary.get('useUserSpecifiedPassivePreferenceOrder')

        # Return an object of this model
        return cls(passive_copy_preference_server_guid_list,
                   passive_only,
                   use_user_specified_passive_preference_order)


