# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.group_info
import cohesity_management_sdk.models.tenant_info
import cohesity_management_sdk.models.user_info


class EntityPermissionInformation(object):

    """Implementation of the 'EntityPermissionInformation' model.

    Specifies the permission information of entities.


    Attributes:

        entity_id (long|int): Specifies the entity id.
        groups (list of GroupInfo): Specifies groups that have access to entity
            in case of restricted user.
        is_inferred (bool): Specifies whether the Entity Permission Information
            is inferred or not. For example, SQL application hosted over
            vCenter will have inferred entity permission information.
        is_registered_by_sp (bool): Specifies whether this entity is registered
            by the SP or not. This will be populated only if the entity is a
            root entity. Refer to magneto/base/permissions.proto for details.
        registering_tenant_id (string): Specifies the tenant id that registered
            this entity. This will be populated only if the entity is a root
            entity.
        tenant (TenantInfo): Specifies basic information of the tenant having
            access to the entity.
        users (list of UserInfo): Specifies users that have access to entity in
            case of restricted user.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "entity_id":'entityId',
        "groups":'groups',
        "is_inferred":'isInferred',
        "is_registered_by_sp":'isRegisteredBySp',
        "registering_tenant_id":'registeringTenantId',
        "tenant":'tenant',
        "users":'users',
    }
    def __init__(self,
                 entity_id=None,
                 groups=None,
                 is_inferred=None,
                 is_registered_by_sp=None,
                 registering_tenant_id=None,
                 tenant=None,
                 users=None,
            ):

        """Constructor for the EntityPermissionInformation class"""

        # Initialize members of the class
        self.entity_id = entity_id
        self.groups = groups
        self.is_inferred = is_inferred
        self.is_registered_by_sp = is_registered_by_sp
        self.registering_tenant_id = registering_tenant_id
        self.tenant = tenant
        self.users = users

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
        entity_id = dictionary.get('entityId')
        groups = None
        if dictionary.get('groups') != None:
            groups = list()
            for structure in dictionary.get('groups'):
                groups.append(cohesity_management_sdk.models.group_info.GroupInfo.from_dictionary(structure))
        is_inferred = dictionary.get('isInferred')
        is_registered_by_sp = dictionary.get('isRegisteredBySp')
        registering_tenant_id = dictionary.get('registeringTenantId')
        tenant = cohesity_management_sdk.models.tenant_info.TenantInfo.from_dictionary(dictionary.get('tenant')) if dictionary.get('tenant') else None
        users = None
        if dictionary.get('users') != None:
            users = list()
            for structure in dictionary.get('users'):
                users.append(cohesity_management_sdk.models.user_info.UserInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(
            entity_id,
            groups,
            is_inferred,
            is_registered_by_sp,
            registering_tenant_id,
            tenant,
            users
)