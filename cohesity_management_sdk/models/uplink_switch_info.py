# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class UplinkSwitchInfo(object):

    """Implementation of the 'UplinkSwitchInfo' model.

    Attributes:
        port_id (string): Port ID.
        sys_descr (string): System description.
        sys_name (string): System name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "port_id":'portId',
        "sys_descr":'sysDescr',
        "sys_name":'sysName'
    }

    def __init__(self,
                 port_id=None,
                 sys_descr=None,
                 sys_name=None):
        """Constructor for the UplinkSwitchInfo class"""

        # Initialize members of the class
        self.port_id = port_id
        self.sys_descr = sys_descr
        self.sys_name = sys_name


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
        port_id = dictionary.get('portId')
        sys_descr = dictionary.get('sysDescr')
        sys_name = dictionary.get('sysName')

        # Return an object of this model
        return cls(port_id,
                   sys_descr,
                   sys_name)


