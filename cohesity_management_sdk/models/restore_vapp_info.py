# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RestoreVappInfo(object):

    """Implementation of the 'RestoreVappInfo' model.

    TODO: type description here.


    Attributes:

        vapp_id (string): Id of the vApp.
        vapp_name (string): Name of the vApp.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "vapp_id":'vappId',
        "vapp_name":'vappName',
    }
    def __init__(self,
                 vapp_id=None,
                 vapp_name=None,
            ):

        """Constructor for the RestoreVappInfo class"""

        # Initialize members of the class
        self.vapp_id = vapp_id
        self.vapp_name = vapp_name

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
        vapp_id = dictionary.get('vappId')
        vapp_name = dictionary.get('vappName')

        # Return an object of this model
        return cls(
            vapp_id,
            vapp_name
)