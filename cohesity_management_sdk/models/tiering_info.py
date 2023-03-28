# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TieringInfo(object):

    """Implementation of the 'TieringInfo' model.

    TODO: type description here.


    Attributes:

        backend_tiering (bool): Specifies whether back-end tiering is enabled.
        frontend_tiering (bool): Specifies whether Front End Tiering Enabled
        max_retention (long|int): Specified the max retention for backup policy
            creation.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "backend_tiering":'backendTiering',
        "frontend_tiering":'frontendTiering',
        "max_retention":'maxRetention',
    }
    def __init__(self,
                 backend_tiering=None,
                 frontend_tiering=None,
                 max_retention=None,
            ):

        """Constructor for the TieringInfo class"""

        # Initialize members of the class
        self.backend_tiering = backend_tiering
        self.frontend_tiering = frontend_tiering
        self.max_retention = max_retention

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
        backend_tiering = dictionary.get('backendTiering')
        frontend_tiering = dictionary.get('frontendTiering')
        max_retention = dictionary.get('maxRetention')

        # Return an object of this model
        return cls(
            backend_tiering,
            frontend_tiering,
            max_retention
)