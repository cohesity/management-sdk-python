# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.app_metadata
import cohesity_management_sdk.models.cluster_info

class App(object):

    """Implementation of the 'App' model.

    App provides information about an application.

    Attributes:
        app_id (long|int): Specifies unique id allocated by the AppStore.
        clusters (list of ClusterInfo): Specifies the list of clusters on
            which the app is installed for a particular account Id.
        download_progress_pct (float): Specifies app download progress
            percentage.
        install_state (InstallStateEnum): Specifies app installation status.
            Specifies status of the app installation.
            kNotInstalled - App yet to be installed.
            kInstallInProgress - App installation is in progress.
            kInstalled - App is installed required_privilegesly and can be
            launched.
            kInstallFailed - App installation failed.
            kUninstallInProgress - App uninstallation is in progress.
            kUninstallFailed - App uninstallation failed.
            kDownloadNotStarted - App download has not started.
            kDownloadInProgress - App download in progress.
            kDownloadComplete - App download completed.
            kDownloadFailed - App download failed.
        install_time (long|int): Specifies timestamp when the app was
            installed.
        is_latest (bool): Specifies whether the app currently installed on all
            clusters is the latest version or not.
        latest_version (long|int): Specifies application version assigned by
            the AppStore for the latest version of an app.
        metadata (AppMetadata): Specifies metadata information about the app.
        required_privileges (RequiredPrivilegesEnum): Specifies privileges
            that are required for this app. App privilege information.
        uninstall_time (long|int): Specifies timestamp when the app was
            uninstalled.
        version (long|int): Specifies application version assigned by the
            AppStore.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_id":'appId',
        "clusters":'clusters',
        "download_progress_pct":'downloadProgressPct',
        "install_state":'installState',
        "install_time":'installTime',
        "is_latest":'isLatest',
        "latest_version":'latestVersion',
        "metadata":'metadata',
        "required_privileges":'requiredPrivileges',
        "uninstall_time":'uninstallTime',
        "version":'version'
    }

    def __init__(self,
                 app_id=None,
                 clusters=None,
                 download_progress_pct=None,
                 install_state=None,
                 install_time=None,
                 is_latest=None,
                 latest_version=None,
                 metadata=None,
                 required_privileges=None,
                 uninstall_time=None,
                 version=None):
        """Constructor for the App class"""

        # Initialize members of the class
        self.app_id = app_id
        self.clusters = clusters
        self.download_progress_pct = download_progress_pct
        self.install_state = install_state
        self.install_time = install_time
        self.is_latest = is_latest
        self.latest_version = latest_version
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
        download_progress_pct = dictionary.get('downloadProgressPct')
        install_state = dictionary.get('installState')
        install_time = dictionary.get('installTime')
        is_latest = dictionary.get('isLatest')
        latest_version = dictionary.get('latestVersion')
        metadata = cohesity_management_sdk.models.app_metadata.AppMetadata.from_dictionary(dictionary.get('metadata')) if dictionary.get('metadata') else None
        required_privileges = dictionary.get('requiredPrivileges')
        uninstall_time = dictionary.get('uninstallTime')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(app_id,
                   clusters,
                   download_progress_pct,
                   install_state,
                   install_time,
                   is_latest,
                   latest_version,
                   metadata,
                   required_privileges,
                   uninstall_time,
                   version)

