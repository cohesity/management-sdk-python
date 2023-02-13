# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.application_parameters
import cohesity_management_sdk.models.disk_unit
import cohesity_management_sdk.models.credentials

class VmwareSpecialParameters(object):

    """Implementation of the 'VmwareSpecialParameters' model.

    Specifies additional special settings applicable for a Protection Source
    of 'kVMware' type in a Protection Job.

    Attributes:
        application_parameters (ApplicationParameters): Specifies parameters
            that are related to applications running on the Protection Source.
        excluded_disks (list of DiskUnit): Specifies the list of Disks to be
            excluded from backing up. These disks are excluded from all
            Protection Sources in the Protection Job.
        vm_credentials (Credentials): Specifies the administrator credentials
            to log in to the guest Windows system of a VM that hosts the
            Microsoft Exchange Server. If truncateExchangeLog is set to true
            and the specified source is a VM, administrator credentials to log
            in to the guest Windows system of the VM must be provided to
            truncate the logs. This field is only applicable to Sources in the
            kVMware environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_parameters":'applicationParameters',
        "excluded_disks":'excludedDisks',
        "vm_credentials":'vmCredentials'
    }

    def __init__(self,
                 application_parameters=None,
                 excluded_disks=None,
                 vm_credentials=None):
        """Constructor for the VmwareSpecialParameters class"""

        # Initialize members of the class
        self.application_parameters = application_parameters
        self.excluded_disks = excluded_disks
        self.vm_credentials = vm_credentials


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
        application_parameters = cohesity_management_sdk.models.application_parameters.ApplicationParameters.from_dictionary(dictionary.get('applicationParameters')) if dictionary.get('applicationParameters') else None
        excluded_disks = None
        if dictionary.get('excludedDisks') != None:
            excluded_disks = list()
            for structure in dictionary.get('excludedDisks'):
                excluded_disks.append(cohesity_management_sdk.models.disk_unit.DiskUnit.from_dictionary(structure))
        vm_credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('vmCredentials')) if dictionary.get('vmCredentials') else None

        # Return an object of this model
        return cls(application_parameters,
                   excluded_disks,
                   vm_credentials)


