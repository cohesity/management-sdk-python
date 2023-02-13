# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VlanParameters(object):

    """Implementation of the 'VlanParameters' model.

    Specifies VLAN parameters for the restore operation.

    Attributes:
        disable_vlan (bool): Specifies whether to use the VIPs even when VLANs
            are configured on the Cluster. If configured, VLAN IP addresses
            are used by default. If VLANs are not configured, this flag is
            ignored. Set this flag to true to force using the partition VIPs
            when VLANs are configured on the Cluster.
        interface_name (string): Specifies the physical interface group name
            to use for mounting Cohesity's view on the remote host. If
            specified, Cohesity hostname or the IP address on this VLAN is
            used.
        vlan (int): Specifies the VLAN to use for mounting Cohesity's view on
            the remote host. If specified, Cohesity hostname or the IP address
            on this VLAN is used.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disable_vlan":'disableVlan',
        "interface_name":'interfaceName',
        "vlan":'vlan'
    }

    def __init__(self,
                 disable_vlan=None,
                 interface_name=None,
                 vlan=None):
        """Constructor for the VlanParameters class"""

        # Initialize members of the class
        self.disable_vlan = disable_vlan
        self.interface_name = interface_name
        self.vlan = vlan


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
        disable_vlan = dictionary.get('disableVlan')
        interface_name = dictionary.get('interfaceName')
        vlan = dictionary.get('vlan')

        # Return an object of this model
        return cls(disable_vlan,
                   interface_name,
                   vlan)


