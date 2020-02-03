# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class CreateBondParameters(object):

    """Implementation of the 'CreateBondParameters' model.

    Specifies the parameters needed to create a bond.

    Attributes:
        bonding_mode (BondingModeEnum): Specifies the bonding mode to use for
            this bond. If not specified, this value will default to
            'kActiveBackup'. 'kActiveBackup' indicates active backup bonding
            mode. 'k802_3ad' indicates 802.3ad bonding mode.
        name (string): Specifies a unique name to identify the bond being
            created.
        slaves (list of string): Specifies the names of the slaves of this
            bond.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "slaves":'slaves',
        "bonding_mode":'bondingMode'
    }

    def __init__(self,
                 name=None,
                 slaves=None,
                 bonding_mode=None):
        """Constructor for the CreateBondParameters class"""

        # Initialize members of the class
        self.bonding_mode = bonding_mode
        self.name = name
        self.slaves = slaves


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
        name = dictionary.get('name')
        slaves = dictionary.get('slaves')
        bonding_mode = dictionary.get('bondingMode')

        # Return an object of this model
        return cls(name,
                   slaves,
                   bonding_mode)


