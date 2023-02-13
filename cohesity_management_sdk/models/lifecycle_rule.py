# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.abort_incomplete_multipart_upload_action
import cohesity_management_sdk.models.expiration_action
import cohesity_management_sdk.models.lifecycle_rule_filter
import cohesity_management_sdk.models.noncurrent_version_expiration_action

class LifecycleRule(object):

    """Implementation of the 'LifecycleRule' model.

    Structure to hold feature usage on cluster side.

    Attributes:
        abort_incomplete_multipart_upload (AbortIncompleteMultipartUploadAction):
            Specifies the days since the initiation of an incomplete multipart
            upload before permanently removing all parts of the upload.
        expiration (ExpirationAction): Specifies the expiration for the
            lifecycle of the object in the form of date, days and, whether the
            object has a delete marker.
        filter (LifecycleRuleFilter): The Filter is used to identify objects
            that a Lifecycle Rule applies to.
        id (string):  Unique identifier for the rule. The value cannot be longer
            than 255 characters.
        noncurrent_version_expiration (NoncurrentVersionExpirationAction): Number
            of VM spinned.
        prefix (string): The prefix is used to identify objects that a lifecycle rule
          applies to.
        status (bool): If set, the rule is currently being applied. If
            'Disabled', the rule is not currently being applied.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "abort_incomplete_multipart_upload": 'abortIncompleteMultipartUpload',
        "expiration": 'expiration',
        "filter": 'filter',
        "id": 'id',
        "noncurrent_version_expiration":'noncurrentVersionExpiration',
        "prefix":'prefix',
        "status":'status'
    }

    def __init__(self,
                 abort_incomplete_multipart_upload=None,
                 expiration=None,
                 filter=None,
                 id=None,
                 noncurrent_version_expiration=None,
                 prefix=None,
                 status=None):
        """Constructor for the LifecycleRule class"""

        # Initialize members of the class
        self.abort_incomplete_multipart_upload = abort_incomplete_multipart_upload
        self.expiration = expiration
        self.filter = filter
        self.id = id
        self.noncurrent_version_expiration = noncurrent_version_expiration
        self.prefix = prefix
        self.status = status

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
        abort_incomplete_multipart_upload = cohesity_management_sdk.models.abort_incomplete_multipart_upload_action.AbortIncompleteMultipartUploadAction.from_dictionary(dictionary.get('abortIncompleteMultipartUpload')) if dictionary.get('abortIncompleteMultipartUpload') else None
        expiration = cohesity_management_sdk.models.expiration_action.ExpirationAction.from_dictionary(dictionary.get('expiration')) if dictionary.get('expiration') else None
        filter = cohesity_management_sdk.models.lifecycle_rule_filter.LifecycleRuleFilter.from_dictionary(dictionary.get('filter')) if dictionary.get('filter') else None
        id = dictionary.get('id')
        noncurrent_version_expiration = cohesity_management_sdk.models.noncurrent_version_expiration_action.NoncurrentVersionExpirationAction.from_dictionary(dictionary.get('noncurrentVersionExpiration')) if dictionary.get('noncurrentVersionExpiration') else None
        prefix = dictionary.get('prefix')
        status = dictionary.get('status')

        # Return an object of this model
        return cls(abort_incomplete_multipart_upload,
                   expiration,
                   filter,
                   id,
                   noncurrent_version_expiration,
                   prefix,
                   status)


