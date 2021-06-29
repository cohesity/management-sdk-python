# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

class OrgVDCNetwork(object):

    """Implementation of the 'OrgVDCNetwork' model.

    Attributes:
        name (string): This is the name of the  Org VDC network.
        vcd_uuid (string): This is the uuid of Org VDC network as identified
            by VCD.
        vcenter_moref_uuid (string): This is the uuid of the corresponding
            network on VCenter.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "vcd_uuid":'vcdUuid',
        "vcenter_moref_uuid":'vcenterMorefUuid'
    }

    def __init__(self,
                 name=None,
                 vcd_uuid=None,
                 vcenter_moref_uuid=None):
        """Constructor for the OrgVDCNetwork class"""

        # Initialize members of the class
        self.name = name
        self.vcd_uuid = vcd_uuid
        self.vcenter_moref_uuid = vcenter_moref_uuid


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
        vcd_uuid = dictionary.get('vcdUuid')
        vcenter_moref_uuid = dictionary.get('vcenterMorefUuid')

        # Return an object of this model
        return cls(name,
                   vcd_uuid,
                   vcenter_moref_uuid)


