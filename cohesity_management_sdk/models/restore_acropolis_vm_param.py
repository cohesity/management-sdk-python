# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.snapshot_info_proto
import cohesity_management_sdk.models.restore_acropolis_vm_param_network_config_info

class RestoreAcropolisVMParam(object):

    """Implementation of the 'RestoreAcropolisVMParam' model.

    TODO: type model description here.

    Attributes:
        base_cbt_snapshot_info_proto (SnapshotInfoProto): Each available
            extension is listed below along with the location of the proto
            file (relative to magneto/connectors) where it is defined. The
            only exception is view.proto and physical.proto which reside in
            magneto/base.  SnapshotInfoProto extension
            Location              Extn
            ===================================================================
            ========== vmware::SnapshotInfo::vmware_snapshot_info
            vmware/vmware.proto       100 sql::SnapshotInfo::sql_snapshot_info
            sql/sql.proto             101
            view::SnapshotInfo::view_snapshot_info         base/view.proto
            102 physical::SnapshotInfo::physical_snapshot_info
            base/physical.proto       103 san::SnapshotInfo::san_snapshot_info
            san/san.proto             104
            file::SnapshotInfo::file_snapshot_info         file/file.proto
            105 hyperv::SnapshotInfo::hyperv_snapshot_info
            hyperv/hyperv.proto       106 acropolis::SnapshotInfo::
            acropolis_snapshot_info
            acropolis/acropolis.proto 107 kvm::SnapshotInfo::kvm_snapshot_info
            kvm/kvm.proto             108
            app_file::SnapshotInfo::app_file_snapshot_info
            app_file/app_file.proto   109
            oracle::SnapshotInfo::oracle_snapshot_info     oracle/oracle.proto
            110 aws::SnapshotInfo::aws_snapshot_info           aws/aws.proto
            111 outlook::SnapshotInfo::outlook_snapshot_info
            outlook/outlook.proto     112
            azure::SnapshotInfo::azure_snapshot_info       azure/azure.proto
            113 gcp::SnapshotInfo::gcp_snapshot_info           gcp/gcp.proto
            114 ad::SnapshotInfo::ad_snapshot_info             ad/ad.proto
            115 MSGraph::SnapshotInfo::one_drive_snapshot_info
            ms_graph/graph.proto      116 kubernetes::SnapshotInfo::
            kubernetes_snapshot_info kubernetes/kubernetes.proto 117
            aws::RDSSnapshotInfo::rds_snapshot_info        aws/aws.proto
            118 o365::SnapshotInfo::o365_snapshot_info         o365/o365.proto
            119 exchange::SnapshotInfo::exchange_snapshot_info
            exchange/exchange.proto   120
            o365::SharepointSnapshotInfo::sharepoint_snapshot_info
            o365/o365.proto           121
            ===================================================================
            ==========
        network_config (RestoreAcropolisVMParamNetworkConfigInfo): Proto to
            define the network configuration to be applied to the restored
            VM.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "base_cbt_snapshot_info_proto":'baseCbtSnapshotInfoProto',
        "network_config":'networkConfig'
    }

    def __init__(self,
                 base_cbt_snapshot_info_proto=None,
                 network_config=None):
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
        network_config = cohesity_management_sdk.models.restore_acropolis_vm_param_network_config_info.RestoreAcropolisVMParamNetworkConfigInfo.from_dictionary(dictionary.get('networkConfig')) if dictionary.get('networkConfig') else None

        # Return an object of this model
        return cls(base_cbt_snapshot_info_proto,
                   network_config)


