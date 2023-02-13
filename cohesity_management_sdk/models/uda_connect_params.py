# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.uda_source_capabilities

class UdaConnectParams(object):

    """Implementation of the 'UdaConnectParams' model.

    Specifies an Object containing information about a registered Universal
    Data Adapter source.

    Attributes:
        capabilities (UdaSourceCapabilities): Types of backups supported.
        host_type (HostTypeEnum): Specifies the environment type for the host.
        hosts (list of string): List of hosts forming the Universal Data
            Adapter cluster.
        live_data_view (bool): Whether to use a live view for data backups.
        live_log_view (bool): Whether to use a live view for log backups.
        mount_dir (string): Mount directory path to be used for writing
            the backup to.
        mount_view (bool): Whether to mount a view during the source backup.
        script_dir (string): Path where various source scripts will be
            located.
        source_args (string): Custom arguments which will be provided to the
            source registration scripts.
        source_type (string): Global app source type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "capabilities": 'capabilities',
        "host_type":'hostType',
        "hosts": 'hosts',
        "live_data_view":'liveDataView',
        "live_log_view":'liveLogView',
        "mount_dir": 'mountDir',
        "mount_view":'mountView',
        "script_dir":'scriptDir',
        "source_args":'sourceArgs',
        "source_type":'sourceType'
    }

    def __init__(self,
                 capabilities=None,
                 host_type=None,
                 hosts=None,
                 live_data_view=None,
                 live_log_view=None,
                 mount_dir=None,
                 mount_view=None,
                 script_dir=None,
                 source_args=None,
                 source_type=None
                 ):
        """Constructor for the UdaConnectParams class"""

        # Initialize members of the class
        self.capabilities = capabilities
        self.hosts = hosts
        self.live_data_view = live_data_view
        self.live_log_view = live_log_view
        self.host_type = host_type
        self.mount_dir = mount_dir
        self.mount_view = mount_view
        self.script_dir = script_dir
        self.source_args = source_args
        self.source_type = source_type

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
        capabilities = cohesity_management_sdk.models.uda_source_capabilities.UdaSourceCapabilities.from_dictionary(dictionary.get('capabilities')) if dictionary.get('capabilities') else None
        hosts = dictionary.get('hosts')
        host_type = dictionary.get('hostType')
        live_data_view = dictionary.get('liveDataView')
        live_log_view = dictionary.get('liveLogView')
        mount_dir = dictionary.get('mountDir')
        mount_view = dictionary.get('mountView')
        script_dir = dictionary.get('scriptDir')
        source_args = dictionary.get('sourceArgs')
        source_type = dictionary.get('sourceType')

        # Return an object of this model
        return cls(capabilities,
                   host_type,
                   hosts,
                   live_data_view,
                   live_log_view,
                   mount_dir,
                   mount_view,
                   script_dir,
                   source_args,
                   source_type)


