# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_site_params_site_owner_drive


class RestoreO365TeamsParams_SourceChannel(object):

    """Implementation of the 'RestoreO365TeamsParams_SourceChannel' model.

    TODO: type description here.


    Attributes:

        drive_vec (list of RestoreSiteParams_SiteOwner_Drive): Drives of this
            channel whose items have to be restored. This will be empty iff
            is_full_channel_restore is true.
        id (string): Id of the source channel for restore.
        is_full_channel_restore (bool): Whether we have to restore the complete
            channel.
        name (string): Name of the source channel for restore.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "drive_vec":'driveVec',
        "id":'id',
        "is_full_channel_restore":'isFullChannelRestore',
        "name":'name',
    }
    def __init__(self,
                 drive_vec=None,
                 id=None,
                 is_full_channel_restore=None,
                 name=None,
            ):

        """Constructor for the RestoreO365TeamsParams_SourceChannel class"""

        # Initialize members of the class
        self.drive_vec = drive_vec
        self.id = id
        self.is_full_channel_restore = is_full_channel_restore
        self.name = name

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
        drive_vec = None
        if dictionary.get('driveVec') != None:
            drive_vec = list()
            for structure in dictionary.get('driveVec'):
                drive_vec.append(cohesity_management_sdk.models.restore_site_params_site_owner_drive.RestoreSiteParams_SiteOwner_Drive.from_dictionary(structure))
        id = dictionary.get('id')
        is_full_channel_restore = dictionary.get('isFullChannelRestore')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(
            drive_vec,
            id,
            is_full_channel_restore,
            name
)