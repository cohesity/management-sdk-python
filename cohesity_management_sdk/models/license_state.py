# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class LicenseState(object):

    """Implementation of the 'LicenseState' model.

    Specifies the state of licensing workflow.

    Attributes:
        failed_attempts (long|int): Specifies no of failed attempts at
            claiming the license server
        state (StateLicenseStateEnum): Specifies the current state of
            licensing workflow. LicenseStateType specifies the licenseState
            type. 'kInProgressNewCluster' indicates licensing server claim is
            in progress for 'New' Cluster. 'kInProgressOldCluster' indicates
            licensing server claim is in progress for 'Old' Cluster.
            'kClaimed' indicates licensing server is claimed. 'kSkipped'
            indicates licensing workflow has been skipped. 'kStarted'
            indicates licensing UI workflow has started.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "failed_attempts":'failedAttempts',
        "state":'state'
    }

    def __init__(self,
                 failed_attempts=None,
                 state=None):
        """Constructor for the LicenseState class"""

        # Initialize members of the class
        self.failed_attempts = failed_attempts
        self.state = state


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
        failed_attempts = dictionary.get('failedAttempts')
        state = dictionary.get('state')

        # Return an object of this model
        return cls(failed_attempts,
                   state)


