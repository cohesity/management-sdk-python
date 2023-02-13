# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.bonding_opts

class NetworkParams(object):

    """Implementation of the 'NetworkParams' model.

    TODO: type model description here.

    Attributes:
        bonding_opts (BondingOpts): Bonding Opts
        mtu (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bonding_opts":'bondingOpts',
        "mtu":'mtu'
    }

    def __init__(self,
                 bonding_opts=None,
                 mtu=None):
        """Constructor for the NetworkParams class"""

        # Initialize members of the class
        self.bonding_opts = bonding_opts
        self.mtu = mtu


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
        bonding_opts = cohesity_management_sdk.models.bonding_opts.BondingOpts.from_dictionary(dictionary.get('bondingOpts')) if dictionary.get('bondingOpts') else None
        mtu = dictionary.get('mtu')

        # Return an object of this model
        return cls(bonding_opts,
                   mtu)


