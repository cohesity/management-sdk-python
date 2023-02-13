# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.app_metadata
import cohesity_management_sdk.models.cluster_info
import cohesity_management_sdk.models.external_network_info
import cohesity_management_sdk.models.vm_name_info

class App(object):

    """Implementation of the 'App' model.

    App provides information about an application.

    Attributes:
        app_id (long|int): Specifies unique id allocated by the AppStore.
        clusters (list of ClusterInfo): Specifies the list of clusters on
            which the app is installed for a particular account Id.
        download_progress_pct (float): Specifies app download progress
            percentage.
        external_ip_required (bool): Specifies if an external ip is required
            for the app.
        external_networks (list of ExternalNetworkInfo): List of external
            network information available for the app.
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
        instance_sizes (list of string): List of applicable instance size
            specifications (e.g. small/medium/large) for the app. Used to
            determine container resources.
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
        vm_name_info_list (list of VmNameInfo): List of vm name info objects.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_id":'appId',
        "clusters":'clusters',
        "download_progress_pct":'downloadProgressPct',
        "external_ip_required":'externalIpRequired',
        "external_networks":'externalNetworks',
        "install_state":'installState',
        "install_time":'installTime',
        "instance_sizes":'instanceSizes',
        "is_latest":'isLatest',
        "latest_version":'latestVersion',
        "metadata":'metadata',
        "required_privileges":'requiredPrivileges',
        "uninstall_time":'uninstallTime',
        "version":'version',
        "vm_name_info_list":'vmNameInfoList'
    }

    def __init__(self,
                 app_id=None,
                 clusters=None,
                 download_progress_pct=None,
                 external_ip_required=None,
                 external_networks=None,
                 install_state=None,
                 install_time=None,
                 instance_sizes=None,
                 is_latest=None,
                 latest_version=None,
                 metadata=None,
                 required_privileges=None,
                 uninstall_time=None,
                 version=None,
                 vm_name_info_list=None):
        """Constructor for the App class"""

        # Initialize members of the class
        self.app_id = app_id
        self.clusters = clusters
        self.download_progress_pct = download_progress_pct
        self.external_ip_required = external_ip_required
        self.external_networks = external_networks
        self.install_state = install_state
        self.install_time = install_time
        self.instance_sizes = instance_sizes
        self.is_latest = is_latest
        self.latest_version = latest_version
        self.metadata = metadata
        self.required_privileges = required_privileges
        self.uninstall_time = uninstall_time
        self.version = version
        self.vm_name_info_list = vm_name_info_list


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
        external_ip_required = dictionary.get('externalIpRequired')
        external_networks = None
        if dictionary.get('externalNetworks') != None:
            external_networks = list()
            for structure in dictionary.get('externalNetworks'):
                external_networks.append(cohesity_management_sdk.models.external_network_info.ExternalNetworkInfo.from_dictionary(structure))
        install_state = dictionary.get('installState')
        install_time = dictionary.get('installTime')
        instance_sizes = dictionary.get('instanceSizes')
        is_latest = dictionary.get('isLatest')
        latest_version = dictionary.get('latestVersion')
        metadata = cohesity_management_sdk.models.app_metadata.AppMetadata.from_dictionary(dictionary.get('metadata')) if dictionary.get('metadata') else None
        required_privileges = dictionary.get('requiredPrivileges')
        uninstall_time = dictionary.get('uninstallTime')
        version = dictionary.get('version')
        vm_name_info_list = None
        if dictionary.get('vmNameInfoList') != None:
            vm_name_info_list = list()
            for structure in dictionary.get('vmNameInfoList'):
                vm_name_info_list.append(cohesity_management_sdk.models.vm_name_info.VmNameInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(app_id,
                   clusters,
                   download_progress_pct,
                   external_ip_required,
                   external_networks,
                   install_state,
                   install_time,
                   instance_sizes,
                   is_latest,
                   latest_version,
                   metadata,
                   required_privileges,
                   uninstall_time,
                   version,
                   vm_name_info_list)

