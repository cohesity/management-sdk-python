# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HardwareInfo(object):

    """Implementation of the 'HardwareInfo' model.

    This struct should match the fields in the hardware JSON file.
    Hardware JSON file serves as cache for hardware info to reduce
    hardware polling which takes time.

    Attributes:
        chassis_model (string): TODO: type description here.
        chassis_serial (string): TODO: type description here.
        chassis_type (string): TODO: type description here.
        cohesity_chassis_serial (string): TODO: type description here.
        cohesity_node_serial (string): TODO: type description here.
        hba_model (string): TODO: type description here.
        ipmi_lan_channel (string): TODO: type description here.
        max_slots (string): TODO: type description here.
        node_model (string): TODO: type description here.
        node_serial (string): TODO: type description here.
        product_model (string): TODO: type description here.
        product_model_type (string): TODO: type description here.
        slot_number (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chassis_model":'chassisModel',
        "chassis_serial":'chassisSerial',
        "chassis_type":'chassisType',
        "cohesity_chassis_serial":'cohesityChassisSerial',
        "cohesity_node_serial":'cohesityNodeSerial',
        "hba_model":'hbaModel',
        "ipmi_lan_channel":'ipmiLanChannel',
        "max_slots":'maxSlots',
        "node_model":'nodeModel',
        "node_serial":'nodeSerial',
        "product_model":'productModel',
        "product_model_type":'productModelType',
        "slot_number":'slotNumber'
    }

    def __init__(self,
                 chassis_model=None,
                 chassis_serial=None,
                 chassis_type=None,
                 cohesity_chassis_serial=None,
                 cohesity_node_serial=None,
                 hba_model=None,
                 ipmi_lan_channel=None,
                 max_slots=None,
                 node_model=None,
                 node_serial=None,
                 product_model=None,
                 product_model_type=None,
                 slot_number=None):
        """Constructor for the HardwareInfo class"""

        # Initialize members of the class
        self.chassis_model = chassis_model
        self.chassis_serial = chassis_serial
        self.chassis_type = chassis_type
        self.cohesity_chassis_serial = cohesity_chassis_serial
        self.cohesity_node_serial = cohesity_node_serial
        self.hba_model = hba_model
        self.ipmi_lan_channel = ipmi_lan_channel
        self.max_slots = max_slots
        self.node_model = node_model
        self.node_serial = node_serial
        self.product_model = product_model
        self.product_model_type = product_model_type
        self.slot_number = slot_number


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
        chassis_model = dictionary.get('chassisModel')
        chassis_serial = dictionary.get('chassisSerial')
        chassis_type = dictionary.get('chassisType')
        cohesity_chassis_serial = dictionary.get('cohesityChassisSerial')
        cohesity_node_serial = dictionary.get('cohesityNodeSerial')
        hba_model = dictionary.get('hbaModel')
        ipmi_lan_channel = dictionary.get('ipmiLanChannel')
        max_slots = dictionary.get('maxSlots')
        node_model = dictionary.get('nodeModel')
        node_serial = dictionary.get('nodeSerial')
        product_model = dictionary.get('productModel')
        product_model_type = dictionary.get('productModelType')
        slot_number = dictionary.get('slotNumber')

        # Return an object of this model
        return cls(chassis_model,
                   chassis_serial,
                   chassis_type,
                   cohesity_chassis_serial,
                   cohesity_node_serial,
                   hba_model,
                   ipmi_lan_channel,
                   max_slots,
                   node_model,
                   node_serial,
                   product_model,
                   product_model_type,
                   slot_number)


