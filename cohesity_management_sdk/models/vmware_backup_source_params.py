# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.source_app_params
import cohesity_management_sdk.models.credentials
import cohesity_management_sdk.models.vmware_disk_exclusion_proto

class VmwareBackupSourceParams(object):

    """Implementation of the 'VMwareBackupSourceParams' model.

    Message to capture additional backup params for a VMware type source.

    Attributes:
        source_app_params (SourceAppParams): This message contains params
            specific to application running on the source such as a VM or a
            physical host.
        vm_credentials (Credentials): Target entity credentials. This should
            usually be set if the source_app_params is set, i.e any additional
            operations that require access within the guest.
            
        vmware_disk_exclusion_info (list of VmwareDiskExclusionProto): List of
            Virtual Disk(s) to be excluded from the backup job for the source.
            Overrides the exclusion list requested (if any) through
            EnvBackupParams.VMwareBackupEnvParams.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "source_app_params":'sourceAppParams',
        "vm_credentials":'vmCredentials',
        "vmware_disk_exclusion_info":'vmwareDiskExclusionInfo'
    }

    def __init__(self,
                 source_app_params=None,
                 vm_credentials=None,
                 vmware_disk_exclusion_info=None):
        """Constructor for the VmwareBackupSourceParams class"""

        # Initialize members of the class
        self.source_app_params = source_app_params
        self.vm_credentials = vm_credentials
        self.vmware_disk_exclusion_info = vmware_disk_exclusion_info


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
        source_app_params = cohesity_management_sdk.models.source_app_params.SourceAppParams.from_dictionary(dictionary.get('sourceAppParams')) if dictionary.get('sourceAppParams') else None
        vm_credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('vmCredentials')) if dictionary.get('vmCredentials') else None
        vmware_disk_exclusion_info = None
        if dictionary.get('vmwareDiskExclusionInfo') != None:
            vmware_disk_exclusion_info = list()
            for structure in dictionary.get('vmwareDiskExclusionInfo'):
                vmware_disk_exclusion_info.append(cohesity_management_sdk.models.vmware_disk_exclusion_proto.VmwareDiskExclusionProto.from_dictionary(structure))

        # Return an object of this model
        return cls(source_app_params,
                   vm_credentials,
                   vmware_disk_exclusion_info)


