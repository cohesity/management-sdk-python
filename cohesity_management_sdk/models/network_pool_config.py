# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NetworkPoolConfig(object):

    """Implementation of the 'NetworkPoolConfig' model.

    While caonfiguring the isilon protection source, this is the selected
    network pool config for the isilon access zone.

    Attributes:
        pool_name (string): Specifies the name of the Network pool.
        subnet (string): Specifies the name of the subnet the network pool
            belongs to.
        use_smart_connect (bool): Specifies whether to use SmartConnect if
            available. If true, DNS name for the SmartConnect zone will be
            used to balance the IPs. Otherwise, pool IPs will be balanced
            manually.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pool_name":'poolName',
        "subnet":'subnet',
        "use_smart_connect":'useSmartConnect'
    }

    def __init__(self,
                 pool_name=None,
                 subnet=None,
                 use_smart_connect=None):
        """Constructor for the NetworkPoolConfig class"""

        # Initialize members of the class
        self.pool_name = pool_name
        self.subnet = subnet
        self.use_smart_connect = use_smart_connect


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
        subnet = None
        if dictionary.get('subnet') != None:
            subnet = list()
            for structure in dictionary.get('subnet'):
                subnet.append(cohesity_management_sdk.models.task_notification.TaskNotification.from_dictionary(structure))
        use_smart_connect = dictionary.get('useSmartConnect')

        # Return an object of this model
        return cls(pool_name,
                   subnet,
                   use_smart_connect)


