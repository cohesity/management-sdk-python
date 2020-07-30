# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class EnvTypeEnum(object):

    """Implementation of the 'EnvType' enum.

    Specifies the environment type of the job.
    Supported environment types such as 'kView', 'kSQL', 'kVMware', etc.
    NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.
    'kVMware' indicates the VMware Protection Source environment.
    'kHyperV' indicates the HyperV Protection Source environment.
    'kSQL' indicates the SQL Protection Source environment.
    'kView' indicates the View Protection Source environment.
    'kPuppeteer' indicates the Cohesity's Remote Adapter.
    'kPhysical' indicates the physical Protection Source environment.
    'kPure' indicates the Pure Storage Protection Source environment.
    'Nimble' indicates the Nimble Storage Protection Source environment.
    'kAzure' indicates the Microsoft's Azure Protection Source environment.
    'kNetapp' indicates the Netapp Protection Source environment.
    'kAgent' indicates the Agent Protection Source environment.
    'kGenericNas' indicates the Generic Network Attached Storage Protection
    Source environment.
    'kAcropolis' indicates the Acropolis Protection Source environment.
    'kPhsicalFiles' indicates the Physical Files Protection Source
    environment.
    'kIsilon' indicates the Dell EMC's Isilon Protection Source environment.
    'kGPFS' indicates IBM's GPFS Protection Source environment.
    'kKVM' indicates the KVM Protection Source environment.
    'kAWS' indicates the AWS Protection Source environment.
    'kExchange' indicates the Exchange Protection Source environment.
    'kHyperVVSS' indicates the HyperV VSS Protection Source
    environment.
    'kOracle' indicates the Oracle Protection Source environment.
    'kGCP' indicates the Google Cloud Platform Protection Source environment.
    'kFlashBlade' indicates the Flash Blade Protection Source environment.
    'kAWSNative' indicates the AWS Native Protection Source environment.
    'kO365' indicates the Office 365 Protection Source environment.
    'kO365Outlook' indicates Office 365 outlook Protection Source
    environment.
    'kHyperFlex' indicates the Hyper Flex Protection Source environment.
    'kGCPNative' indicates the GCP Native Protection Source environment.
    'kAzureNative' indicates the Azure Native Protection Source environment.
    'kKubernetes' indicates a Kubernetes Protection Source environment.
    'kElastifile' indicates Elastifile Protection Source environment.
    'kAD' indicates Active Directory Protection Source environment.
    'kRDSSnapshotManager' indicates AWS RDS Protection Source
    environment.

    Attributes:
        KVMWARE: TODO: type description here.
        KHYPERV: TODO: type description here.
        KSQL: TODO: type description here.
        KVIEW: TODO: type description here.
        KPUPPETEER: TODO: type description here.
        KPHYSICAL: TODO: type description here.
        KPURE: TODO: type description here.
        KNIMBLE: TODO: type description here.
        KAZURE: TODO: type description here.
        KNETAPP: TODO: type description here.
        KAGENT: TODO: type description here.
        KGENERICNAS: TODO: type description here.
        KACROPOLIS: TODO: type description here.
        KPHYSICALFILES: TODO: type description here.
        KISILON: TODO: type description here.
        KGPFS: TODO: type description here.
        KKVM: TODO: type description here.
        KAWS: TODO: type description here.
        KEXCHANGE: TODO: type description here.
        KHYPERVVSS: TODO: type description here.
        KORACLE: TODO: type description here.
        KGCP: TODO: type description here.
        KFLASHBLADE: TODO: type description here.
        KAWSNATIVE: TODO: type description here.
        KO365: TODO: type description here.
        KO365OUTLOOK: TODO: type description here.
        KHYPERFLEX: TODO: type description here.
        KGCPNATIVE: TODO: type description here.
        KAZURENATIVE: TODO: type description here.
        KKUBERNETES: TODO: type description here.
        KELASTIFILE: TODO: type description here.
        KAD: TODO: type description here.
        KRDSSNAPSHOTMANAGER: TODO: type description here.

    """

    K_VMWARE = 'kVMware'

    K_HYPERV = 'kHyperV'

    KSQL = 'kSQL'

    KVIEW = 'kView'

    KPUPPETEER = 'kPuppeteer'

    KPHYSICAL = 'kPhysical'

    KPURE = 'kPure'

    KNIMBLE = 'kNimble'

    KAZURE = 'kAzure'

    KNETAPP = 'kNetapp'

    KAGENT = 'kAgent'

    KGENERICNAS = 'kGenericNas'

    KACROPOLIS = 'kAcropolis'

    KPHYSICALFILES = 'kPhysicalFiles'

    KISILON = 'kIsilon'

    KGPFS = 'kGPFS'

    KKVM = 'kKVM'

    KAWS = 'kAWS'

    KEXCHANGE = 'kExchange'

    K_HYPERV_VSS = 'kHyperVVSS'

    KORACLE = 'kOracle'

    KGCP = 'kGCP'

    KFLASHBLADE = 'kFlashBlade'

    KAWSNATIVE = 'kAWSNative'

    KO365 = 'kO365'

    KO365OUTLOOK = 'kO365Outlook'

    KHYPERFLEX = 'kHyperFlex'

    KGCPNATIVE = 'kGCPNative'

    KAZURENATIVE = 'kAzureNative'

    KKUBERNETES = 'kKubernetes'

    KELASTIFILE = 'kElastifile'

    KAD = 'kAD'

    KRDSSNAPSHOTMANAGER = 'kRDSSnapshotManager'
