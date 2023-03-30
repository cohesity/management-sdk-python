# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.archival_external_target
import cohesity_management_sdk.models.cloud_deploy_target_details
import cohesity_management_sdk.models.universal_id


class RestoreObjectDetails(object):

    """Implementation of the 'RestoreObjectDetails' model.

    Specifies an object to recover or clone or an object to restore files and
    folders from. A VM object can be recovered or cloned. A View object can be
    cloned. To specify a particular snapshot, you must specify a jobRunId and a
    startTimeUsecs. If jobRunId and startTimeUsecs are not specified, the last
    Job Run of the specified Job is used.


    Attributes:

        archival_target (ArchivalExternalTarget): Specifies settings about the
            Archival Target (such as Tape or AWS). This field must be set if
            the object is being recovered or cloned from an archive or if files
            or folders are being restored from an archive.
        cloud_deploy_target (CloudDeployTargetDetails): Specifies settings
            about the Cloud Deploy target. This field must be set if the
            restore type is kDeployVMs and the object is to be deployed to
            cloud using a previously converted image.
        environment (EnvironmentRestoreObjectDetailsEnum): Specifies the type
            of the Protection Source. Supported environment types such as
            'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer' refers to
            Cohesity's Remote Adapter. 'kVMware' indicates the VMware
            Protection Source environment. 'kHyperV' indicates the HyperV
            Protection Source environment. 'kSQL' indicates the SQL Protection
            Source environment. 'kView' indicates the View Protection Source
            environment. 'kPuppeteer' indicates the Cohesity's Remote Adapter.
            'kPhysical' indicates the physical Protection Source environment.
            'kPure' indicates the Pure Storage Protection Source environment.
            'kNimble' indicates the Nimble Storage Protection Source
            environment. 'kAzure' indicates the Microsoft's Azure Protection
            Source environment. 'kNetapp' indicates the Netapp Protection
            Source environment. 'kAgent' indicates the Agent Protection Source
            environment. 'kGenericNas' indicates the Generic Network Attached
            Storage Protection Source environment. 'kAcropolis' indicates the
            Acropolis Protection Source environment. 'kPhysicalFiles' indicates
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
            environment. 'kO365' indicates the Office 365 Protection Source
            environment. 'kO365Outlook' indicates Office 365 outlook Protection
            Source environment. 'kHyperFlex' indicates the Hyper Flex
            Protection Source environment. 'kGCPNative' indicates the GCP
            Native Protection Source environment. 'kAzureNative' indicates the
            Azure Native Protection Source environment. 'kKubernetes' indicates
            a Kubernetes Protection Source environment. 'kElastifile' indicates
            Elastifile Protection Source environment. 'kAD' indicates Active
            Directory Protection Source environment. 'kRDSSnapshotManager'
            indicates AWS RDS Protection Source environment. 'kCassandra'
            indicates Cassandra Protection Source environment. 'kMongoDB'
            indicates MongoDB Protection Source environment. 'kCouchbase'
            indicates Couchbase Protection Source environment. 'kHdfs'
            indicates Hdfs Protection Source environment. 'kHive' indicates
            Hive Protection Source environment. 'kHBase' indicates HBase
            Protection Source environment. 'kUDA' indicates Universal Data
            Adapter Protection Source environment. 'kO365Teams' indicates the
            Office365 Teams Protection Source environment. 'kO365Group'
            indicates the Office365 Groups Protection Source environment.
            'kO365Exchange' indicates the Office365 Mailbox Protection Source
            environment. 'kO365OneDrive' indicates the Office365 OneDrive
            Protection Source environment. 'kO365Sharepoint' indicates the
            Office365 SharePoint Protection Source environment.
            'kO365PublicFolders' indicates the Office365 PublicFolders
            Protection Source environment.
        job_id (long|int): Protection Job Id.  Specifies id of the Protection
            Job that backed up the objects to be restored.
        job_run_id (long|int): Specifies the id of the Job Run that captured
            the snapshot.
        job_uid (UniversalId): Specifies the universal id of the Protection Job
            that backed up the objects to recover or clone or the objects that
            contain the files or folders to recover.
        point_in_time_usecs (long|int): Specifies the timestamp (in
            microseconds. from epoch) for recovering to a point-in-time in the
            past.
        protection_source_id (long|int): Specifies the id of the leaf object to
            recover, clone or recover files/folders from.
        source_name (string): Specifies the name of the Protection Source.
        started_time_usecs (long|int): Specifies the time when the Job Run
            starts capturing a snapshot. Specified as a Unix epoch Timestamp
            (in microseconds).
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "archival_target":'archivalTarget',
        "cloud_deploy_target":'cloudDeployTarget',
        "environment":'environment',
        "job_id":'jobId',
        "job_run_id":'jobRunId',
        "job_uid":'jobUid',
        "point_in_time_usecs":'pointInTimeUsecs',
        "protection_source_id":'protectionSourceId',
        "source_name":'sourceName',
        "started_time_usecs":'startedTimeUsecs',
    }
    def __init__(self,
                 archival_target=None,
                 cloud_deploy_target=None,
                 environment=None,
                 job_id=None,
                 job_run_id=None,
                 job_uid=None,
                 point_in_time_usecs=None,
                 protection_source_id=None,
                 source_name=None,
                 started_time_usecs=None,
            ):

        """Constructor for the RestoreObjectDetails class"""

        # Initialize members of the class
        self.archival_target = archival_target
        self.cloud_deploy_target = cloud_deploy_target
        self.environment = environment
        self.job_id = job_id
        self.job_run_id = job_run_id
        self.job_uid = job_uid
        self.point_in_time_usecs = point_in_time_usecs
        self.protection_source_id = protection_source_id
        self.source_name = source_name
        self.started_time_usecs = started_time_usecs

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
        archival_target = cohesity_management_sdk.models.archival_external_target.ArchivalExternalTarget.from_dictionary(dictionary.get('archivalTarget')) if dictionary.get('archivalTarget') else None
        cloud_deploy_target = cohesity_management_sdk.models.cloud_deploy_target_details.CloudDeployTargetDetails.from_dictionary(dictionary.get('cloudDeployTarget')) if dictionary.get('cloudDeployTarget') else None
        environment = dictionary.get('environment')
        job_id = dictionary.get('jobId')
        job_run_id = dictionary.get('jobRunId')
        job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        point_in_time_usecs = dictionary.get('pointInTimeUsecs')
        protection_source_id = dictionary.get('protectionSourceId')
        source_name = dictionary.get('sourceName')
        started_time_usecs = dictionary.get('startedTimeUsecs')

        # Return an object of this model
        return cls(
            archival_target,
            cloud_deploy_target,
            environment,
            job_id,
            job_run_id,
            job_uid,
            point_in_time_usecs,
            protection_source_id,
            source_name,
            started_time_usecs
)