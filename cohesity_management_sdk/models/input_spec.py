# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.input_spec_input_files_selector
import cohesity_management_sdk.models.input_spec_input_vms_selector

class InputSpec(object):

    """Implementation of the 'InputSpec' model.

    Input selector. Selects the files to map over.

    Attributes:
        files_selector (InputSpec_InputFilesSelector): TODO: type description
            here.
        on_nfs_files (bool): Selects whether input is files inside vmdks or
            files on NFS. One of vm_selector or files_selector will be chosen
            based on this flag.
        vm_Selector (InputSpec_InputVMsSelector): TODO: type description here.


    """

    # Create a mapping from Model property names to API property names
    _names = {
        "files_selector":'filesSelector',
        "on_nfs_files":'onNfsFiles',
        "vm_Selector":'vmSelector'
    }

    def __init__(self,
                 files_selector=None,
                 on_nfs_files=None,
                 vm_Selector=None):
        """Constructor for the InputSpec class"""

        # Initialize members of the class
        self.files_selector = files_selector
        self.on_nfs_files = on_nfs_files
        self.vm_Selector = vm_Selector


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
        files_selector = cohesity_management_sdk.models.input_spec_input_files_selector.InputSpecInputFilesSelector.from_dictionary(dictionary.get('filesSelector')) if dictionary.get('filesSelector') else None
        on_nfs_files = dictionary.get('onNfsFiles')
        vm_Selector = cohesity_management_sdk.models.input_spec_input_vms_selector.InputSpecInputVMsSelector.from_dictionary(dictionary.get('vmSelector')) if dictionary.get('vmSelector') else None

        # Return an object of this model
        return cls(files_selector,
                   on_nfs_files,
                   vm_Selector)


