# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpdateLdapProviderParam(object):

    """Implementation of the 'UpdateLdapProviderParam' model.

    Specifies the update LDAP provider params.

    Attributes:
        ad_domain_name (string): Specifies the domain name of an Active
            Directory which is mapped to this LDAP provider
        attribute_common_name (string): Name of the LDAP attribute used for
            common name of an object.
        attribute_gid (string): Name of the attribute used to lookup unix GID
            of an LDAP user.
        attribute_member_of (string): Name of the LDAP attribute used to lookup
            members of a group.
        attribute_uid (string): Name of the attribute used to lookup unix UID
            of an LDAP user.
        attribute_user_name (string): Name of the LDAP attribute used to
            lookup a user by user ID.
        auth_type (AuthTypeEnum): Specifies the authentication type used while
            connecting to LDAP servers. Authentication level. 'kAnonymous'
            indicates LDAP authentication type 'Anonymous' 'kSimple' indicates
            LDAP authentication type 'Simple'
        base_distinguished_name (string): Specifies the base distinguished
            name used as the base for LDAP search requests.
        domain_name (string): Specifies the name of the domain name to be used
            for querying LDAP servers from DNS. If PreferredLdapServerList is
            set, then DomainName field is ignored.
        id (long|int): Specifies the ID of the LDAP provider.
        name (string): Specifies the name of the LDAP provider.
        object_class_group (string): Name of the LDAP group object class for
            user accounts.
        object_class_user (string): Name of the LDAP user object class for user
            accounts.
        port (int): Specifies LDAP server port.
        preferred_ldap_server_list (list of string): Specifies the preferred
            LDAP servers. Server names should be either in fully qualified
            domain name (FQDN) format or IP addresses.
        tenant_id (string): Specifies the unique id of the tenant.
        use_ssl (bool): Specifies whether to use SSL for LDAP connections.
        user_distinguished_name (string): Specifies the user distinguished
            name that is used for LDAP authentication. It should be provided
            if the AuthType is set to either kSimple or kSasl.
        user_password (string): Specifies the user password that is used for
            LDAP authentication.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ad_domain_name":'adDomainName',
        "attribute_common_name":'attributeCommonName',
        "attribute_gid":'attributeGid',
        "attribute_member_of":'attributeMemberOf',
        "attribute_uid":'attributeUid',
        "attribute_user_name":'attributeUserName',
        "auth_type":'authType',
        "base_distinguished_name":'baseDistinguishedName',
        "domain_name":'domainName',
        "id":'id',
        "name":'name',
        "object_class_group":'objectClassGroup',
        "object_class_user":'objectClassUser',
        "port":'port',
        "preferred_ldap_server_list":'preferredLdapServerList',
        "tenant_id":'tenantId',
        "use_ssl":'useSsl',
        "user_distinguished_name":'userDistinguishedName',
        "user_password":'userPassword'
    }

    def __init__(self,
                 ad_domain_name=None,
                 attribute_common_name=None,
                 attribute_gid=None,
                 attribute_member_of=None,
                 attribute_uid=None,
                 attribute_user_name=None,
                 auth_type=None,
                 base_distinguished_name=None,
                 domain_name=None,
                 id=None,
                 name=None,
                 object_class_group=None,
                 object_class_user=None,
                 port=None,
                 preferred_ldap_server_list=None,
                 tenant_id=None,
                 use_ssl=None,
                 user_distinguished_name=None,
                 user_password=None):
        """Constructor for the UpdateLdapProviderParam class"""

        # Initialize members of the class
        self.ad_domain_name = ad_domain_name
        self.attribute_gid = attribute_gid
        self.attribute_common_name = attribute_common_name
        self.attribute_member_of = attribute_member_of
        self.attribute_uid = attribute_uid
        self.attribute_user_name = attribute_user_name
        self.auth_type = auth_type
        self.base_distinguished_name = base_distinguished_name
        self.domain_name = domain_name
        self.id = id
        self.name = name
        self.object_class_group = object_class_group
        self.object_class_user = object_class_user
        self.port = port
        self.preferred_ldap_server_list = preferred_ldap_server_list
        self.tenant_id = tenant_id
        self.use_ssl = use_ssl
        self.user_distinguished_name = user_distinguished_name
        self.user_password = user_password


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
        ad_domain_name = dictionary.get('adDomainName')
        attribute_common_name = dictionary.get('attributeCommonName')
        attribute_gid = dictionary.get('attributeGid')
        attribute_member_of = dictionary.get('attributeMemberOf')
        attribute_uid = dictionary.get('attributeUid')
        attribute_user_name = dictionary.get('attributeUserName')
        auth_type = dictionary.get('authType')
        base_distinguished_name = dictionary.get('baseDistinguishedName')
        domain_name = dictionary.get('domainName')
        id = dictionary.get('id')
        name = dictionary.get('name')
        object_class_group = dictionary.get('objectClassGroup')
        object_class_user = dictionary.get('objectClassUser')
        port = dictionary.get('port')
        preferred_ldap_server_list = dictionary.get('preferredLdapServerList')
        tenant_id = dictionary.get('tenantId')
        use_ssl = dictionary.get('useSsl')
        user_distinguished_name = dictionary.get('userDistinguishedName')
        user_password = dictionary.get('userPassword')

        # Return an object of this model
        return cls(ad_domain_name,
                   attribute_common_name,
                   attribute_gid,
                   attribute_member_of,
                   attribute_uid,
                   attribute_user_name,
                   auth_type,
                   base_distinguished_name,
                   domain_name,
                   id,
                   name,
                   object_class_group,
                   object_class_user,
                   port,
                   preferred_ldap_server_list,
                   tenant_id,
                   use_ssl,
                   user_distinguished_name,
                   user_password)


