# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.vault_config
import cohesity_management_sdk.models.vault_bandwidth_limits

class Vault(object):

    """Implementation of the 'Vault' model.

    Specifies an external storage location and is equivalent to
    an External Target in the Cohesity Dashboard.
    A Vault can provide an additional Cloud Tier where cold data of the
    Cohesity Cluster can be stored in the Cloud.
    A Vault can also provide archive storage for backup data. This archive
    data
    is stored on Tapes and in Cloud Vaults.

    Attributes:
        ca_trusted_certificate (string): Specifies the CA (certificate
            authority) trusted certificate.
        client_certificate (string): Specifies the client CA  certificate.
            This certificate is in pem format.
        client_private_key (string): Specifies the client private key. This
            certificate is in pem format.
        compression_policy (CompressionPolicyVaultEnum): Specifies whether to
            send data to the Vault in a compressed format. 'kCompressionNone'
            indicates that data is not compressed. 'kCompressionLow' indicates
            that data is compressed using LZ4 or Snappy. 'kCompressionHigh'
            indicates that data is compressed in Gzip.
        config (VaultConfig): Specifies the settings required to connect to a
            specific Vault type. For some Vaults, you must also specify a
            storage location (bucketName).
        customer_managing_encryption_keys (bool): Specifies whether to manage
            the encryption key manually or let the Cohesity Cluster manage it.
            If true, you must get the encryption key store it outside the
            Cluster, before disaster strikes such as the source local Cohesity
            Cluster being down. You can get the encryption key by downloading
            it using the Cohesity Dashboard or by calling the GET
            /public/vaults/encryptionKey/{id} operation.
        dedup_enabled (bool): Specifies whether to deduplicate data before
            sending it to the Vault.
        delete_vault_error (string): Specifies the error message when deleting
            a vault.
        description (string): Specifies a description about the Vault.
        desired_wal_location (DesiredWalLocationEnum): Desired location for
            write ahead logs(wal). 'kHomePartition' indicates desired wal
            location to be the home partition. 'kDisk' indicates desired wal
            location to be the same disk as chunk repo. 'kScribe' indicates
            desired wal location to be scribe. 'kScribeTable' indicates chunk
            repository state is kept as key-value pairs in scribe.
        encryption_key_file_downloaded (bool): Specifies if the encryption key
            file has been downloaded using the Cohesity Dashboard (Cohesity
            UI). If true, the encryption key has been downloaded using the
            Cohesity Dashboard. An encryption key can only be downloaded once
            using the Cohesity Dashboard.
        encryption_policy (EncryptionPolicyVaultEnum): Specifies whether to
            send and store data in an encrypted format. 'kEncryptionNone'
            indicates the data is not encrypted. 'kEncryptionStrong' indicates
            the data is encrypted.
        external_target_type (ExternalTargetTypeEnum): Specifies the type of
            Vault. 'kNearline' indicates a Google Nearline Vault. 'kGlacier'
            indicates an AWS Glacier Vault. 'kS3' indicates an AWS S3 Vault.
            'kAzureStandard' indicates a Microsoft Azure Standard Vault.
            'kS3Compatible' indicates an S3 Compatible Vault. (See the online
            help for supported types.) 'kQStarTape' indicates a QStar Tape
            Vault. 'kGoogleStandard' indicates a Google Standard Vault.
            'kGoogleDRA' indicates a Google DRA Vault. 'kAmazonS3StandardIA'
            indicates an Amazon S3 Standard-IA Vault. 'kAWSGovCloud' indicates
            an AWS Gov Cloud Vault. 'kNAS' indicates a NAS Vault. 'kColdline'
            indicates a Google Coldline Vault. 'kAzureGovCloud' indicates a
            Microsoft Azure Gov Cloud Vault. 'kAzureArchive' indicates an
            Azure Archive Vault. 'kAzure' indicates an Azure Vault. 'kGoogle'
            indicates a Google Vault. 'kAmazon' indicates an Amazon Vault.
            'kOracle' indicates an Oracle Vault. 'kOracleTierStandard'
            indicates an Oracle Tier Standard Vault. 'kOracleTierArchive'
            indicates an Oracle Tier Archive Vault. 'kAmazonC2S' indicates an
            Amazon Commercial Cloud Services Vault.
        full_archive_interval_days (long|int): Specifies the number days
            between full archives to the Vault. The current default is 90
            days. This is only meaningful when incrementalArchivesEnabled is
            true and the Vault usage type is kArchival.
        id (long|int): Specifies an id that identifies the Vault.
        incremental_archives_enabled (bool): Specifies whether to perform
            incremental archival when sending data to the Vault. If false,
            only full backups are performed. If true, incremental backups are
            performed between the full backups.
        key_file_download_time_usecs (long|int): Specifies the time (in
            microseconds) when the encryption key file was downloaded from the
            Cohesity Dashboard (Cohesity UI). An encryption key can only be
            downloaded once using the Cohesity Dashboard.
        key_file_download_user (string): Specifies the user who downloaded the
            encryption key from the Cohesity Dashboard (Cohesity UI). This
            field is only populated if encryption is enabled for the Vault and
            customerManagingEncryptionKeys is true.
        name (string): Specifies the name of the Vault.
        removal_state (RemovalStateVaultEnum): Specifies the state of the
            vault to be removed. 'kDontRemove' means the state of object is
            functional and it is not being removed. 'kMarkedForRemoval' means
            the object is being removed. 'kOkToRemove' means the object has
            been removed on the Cohesity Cluster and if the object is
            physical, it can be removed from the Cohesity Cluster.
        mtype (TypeVaultEnum): Specifies the type of Vault. This field is
            deprecated. This field is split into ExternalTargetType in and
            TierType in respective credentials. Initialize those fields
            instead. deprecated: true 'kNearline' indicates a Google Nearline
            Vault. 'kGlacier' indicates an AWS Glacier Vault. 'kS3' indicates
            an AWS S3 Vault. 'kAzureStandard' indicates a Microsoft Azure
            Standard Vault. 'kS3Compatible' indicates an S3 Compatible Vault.
            (See the online help for supported types.) 'kQStarTape' indicates
            a QStar Tape Vault. 'kGoogleStandard' indicates a Google Standard
            Vault. 'kGoogleDRA' indicates a Google DRA Vault.
            'kAmazonS3StandardIA' indicates an Amazon S3 Standard-IA Vault.
            'kAWSGovCloud' indicates an AWS Gov Cloud Vault. 'kNAS' indicates
            a NAS Vault. 'kColdline' indicates a Google Coldline Vault.
            'kAzureGovCloud' indicates a Microsoft Azure Gov Cloud Vault.
            'kAzureArchive' indicates an Azure Archive Vault. 'kAzure'
            indicates an Azure Vault. 'kGoogle' indicates a Google Vault.
            'kAmazon' indicates an Amazon Vault. 'kOracle' indicates an Oracle
            Vault. 'kOracleTierStandard' indicates an Oracle Tier Standard
            Vault. 'kOracleTierArchive' indicates an Oracle Tier Archive
            Vault. 'kAmazonC2S' indicates an Amazon Commercial Cloud Services
            Vault.
        usage_type (UsageTypeEnum): Specifies the usage type of the Vault.
            'kArchival' indicates the Vault provides archive storage for
            backup data. 'kCloudSpill' indicates the Vault provides additional
            storage for cold data.
        vault_bandwidth_limits (VaultBandwidthLimits): VaultBandwidthLimits
            represents the network bandwidth limits while
            uploading/downloading data to/from the external media.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ca_trusted_certificate":'caTrustedCertificate',
        "client_certificate":'clientCertificate',
        "client_private_key":'clientPrivateKey',
        "compression_policy":'compressionPolicy',
        "config":'config',
        "customer_managing_encryption_keys":'customerManagingEncryptionKeys',
        "dedup_enabled":'dedupEnabled',
        "delete_vault_error":'deleteVaultError',
        "description":'description',
        "desired_wal_location":'desiredWalLocation',
        "encryption_key_file_downloaded":'encryptionKeyFileDownloaded',
        "encryption_policy":'encryptionPolicy',
        "external_target_type":'externalTargetType',
        "full_archive_interval_days":'fullArchiveIntervalDays',
        "id":'id',
        "incremental_archives_enabled":'incrementalArchivesEnabled',
        "key_file_download_time_usecs":'keyFileDownloadTimeUsecs',
        "key_file_download_user":'keyFileDownloadUser',
        "name":'name',
        "removal_state":'removalState',
        "mtype":'type',
        "usage_type":'usageType',
        "vault_bandwidth_limits":'vaultBandwidthLimits'
    }

    def __init__(self,
                 ca_trusted_certificate=None,
                 client_certificate=None,
                 client_private_key=None,
                 compression_policy=None,
                 config=None,
                 customer_managing_encryption_keys=None,
                 dedup_enabled=None,
                 delete_vault_error=None,
                 description=None,
                 desired_wal_location=None,
                 encryption_key_file_downloaded=None,
                 encryption_policy=None,
                 external_target_type=None,
                 full_archive_interval_days=None,
                 id=None,
                 incremental_archives_enabled=None,
                 key_file_download_time_usecs=None,
                 key_file_download_user=None,
                 name=None,
                 removal_state=None,
                 mtype=None,
                 usage_type=None,
                 vault_bandwidth_limits=None):
        """Constructor for the Vault class"""

        # Initialize members of the class
        self.ca_trusted_certificate = ca_trusted_certificate
        self.client_certificate = client_certificate
        self.client_private_key = client_private_key
        self.compression_policy = compression_policy
        self.config = config
        self.customer_managing_encryption_keys = customer_managing_encryption_keys
        self.dedup_enabled = dedup_enabled
        self.delete_vault_error = delete_vault_error
        self.description = description
        self.desired_wal_location = desired_wal_location
        self.encryption_key_file_downloaded = encryption_key_file_downloaded
        self.encryption_policy = encryption_policy
        self.external_target_type = external_target_type
        self.full_archive_interval_days = full_archive_interval_days
        self.id = id
        self.incremental_archives_enabled = incremental_archives_enabled
        self.key_file_download_time_usecs = key_file_download_time_usecs
        self.key_file_download_user = key_file_download_user
        self.name = name
        self.removal_state = removal_state
        self.mtype = mtype
        self.usage_type = usage_type
        self.vault_bandwidth_limits = vault_bandwidth_limits


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
        ca_trusted_certificate = dictionary.get('caTrustedCertificate')
        client_certificate = dictionary.get('clientCertificate')
        client_private_key = dictionary.get('clientPrivateKey')
        compression_policy = dictionary.get('compressionPolicy')
        config = cohesity_management_sdk.models.vault_config.VaultConfig.from_dictionary(dictionary.get('config')) if dictionary.get('config') else None
        customer_managing_encryption_keys = dictionary.get('customerManagingEncryptionKeys')
        dedup_enabled = dictionary.get('dedupEnabled')
        delete_vault_error = dictionary.get('deleteVaultError')
        description = dictionary.get('description')
        desired_wal_location = dictionary.get('desiredWalLocation')
        encryption_key_file_downloaded = dictionary.get('encryptionKeyFileDownloaded')
        encryption_policy = dictionary.get('encryptionPolicy')
        external_target_type = dictionary.get('externalTargetType')
        full_archive_interval_days = dictionary.get('fullArchiveIntervalDays')
        id = dictionary.get('id')
        incremental_archives_enabled = dictionary.get('incrementalArchivesEnabled')
        key_file_download_time_usecs = dictionary.get('keyFileDownloadTimeUsecs')
        key_file_download_user = dictionary.get('keyFileDownloadUser')
        name = dictionary.get('name')
        removal_state = dictionary.get('removalState')
        mtype = dictionary.get('type')
        usage_type = dictionary.get('usageType')
        vault_bandwidth_limits = cohesity_management_sdk.models.vault_bandwidth_limits.VaultBandwidthLimits.from_dictionary(dictionary.get('vaultBandwidthLimits')) if dictionary.get('vaultBandwidthLimits') else None

        # Return an object of this model
        return cls(ca_trusted_certificate,
                   client_certificate,
                   client_private_key,
                   compression_policy,
                   config,
                   customer_managing_encryption_keys,
                   dedup_enabled,
                   delete_vault_error,
                   description,
                   desired_wal_location,
                   encryption_key_file_downloaded,
                   encryption_policy,
                   external_target_type,
                   full_archive_interval_days,
                   id,
                   incremental_archives_enabled,
                   key_file_download_time_usecs,
                   key_file_download_user,
                   name,
                   removal_state,
                   mtype,
                   usage_type,
                   vault_bandwidth_limits)


