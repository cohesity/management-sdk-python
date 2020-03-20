# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.subnet

class AppsConfig(object):

    """Implementation of the 'AppsConfig' model.

    TODO: type model description here.

    Attributes:
        allow_external_traffic (bool): Whether to allow pod external traffic.
        apps_mode (AppsModeEnum): Specifies the various modes for running
            apps. 'kDisabled' specifies that apps are disabled. 'kBareMetal'
            specifies that apps could only run in containers on the node (no
            VM). 'kVmOnly' specifies that apps could only run in containers on
            a VM hosted by the node.
        apps_subnet (Subnet): Defines a Subnet (Subnetwork). The netmask can
            be specified by setting netmaskBits or netmaskIp4. The netmask can
            only be set using netmaskIp4 if the IP address is an IPv4
            address.
        overcommit_memory_pct (int): The system memory to overcommit for
            apps.
        reserved_cpu_millicores (int): The CPU millicores to reserve for
            apps.
        reserved_memory_pct (int): The system memory to reserve for apps.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allow_external_traffic":'allowExternalTraffic',
        "apps_mode":'appsMode',
        "apps_subnet":'appsSubnet',
        "overcommit_memory_pct":'overcommitMemoryPct',
        "reserved_cpu_millicores":'reservedCpuMillicores',
        "reserved_memory_pct":'reservedMemoryPct'
    }

    def __init__(self,
                 allow_external_traffic=None,
                 apps_mode=None,
                 apps_subnet=None,
                 overcommit_memory_pct=None,
                 reserved_cpu_millicores=None,
                 reserved_memory_pct=None):
        """Constructor for the AppsConfig class"""

        # Initialize members of the class
        self.allow_external_traffic = allow_external_traffic
        self.apps_mode = apps_mode
        self.apps_subnet = apps_subnet
        self.overcommit_memory_pct = overcommit_memory_pct
        self.reserved_cpu_millicores = reserved_cpu_millicores
        self.reserved_memory_pct = reserved_memory_pct


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
        allow_external_traffic = dictionary.get('allowExternalTraffic')
        apps_mode = dictionary.get('appsMode')
        apps_subnet = cohesity_management_sdk.models.subnet.Subnet.from_dictionary(dictionary.get('appsSubnet')) if dictionary.get('appsSubnet') else None
        overcommit_memory_pct = dictionary.get('overcommitMemoryPct')
        reserved_cpu_millicores = dictionary.get('reservedCpuMillicores')
        reserved_memory_pct = dictionary.get('reservedMemoryPct')

        # Return an object of this model
        return cls(allow_external_traffic,
                   apps_mode,
                   apps_subnet,
                   overcommit_memory_pct,
                   reserved_cpu_millicores,
                   reserved_memory_pct)


