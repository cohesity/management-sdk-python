# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_config_proto_qo_s_mapping
import cohesity_management_sdk.models.cluster_config_proto_storage_policy_override
import cohesity_management_sdk.models.cluster_config_proto_subnet
import cohesity_management_sdk.models.view_id_mapping_proto_protocol_access_info


class ViewParams(object):

    """Implementation of the 'ViewParams' model.

    TODO: type description here.


    Attributes:

        client_subnet_whitelist_vec (list of ClusterConfigProto_Subnet): List
            of external client subnets from where requests will be received for
            the new view.
        disable_nfs_access (bool): Whether to disable NFS access in the new
            view.
        protocol_access_info (ViewIdMappingProto_ProtocolAccessInfo): The
            protocol access override (if any) of the view.
        qos_mapping_vec (list of ClusterConfigProto_QoSMapping): The qos
            mappings (if any) for the new view.
        storage_policy_override (ClusterConfigProto_StoragePolicyOverride): The
            storage policy override (if any) for the new view.
        view_description (string): The description to be applied to the new
            view.
        worm_lock_expiry_usecs (long|int): This value 'worm_lock_expiry_usecs'
            if specified will be set on the cloned view. This guarantees that
            the cloned view cannot be removed till the specified timestamp has
            reached. NOTE: If this is specified the clone view will be marked
            as immutable.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "client_subnet_whitelist_vec":'clientSubnetWhitelistVec',
        "disable_nfs_access":'disableNfsAccess',
        "protocol_access_info":'protocolAccessInfo',
        "qos_mapping_vec":'qosMappingVec',
        "storage_policy_override":'storagePolicyOverride',
        "view_description":'viewDescription',
        "worm_lock_expiry_usecs":'wormLockExpiryUsecs',
    }
    def __init__(self,
                 client_subnet_whitelist_vec=None,
                 disable_nfs_access=None,
                 protocol_access_info=None,
                 qos_mapping_vec=None,
                 storage_policy_override=None,
                 view_description=None,
                 worm_lock_expiry_usecs=None,
            ):

        """Constructor for the ViewParams class"""

        # Initialize members of the class
        self.client_subnet_whitelist_vec = client_subnet_whitelist_vec
        self.disable_nfs_access = disable_nfs_access
        self.protocol_access_info = protocol_access_info
        self.qos_mapping_vec = qos_mapping_vec
        self.storage_policy_override = storage_policy_override
        self.view_description = view_description
        self.worm_lock_expiry_usecs = worm_lock_expiry_usecs

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
        client_subnet_whitelist_vec = None
        if dictionary.get('clientSubnetWhitelistVec') != None:
            client_subnet_whitelist_vec = list()
            for structure in dictionary.get('clientSubnetWhitelistVec'):
                client_subnet_whitelist_vec.append(cohesity_management_sdk.models.cluster_config_proto_subnet.ClusterConfigProto_Subnet.from_dictionary(structure))
        disable_nfs_access = dictionary.get('disableNfsAccess')
        protocol_access_info = cohesity_management_sdk.models.view_id_mapping_proto_protocol_access_info.ViewIdMappingProto_ProtocolAccessInfo.from_dictionary(dictionary.get('protocolAccessInfo')) if dictionary.get('protocolAccessInfo') else None
        qos_mapping_vec = None
        if dictionary.get('qosMappingVec') != None:
            qos_mapping_vec = list()
            for structure in dictionary.get('qosMappingVec'):
                qos_mapping_vec.append(cohesity_management_sdk.models.cluster_config_proto_qo_s_mapping.ClusterConfigProto_QoSMapping.from_dictionary(structure))
        storage_policy_override = cohesity_management_sdk.models.cluster_config_proto_storage_policy_override.ClusterConfigProto_StoragePolicyOverride.from_dictionary(dictionary.get('storagePolicyOverride')) if dictionary.get('storagePolicyOverride') else None
        view_description = dictionary.get('viewDescription')
        worm_lock_expiry_usecs = dictionary.get('wormLockExpiryUsecs')

        # Return an object of this model
        return cls(
            client_subnet_whitelist_vec,
            disable_nfs_access,
            protocol_access_info,
            qos_mapping_vec,
            storage_policy_override,
            view_description,
            worm_lock_expiry_usecs
)