# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class OracleDBConfigRedoLogGroupConf(object):

    """Implementation of the 'OracleDBConfig_RedoLogGroupConf' model.

    GROUP1 : {DST1/CH1.log, DST2/CH1.log}
    GROUP2 : {DST1/CH2.log, DST2/CH2.log}
    GROUP3 : {DST1/CH3.log, DST2/CH3.log}

    Attributes:
        group_member_vec (list of string): List of members of this redo log
            group.
        member_prefix (string): Log member name prefix.
        num_groups (int): Number of redo log groups.
        size_mb (int): Size of the member in MB.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group_member_vec":'groupMemberVec',
        "member_prefix":'memberPrefix',
        "num_groups":'numGroups',
        "size_mb":'sizeMb'
    }

    def __init__(self,
                 group_member_vec=None,
                 member_prefix=None,
                 num_groups=None,
                 size_mb=None):
        """Constructor for the OracleDBConfigRedoLogGroupConf class"""

        # Initialize members of the class
        self.group_member_vec = group_member_vec
        self.member_prefix = member_prefix
        self.num_groups = num_groups
        self.size_mb = size_mb


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
        group_member_vec = dictionary.get('groupMemberVec')
        member_prefix = dictionary.get('memberPrefix')
        num_groups = dictionary.get('numGroups')
        size_mb = dictionary.get('sizeMb')

        # Return an object of this model
        return cls(group_member_vec,
                   member_prefix,
                   num_groups,
                   size_mb)


