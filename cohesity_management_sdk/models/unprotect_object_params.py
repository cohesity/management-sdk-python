# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UnprotectObjectParams(object):

    """Implementation of the 'UnprotectObjectParams' model.

    Specifies the parameters to unprotect an object.

    Attributes:
        delete_snapshots (bool): Specifies whether to delete the snapshots of
            the Protection Object.
        protection_source_id (long|int): Specifies the id of the Protection
            Source to be unprotected.
        rpo_policy_id (string): Specifies the id of the Rpo Policy from which
            to unprotect the object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protection_source_id":'protectionSourceId',
        "rpo_policy_id":'rpoPolicyId',
        "delete_snapshots":'deleteSnapshots'
    }

    def __init__(self,
                 protection_source_id=None,
                 rpo_policy_id=None,
                 delete_snapshots=None):
        """Constructor for the UnprotectObjectParams class"""

        # Initialize members of the class
        self.delete_snapshots = delete_snapshots
        self.protection_source_id = protection_source_id
        self.rpo_policy_id = rpo_policy_id


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
        protection_source_id = dictionary.get('protectionSourceId')
        rpo_policy_id = dictionary.get('rpoPolicyId')
        delete_snapshots = dictionary.get('deleteSnapshots')

        # Return an object of this model
        return cls(protection_source_id,
                   rpo_policy_id,
                   delete_snapshots)


