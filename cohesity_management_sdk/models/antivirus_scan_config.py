# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.file_extension_filter

class AntivirusScanConfig(object):

    """Implementation of the 'AntivirusScanConfig' model.

    Specifies the antivirus scan config settings for this View.

    Attributes:
        block_access_on_scan_failure (bool): Specifies whether block access to
            the file when antivirus scan fails.
        is_enabled (bool): Specifies whether the antivirus service is enabled
            or not.
        maximum_scan_file_size (long|int): Specifies maximum file size that
            will be sent to antivirus server for scanning. if greater than
            zero, the file size that exceeds this size would be skipped from
            virus scan.
        scan_filter (FileExtensionFilter): TODO: type description here.
        scan_on_access (bool): Specifies whether to scan a file when it is
            opened.
        scan_on_close (bool): Specifies whether to scan a file when it is
            closed after modify.
        scan_timeout_usecs (int): Specifies the maximum amount of time that a
            scan can take before timing out.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "block_access_on_scan_failure":'blockAccessOnScanFailure',
        "is_enabled":'isEnabled',
        "maximum_scan_file_size":'maximumScanFileSize',
        "scan_filter":'scanFilter',
        "scan_on_access":'scanOnAccess',
        "scan_on_close":'scanOnClose',
        "scan_timeout_usecs":'scanTimeoutUsecs'
    }

    def __init__(self,
                 block_access_on_scan_failure=None,
                 is_enabled=None,
                 maximum_scan_file_size=None,
                 scan_filter=None,
                 scan_on_access=None,
                 scan_on_close=None,
                 scan_timeout_usecs=None):
        """Constructor for the AntivirusScanConfig class"""

        # Initialize members of the class
        self.block_access_on_scan_failure = block_access_on_scan_failure
        self.is_enabled = is_enabled
        self.maximum_scan_file_size = maximum_scan_file_size
        self.scan_filter = scan_filter
        self.scan_on_access = scan_on_access
        self.scan_on_close = scan_on_close
        self.scan_timeout_usecs = scan_timeout_usecs


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
        block_access_on_scan_failure = dictionary.get('blockAccessOnScanFailure')
        is_enabled = dictionary.get('isEnabled')
        maximum_scan_file_size = dictionary.get('maximumScanFileSize')
        scan_filter = cohesity_management_sdk.models.file_extension_filter.FileExtensionFilter.from_dictionary(dictionary.get('scanFilter')) if dictionary.get('scanFilter') else None
        scan_on_access = dictionary.get('scanOnAccess')
        scan_on_close = dictionary.get('scanOnClose')
        scan_timeout_usecs = dictionary.get('scanTimeoutUsecs')

        # Return an object of this model
        return cls(block_access_on_scan_failure,
                   is_enabled,
                   maximum_scan_file_size,
                   scan_filter,
                   scan_on_access,
                   scan_on_close,
                   scan_timeout_usecs)


