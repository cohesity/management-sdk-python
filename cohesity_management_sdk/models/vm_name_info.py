# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VmNameInfo(object):

    """Implementation of the 'VmNameInfo' model.

    Struct containing vm-name and ui-name (to be displayed on the UI to get
    number of replicas as input) as members.

    Attributes:
        ui_name (string): UI-name. To be displayed on the UI.
        vm_name (string): Vm-name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ui_name": 'uiName',
        "vm_name": 'vmName'
    }

    def __init__(self,
                 ui_name=None,
                 vm_name=None):
        """Constructor for the VmNameInfo class"""

        # Initialize members of the class
        self.ui_name = ui_name
        self.vm_name = vm_name


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
        ui_name = dictionary.get('uiName', None)
        vm_name = dictionary.get('vmName', None)

        # Return an object of this model
        return cls(ui_name,
                   vm_name)


