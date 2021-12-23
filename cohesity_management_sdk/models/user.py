# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.audit_log_settings
import cohesity_management_sdk.models.cluster_identifier
import cohesity_management_sdk.models.google_account_info
import cohesity_management_sdk.models.idp_user_info
import cohesity_management_sdk.models.mcm_user_profile
import cohesity_management_sdk.models.tenant_config
import cohesity_management_sdk.models.preferences
import cohesity_management_sdk.models.salesforce_account_info

class User(object):

    """Implementation of the 'User' model.

    Specifies details about a user.

    Attributes:
        additional_group_names (list of string): Array of Additional Groups.
            Specifies the names of additional groups this User may belong to.
        audit_log_settings (AuditLogSettings): Specifies audit settings.
        authentication_type (AuthenticationTypeUserEnum): Specifies the
            authentication type of the user. 'kAuthLocal' implies
            authenticated user is a local user. 'kAuthAd' implies
            authenticated user is an Active Directory user. 'kAuthSalesforce'
            implies authenticated user is a Salesforce user. 'kAuthGoogle'
            implies authenticated user is a Google user. 'kAuthSso' implies
            authenticated user is an SSO user.
        cluster_identifiers (list of ClusterIdentifier): Specifies the list of
            clusters this user has access to. If this is not specified, access
            will be granted to all clusters.
        created_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the user account was created on the Cohesity
            Cluster.
        current_password (string): Specifies the current password when
            updating the password.
        description (string): Specifies a description about the user.
        domain (string): Specifies the fully qualified domain name (FQDN) of
            an Active Directory or LOCAL for the default LOCAL domain on the
            Cohesity Cluster. A user is uniquely identified by combination of
            the username and the domain.
        effective_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the user becomes effective. Until that time, the
            user cannot log in.
        email_address (string): Specifies the email address of the user.
        expired_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the user becomes expired. After that, the user
            cannot log in.
        force_password_change (bool): Specifies whether to force user to
            change password.
        google_account (GoogleAccountInfo): Google Account Information of a
            Helios BaaS user.
        group_roles (list of string): Specifies the Cohesity roles to
            associate with the user' group. These roles can only be edited
            from group.
        idp_user_info (IdpUserInfo): Specifies an IdP User's information
            logged in using an IdP. This information is not stored on the
            Cluster.
        is_account_locked (bool): Specifies whether the user account is locked.
        is_active (bool): IsActive specifies whether or not a user is active,
            or has been disactivated by the customer. The default behavior is
            'true'.
        last_successful_login_time_msecs (long|int): Specifies the epoch time
            in milliseconds when the user was last logged in successfully.
        last_updated_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the user account was last modified on the
            Cohesity Cluster.
        lockout_reason (LockoutReasonUserEnum): Specifies the lockout reason
            of the user if it is locked.
            'NotLocked' implies the user is not locked.
            'FailedLoginAttempts' the account is locked due to
            many failed login attempts.
            'LockedByAdmin' implies the account is locked by the admin user.
            'Inactivity' implies the account is locked due to long time of
            inactivity.
        org_membership (list of TenantConfig): OrgMembership contains the list
            of all available tenantIds for this user to switch to. Only when
            creating the session user, this field is populated on the fly. We
            discover the tenantIds from various groups assigned to the users.
        password (string): Specifies the password of this user.
        preferences (Preferences): TODO: type description here.
        previous_login_time_msecs (long|int):  Specifies the epoch time in
            milliseconds of previous user login.
        primary_group_name (string): Specifies the name of the primary group
            of this User.
        privilege_ids (list of PrivilegeIdUserEnum): Array of Privileges.
            Specifies the Cohesity privileges from the roles. This will be
            populated based on the union of all privileges in roles. Type for
            unique privilege Id values. All below enum values specify a value
            for all uniquely defined privileges in Cohesity.
        profiles (list of McmUserProfile): Specifies the user profiles.
            NOTE: Currently used for Helios.
        restricted (bool): Whether the user is a restricted user. A restricted
            user can only view the objects he has permissions to.
        roles (list of string): Array of Roles.  Specifies the Cohesity roles
            to associate with the user such as such as 'Admin', 'Ops' or
            'View'. The Cohesity roles determine privileges on the Cohesity
            Cluster for this user.
        s_3_access_key_id (string): Specifies the S3 Account Access Key ID.
        s_3_account_id (string): Specifies the S3 Account Canonical User ID.
        s_3_secret_key (string): Specifies the S3 Account Secret Key.
        salesforce_account (SalesforceAccountInfo): Salesforce Account
            Information of a Helios user.
        sid (string): Specifies the unique Security ID (SID) of the user. This
            field is mandatory in modifying user.
        tenant_id (string): Specifies the effective Tenant ID of the user.
        username (string): Specifies the login name of the user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_group_names":'additionalGroupNames',
        "audit_log_settings":'auditLogSettings',
        "authentication_type":'authenticationType',
        "cluster_identifiers":'clusterIdentifiers',
        "created_time_msecs":'createdTimeMsecs',
        "current_password":'currentPassword',
        "description":'description',
        "domain":'domain',
        "effective_time_msecs":'effectiveTimeMsecs',
        "email_address":'emailAddress',
        "expired_time_msecs":'expiredTimeMsecs',
        "force_password_change":'forcePasswordChange',
        "google_account":'googleAccount',
        "group_roles":'groupRoles',
        "idp_user_info":'idpUserInfo',
        "is_account_locked":'isAccountLocked',
        "is_active":'isActive',
        "last_successful_login_time_msecs":'lastSuccessfulLoginTimeMsecs',
        "last_updated_time_msecs":'lastUpdatedTimeMsecs',
        "lockout_reason":'lockoutReason',
        "org_membership":'orgMembership',
        "password":'password',
        "preferences":'preferences',
        "previous_login_time_msecs":'previousLoginTimeMsecs',
        "primary_group_name":'primaryGroupName',
        "privilege_ids":'privilegeIds',
        "profiles":'profiles',
        "restricted":'restricted',
        "roles":'roles',
        "s_3_access_key_id":'s3AccessKeyId',
        "s_3_account_id":'s3AccountId',
        "s_3_secret_key":'s3SecretKey',
        "salesforce_account":'salesforceAccount',
        "sid":'sid',
        "tenant_id":'tenantId',
        "username":'username'
    }

    def __init__(self,
                 additional_group_names=None,
                 audit_log_settings=None,
                 authentication_type=None,
                 cluster_identifiers=None,
                 created_time_msecs=None,
                 current_password=None,
                 description=None,
                 domain=None,
                 effective_time_msecs=None,
                 email_address=None,
                 expired_time_msecs=None,
                 force_password_change=None,
                 google_account=None,
                 group_roles=None,
                 idp_user_info=None,
                 is_account_locked=None,
                 is_active=None,
                 last_successful_login_time_msecs=None,
                 last_updated_time_msecs=None,
                 lockout_reason=None,
                 org_membership=None,
                 password=None,
                 preferences=None,
                 previous_login_time_msecs=None,
                 primary_group_name=None,
                 privilege_ids=None,
                 profiles=None,
                 restricted=None,
                 roles=None,
                 s_3_access_key_id=None,
                 s_3_account_id=None,
                 s_3_secret_key=None,
                 salesforce_account=None,
                 sid=None,
                 tenant_id=None,
                 username=None):
        """Constructor for the User class"""

        # Initialize members of the class
        self.additional_group_names = additional_group_names
        self.audit_log_settings = audit_log_settings
        self.authentication_type = authentication_type
        self.cluster_identifiers = cluster_identifiers
        self.created_time_msecs = created_time_msecs
        self.current_password = current_password
        self.description = description
        self.domain = domain
        self.effective_time_msecs = effective_time_msecs
        self.email_address = email_address
        self.expired_time_msecs = expired_time_msecs
        self.force_password_change = force_password_change
        self.google_account = google_account
        self.group_roles = group_roles
        self.idp_user_info = idp_user_info
        self.is_account_locked = is_account_locked
        self.is_active = is_active
        self.last_successful_login_time_msecs = last_successful_login_time_msecs
        self.last_updated_time_msecs = last_updated_time_msecs
        self.lockout_reason = lockout_reason
        self.org_membership = org_membership
        self.password = password
        self.preferences = preferences
        self.previous_login_time_msecs = previous_login_time_msecs
        self.primary_group_name = primary_group_name
        self.privilege_ids = privilege_ids
        self.profiles = profiles
        self.restricted = restricted
        self.roles = roles
        self.s_3_access_key_id = s_3_access_key_id
        self.s_3_account_id = s_3_account_id
        self.s_3_secret_key = s_3_secret_key
        self.salesforce_account = salesforce_account
        self.sid = sid
        self.tenant_id = tenant_id
        self.username = username


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
        additional_group_names = dictionary.get('additionalGroupNames')
        audit_log_settings = cohesity_management_sdk.models.audit_log_settings.AuditLogSettings.from_dictionary(dictionary.get('auditLogSettings')) if dictionary.get('auditLogSettings') else None
        authentication_type = dictionary.get('authenticationType')
        cluster_identifiers = None
        if dictionary.get('clusterIdentifiers') != None:
            cluster_identifiers = list()
            for structure in dictionary.get('clusterIdentifiers'):
                cluster_identifiers.append(cohesity_management_sdk.models.cluster_identifier.ClusterIdentifier.from_dictionary(structure))
        created_time_msecs = dictionary.get('createdTimeMsecs')
        current_password = dictionary.get('currentPassword')
        description = dictionary.get('description')
        domain = dictionary.get('domain')
        effective_time_msecs = dictionary.get('effectiveTimeMsecs')
        email_address = dictionary.get('emailAddress')
        expired_time_msecs = dictionary.get('expiredTimeMsecs')
        force_password_change = dictionary.get('forcePasswordChange')
        google_account = cohesity_management_sdk.models.google_account_info.GoogleAccountInfo.from_dictionary(dictionary.get('googleAccount')) if dictionary.get('googleAccount') else None
        group_roles = dictionary.get('groupRoles')
        idp_user_info = cohesity_management_sdk.models.idp_user_info.IdpUserInfo.from_dictionary(dictionary.get('idpUserInfo')) if dictionary.get('idpUserInfo') else None
        is_account_locked = dictionary.get('isAccountLocked')
        is_active = dictionary.get('isActive')
        last_successful_login_time_msecs = dictionary.get('lastSuccessfulLoginTimeMsecs')
        last_updated_time_msecs = dictionary.get('lastUpdatedTimeMsecs')
        lockout_reason = dictionary.get('lockoutReason')
        org_membership = None
        if dictionary.get('orgMembership') != None:
            org_membership = list()
            for structure in dictionary.get('orgMembership'):
                org_membership.append(cohesity_management_sdk.models.tenant_config.TenantConfig.from_dictionary(structure))
        password = dictionary.get('password')
        preferences = cohesity_management_sdk.models.preferences.Preferences.from_dictionary(dictionary.get('preferences')) if dictionary.get('preferences') else None
        previous_login_time_msecs = dictionary.get('previousLoginTimeMsecs')
        primary_group_name = dictionary.get('primaryGroupName')
        privilege_ids = dictionary.get('privilegeIds')
        profiles = None
        if dictionary.get('profiles') != None:
            profiles = list()
            for structure in dictionary.get('profiles'):
                profiles.append(cohesity_management_sdk.models.mcm_user_profile.McmUserProfile.from_dictionary(structure))
        restricted = dictionary.get('restricted')
        roles = dictionary.get('roles')
        s_3_access_key_id = dictionary.get('s3AccessKeyId')
        s_3_account_id = dictionary.get('s3AccountId')
        s_3_secret_key = dictionary.get('s3SecretKey')
        salesforce_account = cohesity_management_sdk.models.salesforce_account_info.SalesforceAccountInfo.from_dictionary(dictionary.get('salesforceAccount')) if dictionary.get('salesforceAccount') else None
        sid = dictionary.get('sid')
        tenant_id = dictionary.get('tenantId')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(additional_group_names,
                   audit_log_settings,
                   authentication_type,
                   cluster_identifiers,
                   created_time_msecs,
                   current_password,
                   description,
                   domain,
                   effective_time_msecs,
                   email_address,
                   expired_time_msecs,
                   force_password_change,
                   google_account,
                   group_roles,
                   idp_user_info,
                   is_account_locked,
                   is_active,
                   last_successful_login_time_msecs,
                   last_updated_time_msecs,
                   lockout_reason,
                   org_membership,
                   password,
                   preferences,
                   previous_login_time_msecs,
                   primary_group_name,
                   privilege_ids,
                   profiles,
                   restricted,
                   roles,
                   s_3_access_key_id,
                   s_3_account_id,
                   s_3_secret_key,
                   salesforce_account,
                   sid,
                   tenant_id,
                   username)


