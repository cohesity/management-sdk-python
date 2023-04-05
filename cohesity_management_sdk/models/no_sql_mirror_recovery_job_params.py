# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NoSqlMirrorRecoveryJobParams(object):

    """Implementation of the 'NoSqlMirrorRecoveryJobParams' model.

    TODO: type description here.


    Attributes:

        mirror_restore_parent_task_id (long|int): For mirroring, this id
            indicates task id of parent restore task in magneto This Id can be
            used by Imanis scheduler to create unique drectory on Imanis
            Scratch Pad view for storing adapater specific meta-data files (e.g
            error list) that will be passed to adapters for each incremental
            recovery runs
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "mirror_restore_parent_task_id":'mirrorRestoreParentTaskId',
    }
    def __init__(self,
                 mirror_restore_parent_task_id=None,
            ):

        """Constructor for the NoSqlMirrorRecoveryJobParams class"""

        # Initialize members of the class
        self.mirror_restore_parent_task_id = mirror_restore_parent_task_id

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
        mirror_restore_parent_task_id = dictionary.get('mirrorRestoreParentTaskId')

        # Return an object of this model
        return cls(
            mirror_restore_parent_task_id
)