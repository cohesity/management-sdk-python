# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class BackupPolicyProtoScheduleEnd(object):

    """Implementation of the 'BackupPolicyProto_ScheduleEnd' model.

    TODO: type model description here.

    Attributes:
        end_after_num_backups (long|int): If specified, the backup job will no
            longer be run after it has been run these many times.
        end_time_usecs (long|int): If specified, the backup job will no longer
            be run after this time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_after_num_backups":'endAfterNumBackups',
        "end_time_usecs":'endTimeUsecs'
    }

    def __init__(self,
                 end_after_num_backups=None,
                 end_time_usecs=None):
        """Constructor for the BackupPolicyProtoScheduleEnd class"""

        # Initialize members of the class
        self.end_after_num_backups = end_after_num_backups
        self.end_time_usecs = end_time_usecs


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
        end_after_num_backups = dictionary.get('endAfterNumBackups')
        end_time_usecs = dictionary.get('endTimeUsecs')

        # Return an object of this model
        return cls(end_after_num_backups,
                   end_time_usecs)


