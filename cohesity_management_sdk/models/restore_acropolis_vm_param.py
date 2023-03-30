# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_acropolis_vm_param_network_config_info
import cohesity_management_sdk.models.snapshot_info_proto


class RestoreAcropolisVMParam(object):

    """Implementation of the 'RestoreAcropolisVMParam' model.

    TODO: type description here.


    Attributes:

        base_cbt_snapshot_info_proto (SnapshotInfoProto): If specified, this
            field defines the info of the snapshot that is known to be present
            on both Acropolis and Cohesity cluster. We can compute the changed
            blocks between the snapshot to be restored and this reference
            snapshot and thus push only changed blocks to the Acropolis cluster
            for fast/incremental recovery. If this field is not specified,
            Cohesity cluster will push all the VM snapshot data back to the
            Acropolis cluster.
        network_config (RestoreAcropolisVMParam_NetworkConfigInfo): TODO: Type
            description here.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "base_cbt_snapshot_info_proto":'baseCbtSnapshotInfoProto',
        "network_config":'networkConfig',
    }
    def __init__(self,
                 base_cbt_snapshot_info_proto=None,
                 network_config=None,
            ):

        """Constructor for the RestoreAcropolisVMParam class"""

        # Initialize members of the class
        self.base_cbt_snapshot_info_proto = base_cbt_snapshot_info_proto
        self.network_config = network_config

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
        base_cbt_snapshot_info_proto = cohesity_management_sdk.models.snapshot_info_proto.SnapshotInfoProto.from_dictionary(dictionary.get('baseCbtSnapshotInfoProto')) if dictionary.get('baseCbtSnapshotInfoProto') else None
        network_config = cohesity_management_sdk.models.restore_acropolis_vm_param_network_config_info.RestoreAcropolisVMParam_NetworkConfigInfo.from_dictionary(dictionary.get('networkConfig')) if dictionary.get('networkConfig') else None

        # Return an object of this model
        return cls(
            base_cbt_snapshot_info_proto,
            network_config
)