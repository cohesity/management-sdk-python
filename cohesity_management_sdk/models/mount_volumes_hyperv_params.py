# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.credentials


class MountVolumesHyperVParams(object):

    """Implementation of the 'MountVolumesHyperVParams' model.

    TODO: type description here.


    Attributes:

        bring_disks_online (bool): Optional setting which will determine if the
            volumes need to be onlined within the target environment after
            attaching the disks. NOTE: If this is set to true, then
            target_entity_credentials must be specified and HyperV Integration
            Services must be installed on the VM.
        target_entity_credentials (Credentials): Credentials to access the
            target entity such as a VM. This is not required if
            bring_disks_online is set to false.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "bring_disks_online":'bringDisksOnline',
        "target_entity_credentials":'targetEntityCredentials',
    }
    def __init__(self,
                 bring_disks_online=None,
                 target_entity_credentials=None,
            ):

        """Constructor for the MountVolumesHyperVParams class"""

        # Initialize members of the class
        self.bring_disks_online = bring_disks_online
        self.target_entity_credentials = target_entity_credentials

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
        bring_disks_online = dictionary.get('bringDisksOnline')
        target_entity_credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('targetEntityCredentials')) if dictionary.get('targetEntityCredentials') else None

        # Return an object of this model
        return cls(
            bring_disks_online,
            target_entity_credentials
)