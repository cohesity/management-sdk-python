# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vmware_standby_resource

class StandbyResource(object):

    """Implementation of the 'StandbyResource' model.

    Message to encapsulate resources to be used to create a standby entity on
    the primary environment. Each environment should define the parameters it
    needs to create an entity on the primary environment.


    Attributes:
        recovery_point_objective_secs (long|int): User defined recovery point
            objective for the standby VM. Using this RPO, Magneto will hydrate
            the VMs.
        vmware_standby_resource (VMwareStandbyResource): Standby resources
            needed in a VMware environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "recovery_point_objective_secs": 'recoveryPointObjectiveSecs',
        "vmware_standby_resource": 'vmwareStandbyResource'
    }

    def __init__(self,
                 recovery_point_objective_secs=None,
                 vmware_standby_resource=None):
        """Constructor for the StandbyResource class"""

        # Initialize members of the class
        self.recovery_point_objective_secs = recovery_point_objective_secs
        self.vmware_standby_resource = vmware_standby_resource


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
        recovery_point_objective_secs = dictionary.get('recoveryPointObjectiveSecs')
        vmware_standby_resource = cohesity_management_sdk.models.vmware_standby_resource.VMwareStandbyResource.from_dictionary(dictionary.get('vmwareStandbyResource')) if dictionary.get('vmwareStandbyResource') else None

        # Return an object of this model
        return cls(recovery_point_objective_secs,
                   vmware_standby_resource)


