# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IsilonEnvParams_ZoneConfig_NetworkPoolConfig(object):

    """Implementation of the 'IsilonEnvParams_ZoneConfig_NetworkPoolConfig' model.

    Network Pool Configuration.

    Attributes:
        pool_name (string): The name of the pool.
        subnet (string): Name of the subnet the pool belongs to.
        use_smartconnect (bool): Whether to use SmartConnect if available. If
            true, DNS name for the SmartConnect zone will be used to balance
            the IPs. Otherwise, pool IPs will be balanced manually.


    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pool_name":'poolName',
        "subnet":'subnet',
        "use_smartconnect":'useSmartconnect'
    }

    def __init__(self,
                 pool_name=None,
                 subnet=None,
                 use_smartconnect=None):
        """Constructor for the IsilonEnvParams_ZoneConfig_NetworkPoolConfig class"""

        # Initialize members of the class
        self.pool_name = pool_name
        self.subnet = subnet
        self.use_smartconnect = use_smartconnect


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
        pool_name = dictionary.get('poolName')
        subnet = dictionary.get('subnet')
        use_smartconnect = dictionary.get('useSmartconnect')

        # Return an object of this model
        return cls(pool_name,
                   subnet,
                   use_smartconnect)


