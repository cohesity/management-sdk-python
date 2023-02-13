# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.active_directory_entry
import cohesity_management_sdk.models.tenant_deletion_info
import cohesity_management_sdk.models.ldap_provider_response
import cohesity_management_sdk.models.backup_job_proto
import cohesity_management_sdk.models.view
import cohesity_management_sdk.models.swift_params

class Tenant(object):

    """Implementation of the 'Tenant' model.

    Specifies details about a tenant.

    Attributes:
        active_directories (list of ActiveDirectoryEntry): Specifies the
            active directories this tenant is associated to.
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
        created_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the tenant account was created on the Cohesity
            Cluster.
        deleted (bool): Specifies if the Tenant is deleted.
        deleted_time_msecs (long|int): Specifies the timestamp at which the
            tenant was deleted.
        deletion_finished (bool): Specifies if the object collection is
            complete for the tenant.
        deletion_info_vec (list of TenantDeletionInfo): Specifies the current
            deletion state of object categories.
        description (string): Specifies the description of this tenant.
        entity_ids (list of long|int): Specifies the EntityIds this tenant is
            associated to.
        last_updated_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the tenant account was last modified on the
            Cohesity Cluster.
        ldap_providers (list of LdapProviderResponse): Specifies the ldap
            providers this tenant is associated to.
        name (string): Specifies the name of the tenant.
        org_suffix (string): Specifies the organization suffix needed to
            construct tenant id. Tenant id is not completely auto generated
            rather chosen by tenant/SP admin as we needed same tenant id on
            multiple clusters to support replication across clusters, etc.
        parent_tenant_id (string): Specifies the parent tenant of this tenant
            if available.
        policy_ids (list of string): Specifies the PolicyIds this tenant is
            associated to.
        protection_jobs (list of BackupJobProto): Specifies the ProtectionJobs
            this tenant is associated to.
        subscribe_to_alert_emails (bool): Service provider can optionally
            unsubscribe from the Tenant Alert Emails.
        swift_config (SwiftParams): Specifies the Swift configuration of this
            tenant.
        tenant_id (string): Specifies the unique id of the tenant.
        view_box_ids (list of long|int): Specifies the ViewBoxIds this tenant
            is associated to.
        views (list of View): Specifies the Views this tenant is associated
            to.
        vlan_iface_names (list of string): Specifies the VlanIfaceNames this
            tenant is associated to, in the format of bond1.200.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "active_directories":'activeDirectories',
        "bifrost_enabled":'bifrostEnabled',
        "cluster_hostname":'clusterHostname',
        "cluster_ips":'clusterIps',
        "created_time_msecs":'createdTimeMsecs',
        "deleted":'deleted',
        "deleted_time_msecs":'deletedTimeMsecs',
        "deletion_finished":'deletionFinished',
        "deletion_info_vec":'deletionInfoVec',
        "description":'description',
        "entity_ids":'entityIds',
        "last_updated_time_msecs":'lastUpdatedTimeMsecs',
        "ldap_providers":'ldapProviders',
        "name":'name',
        "org_suffix":'orgSuffix',
        "parent_tenant_id":'parentTenantId',
        "policy_ids":'policyIds',
        "protection_jobs":'protectionJobs',
        "subscribe_to_alert_emails":'subscribeToAlertEmails',
        "swift_config":'swiftConfig',
        "tenant_id":'tenantId',
        "view_box_ids":'viewBoxIds',
        "views":'views',
        "vlan_iface_names":'vlanIfaceNames'
    }

    def __init__(self,
                 active_directories=None,
                 bifrost_enabled=None,
                 cluster_hostname=None,
                 cluster_ips=None,
                 created_time_msecs=None,
                 deleted=None,
                 deleted_time_msecs=None,
                 deletion_finished=None,
                 deletion_info_vec=None,
                 description=None,
                 entity_ids=None,
                 last_updated_time_msecs=None,
                 ldap_providers=None,
                 name=None,
                 org_suffix=None,
                 parent_tenant_id=None,
                 policy_ids=None,
                 protection_jobs=None,
                 subscribe_to_alert_emails=None,
                 swift_config=None,
                 tenant_id=None,
                 view_box_ids=None,
                 views=None,
                 vlan_iface_names=None):
        """Constructor for the Tenant class"""

        # Initialize members of the class
        self.active_directories = active_directories
        self.bifrost_enabled = bifrost_enabled
        self.cluster_hostname = cluster_hostname
        self.cluster_ips = cluster_ips
        self.created_time_msecs = created_time_msecs
        self.deleted = deleted
        self.deleted_time_msecs = deleted_time_msecs
        self.deletion_finished = deletion_finished
        self.deletion_info_vec = deletion_info_vec
        self.description = description
        self.entity_ids = entity_ids
        self.last_updated_time_msecs = last_updated_time_msecs
        self.ldap_providers = ldap_providers
        self.name = name
        self.org_suffix = org_suffix
        self.parent_tenant_id = parent_tenant_id
        self.policy_ids = policy_ids
        self.protection_jobs = protection_jobs
        self.subscribe_to_alert_emails = subscribe_to_alert_emails
        self.swift_config = swift_config
        self.tenant_id = tenant_id
        self.view_box_ids = view_box_ids
        self.views = views
        self.vlan_iface_names = vlan_iface_names


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
        active_directories = None
        if dictionary.get('activeDirectories') != None:
            active_directories = list()
            for structure in dictionary.get('activeDirectories'):
                active_directories.append(cohesity_management_sdk.models.active_directory_entry.ActiveDirectoryEntry.from_dictionary(structure))
        bifrost_enabled = dictionary.get('bifrostEnabled')
        cluster_hostname = dictionary.get('clusterHostname')
        cluster_ips = dictionary.get('clusterIps')
        created_time_msecs = dictionary.get('createdTimeMsecs')
        deleted = dictionary.get('deleted')
        deleted_time_msecs = dictionary.get('deletedTimeMsecs')
        deletion_finished = dictionary.get('deletionFinished')
        deletion_info_vec = None
        if dictionary.get('deletionInfoVec') != None:
            deletion_info_vec = list()
            for structure in dictionary.get('deletionInfoVec'):
                deletion_info_vec.append(cohesity_management_sdk.models.tenant_deletion_info.TenantDeletionInfo.from_dictionary(structure))
        description = dictionary.get('description')
        entity_ids = dictionary.get('entityIds')
        last_updated_time_msecs = dictionary.get('lastUpdatedTimeMsecs')
        ldap_providers = None
        if dictionary.get('ldapProviders') != None:
            ldap_providers = list()
            for structure in dictionary.get('ldapProviders'):
                ldap_providers.append(cohesity_management_sdk.models.ldap_provider_response.LdapProviderResponse.from_dictionary(structure))
        name = dictionary.get('name')
        org_suffix = dictionary.get('orgSuffix')
        parent_tenant_id = dictionary.get('parentTenantId')
        policy_ids = dictionary.get('policyIds')
        protection_jobs = None
        if dictionary.get('protectionJobs') != None:
            protection_jobs = list()
            for structure in dictionary.get('protectionJobs'):
                protection_jobs.append(cohesity_management_sdk.models.backup_job_proto.BackupJobProto.from_dictionary(structure))
        subscribe_to_alert_emails = dictionary.get('subscribeToAlertEmails')
        swift_config = cohesity_management_sdk.models.swift_params.SwiftParams.from_dictionary(dictionary.get('swiftConfig')) if dictionary.get('swiftConfig') else None
        tenant_id = dictionary.get('tenantId')
        view_box_ids = dictionary.get('viewBoxIds')
        views = None
        if dictionary.get('views') != None:
            views = list()
            for structure in dictionary.get('views'):
                views.append(cohesity_management_sdk.models.view.View.from_dictionary(structure))
        vlan_iface_names = dictionary.get('vlanIfaceNames')

        # Return an object of this model
        return cls(active_directories,
                   bifrost_enabled,
                   cluster_hostname,
                   cluster_ips,
                   created_time_msecs,
                   deleted,
                   deleted_time_msecs,
                   deletion_finished,
                   deletion_info_vec,
                   description,
                   entity_ids,
                   last_updated_time_msecs,
                   ldap_providers,
                   name,
                   org_suffix,
                   parent_tenant_id,
                   policy_ids,
                   protection_jobs,
                   subscribe_to_alert_emails,
                   swift_config,
                   tenant_id,
                   view_box_ids,
                   views,
                   vlan_iface_names)


