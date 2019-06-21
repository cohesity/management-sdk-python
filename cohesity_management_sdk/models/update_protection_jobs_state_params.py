# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class UpdateProtectionJobsStateParams(object):

    """Implementation of the 'UpdateProtectionJobsStateParams' model.

    Specifies the parameters to perform an action of list of Protection Jobs.

    Attributes:
        action (ActionUpdateProtectionJobsStateParamsEnum): Specifies the
            action to be performed on all the specfied Protection Jobs.
            Specifies the type of action to be performed on Protection Job.
            'kActivate' specifies that Protection Job should be activated.
            'kDeactivate' sepcifies that Protection Job should be deactivated.
            'kPause' specifies that Protection Job should be paused. 'kResume'
            specifies that Protection Job should be resumed.
        job_ids (list of long|int): Specifies a list of Protection Job ids for
            which the state should change.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "action":'action',
        "job_ids":'jobIds'
    }

    def __init__(self,
                 action=None,
                 job_ids=None):
        """Constructor for the UpdateProtectionJobsStateParams class"""

        # Initialize members of the class
        self.action = action
        self.job_ids = job_ids


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
        action = dictionary.get('action')
        job_ids = dictionary.get('jobIds')

        # Return an object of this model
        return cls(action,
                   job_ids)


