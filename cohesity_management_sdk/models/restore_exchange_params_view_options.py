# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class RestoreExchangeParams_ViewOptions(object):

    """Implementation of the 'RestoreExchangeParams_ViewOptions' model.


    Attributes:
        mount_point (string): The path to access the SMB share.
        view_name (string): View to which the files of an Exchange database
            have to be cloned.
        whitelist_restore_view_for_all (bool): If set to true then when
            restore view is cloned then white-list all IPs not just the agent
            IP.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mount_point":'mountPoint',
        "view_name":'viewName',
        "whitelist_restore_view_for_all":'whitelistRestoreViewForAll'
    }

    def __init__(self,
                 mount_point=None,
                 view_name=None,
                 whitelist_restore_view_for_all=None):
        """Constructor for the RestoreExchangeParams_ViewOptions class"""

        # Initialize members of the class
        self.mount_point = mount_point
        self.view_name = view_name
        self.whitelist_restore_view_for_all = whitelist_restore_view_for_all


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API deview_nameion.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        mount_point = cohesity_management_sdk.models.remote_host_connector_params.RemoteHostConnectorParams.from_dictionary(dictionary.get('mountPoint')) if dictionary.get('mountPoint') else None
        view_name = cohesity_management_sdk.models.view_name_path_and_params.view_namePathAndParams.from_dictionary(dictionary.get('viewName')) if dictionary.get('viewName') else None
        whitelist_restore_view_for_all = cohesity_management_sdk.models.view_name_execution_whitelist_restore_view_for_all.view_nameExecutionwhitelist_restore_view_for_all.from_dictionary(dictionary.get('whitelistRestoreViewForAll')) if dictionary.get('whitelistRestoreViewForAll') else None

        # Return an object of this model
        return cls(mount_point,
                   view_name,
                   whitelist_restore_view_for_all)


