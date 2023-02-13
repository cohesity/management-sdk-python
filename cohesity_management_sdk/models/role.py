# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Role(object):

    """Implementation of the 'Role' model.

    Specifies information about role such as the category, privileges,
    description, etc. A role can be a default system role
    or a custom role. Custom roles are user-defined roles that are created
    using the Cohesity Dashboard, the REST API or the CLI.
    System roles are provided by default on the Cohesity Cluster.

    Attributes:
        created_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the role was created.
        description (string): Specifies a description about the role.
        is_custom_role (bool): Specifies if the role is a user-defined custom
            role. If true, the role is a user-defined custom role that was
            created using the REST API, the Cohesity Dashboard or the CLI. If
            false, the role is a default system role that was created during
            Cluster creation.
        label (string): Specifies the label for the role as displayed on the
            Cohesity Dashboard such as 'Viewer'.
        last_updated_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the role was last modified.
        name (string): Specifies the internal Cluster name for the role such
            as COHESITY_VIEWER. For custom roles, the name and the label are
            the same. For default system roles, the name and label are
            different.
        privileges (list of string): Array of Privileges.  Specifies the
            privileges assigned to the role. When a user or group is assigned
            this role, these privileges define the operations the user or
            group can perform on the Cohesity Cluster.
        tenant_id (string): Specifies unique id of the tenant owning the
            role.
        tenant_ids (list of string): Specifies id of tenants using this role.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_time_msecs":'createdTimeMsecs',
        "description":'description',
        "is_custom_role":'isCustomRole',
        "label":'label',
        "last_updated_time_msecs":'lastUpdatedTimeMsecs',
        "name":'name',
        "privileges":'privileges',
        "tenant_id":'tenantId',
        "tenant_ids":'tenantIds'
    }

    def __init__(self,
                 created_time_msecs=None,
                 description=None,
                 is_custom_role=None,
                 label=None,
                 last_updated_time_msecs=None,
                 name=None,
                 privileges=None,
                 tenant_id=None,
                 tenant_ids=None):
        """Constructor for the Role class"""

        # Initialize members of the class
        self.created_time_msecs = created_time_msecs
        self.description = description
        self.is_custom_role = is_custom_role
        self.label = label
        self.last_updated_time_msecs = last_updated_time_msecs
        self.name = name
        self.privileges = privileges
        self.tenant_id = tenant_id
        self.tenant_ids = tenant_ids


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
        created_time_msecs = dictionary.get('createdTimeMsecs')
        description = dictionary.get('description')
        is_custom_role = dictionary.get('isCustomRole')
        label = dictionary.get('label')
        last_updated_time_msecs = dictionary.get('lastUpdatedTimeMsecs')
        name = dictionary.get('name')
        privileges = dictionary.get('privileges')
        tenant_id = dictionary.get('tenantId')
        tenant_ids = dictionary.get('tenantIds')

        # Return an object of this model
        return cls(created_time_msecs,
                   description,
                   is_custom_role,
                   label,
                   last_updated_time_msecs,
                   name,
                   privileges,
                   tenant_id,
                   tenant_ids)


