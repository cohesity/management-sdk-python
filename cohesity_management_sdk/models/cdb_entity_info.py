# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pdb_entity_info

class CDBEntityInfo(object):

    """Implementation of the 'CDBEntityInfo' model.

    Attributes:
        pdb_entity_info_vec (list of PDBEntityInfo): Repeated field of pdb
            entity information for a given CDB. This structure is used to
            retrieve the information about all the pdbs inside a given db.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pdb_entity_info_vec":'pdbEntityInfoVec'
    }

    def __init__(self,
                 pdb_entity_info_vec=None):
        """Constructor for the CDBEntityInfo class"""

        # Initialize members of the class
        self.pdb_entity_info_vec = pdb_entity_info_vec


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
        pdb_entity_info_vec = None
        if dictionary.get('pdbEntityInfoVec') != None:
            pdb_entity_info_vec = list()
            for structure in dictionary.get('pdbEntityInfoVec'):
                pdb_entity_info_vec.append(cohesity_management_sdk.models.pdb_entity_info.PDBEntityInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(pdb_entity_info_vec)


