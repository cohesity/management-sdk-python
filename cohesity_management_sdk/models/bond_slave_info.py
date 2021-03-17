# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.
import cohesity_management_sdk.models.uplink_switch_info

class BondSlaveInfo(object):

    """Implementation of the 'BondSlaveInfo' model.

    Specifies the AMQP target config.

    Attributes:
        link_state (string): Bond slave link state.
        mac_addr (string): Mac address of the bond slave interface.
        name (string): Bond slave name.
        slot (string): Bond slaves slot info.
        speed (string): Bond slave Speed.
        uplink_switch_info (UplinkSwitchInfo): Bond slave uplink switch info.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "link_state": 'linkState',
        "mac_addr": 'macAddr',
        "name":'name',
        "slot":'slot',
        "speed":'speed',
        "uplink_switch_info":'uplinkSwitchInfo'
    }

    def __init__(self,
                 link_state=None,
                 mac_addr=None,
                 name=None,
                 slot=None,
                 speed=None,
                 uplink_switch_info=None
                 ):
        """Constructor for the BondSlaveInfo class"""

        # Initialize members of the class
        self.link_state = link_state
        self.mac_addr = mac_addr
        self.name = name
        self.slot = slot
        self.speed = speed
        self.uplink_switch_info = uplink_switch_info

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
        link_state = dictionary.get('linkState')
        mac_addr = dictionary.get('macAddr')
        name = dictionary.get('name')
        slot = dictionary.get('slot')
        speed = dictionary.get('speed')
        uplink_switch_info = cohesity_management_sdk.models.uplink_switch_info.UplinkSwitchInfo.from_dictionary(dictionary.get('uplinkSwitchInfo')) if dictionary.get('uplinkSwitchInfo') else None

        # Return an object of this model
        return cls(link_state,
                   mac_addr,
                   name,
                   slot,
                   speed,
                   uplink_switch_info)


