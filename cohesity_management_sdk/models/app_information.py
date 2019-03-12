# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.cluster_info
import cohesity_management_sdk.models.app_metadata_information

class AppInformation(object):

    """Implementation of the 'App information.' model.

    App provides information about an application.

    Attributes:
        app_id (long|int): TODO: Bhargava - Change it to AppUid Specifies
            unique id allocated by the AppStore.
        clusters (list of ClusterInfo): Specifies the list of clusters on
            which the app is installed for a particular account Id.
        install_state (InstallStateEnum): Specifies app installation status.
            Specifies status of the app installation. kNotInstalled - App yet
            to be installed. kInstallInProgress - App installation is in
            progress. kInstalled - App is installed successfully and can be
            launched. kInstallFailed - App installation failed.
            kUninstallInProgress - App uninstallation is in progress.
            kUninstallFailed - App uninstallation failed.
        install_time (long|int): Specifies timestamp when the app was
            installed.
        is_latest (bool): Specifies whether the app currently installed on all
            clusters is the latest version or not.
        metadata (AppMetadataInformation): AppMetadata provides metadata
            information about an application.
        required_privileges (list of RequiredPrivilegeEnum): Specifies
            privileges that are required for this app. App privilege
            information.  Specifies privileges that are required for this app.
            kReadAccess - App needs views for read access. kReadWriteAccess -
            App needs views for Read/write access. kManagementAccess - App
            needs management access via iris API.
        uninstall_time (long|int): Specifies timestamp when the app was
            uninstalled.
        version (long|int): Specifies application version assigned by the
            AppStore.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_id":'appId',
        "clusters":'clusters',
        "install_state":'installState',
        "install_time":'installTime',
        "is_latest":'isLatest',
        "metadata":'metadata',
        "required_privileges":'requiredPrivileges',
        "uninstall_time":'uninstallTime',
        "version":'version'
    }

    def __init__(self,
                 app_id=None,
                 clusters=None,
                 install_state=None,
                 install_time=None,
                 is_latest=None,
                 metadata=None,
                 required_privileges=None,
                 uninstall_time=None,
                 version=None):
        """Constructor for the AppInformation class"""

        # Initialize members of the class
        self.app_id = app_id
        self.clusters = clusters
        self.install_state = install_state
        self.install_time = install_time
        self.is_latest = is_latest
        self.metadata = metadata
        self.required_privileges = required_privileges
        self.uninstall_time = uninstall_time
        self.version = version


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
        app_id = dictionary.get('appId')
        clusters = None
        if dictionary.get('clusters') != None:
            clusters = list()
            for structure in dictionary.get('clusters'):
                clusters.append(cohesity_management_sdk.models.cluster_info.ClusterInfo.from_dictionary(structure))
        install_state = dictionary.get('installState')
        install_time = dictionary.get('installTime')
        is_latest = dictionary.get('isLatest')
        metadata = cohesity_management_sdk.models.app_metadata_information.AppMetadataInformation.from_dictionary(dictionary.get('metadata')) if dictionary.get('metadata') else None
        required_privileges = dictionary.get('requiredPrivileges')
        uninstall_time = dictionary.get('uninstallTime')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(app_id,
                   clusters,
                   install_state,
                   install_time,
                   is_latest,
                   metadata,
                   required_privileges,
                   uninstall_time,
                   version)


