# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.bandwidth_limit

class VaultBandwidthLimits(object):

    """Implementation of the 'VaultBandwidthLimits' model.

    VaultBandwidthLimits represents the network bandwidth limits
    while uploading/downloading data to/from the external media.

    Attributes:
        cloud_tier_download (BandwidthLimit): Specifies the max rate limit
            at which we download the data to cloud tier vaults.
        cloud_tier_upload (BandwidthLimit): Specifies the max rate limit at
            which we upload the data to cloud tier vaults.
        download (BandwidthLimit): Specifies settings for limiting the data
            transfer rate between the local and remote Clusters.
        upload (BandwidthLimit): Specifies settings for limiting the data
            transfer rate between the local and remote Clusters.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_tier_download":'cloudTierDownload',
        "cloud_tier_upload":'cloudTierUpload',
        "download":'download',
        "upload":'upload'
    }

    def __init__(self,
                 cloud_tier_download=None,
                 cloud_tier_upload=None,
                 download=None,
                 upload=None):
        """Constructor for the VaultBandwidthLimits class"""

        # Initialize members of the class
        self.cloud_tier_download = cloud_tier_download
        self.cloud_tier_upload = cloud_tier_upload
        self.download = download
        self.upload = upload


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
        cloud_tier_download = cohesity_management_sdk.models.bandwidth_limit.BandwidthLimit.from_dictionary(dictionary.get('cloudTierDownload')) if dictionary.get('cloudTierDownload') else None
        cloud_tier_upload = cohesity_management_sdk.models.bandwidth_limit.BandwidthLimit.from_dictionary(dictionary.get('cloudTierUpload')) if dictionary.get('cloudTierUpload') else None
        download = cohesity_management_sdk.models.bandwidth_limit.BandwidthLimit.from_dictionary(dictionary.get('download')) if dictionary.get('download') else None
        upload = cohesity_management_sdk.models.bandwidth_limit.BandwidthLimit.from_dictionary(dictionary.get('upload')) if dictionary.get('upload') else None

        # Return an object of this model
        return cls(cloud_tier_download,
                   cloud_tier_upload,
                   download,
                   upload)


