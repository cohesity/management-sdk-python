# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.flash_blade_file_system
import cohesity_management_sdk.models.flash_blade_storage_array

class FlashBladeProtectionSource(object):

    """Implementation of the 'FlashBladeProtectionSource' model.

    Specifies a Protection Source in Pure Storage FlashBlade environment.

    Attributes:
        file_system (FlashBladeFileSystem): Specifies information about a
            Flash Blade File System in a Storage Array.
        name (string): Specifies a unique name of the Protection Source.
        storage_array (FlashBladeStorageArray): Specifies information about a
            Pure Storage FlashBlade Array.
        mtype (TypeFlashBladeProtectionSourceEnum): Specifies the type of
            managed object in a Pure Storage FlashBlade like 'kStorageArray'
            or 'kFileSystem'. 'kStorageArray' indicates a top level Pure
            Storage FlashBlade array. 'kFileSystem' indicates a Pure Storage
            FlashBlade file system within the array.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_system":'fileSystem',
        "name":'name',
        "storage_array":'storageArray',
        "mtype":'type'
    }

    def __init__(self,
                 file_system=None,
                 name=None,
                 storage_array=None,
                 mtype=None):
        """Constructor for the FlashBladeProtectionSource class"""

        # Initialize members of the class
        self.file_system = file_system
        self.name = name
        self.storage_array = storage_array
        self.mtype = mtype


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
        file_system = cohesity_management_sdk.models.flash_blade_file_system.FlashBladeFileSystem.from_dictionary(dictionary.get('fileSystem')) if dictionary.get('fileSystem') else None
        name = dictionary.get('name')
        storage_array = cohesity_management_sdk.models.flash_blade_storage_array.FlashBladeStorageArray.from_dictionary(dictionary.get('storageArray')) if dictionary.get('storageArray') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(file_system,
                   name,
                   storage_array,
                   mtype)


