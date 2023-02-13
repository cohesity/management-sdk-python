# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class BondingOpts(object):

    """Implementation of the 'BondingOpts' model.

    Bonding Opts

    Attributes:
        lacp_rate (string): TODO: type description here.
        mode (string): TODO: type description here.
        xmit_hash_policy (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "lacp_rate":'lacpRate',
        "mode":'mode',
        "xmit_hash_policy":'xmitHashPolicy'
    }

    def __init__(self,
                 lacp_rate=None,
                 mode=None,
                 xmit_hash_policy=None):
        """Constructor for the BondingOpts class"""

        # Initialize members of the class
        self.lacp_rate = lacp_rate
        self.mode = mode
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
        lacp_rate = dictionary.get('lacpRate')
        mode = dictionary.get('mode')
        xmit_hash_policy = dictionary.get('xmitHashPolicy')

        # Return an object of this model
        return cls(lacp_rate,
                   mode,
                   xmit_hash_policy)


