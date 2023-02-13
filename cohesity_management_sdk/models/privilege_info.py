# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PrivilegeInfo(object):

    """Implementation of the 'PrivilegeInfo' model.

    Specifies details about a privilege such as the category,
    description, name, etc.

    Attributes:
        privilege_id (PrivilegeIdEnum): Specifies unique id for a privilege.
            This number must be unique when creating a new privilege. Type for
            unique privilege Id values. All below enum values specify a value
            for all uniquely defined privileges in Cohesity.
        category (string): Specifies a category for the privilege such as
            'Access Management'.
        description (string): Specifies a description defining what the
            privilege provides.
        is_available_on_helios (bool): Specifies that this privilege is
            available for Helios operations.
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
        "privilege_id":'PrivilegeId',
        "category":'category',
        "description":'description',
        "is_available_on_helios":'isAvailableOnHelios',
        "is_custom_role_default":'isCustomRoleDefault',
        "is_special":'isSpecial',
        "is_view_only":'isViewOnly',
        "label":'label',
        "name":'name'
    }

    def __init__(self,
                 privilege_id=None,
                 category=None,
                 description=None,
                 is_available_on_helios=None,
                 is_custom_role_default=None,
                 is_special=None,
                 is_view_only=None,
                 label=None,
                 name=None):
        """Constructor for the PrivilegeInfo class"""

        # Initialize members of the class
        self.privilege_id = privilege_id
        self.category = category
        self.description = description
        self.is_available_on_helios = is_available_on_helios
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
        privilege_id = dictionary.get('PrivilegeId')
        category = dictionary.get('category')
        description = dictionary.get('description')
        is_available_on_helios = dictionary.get('isAvailableOnHelios')
        is_custom_role_default = dictionary.get('isCustomRoleDefault')
        is_special = dictionary.get('isSpecial')
        is_view_only = dictionary.get('isViewOnly')
        label = dictionary.get('label')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(privilege_id,
                   category,
                   description,
                   is_available_on_helios,
                   is_custom_role_default,
                   is_special,
                   is_view_only,
                   label,
                   name)


