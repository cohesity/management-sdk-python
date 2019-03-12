# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class PrivilegeInformation(object):

    """Implementation of the 'Privilege Information.' model.

    Specifies details about a privilege such as the category,
    description, name, etc.

    Attributes:
        category (string): Specifies a category for the privilege such as
            'Access Management'.
        description (string): Specifies a description defining what the
            privilege provides.
        is_custom_role_default (bool): Specifies if this privilege is
            automatically assigned to custom roles.
        is_special (bool): Specifies if this privilege is automatically
            assigned to the default System Admin user called 'admin'. If true,
            the privilege is NOT assigned to the default System Admin user
            called 'admin'. By default, privileges are automatically assigned
            to the default System Admin user called 'admin'.
        is_view_only (bool): Specifies if privilege is view-only privilege
            that cannot make changes.
        label (string): Specifies the label for the privilege as displayed on
            the Cohesity Dashboard such as 'Access Management View'.
        name (string): Specifies the Cluster name for the privilege such as
            PRINCIPAL_VIEW.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "category":'category',
        "description":'description',
        "is_custom_role_default":'isCustomRoleDefault',
        "is_special":'isSpecial',
        "is_view_only":'isViewOnly',
        "label":'label',
        "name":'name'
    }

    def __init__(self,
                 category=None,
                 description=None,
                 is_custom_role_default=None,
                 is_special=None,
                 is_view_only=None,
                 label=None,
                 name=None):
        """Constructor for the PrivilegeInformation class"""

        # Initialize members of the class
        self.category = category
        self.description = description
        self.is_custom_role_default = is_custom_role_default
        self.is_special = is_special
        self.is_view_only = is_view_only
        self.label = label
        self.name = name


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
        category = dictionary.get('category')
        description = dictionary.get('description')
        is_custom_role_default = dictionary.get('isCustomRoleDefault')
        is_special = dictionary.get('isSpecial')
        is_view_only = dictionary.get('isViewOnly')
        label = dictionary.get('label')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(category,
                   description,
                   is_custom_role_default,
                   is_special,
                   is_view_only,
                   label,
                   name)


