# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.site_backup_file

class SiteBackupStatus(object):

    """Implementation of the 'SiteBackupStatus' model.

    Attributes:
        backup_file_vec (list of SiteBackupFile): List of backuped files. Its
            PnP package and any other files required to recover the site.
        ipmi_password (string): Specifies the IPMI Password.
        ipmi_subnet_mask (string): Specifies the subnet mask for the IPMI
            network.
        ipmi_username (string): Specifies the IPMI Username.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_file_vec":'backupFileVec',
        "ipmi_password":'ipmiPassword',
        "ipmi_subnet_mask":'ipmiSubnetMask',
        "ipmi_username":'ipmiUsername'
    }

    def __init__(self,
                 backup_file_vec=None,
                 ipmi_password=None,
                 ipmi_subnet_mask=None,
                 ipmi_username=None):
        """Constructor for the SiteBackupStatus class"""

        # Initialize members of the class
        self.backup_file_vec = backup_file_vec
        self.ipmi_password = ipmi_password
        self.ipmi_subnet_mask = ipmi_subnet_mask
        self.ipmi_username = ipmi_username


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
        backup_file_vec = None
        if dictionary.get('backupFileVec') != None:
            backup_file_vec = list()
            for structure in dictionary.get('backupFileVec'):
                backup_file_vec.append(cohesity_management_sdk.models.site_backup_file.SiteBackupFile.from_dictionary(structure))
        ipmi_password = dictionary.get('ipmiPassword')
        ipmi_subnet_mask = dictionary.get('ipmiSubnetMask')
        ipmi_username = dictionary.get('ipmiUsername')

        # Return an object of this model
        return cls(backup_file_vec,
                   ipmi_password,
                   ipmi_subnet_mask,
                   ipmi_username)


