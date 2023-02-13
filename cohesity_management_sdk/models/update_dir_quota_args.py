# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.dir_quota_policy

class UpdateDirQuotaArgs(object):

    """Implementation of the 'UpdateDirQuotaArgs' model.

    Specifies the arguments for updating the directory quota policies. This
    structure can be used for adding, updating and removing the policies.

    Attributes:
        disable_dir_quota (bool): Specifies directory quota to be disabled on
            the view.
        quota (DirQuotaPolicy): Specifies a policy configuration for the
            directory quota. A policy is the sole entity which describes the
            usage limits of a directory in a view.  `DirPath` is the
            identifier of a policy. It must be specified for adding, updating
            or removing a policy. If `Policy` is not set, then it is
            considered to be removed.
        view_name (string): Specifies the name of the view.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disable_dir_quota":'disableDirQuota',
        "quota":'quota',
        "view_name":'viewName'
    }

    def __init__(self,
                 disable_dir_quota=None,
                 quota=None,
                 view_name=None):
        """Constructor for the UpdateDirQuotaArgs class"""

        # Initialize members of the class
        self.disable_dir_quota = disable_dir_quota
        self.quota = quota
        self.view_name = view_name


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
        disable_dir_quota = dictionary.get('disableDirQuota')
        quota = cohesity_management_sdk.models.dir_quota_policy.DirQuotaPolicy.from_dictionary(dictionary.get('quota')) if dictionary.get('quota') else None
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(disable_dir_quota,
                   quota,
                   view_name)


