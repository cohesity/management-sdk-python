# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.cluster_identifier
import cohesity_management_sdk.models.google_account_info
import cohesity_management_sdk.models.idp_user_info
import cohesity_management_sdk.models.tenant_config
import cohesity_management_sdk.models.preferences
import cohesity_management_sdk.models.salesforce_account_info

class User(object):

    """Implementation of the 'User' model.

    Specifies details about a user.

    Attributes:
        additional_group_names (list of string): Array of Additional Groups.
            Specifies the names of additional groups this User may belong to.
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
        google_account (GoogleAccountInfo): Google Account Information of a
            Helios BaaS user.
        idp_user_info (IdpUserInfo): Specifies an IdP User's information
            logged in using an IdP. This information is not stored on the
            Cluster.
        last_updated_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the user account was last modified on the
            Cohesity Cluster.
        org_membership (list of TenantConfig): OrgMembership contains the list
            of all available tenantIds for this user to switch to. Only when
            creating the session user, this field is populated on the fly. We
            discover the tenantIds from various groups assigned to the users.
        password (string): Specifies the password of this user.
        preferences (Preferences): TODO: type description here.
        primary_group_name (string): Specifies the name of the primary group
            of this User.
        privilege_ids (list of PrivilegeIdUserEnum): Array of Privileges.
            Specifies the Cohesity privileges from the roles. This will be
            populated based on the union of all privileges in roles. Type for
            unique privilege Id values. All below enum values specify a value
            for all uniquely defined privileges in Cohesity.
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
        sid (string): Specifies the unique Security ID (SID) of the user.
        tenant_id (string): Specifies the effective Tenant ID of the user.
        username (string): Specifies the login name of the user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_group_names":'additionalGroupNames',
        "authentication_type":'authenticationType',
        "cluster_identifiers":'clusterIdentifiers',
        "created_time_msecs":'createdTimeMsecs',
        "description":'description',
        "domain":'domain',
        "effective_time_msecs":'effectiveTimeMsecs',
        "email_address":'emailAddress',
        "expired_time_msecs":'expiredTimeMsecs',
        "google_account":'googleAccount',
        "idp_user_info":'idpUserInfo',
        "last_updated_time_msecs":'lastUpdatedTimeMsecs',
        "org_membership":'orgMembership',
        "password":'password',
        "preferences":'preferences',
        "primary_group_name":'primaryGroupName',
        "privilege_ids":'privilegeIds',
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
                 authentication_type=None,
                 cluster_identifiers=None,
                 created_time_msecs=None,
                 description=None,
                 domain=None,
                 effective_time_msecs=None,
                 email_address=None,
                 expired_time_msecs=None,
                 google_account=None,
                 idp_user_info=None,
                 last_updated_time_msecs=None,
                 org_membership=None,
                 password=None,
                 preferences=None,
                 primary_group_name=None,
                 privilege_ids=None,
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
        self.authentication_type = authentication_type
        self.cluster_identifiers = cluster_identifiers
        self.created_time_msecs = created_time_msecs
        self.description = description
        self.domain = domain
        self.effective_time_msecs = effective_time_msecs
        self.email_address = email_address
        self.expired_time_msecs = expired_time_msecs
        self.google_account = google_account
        self.idp_user_info = idp_user_info
        self.last_updated_time_msecs = last_updated_time_msecs
        self.org_membership = org_membership
        self.password = password
        self.preferences = preferences
        self.primary_group_name = primary_group_name
        self.privilege_ids = privilege_ids
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
        authentication_type = dictionary.get('authenticationType')
        cluster_identifiers = None
        if dictionary.get('clusterIdentifiers') != None:
            cluster_identifiers = list()
            for structure in dictionary.get('clusterIdentifiers'):
                cluster_identifiers.append(cohesity_management_sdk.models.cluster_identifier.ClusterIdentifier.from_dictionary(structure))
        created_time_msecs = dictionary.get('createdTimeMsecs')
        description = dictionary.get('description')
        domain = dictionary.get('domain')
        effective_time_msecs = dictionary.get('effectiveTimeMsecs')
        email_address = dictionary.get('emailAddress')
        expired_time_msecs = dictionary.get('expiredTimeMsecs')
        google_account = cohesity_management_sdk.models.google_account_info.GoogleAccountInfo.from_dictionary(dictionary.get('googleAccount')) if dictionary.get('googleAccount') else None
        idp_user_info = cohesity_management_sdk.models.idp_user_info.IdpUserInfo.from_dictionary(dictionary.get('idpUserInfo')) if dictionary.get('idpUserInfo') else None
        last_updated_time_msecs = dictionary.get('lastUpdatedTimeMsecs')
        org_membership = None
        if dictionary.get('orgMembership') != None:
            org_membership = list()
            for structure in dictionary.get('orgMembership'):
                org_membership.append(cohesity_management_sdk.models.tenant_config.TenantConfig.from_dictionary(structure))
        password = dictionary.get('password')
        preferences = cohesity_management_sdk.models.preferences.Preferences.from_dictionary(dictionary.get('preferences')) if dictionary.get('preferences') else None
        primary_group_name = dictionary.get('primaryGroupName')
        privilege_ids = dictionary.get('privilegeIds')
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
                   authentication_type,
                   cluster_identifiers,
                   created_time_msecs,
                   description,
                   domain,
                   effective_time_msecs,
                   email_address,
                   expired_time_msecs,
                   google_account,
                   idp_user_info,
                   last_updated_time_msecs,
                   org_membership,
                   password,
                   preferences,
                   primary_group_name,
                   privilege_ids,
                   restricted,
                   roles,
                   s_3_access_key_id,
                   s_3_account_id,
                   s_3_secret_key,
                   salesforce_account,
                   sid,
                   tenant_id,
                   username)


