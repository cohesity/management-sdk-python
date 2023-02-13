# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vmware_disk_exclusion_proto

class VmwareBackupEnvParams(object):

    """Implementation of the 'VMwareBackupEnvParams' model.

    Message to capture any additional backup params for a VMware environment.

    Attributes:
        allow_crash_consistent_snapshot (bool): Whether to fallback to take a
            crash-consistent snapshot incase taking an app-consistent snapshot
            fails.
        allow_nbdssl_transport_fallback (bool): Whether to fallback to use
            NBDSSL transport for backup in case using SAN transport backup
            fails.
        allow_vms_with_physical_rdm_disks (bool): Physical RDM disks cannot be
            backed up using VADP. By default the backups of such VMs will
            fail. If this is set to true, then such VMs in this backup job
            will be backed up by excluding the physical RDM disks.
        enable_cbt_allowed (bool): Whether the backup job should allow enabling
            CBT for VM when the backup runs. Currently, by default, the backup
            run enables CBT for a VM during the backup if it's not already
            enabled. However, there may be a case, where customer doesn't want
            to enable CBT during the backup. This param will be used to
            determine that.
        vmware_disk_exclusion_info (list of VmwareDiskExclusionProto): List of
            Virtual Disk(s) to be excluded from the backup job. These disks
            will be excluded for all VMs in this environment unless overriden
            by the disk exclusion list from
            BackupSourceParams.VMwareBackupSourceParams.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allow_crash_consistent_snapshot":'allowCrashConsistentSnapshot',
        "allow_nbdssl_transport_fallback":'allowNbdsslTransportFallback',
        "allow_vms_with_physical_rdm_disks":'allowVmsWithPhysicalRdmDisks',
        "enable_cbt_allowed":'enableCbtAllowed',
        "vmware_disk_exclusion_info":'vmwareDiskExclusionInfo'
    }

    def __init__(self,
                 allow_crash_consistent_snapshot=None,
                 allow_nbdssl_transport_fallback=None,
                 allow_vms_with_physical_rdm_disks=None,
                 enable_cbt_allowed=None,
                 vmware_disk_exclusion_info=None):
        """Constructor for the VmwareBackupEnvParams class"""

        # Initialize members of the class
        self.allow_crash_consistent_snapshot = allow_crash_consistent_snapshot
        self.allow_nbdssl_transport_fallback = allow_nbdssl_transport_fallback
        self.allow_vms_with_physical_rdm_disks = allow_vms_with_physical_rdm_disks
        self.enable_cbt_allowed = enable_cbt_allowed
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
        allow_crash_consistent_snapshot = dictionary.get('allowCrashConsistentSnapshot')
        allow_nbdssl_transport_fallback = dictionary.get('allowNbdsslTransportFallback')
        allow_vms_with_physical_rdm_disks = dictionary.get('allowVmsWithPhysicalRdmDisks')
        enable_cbt_allowed = dictionary.get('enableCbtAllowed')
        vmware_disk_exclusion_info = None
        if dictionary.get('vmwareDiskExclusionInfo') != None:
            vmware_disk_exclusion_info = list()
            for structure in dictionary.get('vmwareDiskExclusionInfo'):
                vmware_disk_exclusion_info.append(cohesity_management_sdk.models.vmware_disk_exclusion_proto.VmwareDiskExclusionProto.from_dictionary(structure))

        # Return an object of this model
        return cls(allow_crash_consistent_snapshot,
                   allow_nbdssl_transport_fallback,
                   allow_vms_with_physical_rdm_disks,
                   enable_cbt_allowed,
                   vmware_disk_exclusion_info)


