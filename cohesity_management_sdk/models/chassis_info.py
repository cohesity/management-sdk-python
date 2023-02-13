# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ChassisInfo(object):

    """Implementation of the 'ChassisInfo' model.

    ChassisInfo is the struct for the Chassis.

    Attributes:
        chassis_id (long|int): ChassisId is a unique id assigned to the
            chassis.
        chassis_name (string): ChassisName is the name of the chassis. This
            could be the chassis serial number by default.
        chassis_serial (string): Chassis serial.
        location (string): Location is the location of the chassis within the
            rack.
        rack_id (long|int): Rack is the rack within which this chassis lives.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chassis_id":'chassisId',
        "chassis_name":'chassisName',
        "chassis_serial":'chassisSerial',
        "location":'location',
        "rack_id":'rackId'
    }

    def __init__(self,
                 chassis_id=None,
                 chassis_name=None,
                 chassis_serial=None,
                 location=None,
                 rack_id=None):
        """Constructor for the ChassisInfo class"""

        # Initialize members of the class
        self.chassis_id = chassis_id
        self.chassis_name = chassis_name
        self.chassis_serial = chassis_serial
        self.location = location
        self.rack_id = rack_id


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
        chassis_id = dictionary.get('chassisId')
        chassis_name = dictionary.get('chassisName')
        chassis_serial = dictionary.get('chassisSerial')
        location = dictionary.get('location')
        rack_id = dictionary.get('rackId')

        # Return an object of this model
        return cls(chassis_id,
                   chassis_name,
                   chassis_serial,
                   location,
                   rack_id)


