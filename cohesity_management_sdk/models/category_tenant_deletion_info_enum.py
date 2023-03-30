# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CategoryTenantDeletionInfoEnum(object):

    """Implementation of the 'CategoryTenantDeletionInfo' enum.
    Specifies the category of objects whose deletion state is being captured.
    Specifies the Category of objects which are required to be deleted. On the
    first pass (when Tenant is marked 'deleted' and 'object_deletion_required'
    is set to true, for all the objects recognized in the enum - default
    deletion_info_vec is created. In order to skip the deletion of a few object
    categories, this object should be created manually during the 'Delete API'
    and these categories should be skipped.


    Attributes:
        PROTECTIONJOBS: TODO: type description here.
        VIEWS: TODO: type description here.
        PROTECTIONSOURCES: TODO: type description here.
        USERS: TODO: type description here.
        PROTECTIONPOLICIES: TODO: type description here.
        GROUPS: TODO: type description here.
        ACTIVEDIRECTORIES: TODO: type description here.
        LDAP: TODO: type description here.
        RECOVERYTASK: TODO: type description here.
        REMOTECLUSTERS: TODO: type description here.
        STORAGEDOMAINS: TODO: type description here.
        ALERTS: TODO: type description here.
        REPORTINGSCHEDULES: TODO: type description here.
        IDPS: TODO: type description here.
        SWIFT: TODO: type description here.

    """

    PROTECTIONJOBS = 'ProtectionJobs'

    VIEWS = 'Views'

    PROTECTIONSOURCES = 'ProtectionSources'

    USERS = 'Users'

    PROTECTIONPOLICIES = 'ProtectionPolicies'

    GROUPS = 'Groups'

    ACTIVEDIRECTORIES = 'ActiveDirectories'

    LDAP = 'Ldap'

    RECOVERYTASK = 'RecoveryTask'

    REMOTECLUSTERS = 'RemoteClusters'

    STORAGEDOMAINS = 'StorageDomains'

    ALERTS = 'Alerts'

    REPORTINGSCHEDULES = 'ReportingSchedules'

    IDPS = 'Idps'

    SWIFT = 'Swift'
