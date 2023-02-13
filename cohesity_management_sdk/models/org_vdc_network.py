# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class OrgVdcNetwork(object):

    """Implementation of the 'OrgVdcNetwork' model.

    Specifies the parameters of an Org VDC network.

    Attributes:
        name (string): Specifies the name of the Org VDC Network.
        vcd_uuid (string): Specifies the UUID as identified by the VCD.
        vcenter_uuid (string): Specifies the UUID of the corresponding network
            on the vCenter.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "vcd_uuid":'vcdUuid',
        "vcenter_uuid":'vcenterUuid'
    }

    def __init__(self,
                 name=None,
                 vcd_uuid=None,
                 vcenter_uuid=None):
        """Constructor for the OrgVdcNetwork class"""

        # Initialize members of the class
        self.name = name
        self.vcd_uuid = vcd_uuid
        self.vcenter_uuid = vcenter_uuid


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
        vcenter_uuid = dictionary.get('vcenterUuid')

        # Return an object of this model
        return cls(name,
                   vcd_uuid,
                   vcenter_uuid)


