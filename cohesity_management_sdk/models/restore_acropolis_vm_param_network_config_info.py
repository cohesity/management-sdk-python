# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_acropolis_vm_param_network_config_info_nic_spec

class RestoreAcropolisVMParamNetworkConfigInfo(object):

    """Implementation of the 'RestoreAcropolisVMParam_NetworkConfigInfo' model.

    Proto to define the network configuration to be applied to the restored
    VM.

    Attributes:
        network_state_change (int): Network state to be applied to the
            restored VM.
        nic_vec (list of RestoreAcropolisVMParamNetworkConfigInfoNICSpec):
            This field is applicable only if the network_state_change is set
            to 'kAttachNewNetwork'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "network_state_change":'networkStateChange',
        "nic_vec":'nicVec'
    }

    def __init__(self,
                 network_state_change=None,
                 nic_vec=None):
        """Constructor for the RestoreAcropolisVMParamNetworkConfigInfo class"""

        # Initialize members of the class
        self.network_state_change = network_state_change
        self.nic_vec = nic_vec


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
        network_state_change = dictionary.get('networkStateChange')
        nic_vec = None
        if dictionary.get('nicVec') != None:
            nic_vec = list()
            for structure in dictionary.get('nicVec'):
                nic_vec.append(cohesity_management_sdk.models.restore_acropolis_vm_param_network_config_info_nic_spec.RestoreAcropolisVMParamNetworkConfigInfoNICSpec.from_dictionary(structure))

        # Return an object of this model
        return cls(network_state_change,
                   nic_vec)


