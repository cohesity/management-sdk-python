# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.recover_virtual_disk_info_proto
import cohesity_management_sdk.models.recover_virtual_disk_params

class RecoverDisksTaskStateProto(object):

    """Implementation of the 'RecoverDisksTaskStateProto' model.

    TODO: type model description here.

    Attributes:
        recover_virtual_disk_info (RecoverVirtualDiskInfoProto): Each
            available extension is listed below along with the location of the
            proto file (relative to magneto/connectors) where it is defined.
            RecoverVirtualDiskInfoProto extension                     Location
            ===================================================================
            ==========
            ===================================================================
            ==========
        recover_virtual_disk_params (RecoverVirtualDiskParams): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "recover_virtual_disk_info":'recoverVirtualDiskInfo',
        "recover_virtual_disk_params":'recoverVirtualDiskParams'
    }

    def __init__(self,
                 recover_virtual_disk_info=None,
                 recover_virtual_disk_params=None):
        """Constructor for the RecoverDisksTaskStateProto class"""

        # Initialize members of the class
        self.recover_virtual_disk_info = recover_virtual_disk_info
        self.recover_virtual_disk_params = recover_virtual_disk_params


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
        recover_virtual_disk_info = cohesity_management_sdk.models.recover_virtual_disk_info_proto.RecoverVirtualDiskInfoProto.from_dictionary(dictionary.get('recoverVirtualDiskInfo')) if dictionary.get('recoverVirtualDiskInfo') else None
        recover_virtual_disk_params = cohesity_management_sdk.models.recover_virtual_disk_params.RecoverVirtualDiskParams.from_dictionary(dictionary.get('recoverVirtualDiskParams')) if dictionary.get('recoverVirtualDiskParams') else None

        # Return an object of this model
        return cls(recover_virtual_disk_info,
                   recover_virtual_disk_params)


