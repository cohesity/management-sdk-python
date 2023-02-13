# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.data_transfer_to_vault_summary

class DataTransferToVaultsSummaryResponse(object):

    """Implementation of the 'DataTransferToVaultsSummaryResponse' model.

    Provides summary statistics about the transfer of data from this
    Cohesity Cluster to Vaults (External Targets).

    Attributes:
        data_transfer_summary (list of DataTransferToVaultSummary): Array of
            Summary Data Transfer Statistics.
            Specifies summary statistics about the transfer of data from
            Vaults to the Cohesity Cluster.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_transfer_summary":'dataTransferSummary'
    }

    def __init__(self,
                 data_transfer_summary=None):
        """Constructor for the DataTransferToVaultsSummaryResponse class"""

        # Initialize members of the class
        self.data_transfer_summary = data_transfer_summary


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
        data_transfer_summary = None
        if dictionary.get('dataTransferSummary') != None:
            data_transfer_summary = list()
            for structure in dictionary.get('dataTransferSummary'):
                data_transfer_summary.append(cohesity_management_sdk.models.data_transfer_to_vault_summary.DataTransferToVaultSummary.from_dictionary(structure))

        # Return an object of this model
        return cls(data_transfer_summary)


