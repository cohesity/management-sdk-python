# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pdb_restore_param

class GranularRestoreInfo(object):

    """Implementation of the 'GranularRestoreInfo' model.

    Currently used for pdb restore. Extend the structure for table/datafile
    or any other restore.

    Attributes:
        granularity_type (int): Type of granular restore.
        pdb_restore_params (PDBRestoreParam): PDB Restore parameters.
            This includes information about the list of pdbs to be restored.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "granularity_type": 'granularityType',
        "pdb_restore_params": 'pdbRestoreParams'
    }

    def __init__(self,
                 granularity_type=None,
                 pdb_restore_params=None):
        """Constructor for the GranularRestoreInfo class"""

        # Initialize members of the class
        self.granularity_type = granularity_type
        self.pdb_restore_params = pdb_restore_params


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
        granularity_type = dictionary.get('granularityType')
        pdb_restore_params = cohesity_management_sdk.models.pdb_restore_param.PDBRestoreParam.from_dictionary(dictionary.get('pdbRestoreParams')) if dictionary.get('pdbRestoreParams') else None

        # Return an object of this model
        return cls(granularity_type,
                   pdb_restore_params)


