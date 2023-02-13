# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ChangeProtectionJobStateParam(object):

    """Implementation of the 'ChangeProtectionJobStateParam' model.

    Specifies if the Run state of a Protection Job should change.

    Attributes:
        pause (bool): If true, the specified Protection Job is paused and no
            new Runs of the Job are started. Any Runs that were executing
            continue to run. If false and the Protection Job was in a paused
            state, the Protection Job resumes and new Runs are started
            according to the schedule defined in the associated Policy.
        pause_reason (int): Specifies the reason of pausing the job so that
            depending on the pause reason, only specific jobs can be resumed.
            All the jobs paused manually by the user will be identified by nil
            PauseReason.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pause":'pause',
        "pause_reason":'pauseReason'
    }

    def __init__(self,
                 pause=None,
                 pause_reason=None):
        """Constructor for the ChangeProtectionJobStateParam class"""

        # Initialize members of the class
        self.pause = pause
        self.pause_reason = pause_reason


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
        pause = dictionary.get('pause')
        pause_reason = dictionary.get('pauseReason')

        # Return an object of this model
        return cls(pause,
                   pause_reason)


