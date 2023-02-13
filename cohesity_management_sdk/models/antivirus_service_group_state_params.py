# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AntivirusServiceGroupStateParams(object):

    """Implementation of the 'AntivirusServiceGroupStateParams' model.

    Specifies the configuration settings to change the state of an Antivirus
    service group.

    Attributes:
        enable (bool): Specifies the enable flag to enable the Antivirus
            service group.
        id (long|int): Specifies the Id of the Antivirus service group.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enable":'enable',
        "id":'id'
    }

    def __init__(self,
                 enable=None,
                 id=None):
        """Constructor for the AntivirusServiceGroupStateParams class"""

        # Initialize members of the class
        self.enable = enable
        self.id = id


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
        enable = dictionary.get('enable')
        id = dictionary.get('id')

        # Return an object of this model
        return cls(enable,
                   id)


