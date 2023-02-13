# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VlanParams(object):

    """Implementation of the 'VlanParams' model.

    Contains vlan params associated with the backup/restore operation.

    Attributes:
        disable_vlan (bool): If this is set to true, then even if VLANs are
            configured on the system, the partition VIPs will be used for the
            restore.
        interface_name (string): Interface group to use for restore. If this
            is not specified, primary interface group for the cluster will be
            used.
        vlan_id (int): If this is set, then the Cohesity host name or the IP
            address associated with this vlan is used for mounting Cohesity's
            view on the remote host.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disable_vlan":'disableVlan',
        "interface_name":'interfaceName',
        "vlan_id": 'vlanId'
    }

    def __init__(self,
                 disable_vlan=None,
                 interface_name=None,
                 vlan_id=None):
        """Constructor for the VlanParams class"""

        # Initialize members of the class
        self.disable_vlan = disable_vlan
        self.interface_name = interface_name
        self.vlan_id = vlan_id


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
        vlan_id = dictionary.get('vlanId')

        # Return an object of this model
        return cls(disable_vlan,
                   interface_name,
                   vlan_id)


