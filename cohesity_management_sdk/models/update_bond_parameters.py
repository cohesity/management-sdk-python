# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpdateBondParameters(object):

    """Implementation of the 'UpdateBondParameters' model.

    Specifies the parameters needed to modify the bonding mode of a bond.

    Attributes:
        bonding_mode (BondingModeUpdateBondParametersEnum): Specifies the new
            bonding mode. 'kActiveBackup' indicates active backup bonding
            mode. 'k802_3ad' indicates 802.3ad bonding mode.
        lacp_rate (string): Specifies the LACP rate. If not specified, This
            value will default to 0 (slow).
        name (string): Specifies the name of the bond being updated.
        xmit_hash_policy (string): Specifies the xmit hash policy. If not
            specified, This value will default to 1 (layer3+4).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bonding_mode":'bondingMode',
        "name":'name',
        "lacp_rate":'lacpRate',
        "xmit_hash_policy":'xmitHashPolicy'
    }

    def __init__(self,
                 bonding_mode=None,
                 name=None,
                 lacp_rate=None,
                 xmit_hash_policy=None):
        """Constructor for the UpdateBondParameters class"""

        # Initialize members of the class
        self.bonding_mode = bonding_mode
        self.lacp_rate = lacp_rate
        self.name = name
        self.xmit_hash_policy = xmit_hash_policy


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
        bonding_mode = dictionary.get('bondingMode')
        name = dictionary.get('name')
        lacp_rate = dictionary.get('lacpRate')
        xmit_hash_policy = dictionary.get('xmitHashPolicy')

        # Return an object of this model
        return cls(bonding_mode,
                   name,
                   lacp_rate,
                   xmit_hash_policy)


