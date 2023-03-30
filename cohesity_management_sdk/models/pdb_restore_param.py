# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cdb_entity_info
import cohesity_management_sdk.models.pdb_restore_param_rename_pdb_map_entry


class PDBRestoreParam(object):

    """Implementation of the 'PDBRestoreParam' model.

    TODO: type description here.


    Attributes:

        drop_pdbs_if_exists (bool): During the restore workflow, drop the pdb
            if the same name pdb exists.
        existing_cdb (bool): Restore given list of pdbs to an existing CDB.
        pdb_entity_info_vec (CDBEntityInfo): List of PDB's to restore.
        rename_pdb_map (list of PDBRestoreParam_RenamePdbMapEntry): If rename
            pdb is provided, list of new names for the pdb.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "drop_pdbs_if_exists":'dropPdbsIfExists',
        "existing_cdb":'existingCdb',
        "pdb_entity_info_vec":'pdbEntityInfoVec',
        "rename_pdb_map":'renamePdbMap',
    }
    def __init__(self,
                 drop_pdbs_if_exists=None,
                 existing_cdb=None,
                 pdb_entity_info_vec=None,
                 rename_pdb_map=None,
            ):

        """Constructor for the PDBRestoreParam class"""

        # Initialize members of the class
        self.drop_pdbs_if_exists = drop_pdbs_if_exists
        self.existing_cdb = existing_cdb
        self.pdb_entity_info_vec = pdb_entity_info_vec
        self.rename_pdb_map = rename_pdb_map

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
        drop_pdbs_if_exists = dictionary.get('dropPdbsIfExists')
        existing_cdb = dictionary.get('existingCdb')
        pdb_entity_info_vec = cohesity_management_sdk.models.cdb_entity_info.CDBEntityInfo.from_dictionary(dictionary.get('pdbEntityInfoVec')) if dictionary.get('pdbEntityInfoVec') else None
        rename_pdb_map = None
        if dictionary.get('renamePdbMap') != None:
            rename_pdb_map = list()
            for structure in dictionary.get('renamePdbMap'):
                rename_pdb_map.append(cohesity_management_sdk.models.pdb_restore_param_rename_pdb_map_entry.PDBRestoreParam_RenamePdbMapEntry.from_dictionary(structure))

        # Return an object of this model
        return cls(
            drop_pdbs_if_exists,
            existing_cdb,
            pdb_entity_info_vec,
            rename_pdb_map
)