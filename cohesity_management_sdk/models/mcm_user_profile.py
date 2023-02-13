# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_identifier

class McmUserProfile(object):

    """Implementation of the 'McmUserProfile' model.

    Specfies the User profile for MCM user.

    Attributes:
        cluster_identifiers (list of ClusterIdentifier): Specifies the list of
            clusters. This is only valid if tenant type is OnPrem.
        is_active (bool): Specifies whether or not the tenant is active.
        is_deleted (bool): Specifies whether or not the tenant is deleted.
        region_ids (list of string): Specifies the list of regions. This is
            only valid if tenant type is Dmaas.
        tenant_id (string): Specifies the tenant id.
        tenant_name (string): Specifies the tenant name.
        tenant_type (TenantTypeEnum): Specifies the MCM tenant type.
            'Dmaas' implies tenant type is DMaaS.
            'OnPrem' implies tenant is cluster tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_identifiers": 'clusterIdentifiers',
        "is_active": 'isActive',
        "is_deleted": 'isDeleted',
        "region_ids":'regionIds',
        "tenant_id":'tenantId',
        "tenant_name":'tenantName',
        "tenant_type":'tenantType'
    }

    def __init__(self,
                 cluster_identifiers=None,
                 is_active=None,
                 is_deleted=None,
                 region_ids=None,
                 tenant_id=None,
                 tenant_name=None,
                 tenant_type=None
                 ):
        """Constructor for the McmUserProfile class"""

        # Initialize members of the class
        self.cluster_identifiers = cluster_identifiers
        self.is_active = is_active
        self.is_deleted = is_deleted
        self.region_ids = region_ids
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
        is_active = dictionary.get('isActive')
        is_deleted = dictionary.get('isDeleted')
        region_ids = dictionary.get('regionIds')
        tenant_id = dictionary.get('tenantId')
        tenant_name = dictionary.get('tenantName')
        tenant_type = dictionary.get('tenantType')

        # Return an object of this model
        return cls(cluster_identifiers,
                   is_active,
                   is_deleted,
                   region_ids,
                   tenant_id,
                   tenant_name,
                   tenant_type)


