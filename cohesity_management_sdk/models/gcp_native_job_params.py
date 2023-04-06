# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.gcp_job_disk_exclusion_rule


class GCPNativeJobParams(object):

    """Implementation of the 'GCPNativeJobParams' model.

    TODO: type description here.


    Attributes:

        disk_exclusion_raw_query (string): Specifies the disk exclusion raw
            query used to exclude disks from backup.
        disk_exclusion_rule_vec (list of GCPJobDiskExclusionRule): Specifies
            the different criteria to exclude disks from backup. The values set
            in disk_exclusion_params will be used for OR operation. For E.g: if
            disk_exclusion_params has values [(Balanced-Persistant &&
            instance1-disk),((k1:v1) && (k2:v2))] then the exclusion criteria
            will be (Balanced-Persistant && instance1-disk) || ((k1:v1) &&
            (k2:v2))
        exclude_vm_without_disk (bool): Specifies whether to exclude VM without
            disk.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "disk_exclusion_raw_query":'diskExclusionRawQuery',
        "disk_exclusion_rule_vec":'diskExclusionRuleVec',
        "exclude_vm_without_disk":'excludeVmWithoutDisk',
    }
    def __init__(self,
                 disk_exclusion_raw_query=None,
                 disk_exclusion_rule_vec=None,
                 exclude_vm_without_disk=None,
            ):

        """Constructor for the GCPNativeJobParams class"""

        # Initialize members of the class
        self.disk_exclusion_raw_query = disk_exclusion_raw_query
        self.disk_exclusion_rule_vec = disk_exclusion_rule_vec
        self.exclude_vm_without_disk = exclude_vm_without_disk

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
        disk_exclusion_raw_query = dictionary.get('diskExclusionRawQuery')
        disk_exclusion_rule_vec = None
        if dictionary.get('diskExclusionRuleVec') != None:
            disk_exclusion_rule_vec = list()
            for structure in dictionary.get('diskExclusionRuleVec'):
                disk_exclusion_rule_vec.append(cohesity_management_sdk.models.gcp_job_disk_exclusion_rule.GCPJobDiskExclusionRule.from_dictionary(structure))
        exclude_vm_without_disk = dictionary.get('excludeVmWithoutDisk')

        # Return an object of this model
        return cls(
            disk_exclusion_raw_query,
            disk_exclusion_rule_vec,
            exclude_vm_without_disk
)