# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CreateIdpConfigurationRequest(object):

    """Implementation of the 'CreateIdpConfigurationRequest' model.

    Specifies the configuration for an IdP service to be created.

    Attributes:
        allow_local_authentication (bool): Specifies whether to allow local
            authentication. When IdP is configured, only IdP users are allowed
            to login to the Cluster. Local login is disabled except for users
            with admin role. If this flag is set to true, local (non-IdP)
            logins are allowed for all local and AD users. Local or AD users
            with admin role can login always independent of this flag's
            setting.
        certificate (string): Specifies the certificate generated for the app
            by the IdP service when the Cluster is registerd as an app. This
            is required to verify the SAML response.
        certificate_filename (string): Specifies the filename used to upload
            the certificate.
        domain (string): Specifies a unique name for this IdP configuration.
        enable (bool): Specifies a flag to enable or disable this IdP service.
            When it is set to true, IdP service is enabled. When it is set to
            false, IdP service is disabled. When an IdP service is created, it
            is set to true.
        issuer_id (string): Specifies the IdP provided Issuer ID for the app.
            For example, exkh1aov1nhHrgFhN0h7.
        name (string): Specifies the name of the vendor providing IdP
            service.
        roles (list of string): Specifies a list roles assigned to an IdP user
            if samlAttributeName is not given.
        saml_attribute_name (string): Specifies the SAML attribute name that
            contains a comma separated list of Cluster roles. Either this
            field or roles must be set. This field takes higher precedence
            than the roles field.
        sign_request (bool): Specifies whether to sign the SAML request or
            not. When it is set to true, SAML request will be signed. When it
            is set to false, SAML request is not signed. Default is false. Set
            this flag to true if the IdP site is configured to expect the SAML
            request from the Cluster signed. If this is set to true, users
            must get the Cluster's certificate and upload it on the IdP site.
        sso_url (string): Specifies the SSO URL of the IdP service for the
            customer. This is the URL given by IdP when the customer created
            an account. Customers may use this for several clusters that are
            registered with on IdP site. For example,
            dev-332534.oktapreview.com
        tenant_id (string): Specifies the Tenant Id if the IdP is configured
            for a Tenant. If this is not set, this IdP configuration is used
            for the Cluster level users and for all users of Tenants not
            having an IdP configuration.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allow_local_authentication":'allowLocalAuthentication',
        "certificate":'certificate',
        "certificate_filename":'certificateFilename',
        "domain":'domain',
        "enable":'enable',
        "issuer_id":'issuerId',
        "name":'name',
        "roles":'roles',
        "saml_attribute_name":'samlAttributeName',
        "sign_request":'signRequest',
        "sso_url":'ssoUrl',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 allow_local_authentication=None,
                 certificate=None,
                 certificate_filename=None,
                 domain=None,
                 enable=None,
                 issuer_id=None,
                 name=None,
                 roles=None,
                 saml_attribute_name=None,
                 sign_request=None,
                 sso_url=None,
                 tenant_id=None):
        """Constructor for the CreateIdpConfigurationRequest class"""

        # Initialize members of the class
        self.allow_local_authentication = allow_local_authentication
        self.certificate = certificate
        self.certificate_filename = certificate_filename
        self.domain = domain
        self.enable = enable
        self.issuer_id = issuer_id
        self.name = name
        self.roles = roles
        self.saml_attribute_name = saml_attribute_name
        self.sign_request = sign_request
        self.sso_url = sso_url
        self.tenant_id = tenant_id


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
        allow_local_authentication = dictionary.get('allowLocalAuthentication')
        certificate = dictionary.get('certificate')
        certificate_filename = dictionary.get('certificateFilename')
        domain = dictionary.get('domain')
        enable = dictionary.get('enable')
        issuer_id = dictionary.get('issuerId')
        name = dictionary.get('name')
        roles = dictionary.get('roles')
        saml_attribute_name = dictionary.get('samlAttributeName')
        sign_request = dictionary.get('signRequest')
        sso_url = dictionary.get('ssoUrl')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(allow_local_authentication,
                   certificate,
                   certificate_filename,
                   domain,
                   enable,
                   issuer_id,
                   name,
                   roles,
                   saml_attribute_name,
                   sign_request,
                   sso_url,
                   tenant_id)


