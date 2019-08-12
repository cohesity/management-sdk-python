# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.acropolis_protection_source
import cohesity_management_sdk.models.ad_protection_source
import cohesity_management_sdk.models.aws_protection_source
import cohesity_management_sdk.models.azure_protection_source
import cohesity_management_sdk.models.flash_blade_protection_source
import cohesity_management_sdk.models.gcp_protection_source
import cohesity_management_sdk.models.gpfs_protection_source
import cohesity_management_sdk.models.hyper_flex_protection_source
import cohesity_management_sdk.models.hyperv_protection_source
import cohesity_management_sdk.models.isilon_protection_source
import cohesity_management_sdk.models.kubernetes_protection_source
import cohesity_management_sdk.models.kvm_protection_source
import cohesity_management_sdk.models.nas_protection_source
import cohesity_management_sdk.models.netapp_protection_source
import cohesity_management_sdk.models.office_365_protection_source
import cohesity_management_sdk.models.oracle_protection_source
import cohesity_management_sdk.models.physical_protection_source
import cohesity_management_sdk.models.pure_protection_source
import cohesity_management_sdk.models.sql_protection_source
import cohesity_management_sdk.models.view_protection_source
import cohesity_management_sdk.models.vmware_protection_source

class ProtectionSource(object):

    """Implementation of the 'ProtectionSource' model.

    Specifies a generic structure that represents a node
    in the Protection Source tree. Node details will depend on the
    environment of the Protection Source.

    Attributes:
        acropolis_protection_source (AcropolisProtectionSource): Specifies
            details about an Acropolis Protection Source when the environment
            is set to 'kAcropolis'.
        ad_protection_source (AdProtectionSource): Specifies details about an
            AD Protection Source when the environment is set to 'kAD'.
        aws_protection_source (AwsProtectionSource): Specifies details about
            an AWS Protection Source when the environment is set to 'kAWS'.
        azure_protection_source (AzureProtectionSource): Specifies details
            about an Azure Protection Source when the environment is set to
            'kAzure'.
        environment (EnvironmentEnum): Specifies the environment (such as
            'kVMware' or 'kSQL') where the Protection Source exists. Depending
            on the environment, one of the following Protection Sources are
            initialized.  NOTE: kPuppeteer refers to Cohesity's Remote
            Adapter. Supported environment types such as 'kView', 'kSQL',
            'kVMware', etc. NOTE: 'kPuppeteer' refers to Cohesity's Remote
            Adapter. 'kVMware' indicates the VMware Protection Source
            environment. 'kHyperV' indicates the HyperV Protection Source
            environment. 'kSQL' indicates the SQL Protection Source
            environment. 'kView' indicates the View Protection Source
            environment. 'kPuppeteer' indicates the Cohesity's Remote Adapter.
            'kPhysical' indicates the physical Protection Source environment.
            'kPure' indicates the Pure Storage Protection Source environment.
            'kAzure' indicates the Microsoft's Azure Protection Source
            environment. 'kNetapp' indicates the Netapp Protection Source
            environment. 'kAgent' indicates the Agent Protection Source
            environment. 'kGenericNas' indicates the Genreric Network Attached
            Storage Protection Source environment. 'kAcropolis' indicates the
            Acropolis Protection Source environment. 'kPhsicalFiles' indicates
            the Physical Files Protection Source environment. 'kIsilon'
            indicates the Dell EMC's Isilon Protection Source environment.
            'kGPFS' indicates IBM's GPFS Protection Source environment. 'kKVM'
            indicates the KVM Protection Source environment. 'kAWS' indicates
            the AWS Protection Source environment. 'kExchange' indicates the
            Exchange Protection Source environment. 'kHyperVVSS' indicates the
            HyperV VSS Protection Source environment. 'kOracle' indicates the
            Oracle Protection Source environment. 'kGCP' indicates the Google
            Cloud Platform Protection Source environment. 'kFlashBlade'
            indicates the Flash Blade Protection Source environment.
            'kAWSNative' indicates the AWS Native Protection Source
            environment. 'kVCD' indicates the VMware's Virtual cloud Director
            Protection Source environment. 'kO365' indicates the Office 365
            Protection Source environment. 'kO365Outlook' indicates Office 365
            outlook Protection Source environment. 'kHyperFlex' indicates the
            Hyper Flex Protection Source environment. 'kGCPNative' indicates
            the GCP Native Protection Source environment. 'kAzureNative'
            indicates the Azure Native Protection Source environment.
            'kKubernetes' indicates a Kubernetes Protection Source
            environment.
        flash_blade_protection_source (FlashBladeProtectionSource): Specifies
            details about a Pure Storage FlashBlade Protection Source when the
            environment is set to 'kFlashBlade'.
        gcp_protection_source (GcpProtectionSource): Specifies details about
            an GCP Protection Source when the environment is set to 'kGCP'.
        gpfs_protection_source (GpfsProtectionSource): Specifies details about
            an GPFS Protection Source when the environment is set to 'kGPFS'.
        hyper_flex_protection_source (HyperFlexProtectionSource): Specifies
            details about a HyperFlex Storage Snapshot source when the
            environment is set to 'kHyperFlex'
        hyperv_protection_source (HypervProtectionSource): Specifies details
            about a HyperV Protection Source when the environment is set to
            'kHyperV'.
        id (long|int): Specifies an id of the Protection Source.
        isilon_protection_source (IsilonProtectionSource): Specifies details
            about an Isilon OneFs Protection Source when the environment is
            set to 'kIsilon'.
        kubernetes_protection_source (KubernetesProtectionSource): Specifies
            details about a Kubernetes Protection Source when the environment
            is set to 'kKubernetes'.
        kvm_protection_source (KvmProtectionSource): Specifies details about a
            KVM Protection Source when the environment is set to 'kKVM'.
        name (string): Specifies a name of the Protection Source.
        nas_protection_source (NasProtectionSource): Specifies details about a
            Generic NAS Protection Source when the environment is set to
            'kGenericNas'.
        netapp_protection_source (NetappProtectionSource): Specifies details
            about a NetApp Protection Source when the environment is set to
            'kNetapp'.
        office_365_protection_source (Office365ProtectionSource): Specifies
            details about an Office 365 Protection Source when the environment
            is set to 'kO365'.
        oracle_protection_source (OracleProtectionSource): Specifies details
            about an Oracle Protection Source when the environment is set to
            'kOracle'.
        parent_id (long|int): Specifies an id of the parent of the Protection
            Source.
        physical_protection_source (PhysicalProtectionSource): Specifies
            details about a Physical Protection Source when the environment is
            set to 'kPhysical'.
        pure_protection_source (PureProtectionSource): Specifies details about
            a Pure Protection Source when the environment is set to 'kPure'.
        sql_protection_source (SqlProtectionSource): Specifies details about a
            SQL Protection Source when the environment is set to 'kSQL'.
        view_protection_source (ViewProtectionSource): Specifies details about
            a View Protection Source when the environment is set to 'kView'.
        vmware_protection_source (VmwareProtectionSource): Specifies details
            about a VMware Protection Source when the environment is set to
            'kVMware'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "acropolis_protection_source":'acropolisProtectionSource',
        "ad_protection_source":'adProtectionSource',
        "aws_protection_source":'awsProtectionSource',
        "azure_protection_source":'azureProtectionSource',
        "environment":'environment',
        "flash_blade_protection_source":'flashBladeProtectionSource',
        "gcp_protection_source":'gcpProtectionSource',
        "gpfs_protection_source":'gpfsProtectionSource',
        "hyper_flex_protection_source":'hyperFlexProtectionSource',
        "hyperv_protection_source":'hypervProtectionSource',
        "id":'id',
        "isilon_protection_source":'isilonProtectionSource',
        "kubernetes_protection_source":'kubernetesProtectionSource',
        "kvm_protection_source":'kvmProtectionSource',
        "name":'name',
        "nas_protection_source":'nasProtectionSource',
        "netapp_protection_source":'netappProtectionSource',
        "office_365_protection_source":'office365ProtectionSource',
        "oracle_protection_source":'oracleProtectionSource',
        "parent_id":'parentId',
        "physical_protection_source":'physicalProtectionSource',
        "pure_protection_source":'pureProtectionSource',
        "sql_protection_source":'sqlProtectionSource',
        "view_protection_source":'viewProtectionSource',
        "vmware_protection_source":'vmWareProtectionSource'
    }

    def __init__(self,
                 acropolis_protection_source=None,
                 ad_protection_source=None,
                 aws_protection_source=None,
                 azure_protection_source=None,
                 environment=None,
                 flash_blade_protection_source=None,
                 gcp_protection_source=None,
                 gpfs_protection_source=None,
                 hyper_flex_protection_source=None,
                 hyperv_protection_source=None,
                 id=None,
                 isilon_protection_source=None,
                 kubernetes_protection_source=None,
                 kvm_protection_source=None,
                 name=None,
                 nas_protection_source=None,
                 netapp_protection_source=None,
                 office_365_protection_source=None,
                 oracle_protection_source=None,
                 parent_id=None,
                 physical_protection_source=None,
                 pure_protection_source=None,
                 sql_protection_source=None,
                 view_protection_source=None,
                 vmware_protection_source=None):
        """Constructor for the ProtectionSource class"""

        # Initialize members of the class
        self.acropolis_protection_source = acropolis_protection_source
        self.ad_protection_source = ad_protection_source
        self.aws_protection_source = aws_protection_source
        self.azure_protection_source = azure_protection_source
        self.environment = environment
        self.flash_blade_protection_source = flash_blade_protection_source
        self.gcp_protection_source = gcp_protection_source
        self.gpfs_protection_source = gpfs_protection_source
        self.hyper_flex_protection_source = hyper_flex_protection_source
        self.hyperv_protection_source = hyperv_protection_source
        self.id = id
        self.isilon_protection_source = isilon_protection_source
        self.kubernetes_protection_source = kubernetes_protection_source
        self.kvm_protection_source = kvm_protection_source
        self.name = name
        self.nas_protection_source = nas_protection_source
        self.netapp_protection_source = netapp_protection_source
        self.office_365_protection_source = office_365_protection_source
        self.oracle_protection_source = oracle_protection_source
        self.parent_id = parent_id
        self.physical_protection_source = physical_protection_source
        self.pure_protection_source = pure_protection_source
        self.sql_protection_source = sql_protection_source
        self.view_protection_source = view_protection_source
        self.vmware_protection_source = vmware_protection_source


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
        acropolis_protection_source = cohesity_management_sdk.models.acropolis_protection_source.AcropolisProtectionSource.from_dictionary(dictionary.get('acropolisProtectionSource')) if dictionary.get('acropolisProtectionSource') else None
        ad_protection_source = cohesity_management_sdk.models.ad_protection_source.AdProtectionSource.from_dictionary(dictionary.get('adProtectionSource')) if dictionary.get('adProtectionSource') else None
        aws_protection_source = cohesity_management_sdk.models.aws_protection_source.AwsProtectionSource.from_dictionary(dictionary.get('awsProtectionSource')) if dictionary.get('awsProtectionSource') else None
        azure_protection_source = cohesity_management_sdk.models.azure_protection_source.AzureProtectionSource.from_dictionary(dictionary.get('azureProtectionSource')) if dictionary.get('azureProtectionSource') else None
        environment = dictionary.get('environment')
        flash_blade_protection_source = cohesity_management_sdk.models.flash_blade_protection_source.FlashBladeProtectionSource.from_dictionary(dictionary.get('flashBladeProtectionSource')) if dictionary.get('flashBladeProtectionSource') else None
        gcp_protection_source = cohesity_management_sdk.models.gcp_protection_source.GcpProtectionSource.from_dictionary(dictionary.get('gcpProtectionSource')) if dictionary.get('gcpProtectionSource') else None
        gpfs_protection_source = cohesity_management_sdk.models.gpfs_protection_source.GpfsProtectionSource.from_dictionary(dictionary.get('gpfsProtectionSource')) if dictionary.get('gpfsProtectionSource') else None
        hyper_flex_protection_source = cohesity_management_sdk.models.hyper_flex_protection_source.HyperFlexProtectionSource.from_dictionary(dictionary.get('hyperFlexProtectionSource')) if dictionary.get('hyperFlexProtectionSource') else None
        hyperv_protection_source = cohesity_management_sdk.models.hyperv_protection_source.HypervProtectionSource.from_dictionary(dictionary.get('hypervProtectionSource')) if dictionary.get('hypervProtectionSource') else None
        id = dictionary.get('id')
        isilon_protection_source = cohesity_management_sdk.models.isilon_protection_source.IsilonProtectionSource.from_dictionary(dictionary.get('isilonProtectionSource')) if dictionary.get('isilonProtectionSource') else None
        kubernetes_protection_source = cohesity_management_sdk.models.kubernetes_protection_source.KubernetesProtectionSource.from_dictionary(dictionary.get('kubernetesProtectionSource')) if dictionary.get('kubernetesProtectionSource') else None
        kvm_protection_source = cohesity_management_sdk.models.kvm_protection_source.KvmProtectionSource.from_dictionary(dictionary.get('kvmProtectionSource')) if dictionary.get('kvmProtectionSource') else None
        name = dictionary.get('name')
        nas_protection_source = cohesity_management_sdk.models.nas_protection_source.NasProtectionSource.from_dictionary(dictionary.get('nasProtectionSource')) if dictionary.get('nasProtectionSource') else None
        netapp_protection_source = cohesity_management_sdk.models.netapp_protection_source.NetappProtectionSource.from_dictionary(dictionary.get('netappProtectionSource')) if dictionary.get('netappProtectionSource') else None
        office_365_protection_source = cohesity_management_sdk.models.office_365_protection_source.Office365ProtectionSource.from_dictionary(dictionary.get('office365ProtectionSource')) if dictionary.get('office365ProtectionSource') else None
        oracle_protection_source = cohesity_management_sdk.models.oracle_protection_source.OracleProtectionSource.from_dictionary(dictionary.get('oracleProtectionSource')) if dictionary.get('oracleProtectionSource') else None
        parent_id = dictionary.get('parentId')
        physical_protection_source = cohesity_management_sdk.models.physical_protection_source.PhysicalProtectionSource.from_dictionary(dictionary.get('physicalProtectionSource')) if dictionary.get('physicalProtectionSource') else None
        pure_protection_source = cohesity_management_sdk.models.pure_protection_source.PureProtectionSource.from_dictionary(dictionary.get('pureProtectionSource')) if dictionary.get('pureProtectionSource') else None
        sql_protection_source = cohesity_management_sdk.models.sql_protection_source.SqlProtectionSource.from_dictionary(dictionary.get('sqlProtectionSource')) if dictionary.get('sqlProtectionSource') else None
        view_protection_source = cohesity_management_sdk.models.view_protection_source.ViewProtectionSource.from_dictionary(dictionary.get('viewProtectionSource')) if dictionary.get('viewProtectionSource') else None
        vmware_protection_source = cohesity_management_sdk.models.vmware_protection_source.VmwareProtectionSource.from_dictionary(dictionary.get('vmWareProtectionSource')) if dictionary.get('vmWareProtectionSource') else None

        # Return an object of this model
        return cls(acropolis_protection_source,
                   ad_protection_source,
                   aws_protection_source,
                   azure_protection_source,
                   environment,
                   flash_blade_protection_source,
                   gcp_protection_source,
                   gpfs_protection_source,
                   hyper_flex_protection_source,
                   hyperv_protection_source,
                   id,
                   isilon_protection_source,
                   kubernetes_protection_source,
                   kvm_protection_source,
                   name,
                   nas_protection_source,
                   netapp_protection_source,
                   office_365_protection_source,
                   oracle_protection_source,
                   parent_id,
                   physical_protection_source,
                   pure_protection_source,
                   sql_protection_source,
                   view_protection_source,
                   vmware_protection_source)


