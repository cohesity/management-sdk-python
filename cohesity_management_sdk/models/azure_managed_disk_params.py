# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AzureManagedDiskParams(object):

    """Implementation of the 'AzureManagedDiskParams' model.

    Contains managed disk parameters needed to deploy to Azure using managed
    disk.

    Attributes:
        data_disks_sku_type (int): SKU type for data disks.
        os_disk_sku_type (int): SKU type for OS disk.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_disks_sku_type":'dataDisksSkuType',
        "os_disk_sku_type":'osDiskSkuType'
    }

    def __init__(self,
                 data_disks_sku_type=None,
                 os_disk_sku_type=None):
        """Constructor for the AzureManagedDiskParams class"""

        # Initialize members of the class
        self.data_disks_sku_type = data_disks_sku_type
        self.os_disk_sku_type = os_disk_sku_type


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
        data_disks_sku_type = dictionary.get('dataDisksSkuType')
        os_disk_sku_type = dictionary.get('osDiskSkuType')

        # Return an object of this model
        return cls(data_disks_sku_type,
                   os_disk_sku_type)


