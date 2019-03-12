# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.subnet

class AthenaAppsConfiguration(object):

    """Implementation of the 'Athena Apps Configuration.' model.

    TODO: type model description here.

    Attributes:
        allow_external_traffic (bool): Whether to allow pod external traffic.
        apps_mode (int): The apps mode - kDisabled, kBareMetal, kVmOnly.
        apps_subnet (Subnet): Defines a Subnet (Subnetwork). The netmask can
            be specified by setting netmaskBits or netmaskIp4. The netmask can
            only be set using netmaskIp4 if the IP address is an IPv4
            address.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allow_external_traffic":'allowExternalTraffic',
        "apps_mode":'appsMode',
        "apps_subnet":'appsSubnet'
    }

    def __init__(self,
                 allow_external_traffic=None,
                 apps_mode=None,
                 apps_subnet=None):
        """Constructor for the AthenaAppsConfiguration class"""

        # Initialize members of the class
        self.allow_external_traffic = allow_external_traffic
        self.apps_mode = apps_mode
        self.apps_subnet = apps_subnet


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

        # Return an object of this model
        return cls(allow_external_traffic,
                   apps_mode,
                   apps_subnet)


