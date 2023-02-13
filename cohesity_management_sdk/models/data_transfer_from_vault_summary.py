# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.data_transfer_from_vault_per_task

class DataTransferFromVaultSummary(object):

    """Implementation of the 'DataTransferFromVaultSummary' model.

    Specifies summary statistics about the transfer of data from a Vault
    to this Cohesity Cluster.

    Attributes:
        data_transfer_per_task (list of DataTransferFromVaultPerTask): Array
            of Data Transferred Per Task.  Specifies the transfer of data from
            this Vault to this Cohesity Cluster for each clone or recover
            task.
        num_logical_bytes_transferred (long|int): Specifies the total number
            of logical bytes that have been transferred from this Vault
            (External Target) to this Cohesity Cluster. The logical size is
            when the data is fully hydrated or expanded.
        num_physical_bytes_transferred (long|int): Specifies the total number
            of physical bytes that have been transferred from this Vault
            (External Target) to the Cohesity Cluster.
        num_tasks (long|int): Specifies the number of recover or clone tasks
            that have transferred data from this Vault (External Target) to
            this Cohesity Cluster.
        physical_data_transferred_bytes_during_time_range (list of long|int):
            Array of Physical Data Transferred Per Day.  Specifies the
            physical data transferred from this Vault to the Cohesity Cluster
            during the time period specified using the startTimeMsecs and
            endTimeMsecs parameters. For each day in the time period, an array
            element is returned, for example if 7 days are specified, 7 array
            elements are returned.
        vault_name (string): Specifies the name of the Vault (External
            Target).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_transfer_per_task":'dataTransferPerTask',
        "num_logical_bytes_transferred":'numLogicalBytesTransferred',
        "num_physical_bytes_transferred":'numPhysicalBytesTransferred',
        "num_tasks":'numTasks',
        "physical_data_transferred_bytes_during_time_range":'physicalDataTransferredBytesDuringTimeRange',
        "vault_name":'vaultName'
    }

    def __init__(self,
                 data_transfer_per_task=None,
                 num_logical_bytes_transferred=None,
                 num_physical_bytes_transferred=None,
                 num_tasks=None,
                 physical_data_transferred_bytes_during_time_range=None,
                 vault_name=None):
        """Constructor for the DataTransferFromVaultSummary class"""

        # Initialize members of the class
        self.data_transfer_per_task = data_transfer_per_task
        self.num_logical_bytes_transferred = num_logical_bytes_transferred
        self.num_physical_bytes_transferred = num_physical_bytes_transferred
        self.num_tasks = num_tasks
        self.physical_data_transferred_bytes_during_time_range = physical_data_transferred_bytes_during_time_range
        self.vault_name = vault_name


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
        data_transfer_per_task = None
        if dictionary.get('dataTransferPerTask') != None:
            data_transfer_per_task = list()
            for structure in dictionary.get('dataTransferPerTask'):
                data_transfer_per_task.append(cohesity_management_sdk.models.data_transfer_from_vault_per_task.DataTransferFromVaultPerTask.from_dictionary(structure))
        num_logical_bytes_transferred = dictionary.get('numLogicalBytesTransferred')
        num_physical_bytes_transferred = dictionary.get('numPhysicalBytesTransferred')
        num_tasks = dictionary.get('numTasks')
        physical_data_transferred_bytes_during_time_range = dictionary.get('physicalDataTransferredBytesDuringTimeRange')
        vault_name = dictionary.get('vaultName')

        # Return an object of this model
        return cls(data_transfer_per_task,
                   num_logical_bytes_transferred,
                   num_physical_bytes_transferred,
                   num_tasks,
                   physical_data_transferred_bytes_during_time_range,
                   vault_name)


