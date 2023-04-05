# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AirgapConfig(object):

    """Implementation of the 'AirgapConfig' model.

    Structure to hold Airgap Configuration


    Attributes:

        airgap_status (AirgapStatusEnum): Airgap Status 'kEnable' indicates
            that Airgap is enbaled 'kDisable' indicates that Airgap is disabled
        exception_profiles (list of string): Exception firewall profile names
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "airgap_status":'airgapStatus',
        "exception_profiles":'exceptionProfiles',
    }
    def __init__(self,
                 airgap_status=None,
                 exception_profiles=None,
            ):

        """Constructor for the AirgapConfig class"""

        # Initialize members of the class
        self.airgap_status = airgap_status
        self.exception_profiles = exception_profiles

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
        airgap_status = dictionary.get('airgapStatus')
        exception_profiles = dictionary.get("exceptionProfiles")

        # Return an object of this model
        return cls(
            airgap_status,
            exception_profiles
)