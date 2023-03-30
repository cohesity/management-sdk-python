# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cloud_archive_run


class CloudArchiveSummary(object):

    """Implementation of the 'CloudArchiveSummary' model.

    Specifies statistics about the transfer of data from this Cohesity Cluster
    to a Vault.


    Attributes:

        job_id (long|int): Specifies the id of the job.
        job_name (string): Specifies the name of the Protection Job.
        job_type (JobTypeEnum): Specifies the type of the Protection Job.
            Supported environment types such as 'kView', 'kSQL', 'kVMware',
            etc. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.
            'kVMware' indicates the VMware Protection Source environment.
            'kHyperV' indicates the HyperV Protection Source environment.
            'kSQL' indicates the SQL Protection Source environment. 'kView'
            indicates the View Protection Source environment. 'kPuppeteer'
            indicates the Cohesity's Remote Adapter. 'kPhysical' indicates the
            physical Protection Source environment. 'kPure' indicates the Pure
            Storage Protection Source environment. 'kNimble' indicates the
            Nimble Storage Protection Source environment. 'kAzure' indicates
            the Microsoft's Azure Protection Source environment. 'kNetapp'
            indicates the Netapp Protection Source environment. 'kAgent'
            indicates the Agent Protection Source environment. 'kGenericNas'
            indicates the Generic Network Attached Storage Protection Source
            environment. 'kAcropolis' indicates the Acropolis Protection Source
            environment. 'kPhysicalFiles' indicates the Physical Files
            Protection Source environment. 'kIsilon' indicates the Dell EMC's
            Isilon Protection Source environment. 'kGPFS' indicates IBM's GPFS
            Protection Source environment. 'kKVM' indicates the KVM Protection
            Source environment. 'kAWS' indicates the AWS Protection Source
            environment. 'kExchange' indicates the Exchange Protection Source
            environment. 'kHyperVVSS' indicates the HyperV VSS Protection
            Source environment. 'kOracle' indicates the Oracle Protection
            Source environment. 'kGCP' indicates the Google Cloud Platform
            Protection Source environment. 'kFlashBlade' indicates the Flash
            Blade Protection Source environment. 'kAWSNative' indicates the AWS
            Native Protection Source environment. 'kO365' indicates the Office
            365 Protection Source environment. 'kO365Outlook' indicates Office
            365 outlook Protection Source environment. 'kHyperFlex' indicates
            the Hyper Flex Protection Source environment. 'kGCPNative'
            indicates the GCP Native Protection Source environment.
            'kAzureNative' indicates the Azure Native Protection Source
            environment. 'kKubernetes' indicates a Kubernetes Protection Source
            environment. 'kElastifile' indicates Elastifile Protection Source
            environment. 'kAD' indicates Active Directory Protection Source
            environment. 'kRDSSnapshotManager' indicates AWS RDS Protection
            Source environment. 'kCassandra' indicates Cassandra Protection
            Source environment. 'kMongoDB' indicates MongoDB Protection Source
            environment. 'kCouchbase' indicates Couchbase Protection Source
            environment. 'kHdfs' indicates Hdfs Protection Source environment.
            'kHive' indicates Hive Protection Source environment. 'kHBase'
            indicates HBase Protection Source environment. 'kUDA' indicates
            Universal Data Adapter Protection Source environment. 'kO365Teams'
            indicates the Office365 Teams Protection Source environment.
            'kO365Group' indicates the Office365 Groups Protection Source
            environment. 'kO365Exchange' indicates the Office365 Mailbox
            Protection Source environment. 'kO365OneDrive' indicates the
            Office365 OneDrive Protection Source environment. 'kO365Sharepoint'
            indicates the Office365 SharePoint Protection Source environment.
            'kO365PublicFolders' indicates the Office365 PublicFolders
            Protection Source environment.
        number_of_failed_runs (int): Specifies the number of failed runs for a
            Protection Job.
        number_of_queued_runs (int): Specifies the number of queued runs for a
            Protection Job.
        number_of_successful_runs (int): Specifies the number of successful
            runs for a Protection Job.
        runs (list of CloudArchiveRun): Specifies the list of cloud archive
            runs.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "job_id":'jobId',
        "job_name":'jobName',
        "job_type":'jobType',
        "number_of_failed_runs":'numberOfFailedRuns',
        "number_of_queued_runs":'numberOfQueuedRuns',
        "number_of_successful_runs":'numberOfSuccessfulRuns',
        "runs":'runs',
    }
    def __init__(self,
                 job_id=None,
                 job_name=None,
                 job_type=None,
                 number_of_failed_runs=None,
                 number_of_queued_runs=None,
                 number_of_successful_runs=None,
                 runs=None,
            ):

        """Constructor for the CloudArchiveSummary class"""

        # Initialize members of the class
        self.job_id = job_id
        self.job_name = job_name
        self.job_type = job_type
        self.number_of_failed_runs = number_of_failed_runs
        self.number_of_queued_runs = number_of_queued_runs
        self.number_of_successful_runs = number_of_successful_runs
        self.runs = runs

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
        job_id = dictionary.get('jobId')
        job_name = dictionary.get('jobName')
        job_type = dictionary.get('jobType')
        number_of_failed_runs = dictionary.get('numberOfFailedRuns')
        number_of_queued_runs = dictionary.get('numberOfQueuedRuns')
        number_of_successful_runs = dictionary.get('numberOfSuccessfulRuns')
        runs = None
        if dictionary.get('runs') != None:
            runs = list()
            for structure in dictionary.get('runs'):
                runs.append(cohesity_management_sdk.models.cloud_archive_run.CloudArchiveRun.from_dictionary(structure))

        # Return an object of this model
        return cls(
            job_id,
            job_name,
            job_type,
            number_of_failed_runs,
            number_of_queued_runs,
            number_of_successful_runs,
            runs
)