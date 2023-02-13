# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.acl_proto
import cohesity_management_sdk.models.lifecycle_config_proto
import cohesity_management_sdk.models.owner_info
import cohesity_management_sdk.models.swift_container_tagging_proto
import cohesity_management_sdk.models.s3_bucket_config_proto_tag_map_entry

class S3BucketConfigProto(object):

    """Implementation of the 'S3BucketConfigProto' model.

    Proto to define the config/metadata of a S3 bucket.

    Attributes:
        acl (ACLProto): description: ACL of the bucket.
        lifecycle_config (LifecycleConfigProto): Lifecycle policy of the
            bucket. If not specified, no lifecycle management is performed
            for objects in this bucket.
        owner_info (OwnerInfo): Information about the bucket owner.
        protocol_type (int): Protocol type of this bucket.
        swift_container_tag (SwiftContainerTaggingProto): Swfit container
            tagging information.
        tag_map (list of S3BucketConfigProto_TagMapEntry): Tags (or labels)
            assigned to the bucket. Tags are set of <key, value> pairs.
        versioning_state (int): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "acl": 'acl',
        "lifecycle_config": 'lifecycleConfig',
        "owner_info": 'ownerInfo',
        "protocol_type":'protocolType',
        "swift_container_tag":'swiftContainerTag',
        "tag_map":'tagMap',
        "versioning_state":'versioningState'
    }

    def __init__(self,
                 acl=None,
                 lifecycle_config=None,
                 owner_info=None,
                 protocol_type=None,
                 swift_container_tag=None,
                 tag_map=None,
                 versioning_state=None
                 ):
        """Constructor for the S3BucketConfigProto class"""

        # Initialize members of the class
        self.acl = acl
        self.lifecycle_config = lifecycle_config
        self.owner_info = owner_info
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
        lifecycle_config = cohesity_management_sdk.models.lifecycle_config_proto.LifecycleConfigProto.from_dictionary(dictionary.get('lifecycleConfig')) if dictionary.get('lifecycleConfig') else None
        owner_info = cohesity_management_sdk.models.owner_info.OwnerInfo.from_dictionary(dictionary.get('ownerInfo')) if dictionary.get('ownerInfo') else None
        protocol_type = dictionary.get('protocolType')
        swift_container_tag = cohesity_management_sdk.models.swift_container_tagging_proto.SwiftContainerTaggingProto.from_dictionary(dictionary.get('swiftContainerTag')) if dictionary.get('swiftContainerTag') else None
        tag_map = None
        if dictionary.get('tagMap') != None:
            tag_map = list()
            for structure in dictionary.get('tagMap'):
                tag_map.append(cohesity_management_sdk.models.s3_bucket_config_proto_tag_map_entry.S3BucketConfigProto_TagMapEntry.from_dictionary(structure))
        versioning_state = dictionary.get('versioningState')

        # Return an object of this model
        return cls(acl,
                   lifecycle_config,
                   owner_info,
                   protocol_type,
                   swift_container_tag,
                   tag_map,
                   versioning_state)


