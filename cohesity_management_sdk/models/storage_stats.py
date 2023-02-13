# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class StorageStats(object):

    """Implementation of the 'StorageStats' model.

    Specifies the storage statistics of the cluster.

    Attributes:
        data_protection_logical_usage_bytes (long|int): Specifies the logical
            size of protected objects in bytes.
        data_protection_physical_usage_bytes (long|int): Specifies the
            physical size of protected objects in bytes.
        file_services_logical_usage_bytes (long|int): Specifies the logical
            size consumed by file services in bytes.
        file_services_physical_usage_bytes (long|int): Specifies the physical
            size consumed by file services in bytes.
        local_available_bytes (long|int): Specifies the local storage
            currently available on the cluster in bytes.
        local_usage_bytes (long|int): Specifies the local storage currently in
            use on the cluster in bytes.
        total_capacity_bytes (long|int): Specifies the total capacity of the
            cluster in bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_protection_logical_usage_bytes":'dataProtectionLogicalUsageBytes',
        "data_protection_physical_usage_bytes":'dataProtectionPhysicalUsageBytes',
        "file_services_logical_usage_bytes":'fileServicesLogicalUsageBytes',
        "file_services_physical_usage_bytes":'fileServicesPhysicalUsageBytes',
        "local_available_bytes":'localAvailableBytes',
        "local_usage_bytes":'localUsageBytes',
        "total_capacity_bytes":'totalCapacityBytes'
    }

    def __init__(self,
                 data_protection_logical_usage_bytes=None,
                 data_protection_physical_usage_bytes=None,
                 file_services_logical_usage_bytes=None,
                 file_services_physical_usage_bytes=None,
                 local_available_bytes=None,
                 local_usage_bytes=None,
                 total_capacity_bytes=None):
        """Constructor for the StorageStats class"""

        # Initialize members of the class
        self.data_protection_logical_usage_bytes = data_protection_logical_usage_bytes
        self.data_protection_physical_usage_bytes = data_protection_physical_usage_bytes
        self.file_services_logical_usage_bytes = file_services_logical_usage_bytes
        self.file_services_physical_usage_bytes = file_services_physical_usage_bytes
        self.local_available_bytes = local_available_bytes
        self.local_usage_bytes = local_usage_bytes
        self.total_capacity_bytes = total_capacity_bytes


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
        data_protection_logical_usage_bytes = dictionary.get('dataProtectionLogicalUsageBytes')
        data_protection_physical_usage_bytes = dictionary.get('dataProtectionPhysicalUsageBytes')
        file_services_logical_usage_bytes = dictionary.get('fileServicesLogicalUsageBytes')
        file_services_physical_usage_bytes = dictionary.get('fileServicesPhysicalUsageBytes')
        local_available_bytes = dictionary.get('localAvailableBytes')
        local_usage_bytes = dictionary.get('localUsageBytes')
        total_capacity_bytes = dictionary.get('totalCapacityBytes')

        # Return an object of this model
        return cls(data_protection_logical_usage_bytes,
                   data_protection_physical_usage_bytes,
                   file_services_logical_usage_bytes,
                   file_services_physical_usage_bytes,
                   local_available_bytes,
                   local_usage_bytes,
                   total_capacity_bytes)


