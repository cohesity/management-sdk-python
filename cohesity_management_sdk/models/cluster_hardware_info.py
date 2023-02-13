# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ClusterHardwareInfo(object):

    """Implementation of the 'ClusterHardwareInfo' model.

    Specifies a hardware type for motherboard of the Nodes
    that make up this Cohesity Cluster such as S2600WB for Ivy Bridge
    or S2600TP for Haswell.

    Attributes:
        hardware_models (list of string): TODO: type description here.
        hardware_vendors (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hardware_models":'hardwareModels',
        "hardware_vendors":'hardwareVendors'
    }

    def __init__(self,
                 hardware_models=None,
                 hardware_vendors=None):
        """Constructor for the ClusterHardwareInfo class"""

        # Initialize members of the class
        self.hardware_models = hardware_models
        self.hardware_vendors = hardware_vendors


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
        hardware_models = dictionary.get('hardwareModels')
        hardware_vendors = dictionary.get('hardwareVendors')

        # Return an object of this model
        return cls(hardware_models,
                   hardware_vendors)


