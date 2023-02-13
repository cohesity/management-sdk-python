# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.erasure_coding_info

class StoragePolicy(object):

    """Implementation of the 'StoragePolicy' model.

    Specifies the storage options applied to a Storage Domain (View Box).

    Attributes:
        app_marker_detection (bool): Specifies Whether to support app marker
            detection. When this is set to true, app markers (like commvault
            markers) will be removed from data and put in separate chunks.
            This way deduplication is improved as it is done on data that has
            no app markers.
        cloud_spill_vault_id (long|int): Specifies the vault id assigned for
            an external Storage Target to facilitate cloud spill.
        compression_policy (CompressionPolicyEnum): Specifies the compression
            setting to be applied to a Storage Domain (View Box).
            'kCompressionNone' indicates that data is not compressed.
            'kCompressionLow' indicates that data is compressed using LZ4 or
            Snappy. 'kCompressionHigh' indicates that data is compressed in
            Gzip.
        deduplicate_compress_delay_secs (int): Specifies the time in seconds
            when deduplication and compression of data on the Storage Domain
            (View Box) starts. If set to 0, deduplication and compression is
            done inline (as the data is being written). Otherwise,
            post-process deduplication and compression is done after the
            specified delay.
        deduplication_enabled (bool): Specifies if deduplication is enabled
            for the Storage Domain (View Box). If deduplication is enabled,
            the Cohesity Cluster eliminates duplicate blocks of repeating data
            stored on the Cluster thus reducing the amount of storage space
            needed to store data.
        encryption_policy (EncryptionPolicyEnum): Specifies the encryption
            setting for the Storage Domain (View Box). 'kEncryptionNone'
            indicates the data is not encrypted. 'kEncryptionStrong' indicates
            the data is encrypted.
        erasure_coding_info (ErasureCodingInfo): Specifies information for
            erasure coding.
        inline_compress (bool): Specifies if compression should occur inline
            (as the data is being written). This field is only relevant if
            compression is enabled. If deduplication is set to inline,
            Cohesity recommends setting compression to inline.
        inline_deduplicate (bool): Specifies if deduplication should occur
            inline (as the data is being written). This field is only relevant
            if deduplication is enabled.
        num_failures_tolerated (int): Number of disk failures to tolerate.
            This is an optional field. Default value is 1 for cluster having 3
            or more nodes. If erasure coding is not enabled, then this
            specifies the replication factor for the Storage Domain (View
            Box). For RF=2, number of failures to tolerate should be specified
            as 1. If erasure coding is enabled, then this value will be same
            as number of coded stripes.
        num_node_failures_tolerated (int): Number of node failures to
            tolerate. If NumNodeFailuresTolerated is set to 2, then we would
            tolerate up to two node failures. If the following is not set,
            then the number of node failures tolerated would be same as
            replication factor - 1 for replicated chunk files or number of
            coded stripes for erasure coding chunk files.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_marker_detection":'appMarkerDetection',
        "cloud_spill_vault_id":'cloudSpillVaultId',
        "compression_policy":'compressionPolicy',
        "deduplicate_compress_delay_secs":'deduplicateCompressDelaySecs',
        "deduplication_enabled":'deduplicationEnabled',
        "encryption_policy":'encryptionPolicy',
        "erasure_coding_info":'erasureCodingInfo',
        "inline_compress":'inlineCompress',
        "inline_deduplicate":'inlineDeduplicate',
        "num_failures_tolerated":'numFailuresTolerated',
        "num_node_failures_tolerated":'numNodeFailuresTolerated'
    }

    def __init__(self,
                 app_marker_detection=None,
                 cloud_spill_vault_id=None,
                 compression_policy=None,
                 deduplicate_compress_delay_secs=None,
                 deduplication_enabled=None,
                 encryption_policy=None,
                 erasure_coding_info=None,
                 inline_compress=None,
                 inline_deduplicate=None,
                 num_failures_tolerated=None,
                 num_node_failures_tolerated=None):
        """Constructor for the StoragePolicy class"""

        # Initialize members of the class
        self.app_marker_detection = app_marker_detection
        self.cloud_spill_vault_id = cloud_spill_vault_id
        self.compression_policy = compression_policy
        self.deduplicate_compress_delay_secs = deduplicate_compress_delay_secs
        self.deduplication_enabled = deduplication_enabled
        self.encryption_policy = encryption_policy
        self.erasure_coding_info = erasure_coding_info
        self.inline_compress = inline_compress
        self.inline_deduplicate = inline_deduplicate
        self.num_failures_tolerated = num_failures_tolerated
        self.num_node_failures_tolerated = num_node_failures_tolerated


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
        app_marker_detection = dictionary.get('appMarkerDetection')
        cloud_spill_vault_id = dictionary.get('cloudSpillVaultId')
        compression_policy = dictionary.get('compressionPolicy')
        deduplicate_compress_delay_secs = dictionary.get('deduplicateCompressDelaySecs')
        deduplication_enabled = dictionary.get('deduplicationEnabled')
        encryption_policy = dictionary.get('encryptionPolicy')
        erasure_coding_info = cohesity_management_sdk.models.erasure_coding_info.ErasureCodingInfo.from_dictionary(dictionary.get('erasureCodingInfo')) if dictionary.get('erasureCodingInfo') else None
        inline_compress = dictionary.get('inlineCompress')
        inline_deduplicate = dictionary.get('inlineDeduplicate')
        num_failures_tolerated = dictionary.get('numFailuresTolerated')
        num_node_failures_tolerated = dictionary.get('numNodeFailuresTolerated')

        # Return an object of this model
        return cls(app_marker_detection,
                   cloud_spill_vault_id,
                   compression_policy,
                   deduplicate_compress_delay_secs,
                   deduplication_enabled,
                   encryption_policy,
                   erasure_coding_info,
                   inline_compress,
                   inline_deduplicate,
                   num_failures_tolerated,
                   num_node_failures_tolerated)


