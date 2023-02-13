# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.oracle_vlan_info

class OracleSbtHostParams(object):

    """Implementation of the 'OracleSbtHostParams' model.

    TODO: Type model description here.

    Attributes:
        sbt_library_path (string): The path of sbt library, This is set only
            when backup type is kSbt.
        view_fs_path (string): Cohesity view path.
        vip_vec (list of string): Vector of Cohesity primary VIPs.
        vlan_info_vec (list of OracleVlanInfo): Vlan information for Cohesity
            cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sbt_library_path":'sbtLibraryPath',
        "view_fs_path":'viewFsPath',
        "vip_vec":'vipVec',
        "vlan_info_vec":'vlanInfoVec'
    }

    def __init__(self,
                 sbt_library_path=None,
                 view_fs_path=None,
                 vip_vec=None,
                 vlan_info_vec=None):
        """Constructor for the OracleSbtHostParams class"""

        # Initialize members of the class
        self.sbt_library_path = sbt_library_path
        self.view_fs_path = view_fs_path
        self.vip_vec = vip_vec
        self.vlan_info_vec = vlan_info_vec


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
        sbt_library_path = dictionary.get('sbtLibraryPath')
        view_fs_path = dictionary.get('viewFsPath')
        vip_vec = dictionary.get('vipVec')
        vlan_info_vec = None
        if dictionary.get('vlanInfoVec') != None:
            vlan_info_vec = list()
            for structure in dictionary.get('vlanInfoVec'):
                vlan_info_vec.append(cohesity_management_sdk.models.oracle_vlan_info.OracleVlanInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(sbt_library_path,
                   view_fs_path,
                   vip_vec,
                   vlan_info_vec)

