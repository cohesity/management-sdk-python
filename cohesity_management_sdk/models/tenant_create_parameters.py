# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantCreateParameters(object):

    """Implementation of the 'TenantCreateParameters' model.

    Specifies the settings used to create/add a new tenant.

    Attributes:
        bifrost_enabled (bool): Specifies whether bifrost (Ambassador proxy)
            is enabled for tenant.
        cluster_hostname (string): The hostname for Cohesity cluster as seen by
            tenants and as is routable from the tenant's network. Tenant's
            VLAN's hostname, if available can be used instead but it is
            mandatory to provide this value if there's no VLAN hostname to
            use. Also, when set, this field would take precedence over VLAN
            hostname.
        cluster_ips (list of string): Set of IPs as seen from the tenant's
            network for the Cohesity cluster. Only one from 'ClusterHostname'
            and 'ClusterIps' is needed.
        description (string): Specifies the description of this tenant.
        name (string): Specifies the name of the tenant.
        org_suffix (string): Specifies the organization suffix needed to
            construct tenant id. Tenant id is not completely auto generated
            rather chosen by tenant/SP admin as we needed same tenant id on
            multiple clusters to support replication across clusters, etc.
        parent_tenant_id (string): Specifies the parent tenant of this tenant
            if available.
        subscribe_to_alert_emails (bool): Service provider can optionally
            unsubscribe from the Tenant Alert Emails.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bifrost_enabled":'bifrostEnabled',
        "cluster_hostname":'clusterHostname',
        "cluster_ips":'clusterIps',
        "description":'description',
        "name":'name',
        "org_suffix":'orgSuffix',
        "parent_tenant_id":'parentTenantId',
        "subscribe_to_alert_emails":'subscribeToAlertEmails'
    }

    def __init__(self,
                 bifrost_enabled=None,
                 cluster_hostname=None,
                 cluster_ips=None,
                 description=None,
                 name=None,
                 org_suffix=None,
                 parent_tenant_id=None,
                 subscribe_to_alert_emails=None):
        """Constructor for the TenantCreateParameters class"""

        # Initialize members of the class
        self.bifrost_enabled = bifrost_enabled
        self.cluster_hostname = cluster_hostname
        self.cluster_ips = cluster_ips
        self.description = description
        self.name = name
        self.org_suffix = org_suffix
        self.parent_tenant_id = parent_tenant_id
        self.subscribe_to_alert_emails = subscribe_to_alert_emails


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
        bifrost_enabled = dictionary.get('bifrostEnabled')
        cluster_hostname = dictionary.get('clusterHostname')
        cluster_ips = dictionary.get('clusterIps')
        description = dictionary.get('description')
        name = dictionary.get('name')
        org_suffix = dictionary.get('orgSuffix')
        parent_tenant_id = dictionary.get('parentTenantId')
        subscribe_to_alert_emails = dictionary.get('subscribeToAlertEmails')

        # Return an object of this model
        return cls(bifrost_enabled,
                   cluster_hostname,
                   cluster_ips,
                   description,
                   name,
                   org_suffix,
                   parent_tenant_id,
                   subscribe_to_alert_emails)


