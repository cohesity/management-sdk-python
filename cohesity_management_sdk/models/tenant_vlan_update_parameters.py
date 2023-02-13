# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantVlanUpdateParameters(object):

    """Implementation of the 'TenantVlanUpdateParameters' model.

    Specifies vlan update details about a tenant.

    Attributes:
        tenant_id (string): Specifies the unique id of the tenant.
        vlan_iface_names (list of string): Specifies the VlanIfaceNames for
            respective tenant, in the format of bond1.200.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tenant_id":'tenantId',
        "vlan_iface_names":'vlanIfaceNames'
    }

    def __init__(self,
                 tenant_id=None,
                 vlan_iface_names=None):
        """Constructor for the TenantVlanUpdateParameters class"""

        # Initialize members of the class
        self.tenant_id = tenant_id
        self.vlan_iface_names = vlan_iface_names


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
        tenant_id = dictionary.get('tenantId')
        vlan_iface_names = dictionary.get('vlanIfaceNames')

        # Return an object of this model
        return cls(tenant_id,
                   vlan_iface_names)


