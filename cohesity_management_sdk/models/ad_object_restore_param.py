# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.credentials

class ADObjectRestoreParam(object):

    """Implementation of the 'ADObjectRestoreParam' model.

    TODO: type model description here.

    Attributes:
        credentials (Credentials): Specifies credentials to access a target
            source.
        guid_vec (list of string): Array of AD object guids to restore either
            from recycle bin or from AD snapshot. The guid should not exist in
            production AD. If it exits, then kDuplicate error is output in
            status.
        option_flags (int): Restore option flags of type
            ADObjectRestoreOptionFlags.
        ou_path (string): Distinguished name(DN) of the target Organization
            Unit (OU) to restore non-OU object. This can be empty, in which
            case objects are restored to their original OU. The 'credential'
            specified must have privileges to add objects to this OU. Example:
            'OU=SJC,OU=EngOU,DC=contoso,DC=com'. This parameter is ignored for
            OU objects.
        src_sysvol_folder (string, optional): When restoring a GPO, need to
            know the absolute path for SYSVOL folder.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "credentials":'credentials',
        "guid_vec":'guidVec',
        "option_flags":'optionFlags',
        "ou_path":'ouPath',
        "src_sysvol_folder":'srcSysvolFolder'
    }

    def __init__(self,
                 credentials=None,
                 guid_vec=None,
                 option_flags=None,
                 ou_path=None,
                 src_sysvol_folder=None):
        """Constructor for the ADObjectRestoreParam class"""

        # Initialize members of the class
        self.credentials = credentials
        self.guid_vec = guid_vec
        self.option_flags = option_flags
        self.ou_path = ou_path
        self.src_sysvol_folder = src_sysvol_folder


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
        credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('credentials')) if dictionary.get('credentials') else None
        guid_vec = dictionary.get('guidVec')
        option_flags = dictionary.get('optionFlags')
        ou_path = dictionary.get('ouPath')
        src_sysvol_folder = dictionary.get('srcSysvolFolder')

        # Return an object of this model
        return cls(credentials,
                   guid_vec,
                   option_flags,
                   ou_path,
                   src_sysvol_folder)


