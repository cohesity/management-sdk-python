# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.acl_proto
import cohesity_management_sdk.models.bucket_ownership_controls
import cohesity_management_sdk.models.bucket_policy
import cohesity_management_sdk.models.lifecycle_config_proto
import cohesity_management_sdk.models.owner_info
import cohesity_management_sdk.models.s3_bucket_config_proto_prefix_to_child_bucket_map_entry
import cohesity_management_sdk.models.s3_bucket_config_proto_tag_map_entry
import cohesity_management_sdk.models.swift_container_tagging_proto


class S3BucketConfigProto(object):

    """Implementation of the 'S3BucketConfigProto' model.

    TODO: type description here.


    Attributes:

        acl (ACLProto): ACL of the bucket.
        bucket_policy (BucketPolicy): Policy in effect for the bucket.
        efficient_mpu_enabled (bool): bool representing whether this mpu
            structure is based on S3 MPU 2.0
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
        object_tags_added (bool): Whether this view has ever had any object
            with tags. This should be enabled only when first object tag is
            ever put in this view.
        owner_info (OwnerInfo): Information about the bucket owner.
        ownership_controls (BucketOwnershipControls): Bucket Ownership Controls
            for the bucket.
        prefix_delimiter (string): Delimiter used in prefix based request
            routing. An application needs to explicitly set the
            prefix_delimiter during bucket creation. If the prefix_delimiter is
            not explicitly set, '/' will be used as the default prefix
            delimiter for buckets that has prefix-based-routing enabled.
            SnapDiff backups uses '/' in the object names hence it was chosen
            as the default prefix to avoid further UI changes in this project.
            If there are other use cases that require a different
            prefix_delimiter, it has to be set during bucket creation. Once
            prefix_delimiter is chosen, it cannot be changed.
        prefix_to_child_bucket_map (list of
            S3BucketConfigProto_PrefixToChildBucketMapEntry): Stores the prefix
            to child bucket mapping to enable prefix based routing of object
            requests to child buckets.
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
        "efficient_mpu_enabled":'efficientMpuEnabled',
        "enable_obj_store_access":'enableObjStoreAccess',
        "init_cluster_id":'initClusterId',
        "init_cluster_incarnation_id":'initClusterIncarnationId',
        "lifecycle_config":'lifecycleConfig',
        "object_tags_added":'objectTagsAdded',
        "owner_info":'ownerInfo',
        "ownership_controls":'ownershipControls',
        "prefix_delimiter":'prefixDelimiter',
        "prefix_to_child_bucket_map":'prefixToChildBucketMap',
        "protocol_type":'protocolType',
        "swift_container_tag":'swiftContainerTag',
        "tag_map":'tagMap',
        "versioning_state":'versioningState',
    }
    def __init__(self,
                 acl=None,
                 bucket_policy=None,
                 efficient_mpu_enabled=None,
                 enable_obj_store_access=None,
                 init_cluster_id=None,
                 init_cluster_incarnation_id=None,
                 lifecycle_config=None,
                 object_tags_added=None,
                 owner_info=None,
                 ownership_controls=None,
                 prefix_delimiter=None,
                 prefix_to_child_bucket_map=None,
                 protocol_type=None,
                 swift_container_tag=None,
                 tag_map=None,
                 versioning_state=None,
            ):

        """Constructor for the S3BucketConfigProto class"""

        # Initialize members of the class
        self.acl = acl
        self.bucket_policy = bucket_policy
        self.efficient_mpu_enabled = efficient_mpu_enabled
        self.enable_obj_store_access = enable_obj_store_access
        self.init_cluster_id = init_cluster_id
        self.init_cluster_incarnation_id = init_cluster_incarnation_id
        self.lifecycle_config = lifecycle_config
        self.object_tags_added = object_tags_added
        self.owner_info = owner_info
        self.ownership_controls = ownership_controls
        self.prefix_delimiter = prefix_delimiter
        self.prefix_to_child_bucket_map = prefix_to_child_bucket_map
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
        efficient_mpu_enabled = dictionary.get('efficientMpuEnabled')
        enable_obj_store_access = dictionary.get('enableObjStoreAccess')
        init_cluster_id = dictionary.get('initClusterId')
        init_cluster_incarnation_id = dictionary.get('initClusterIncarnationId')
        lifecycle_config = cohesity_management_sdk.models.lifecycle_config_proto.LifecycleConfigProto.from_dictionary(dictionary.get('lifecycleConfig')) if dictionary.get('lifecycleConfig') else None
        object_tags_added = dictionary.get('objectTagsAdded')
        owner_info = cohesity_management_sdk.models.owner_info.OwnerInfo.from_dictionary(dictionary.get('ownerInfo')) if dictionary.get('ownerInfo') else None
        ownership_controls = cohesity_management_sdk.models.bucket_ownership_controls.BucketOwnershipControls.from_dictionary(dictionary.get('ownershipControls')) if dictionary.get('ownershipControls') else None
        prefix_delimiter = dictionary.get('prefixDelimiter')
        prefix_to_child_bucket_map = None
        if dictionary.get('prefixToChildBucketMap') != None:
            prefix_to_child_bucket_map = list()
            for structure in dictionary.get('prefixToChildBucketMap'):
                prefix_to_child_bucket_map.append(cohesity_management_sdk.models.s3_bucket_config_proto_prefix_to_child_bucket_map_entry.S3BucketConfigProto_PrefixToChildBucketMapEntry.from_dictionary(structure))
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
            efficient_mpu_enabled,
            enable_obj_store_access,
            init_cluster_id,
            init_cluster_incarnation_id,
            lifecycle_config,
            object_tags_added,
            owner_info,
            ownership_controls,
            prefix_delimiter,
            prefix_to_child_bucket_map,
            protocol_type,
            swift_container_tag,
            tag_map,
            versioning_state
)