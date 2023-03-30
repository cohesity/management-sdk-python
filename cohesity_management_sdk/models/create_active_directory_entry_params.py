# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.preferred_domain_controller
import cohesity_management_sdk.models.user_id_mapping


class CreateActiveDirectoryEntryParams(object):

    """Implementation of the 'CreateActiveDirectoryEntryParams' model.

    TODO: type description here.


    Attributes:

        domain_name (string): Specifies the fully qualified domain name (FQDN)
            of an Active Directory.
        fallback_user_id_mapping_info (UserIdMapping): Specifies the fallback
            id mapping info which is used when an ID mapping for a user is not
            found via the above IdMappingInfo. Only supported for two types of
            fallback mapping types - 'kRid' and 'kFixed'.
        force_remove (bool): Specifies if Active Directory entry should be
            force removed from cluster.
        ignored_trusted_domains (list of string): Specifies the list of trusted
            domains that were set by the user to be ignored during trusted
            domain discovery.
        ldap_provider_id (long|int): Specifies the LDAP provider id which is
            map to this Active Directory
        machine_accounts (list of string): Array of Machine Accounts. 
            Specifies an array of computer names used to identify the Cohesity
            Cluster on the domain.
        only_use_whitelisted_domains (bool): Specifies whether to use
            'whitelistedDomains' only for authentication.
        ou_name (string): Specifies an optional Organizational Unit name.
        overwrite_existing_accounts (bool): Specifies whether the specified
            machine accounts should overwrite the existing machine accounts in
            this domain.
        password (string): Specifies the password for the specified userName.
        preferred_domain_controllers (list of PreferredDomainController):
            Specifies Map of Active Directory domain names to its preferred
            domain controllers.
        task_path (string): Specifies the task path for AD joining task.
        tenant_id (string): Specifies the unique id of the tenant.
        trusted_domains (list of string): Specifies the trusted domains of the
            Active Directory domain.
        trusted_domains_enabled (bool): Specifies whether Trusted Domain
            discovery is disabled.
        unix_root_sid (string): Specifies the SID of the Active Directory
            domain user to be mapped to Unix root user.
        user_id_mapping_info (UserIdMapping): Specifies the information about
            how the Unix and Windows users are mapped for this domain.
        user_name (string): Specifies a userName that has administrative
            privileges in the domain.
        whitelisted_domains (list of string): Specifies the Whitelisted Domains
            of the Active Directory domain.
        workgroup (string): Specifies an optional Workgroup name.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "domain_name":'domainName',
        "fallback_user_id_mapping_info":'fallbackUserIdMappingInfo',
        "force_remove":'forceRemove',
        "ignored_trusted_domains":'ignoredTrustedDomains',
        "ldap_provider_id":'ldapProviderId',
        "machine_accounts":'machineAccounts',
        "only_use_whitelisted_domains":'onlyUseWhitelistedDomains',
        "ou_name":'ouName',
        "overwrite_existing_accounts":'overwriteExistingAccounts',
        "password":'password',
        "preferred_domain_controllers":'preferredDomainControllers',
        "task_path":'taskPath',
        "tenant_id":'tenantId',
        "trusted_domains":'trustedDomains',
        "trusted_domains_enabled":'trustedDomainsEnabled',
        "unix_root_sid":'unixRootSid',
        "user_id_mapping_info":'userIdMappingInfo',
        "user_name":'userName',
        "whitelisted_domains":'whitelistedDomains',
        "workgroup":'workgroup',
    }
    def __init__(self,
                 domain_name=None,
                 fallback_user_id_mapping_info=None,
                 force_remove=None,
                 ignored_trusted_domains=None,
                 ldap_provider_id=None,
                 machine_accounts=None,
                 only_use_whitelisted_domains=None,
                 ou_name=None,
                 overwrite_existing_accounts=None,
                 password=None,
                 preferred_domain_controllers=None,
                 task_path=None,
                 tenant_id=None,
                 trusted_domains=None,
                 trusted_domains_enabled=None,
                 unix_root_sid=None,
                 user_id_mapping_info=None,
                 user_name=None,
                 whitelisted_domains=None,
                 workgroup=None,
            ):

        """Constructor for the CreateActiveDirectoryEntryParams class"""

        # Initialize members of the class
        self.domain_name = domain_name
        self.fallback_user_id_mapping_info = fallback_user_id_mapping_info
        self.force_remove = force_remove
        self.ignored_trusted_domains = ignored_trusted_domains
        self.ldap_provider_id = ldap_provider_id
        self.machine_accounts = machine_accounts
        self.only_use_whitelisted_domains = only_use_whitelisted_domains
        self.ou_name = ou_name
        self.overwrite_existing_accounts = overwrite_existing_accounts
        self.password = password
        self.preferred_domain_controllers = preferred_domain_controllers
        self.task_path = task_path
        self.tenant_id = tenant_id
        self.trusted_domains = trusted_domains
        self.trusted_domains_enabled = trusted_domains_enabled
        self.unix_root_sid = unix_root_sid
        self.user_id_mapping_info = user_id_mapping_info
        self.user_name = user_name
        self.whitelisted_domains = whitelisted_domains
        self.workgroup = workgroup

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
        domain_name = dictionary.get('domainName')
        fallback_user_id_mapping_info = cohesity_management_sdk.models.user_id_mapping.UserIdMapping.from_dictionary(dictionary.get('fallbackUserIdMappingInfo')) if dictionary.get('fallbackUserIdMappingInfo') else None
        force_remove = dictionary.get('forceRemove')
        ignored_trusted_domains = dictionary.get("ignoredTrustedDomains")
        ldap_provider_id = dictionary.get('ldapProviderId')
        machine_accounts = dictionary.get("machineAccounts")
        only_use_whitelisted_domains = dictionary.get('onlyUseWhitelistedDomains')
        ou_name = dictionary.get('ouName')
        overwrite_existing_accounts = dictionary.get('overwriteExistingAccounts')
        password = dictionary.get('password')
        preferred_domain_controllers = None
        if dictionary.get('preferredDomainControllers') != None:
            preferred_domain_controllers = list()
            for structure in dictionary.get('preferredDomainControllers'):
                preferred_domain_controllers.append(cohesity_management_sdk.models.preferred_domain_controller.PreferredDomainController.from_dictionary(structure))
        task_path = dictionary.get('taskPath')
        tenant_id = dictionary.get('tenantId')
        trusted_domains = dictionary.get("trustedDomains")
        trusted_domains_enabled = dictionary.get('trustedDomainsEnabled')
        unix_root_sid = dictionary.get('unixRootSid')
        user_id_mapping_info = cohesity_management_sdk.models.user_id_mapping.UserIdMapping.from_dictionary(dictionary.get('userIdMappingInfo')) if dictionary.get('userIdMappingInfo') else None
        user_name = dictionary.get('userName')
        whitelisted_domains = dictionary.get("whitelistedDomains")
        workgroup = dictionary.get('workgroup')

        # Return an object of this model
        return cls(
            domain_name,
            fallback_user_id_mapping_info,
            force_remove,
            ignored_trusted_domains,
            ldap_provider_id,
            machine_accounts,
            only_use_whitelisted_domains,
            ou_name,
            overwrite_existing_accounts,
            password,
            preferred_domain_controllers,
            task_path,
            tenant_id,
            trusted_domains,
            trusted_domains_enabled,
            unix_root_sid,
            user_id_mapping_info,
            user_name,
            whitelisted_domains,
            workgroup
)