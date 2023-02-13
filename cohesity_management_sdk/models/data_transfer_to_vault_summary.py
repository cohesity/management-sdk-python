# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.data_transfer_to_vault_per_protection_job

class DataTransferToVaultSummary(object):

    """Implementation of the 'DataTransferToVaultSummary' model.

    Specifies statistics about the transfer of data from this Cohesity
    Cluster to a Vault.

    Attributes:
        data_transfer_per_protection_job (list of
            DataTransferToVaultPerProtectionJob):
            Array of Data Transfer Statistics Per Protection Jobs.
            Specifies the data transfer summary statistics for each Protection
            Job that is transferring data from this Cohesity Cluster to this
            Vault (External Target).
        logical_data_transferred_bytes_during_time_range(int|long): Array
            of Logical Data Transferred Per Day.
            Specifies the logical data transferred from this Cohesity Cluster
            to this Vault during the time period specified using the
            startTimeMsecs and endTimeMsecs parameters.
            For each day in the time period, an array element is returned,
            for example if 7 days are specified, 7 array elements are returned.
            The logical size is when the data is fully hydrated or expanded.
        num_logical_bytes_transferred (long|int): Specifies the total number
            of logical bytes that have been transferred from this Vault
            (External Target) to this Cohesity Cluster. The logical size is
            when the data is fully hydrated or expanded.
        num_physical_bytes_transferred (long|int): Specifies the total number
            of physical bytes that have been transferred from this Vault
            (External Target) to the Cohesity Cluster.
        num_protection_jobs (long|int): Specifies the number of Protection
            Jobs that transfer data to this Vault.
        physical_data_transferred_bytes_during_time_range (list of long|int):
            Array of Physical Data Transferred Per Day.  Specifies the
            physical data transferred from this Vault to the Cohesity Cluster
            during the time period specified using the startTimeMsecs and
            endTimeMsecs parameters. For each day in the time period, an array
            element is returned, for example if 7 days are specified, 7 array
            elements are returned.
        storage_consumed_bytes (int|long): Specifies the storage consumed on
            the Vault as of last day in the specified time range.
        vault_id (int|long): The vault Id associated with the vault.
        vault_name (string): Specifies the name of the Vault (External
            Target).
        vault_type (VaultTypeDataTransferToVaultSummaryEnum): Specifies the
            type of Vault.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_transfer_per_protection_job":'dataTransferPerProtectionJob',
        "logical_data_transferred_bytes_during_time_range":'logicalDataTransferredBytesDuringTimeRange',
        "num_logical_bytes_transferred":'numLogicalBytesTransferred',
        "num_physical_bytes_transferred":'numPhysicalBytesTransferred',
        "num_protection_jobs":'numProtectionJobs',
        "physical_data_transferred_bytes_during_time_range":'physicalDataTransferredBytesDuringTimeRange',
        "storage_consumed_bytes":'storageConsumedBytes',
        "vault_id":'vaultId',
        "vault_name":'vaultName',
        "vault_type":'vaultType'
    }

    def __init__(self,
                 data_transfer_per_protection_job=None,
                 logical_data_transferred_bytes_during_time_range=None,
                 num_logical_bytes_transferred=None,
                 num_physical_bytes_transferred=None,
                 num_protection_jobs=None,
                 physical_data_transferred_bytes_during_time_range=None,
                 storage_consumed_bytes=None,
                 vault_id=None,
                 vault_name=None,
                 vault_type=None):
        """Constructor for the DataTransferToVaultSummary class"""

        # Initialize members of the class
        self.data_transfer_per_protection_job = data_transfer_per_protection_job
        self.logical_data_transferred_bytes_during_time_range = logical_data_transferred_bytes_during_time_range
        self.num_logical_bytes_transferred = num_logical_bytes_transferred
        self.num_physical_bytes_transferred = num_physical_bytes_transferred
        self.num_protection_jobs = num_protection_jobs
        self.physical_data_transferred_bytes_during_time_range = physical_data_transferred_bytes_during_time_range
        self.storage_consumed_bytes = storage_consumed_bytes
        self.vault_id = vault_id
        self.vault_name = vault_name
        self.vault_type = vault_type


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
        data_transfer_per_protection_job = None
        if dictionary.get('dataTransferPerProtectionJob') != None:
            data_transfer_per_protection_job = list()
            for structure in dictionary.get('dataTransferPerProtectionJob'):
                data_transfer_per_protection_job.append(cohesity_management_sdk.models.data_transfer_to_vault_per_protection_job.DataTransferToVaultPerProtectionJob.from_dictionary(structure))
        logical_data_transferred_bytes_during_time_range = dictionary.get('logicalDataTransferredBytesDuringTimeRange')
        num_logical_bytes_transferred = dictionary.get('numLogicalBytesTransferred')
        num_physical_bytes_transferred = dictionary.get('numPhysicalBytesTransferred')
        num_protection_jobs = dictionary.get('numProtectionJobs')
        physical_data_transferred_bytes_during_time_range = dictionary.get('physicalDataTransferredBytesDuringTimeRange')
        storage_consumed_bytes = dictionary.get('storageConsumedBytes')
        vault_id = dictionary.get('vaultId')
        vault_name = dictionary.get('vaultName')
        vault_type = dictionary.get('vaultType')

        # Return an object of this model
        return cls(data_transfer_per_protection_job,
                   logical_data_transferred_bytes_during_time_range,
                   num_logical_bytes_transferred,
                   num_physical_bytes_transferred,
                   num_protection_jobs,
                   physical_data_transferred_bytes_during_time_range,
                   storage_consumed_bytes,
                   vault_id,
                   vault_name,
                   vault_type)


