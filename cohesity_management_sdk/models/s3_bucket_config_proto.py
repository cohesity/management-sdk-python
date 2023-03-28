# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.acl_proto
import cohesity_management_sdk.models.bucket_ownership_controls
import cohesity_management_sdk.models.bucket_policy
import cohesity_management_sdk.models.lifecycle_config_proto
import cohesity_management_sdk.models.owner_info
import cohesity_management_sdk.models.s3_bucket_config_proto_tag_map_entry
import cohesity_management_sdk.models.swift_container_tagging_proto


class S3BucketConfigProto(object):

    """Implementation of the 'S3BucketConfigProto' model.

    TODO: type description here.


    Attributes:

        acl (ACLProto): ACL of the bucket.
        bucket_policy (BucketPolicy): Policy in effect for the bucket.
        enable_obj_store_access (bool): If set to false, we disable access to
            view using S3/Swift protocol. This overrides any
            'protocol_access_info' set on view for S3/Swift. This flag is added
            as the transition for S3 native to non-S3 native is disabled and
            therefore the access using S3/Swift protocol cannot be disabled by
            madrox.
        init_cluster_id (long|int): The cluster id for the cluster where the
            view was initially created without replication. For view on Rx, the
            init_cluster_id will remain same as that of the initial cluster.
        init_cluster_incarnation_id (long|int): The cluster incarnation id for
            the cluster where the view was initially created without
            replication. For view on Rx, the init_incarnation_cluster_id will
            remain same as that of the initial cluster.
        lifecycle_config (LifecycleConfigProto): Lifecycle policy of the
            bucket. If not specified, no lifecycle management is performed for
            objects in this bucket.
        owner_info (OwnerInfo): Information about the bucket owner.
        ownership_controls (BucketOwnershipControls): Bucket Ownership Controls
            for the bucket.
        protocol_type (int): Protocol type of this bucket.
        swift_container_tag (SwiftContainerTaggingProto): Swfit container
            tagging information.
        tag_map (list of S3BucketConfigProto_TagMapEntry): Tags (or labels)
            assigned to the bucket. Tags are set of <key, value> pairs.
        versioning_state (int): TODO: Type description here.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "acl":'acl',
        "bucket_policy":'bucketPolicy',
        "enable_obj_store_access":'enableObjStoreAccess',
        "init_cluster_id":'initClusterId',
        "init_cluster_incarnation_id":'initClusterIncarnationId',
        "lifecycle_config":'lifecycleConfig',
        "owner_info":'ownerInfo',
        "ownership_controls":'ownershipControls',
        "protocol_type":'protocolType',
        "swift_container_tag":'swiftContainerTag',
        "tag_map":'tagMap',
        "versioning_state":'versioningState',
    }
    def __init__(self,
                 acl=None,
                 bucket_policy=None,
                 enable_obj_store_access=None,
                 init_cluster_id=None,
                 init_cluster_incarnation_id=None,
                 lifecycle_config=None,
                 owner_info=None,
                 ownership_controls=None,
                 protocol_type=None,
                 swift_container_tag=None,
                 tag_map=None,
                 versioning_state=None,
            ):

        """Constructor for the S3BucketConfigProto class"""

        # Initialize members of the class
        self.acl = acl
        self.bucket_policy = bucket_policy
        self.enable_obj_store_access = enable_obj_store_access
        self.init_cluster_id = init_cluster_id
        self.init_cluster_incarnation_id = init_cluster_incarnation_id
        self.lifecycle_config = lifecycle_config
        self.owner_info = owner_info
        self.ownership_controls = ownership_controls
        self.protocol_type = protocol_type
        self.swift_container_tag = swift_container_tag
        self.tag_map = tag_map
        self.versioning_state = versioning_state

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
        acl = cohesity_management_sdk.models.acl_proto.ACLProto.from_dictionary(dictionary.get('acl')) if dictionary.get('acl') else None
        bucket_policy = cohesity_management_sdk.models.bucket_policy.BucketPolicy.from_dictionary(dictionary.get('bucketPolicy')) if dictionary.get('bucketPolicy') else None
        enable_obj_store_access = dictionary.get('enableObjStoreAccess')
        init_cluster_id = dictionary.get('initClusterId')
        init_cluster_incarnation_id = dictionary.get('initClusterIncarnationId')
        lifecycle_config = cohesity_management_sdk.models.lifecycle_config_proto.LifecycleConfigProto.from_dictionary(dictionary.get('lifecycleConfig')) if dictionary.get('lifecycleConfig') else None
        owner_info = cohesity_management_sdk.models.owner_info.OwnerInfo.from_dictionary(dictionary.get('ownerInfo')) if dictionary.get('ownerInfo') else None
        ownership_controls = cohesity_management_sdk.models.bucket_ownership_controls.BucketOwnershipControls.from_dictionary(dictionary.get('ownershipControls')) if dictionary.get('ownershipControls') else None
        protocol_type = dictionary.get('protocolType')
        swift_container_tag = cohesity_management_sdk.models.swift_container_tagging_proto.SwiftContainerTaggingProto.from_dictionary(dictionary.get('swiftContainerTag')) if dictionary.get('swiftContainerTag') else None
        tag_map = None
        if dictionary.get('tagMap') != None:
            tag_map = list()
            for structure in dictionary.get('tagMap'):
                tag_map.append(cohesity_management_sdk.models.s3_bucket_config_proto_tag_map_entry.S3BucketConfigProto_TagMapEntry.from_dictionary(structure))
        versioning_state = dictionary.get('versioningState')

        # Return an object of this model
        return cls(
            acl,
            bucket_policy,
            enable_obj_store_access,
            init_cluster_id,
            init_cluster_incarnation_id,
            lifecycle_config,
            owner_info,
            ownership_controls,
            protocol_type,
            swift_container_tag,
            tag_map,
            versioning_state
)