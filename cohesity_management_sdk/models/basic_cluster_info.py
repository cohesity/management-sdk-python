# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.domain


class BasicClusterInfo(object):

    """Implementation of the 'BasicClusterInfo' model.

    Specifies basic information about the Cohesity Cluster.


    Attributes:

        authentication_type (AuthenticationTypeEnum): Specifies the
            authentication scheme for the cluster. 'kPasswordOnly' indicates
            the normal cohesity authentication type. 'kCertificateOnly'
            indicates that certificate based authentication has been enabled
            and the password based authentication has been turned off.
            'kPasswordAndCertificate' indicates that both the authenticatio
            schemes are required.
        banner_enabled (bool): Specifies if banner is enabled on the cluster.
        cluster_domains (list of Domain): Specifies a list of domains joined to
            the Cohesity Cluster with their trust relationships.
        cluster_software_version (string): This field is deprecated. Specifies
            the current release of the Cohesity software running on this
            Cohesity Cluster. deprecated: true
        cluster_type (ClusterTypeEnum): Specifies the type of Cohesity Cluster.
            'kPhysical' indicates the Cohesity Cluster is hosted directly on
            hardware. 'kVirtualRobo' indicates the Cohesity Cluster is hosted
            in a VM on a ESXi Host of a VMware vCenter Server using Cohesity's
            Virtual Edition. 'kMicrosoftCloud' indicates the Cohesity Cluster
            is hosted in a VM on Microsoft Azure using Cohesity's Cloud
            Edition. 'kAmazonCloud' indicates the Cohesity Cluster is hosted in
            a VM on Amazon S3 using Cohesity's Cloud Edition. 'kGoogleCloud'
            indicates the Cohesity Cluster is hosted in a VM on Google Cloud
            Platform using Cohesity's Cloud Edition.
        dodin_mode_enabled (bool): Specifies if dodin mode is enabled on the
            cluster.
        domains (list of string): Array of Domains.  Specifies a list of
            domains joined to the Cohesity Cluster, including the default LOCAL
            Cohesity domain used to store the local Cohesity users.
        helios_control_plane_env (string): Specifies the HeliosControlPlaneEnv.
        idp_configured (bool): Specifies Idp is configured for the Cluster.
        idp_tenant_exists (bool): Specifies Idp is configured for a Tenant.
        language_locale (string): Specifies the language and locale for the
            Cohesity Cluster.
        mcm_mode (bool): Specifies whether server is running in mcm-mode. If
            set to true, it is in mcm-mode.
        mcm_on_prem_mode (bool): Specifies whether server is running in
            mcm-on-prem-mode. If set to true, it is in mcm on prem mode. This
            need mcm-mode to be true.
        multi_tenancy_enabled (bool): Specifies if multi-tenancy is enabled on
            the cluster.
        name (string): Specifies the name of the Cohesity Cluster.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "authentication_type":'authenticationType',
        "banner_enabled":'bannerEnabled',
        "cluster_domains":'clusterDomains',
        "cluster_software_version":'clusterSoftwareVersion',
        "cluster_type":'clusterType',
        "dodin_mode_enabled":'dodinModeEnabled',
        "domains":'domains',
        "helios_control_plane_env":'heliosControlPlaneEnv',
        "idp_configured":'idpConfigured',
        "idp_tenant_exists":'idpTenantExists',
        "language_locale":'languageLocale',
        "mcm_mode":'mcmMode',
        "mcm_on_prem_mode":'mcmOnPremMode',
        "multi_tenancy_enabled":'multiTenancyEnabled',
        "name":'name',
    }
    def __init__(self,
                 authentication_type=None,
                 banner_enabled=None,
                 cluster_domains=None,
                 cluster_software_version=None,
                 cluster_type=None,
                 dodin_mode_enabled=None,
                 domains=None,
                 helios_control_plane_env=None,
                 idp_configured=None,
                 idp_tenant_exists=None,
                 language_locale=None,
                 mcm_mode=None,
                 mcm_on_prem_mode=None,
                 multi_tenancy_enabled=None,
                 name=None,
            ):

        """Constructor for the BasicClusterInfo class"""

        # Initialize members of the class
        self.authentication_type = authentication_type
        self.banner_enabled = banner_enabled
        self.cluster_domains = cluster_domains
        self.cluster_software_version = cluster_software_version
        self.cluster_type = cluster_type
        self.dodin_mode_enabled = dodin_mode_enabled
        self.domains = domains
        self.helios_control_plane_env = helios_control_plane_env
        self.idp_configured = idp_configured
        self.idp_tenant_exists = idp_tenant_exists
        self.language_locale = language_locale
        self.mcm_mode = mcm_mode
        self.mcm_on_prem_mode = mcm_on_prem_mode
        self.multi_tenancy_enabled = multi_tenancy_enabled
        self.name = name

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
        authentication_type = dictionary.get('authenticationType')
        banner_enabled = dictionary.get('bannerEnabled')
        cluster_domains = None
        if dictionary.get('clusterDomains') != None:
            cluster_domains = list()
            for structure in dictionary.get('clusterDomains'):
                cluster_domains.append(cohesity_management_sdk.models.domain.Domain.from_dictionary(structure))
        cluster_software_version = dictionary.get('clusterSoftwareVersion')
        cluster_type = dictionary.get('clusterType')
        dodin_mode_enabled = dictionary.get('dodinModeEnabled')
        domains = dictionary.get("domains")
        helios_control_plane_env = dictionary.get('heliosControlPlaneEnv')
        idp_configured = dictionary.get('idpConfigured')
        idp_tenant_exists = dictionary.get('idpTenantExists')
        language_locale = dictionary.get('languageLocale')
        mcm_mode = dictionary.get('mcmMode')
        mcm_on_prem_mode = dictionary.get('mcmOnPremMode')
        multi_tenancy_enabled = dictionary.get('multiTenancyEnabled')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(
            authentication_type,
            banner_enabled,
            cluster_domains,
            cluster_software_version,
            cluster_type,
            dodin_mode_enabled,
            domains,
            helios_control_plane_env,
            idp_configured,
            idp_tenant_exists,
            language_locale,
            mcm_mode,
            mcm_on_prem_mode,
            multi_tenancy_enabled,
            name
)