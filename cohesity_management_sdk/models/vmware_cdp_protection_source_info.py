# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cdp_io_filter_state

class VMwareCdpProtectionSourceInfo(object):

    """Implementation of the 'VMwareCdpProtectionSourceInfo' model.

    Specifies the details about the Continuous Data Protection (CDP) info of a
    VMware Protection Source.

    Attributes:
        io_filter_state (CdpIoFilterState): Specifies the current state of the
            CDP IO Filter.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "io_filter_state":'ioFilterState'
    }

    def __init__(self,
                 io_filter_state=None):
        """Constructor for the VMwareCdpProtectionSourceInfo class"""

        # Initialize members of the class
        self.io_filter_state = io_filter_state


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
        io_filter_state = cohesity_management_sdk.models.cdp_io_filter_state.CdpIoFilterState.from_dictionary(dictionary.get('ioFilterState')) if dictionary.get('ioFilterState') else None

        # Return an object of this model
        return cls(io_filter_state)


