# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.physical_node_configuration

class ExpandPhysicalClusterParameters(object):

    """Implementation of the 'ExpandPhysicalClusterParameters' model.

    Specifies the parameters needed to expand a Cohesity Physical
    Edition Cluster.

    Attributes:
        chassis_serial_to_rack_id_map (int|long): ChassisSerialToRackId Map.
        node_configs (list of PhysicalNodeConfiguration): Specifies the
            configuration details of the Nodes in the Cluster.
        vips (list of string): Specifies the virtual IPs to add to the
            Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chassis_serial_to_rack_id_map":'chassisSerialToRackIdMap',
        "node_configs":'nodeConfigs',
        "vips":'vips'
    }

    def __init__(self,
                 chassis_serial_to_rack_id_map=None,
                 node_configs=None,
                 vips=None):
        """Constructor for the ExpandPhysicalClusterParameters class"""

        # Initialize members of the class
        self.chassis_serial_to_rack_id_map = chassis_serial_to_rack_id_map
        self.node_configs = node_configs
        self.vips = vips


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
        chassis_serial_to_rack_id_map = dictionary.get('chassisSerialToRackIdMap')
        node_configs = None
        if dictionary.get('nodeConfigs') != None:
            node_configs = list()
            for structure in dictionary.get('nodeConfigs'):
                node_configs.append(cohesity_management_sdk.models.physical_node_configuration.PhysicalNodeConfiguration.from_dictionary(structure))
        vips = dictionary.get('vips')

        # Return an object of this model
        return cls(chassis_serial_to_rack_id_map,
                   node_configs,
                   vips)


