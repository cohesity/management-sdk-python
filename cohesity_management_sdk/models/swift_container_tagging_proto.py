# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.user
import cohesity_management_sdk.models.project

class SwiftContainerTaggingProto(object):

    """Implementation of the 'SwiftContainerTaggingProto' model.

    Proto to define the tagging info associated with a Swift container.

    Attributes:
        acl_root_user (User): [optional] The Keystone user who could get grant of
            access to this container after creation by ACL. It is used to let
            this user get access to this container if noboby has any Swift
            roles from Keystone. If this user has a Swift role, other Keystone
            users could get grant by this 'root' user through ACL.
            If 'acl_root_user' is set, below fields are mandatory.
            [mandatory] acl_root_user.name
            [mandatory] acl_root_user.domain.name
        project_tag (Project): Start IP of the range

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "acl_root_user": 'aclRootUser',
        "project_tag": 'projectTag'
    }

    def __init__(self,
                 acl_root_user=None,
                 project_tag=None):
        """Constructor for the SwiftContainerTaggingProto class"""

        # Initialize members of the class
        self.acl_root_user = acl_root_user
        self.project_tag = project_tag


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
        acl_root_user = cohesity_management_sdk.models.user.User.from_dictionary(dictionary.get('aclRootUser')) if dictionary.get('aclRootUser') else None
        project_tag = cohesity_management_sdk.models.project.Project.from_dictionary(dictionary.get('projectTag')) if dictionary.get('projectTag') else None

        # Return an object of this model
        return cls(acl_root_user,
                   project_tag)


