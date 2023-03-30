# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class OrgVDCNetwork(object):

    """Implementation of the 'OrgVDCNetwork' model.

    TODO: type description here.


    Attributes:

        name (string): This is the name of the  Org VDC network.
        network_type (string): This is the type of the corresponding network on
            VCenter.
        vcd_uuid (string): This is the uuid of Org VDC network as identified by
            VCD.
        vcenter_moref_uuid (string): This is the moref of the corresponding
            network on VCenter.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "network_type":'networkType',
        "vcd_uuid":'vcdUuid',
        "vcenter_moref_uuid":'vcenterMorefUuid',
    }
    def __init__(self,
                 name=None,
                 network_type=None,
                 vcd_uuid=None,
                 vcenter_moref_uuid=None,
            ):

        """Constructor for the OrgVDCNetwork class"""

        # Initialize members of the class
        self.name = name
        self.network_type = network_type
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
        network_type = dictionary.get('networkType')
        vcd_uuid = dictionary.get('vcdUuid')
        vcenter_moref_uuid = dictionary.get('vcenterMorefUuid')

        # Return an object of this model
        return cls(
            name,
            network_type,
            vcd_uuid,
            vcenter_moref_uuid
)