# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.bandwidth_limit

class VaultBandwidthLimits(object):

    """Implementation of the 'VaultBandwidthLimits' model.

    VaultBandwidthLimits represents the network bandwidth limits
    while uploading/downloading data to/from the external media.

    Attributes:
        download (BandwidthLimit): Specifies settings for limiting the data
            transfer rate between the local and remote Clusters.
        upload (BandwidthLimit): Specifies settings for limiting the data
            transfer rate between the local and remote Clusters.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "download":'download',
        "upload":'upload'
    }

    def __init__(self,
                 download=None,
                 upload=None):
        """Constructor for the VaultBandwidthLimits class"""

        # Initialize members of the class
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
        download = cohesity_management_sdk.models.bandwidth_limit.BandwidthLimit.from_dictionary(dictionary.get('download')) if dictionary.get('download') else None
        upload = cohesity_management_sdk.models.bandwidth_limit.BandwidthLimit.from_dictionary(dictionary.get('upload')) if dictionary.get('upload') else None

        # Return an object of this model
        return cls(download,
                   upload)


