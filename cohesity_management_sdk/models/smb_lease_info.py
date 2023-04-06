# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SmbLeaseInfo(object):

    """Implementation of the 'SmbLeaseInfo' model.

    TODO: type description here.


    Attributes:

        is_breaking (bool): Whether lease break is in progress
        lease_break_type (list of string): Lease type that is attempted to
            being broken.
        lease_tye (list of string): Lease type granted for open.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_breaking":'isBreaking',
        "lease_break_type":'leaseBreakType',
        "lease_tye":'leaseTye',
    }
    def __init__(self,
                 is_breaking=None,
                 lease_break_type=None,
                 lease_tye=None,
            ):

        """Constructor for the SmbLeaseInfo class"""

        # Initialize members of the class
        self.is_breaking = is_breaking
        self.lease_break_type = lease_break_type
        self.lease_tye = lease_tye

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
        is_breaking = dictionary.get('isBreaking')
        lease_break_type = dictionary.get("leaseBreakType")
        lease_tye = dictionary.get("leaseTye")

        # Return an object of this model
        return cls(
            is_breaking,
            lease_break_type,
            lease_tye
)