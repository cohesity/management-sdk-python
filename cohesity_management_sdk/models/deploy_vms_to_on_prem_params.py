# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_vmware_vm_params


class DeployVMsToOnPremParams(object):

    """Implementation of the 'DeployVMsToOnPremParams' model.

    Contains the onprem specific information needed to identify various
    resources when deploying a VM.


    Attributes:

        deploy_vms_to_vmware_params (RestoreVMwareVMParams): Deploy params
            specific to VMware.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "deploy_vms_to_vmware_params":'deployVmsToVmwareParams',
    }
    def __init__(self,
                 deploy_vms_to_vmware_params=None,
            ):

        """Constructor for the DeployVMsToOnPremParams class"""

        # Initialize members of the class
        self.deploy_vms_to_vmware_params = deploy_vms_to_vmware_params

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
        deploy_vms_to_vmware_params = cohesity_management_sdk.models.restore_vmware_vm_params.RestoreVMwareVMParams.from_dictionary(dictionary.get('deployVmsToVmwareParams')) if dictionary.get('deployVmsToVmwareParams') else None

        # Return an object of this model
        return cls(
            deploy_vms_to_vmware_params
)