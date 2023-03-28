# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_identifier


class TenantAccess(object):

    """Implementation of the 'TenantAccess' model.

    TODO: type description here.


    Attributes:

        cluster_identifiers (list of ClusterIdentifier): Specifies the list of
            clusters.
        created_time_msecs (long|int): Specifies the epoch time in milliseconds
            when the tenant access was created.
        effective_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the tenant access becomes effective. Until that
            time, the user cannot log in.
        expired_time_msecs (long|int): Specifies the epoch time in milliseconds
            when the tenant access becomes expired. After that, the user cannot
            log in.
        is_access_active (bool): IsAccessActive specifies whether or not a
            tenant access is active, or has been deactivated by the customer.
            The default behavior is 'true'.
        is_active (bool): Specifies whether or not the tenant is active.
        is_deleted (bool): Specifies whether or not the tenant is deleted.
        last_updated_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the tenant access was last modified.
        roles (list of string): Specifies the Cohesity roles to associate with
            the user such as such as 'Admin', 'Ops' or 'View'.
        tenant_id (string): Specifies the tenant id.
        tenant_name (string): Specifies the tenant name.
        tenant_type (TenantTypeEnum): Specifies the MCM tenant type. 'Dmaas'
            implies tenant type is DMaaS. 'Mcm' implies tenant is Mcm Cluster
            tenant.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_identifiers":'clusterIdentifiers',
        "created_time_msecs":'createdTimeMsecs',
        "effective_time_msecs":'effectiveTimeMsecs',
        "expired_time_msecs":'expiredTimeMsecs',
        "is_access_active":'isAccessActive',
        "is_active":'isActive',
        "is_deleted":'isDeleted',
        "last_updated_time_msecs":'lastUpdatedTimeMsecs',
        "roles":'roles',
        "tenant_id":'tenantId',
        "tenant_name":'tenantName',
        "tenant_type":'tenantType',
    }
    def __init__(self,
                 cluster_identifiers=None,
                 created_time_msecs=None,
                 effective_time_msecs=None,
                 expired_time_msecs=None,
                 is_access_active=None,
                 is_active=None,
                 is_deleted=None,
                 last_updated_time_msecs=None,
                 roles=None,
                 tenant_id=None,
                 tenant_name=None,
                 tenant_type=None,
            ):

        """Constructor for the TenantAccess class"""

        # Initialize members of the class
        self.cluster_identifiers = cluster_identifiers
        self.created_time_msecs = created_time_msecs
        self.effective_time_msecs = effective_time_msecs
        self.expired_time_msecs = expired_time_msecs
        self.is_access_active = is_access_active
        self.is_active = is_active
        self.is_deleted = is_deleted
        self.last_updated_time_msecs = last_updated_time_msecs
        self.roles = roles
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
        self.tenant_type = tenant_type

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
        cluster_identifiers = None
        if dictionary.get('clusterIdentifiers') != None:
            cluster_identifiers = list()
            for structure in dictionary.get('clusterIdentifiers'):
                cluster_identifiers.append(cohesity_management_sdk.models.cluster_identifier.ClusterIdentifier.from_dictionary(structure))
        created_time_msecs = dictionary.get('createdTimeMsecs')
        effective_time_msecs = dictionary.get('effectiveTimeMsecs')
        expired_time_msecs = dictionary.get('expiredTimeMsecs')
        is_access_active = dictionary.get('isAccessActive')
        is_active = dictionary.get('isActive')
        is_deleted = dictionary.get('isDeleted')
        last_updated_time_msecs = dictionary.get('lastUpdatedTimeMsecs')
        roles = dictionary.get("roles")
        tenant_id = dictionary.get('tenantId')
        tenant_name = dictionary.get('tenantName')
        tenant_type = dictionary.get('tenantType')

        # Return an object of this model
        return cls(
            cluster_identifiers,
            created_time_msecs,
            effective_time_msecs,
            expired_time_msecs,
            is_access_active,
            is_active,
            is_deleted,
            last_updated_time_msecs,
            roles,
            tenant_id,
            tenant_name,
            tenant_type
)