# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.deploy_vms_to_on_prem_params
import cohesity_management_sdk.models.entity_proto


class OnPremDeployTarget(object):

    """Implementation of the 'OnPremDeployTarget' model.

    Message that specifies the details about OnPremDeploy target where backup
    snapshots may be converted and deployed.


    Attributes:

        deploy_vms_to_onprem_params (DeployVMsToOnPremParams): Contains
            information needed to identify various resources when deploying VMs
            to OnPrem sources like VMware.
        target_entity (EntityProto): Entity corresponding to the onprem deploy
            target.
        mtype (int): The type of the OnPremDeploy target. Only VMware is
            supported for now.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "deploy_vms_to_onprem_params":'deployVmsToOnpremParams',
        "target_entity":'targetEntity',
        "mtype":'type',
    }
    def __init__(self,
                 deploy_vms_to_onprem_params=None,
                 target_entity=None,
                 mtype=None,
            ):

        """Constructor for the OnPremDeployTarget class"""

        # Initialize members of the class
        self.deploy_vms_to_onprem_params = deploy_vms_to_onprem_params
        self.target_entity = target_entity
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
        deploy_vms_to_onprem_params = cohesity_management_sdk.models.deploy_vms_to_on_prem_params.DeployVMsToOnPremParams.from_dictionary(dictionary.get('deployVmsToOnpremParams')) if dictionary.get('deployVmsToOnpremParams') else None
        target_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetEntity')) if dictionary.get('targetEntity') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(
            deploy_vms_to_onprem_params,
            target_entity,
            mtype
)