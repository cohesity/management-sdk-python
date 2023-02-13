# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DataTransferFromVaultPerTask(object):

    """Implementation of the 'DataTransferFromVaultPerTask' model.

    Specifies statistics about the transfer of data from a Vault
    (External Target) to this Cohesity Cluster for a recover or
    clone task.

    Attributes:
        num_logical_bytes_transferred (long|int): Specifies the total number
            of logical bytes that are transferred from this Vault to the
            Cohesity Cluster for this task. The logical size is when the data
            is fully hydrated or expanded.
        num_physical_bytes_transferred (long|int): Specifies the total number
            of physical bytes that are transferred from this Vault to the
            Cohesity Cluster for this task.
        task_name (string): Specifies the task name.
        task_type (string): Specifies the task type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_logical_bytes_transferred":'numLogicalBytesTransferred',
        "num_physical_bytes_transferred":'numPhysicalBytesTransferred',
        "task_name":'taskName',
        "task_type":'taskType'
    }

    def __init__(self,
                 num_logical_bytes_transferred=None,
                 num_physical_bytes_transferred=None,
                 task_name=None,
                 task_type=None):
        """Constructor for the DataTransferFromVaultPerTask class"""

        # Initialize members of the class
        self.num_logical_bytes_transferred = num_logical_bytes_transferred
        self.num_physical_bytes_transferred = num_physical_bytes_transferred
        self.task_name = task_name
        self.task_type = task_type


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
        num_logical_bytes_transferred = dictionary.get('numLogicalBytesTransferred')
        num_physical_bytes_transferred = dictionary.get('numPhysicalBytesTransferred')
        task_name = dictionary.get('taskName')
        task_type = dictionary.get('taskType')

        # Return an object of this model
        return cls(num_logical_bytes_transferred,
                   num_physical_bytes_transferred,
                   task_name,
                   task_type)


