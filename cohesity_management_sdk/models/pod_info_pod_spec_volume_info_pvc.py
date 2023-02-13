# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PodInfo_PodSpec_VolumeInfo_PVC(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_PVC' model.

    Persistent volume claims are logical volumes that consume persistent
    volumes as backend. The pod just requests for a volume and can be
    unaware of the backend providing the volume.

    Attributes:
        claim_name (string): TODO: Type description here.
        read_only (bool): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "claim_name": 'claimName',
        "read_only": 'readOnly'
    }

    def __init__(self,
                 claim_name=None,
                 read_only=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_PVC class"""

        # Initialize members of the class
        self.claim_name = claim_name
        self.read_only = read_only


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
        claim_name = dictionary.get('claimName', None)
        read_only = dictionary.get('readOnly', None)

        # Return an object of this model
        return cls(claim_name,
                   read_only)


