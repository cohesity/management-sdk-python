# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class BackupJobProtoDRToCloudParams(object):

    """Implementation of the 'BackupJobProto_DRToCloudParams' model.

    A Proto needed in case objects backed up by this job need to DR to cloud.
    "Fail over" signifies the mechanism to move the workload to cloud.

    Attributes:
        need_to_fail_over (bool): Whether the objects in this job will be
            failed over to cloud. In case of VMs, we need to fetch information
            about the logical volumes present on the VM. Magneto might fail
            backup of a VM in case volume information can not be fetched
            (maybe because the agent is not installed or if the VM is turned
            off etc.).  The VM will be backed up using the physical agent when
            it is running in the cloud. We might choose to backup the VM in
            the cloud using native API at a later point.  This flag makes
            sense when configuring a job to backup on-prem VMs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "need_to_fail_over":'needToFailOver'
    }

    def __init__(self,
                 need_to_fail_over=None):
        """Constructor for the BackupJobProtoDRToCloudParams class"""

        # Initialize members of the class
        self.need_to_fail_over = need_to_fail_over


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
        need_to_fail_over = dictionary.get('needToFailOver')

        # Return an object of this model
        return cls(need_to_fail_over)


