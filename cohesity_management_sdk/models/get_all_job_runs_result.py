# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class GetAllJobRunsResult(object):

    """Implementation of the 'GetAllJobRunsResult' model.

    Specifies the common result structure of the response of all runs info (
    protection, replication, archival etc.).


    Attributes:

        end_time_msecs (long|int): Specifies the end time of the run.
        env_type (EnvTypeEnum): Specifies the environment type of the job.
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
        job_id (string): Specifies the job id.
        job_name (string): Specifies the job name.
        job_run_id (string): Specifies the job run id.
        job_type (string): Specifies the job type, protection, replication,
            archival, apollo, indexing etc.
        start_time_msecs (long|int): Specifies the start time of the run.
        view_box_id (long|int): Specifies the view box id.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "end_time_msecs":'endTimeMsecs',
        "env_type":'envType',
        "job_id":'jobId',
        "job_name":'jobName',
        "job_run_id":'jobRunId',
        "job_type":'jobType',
        "start_time_msecs":'startTimeMsecs',
        "view_box_id":'viewBoxId',
    }
    def __init__(self,
                 end_time_msecs=None,
                 env_type=None,
                 job_id=None,
                 job_name=None,
                 job_run_id=None,
                 job_type=None,
                 start_time_msecs=None,
                 view_box_id=None,
            ):

        """Constructor for the GetAllJobRunsResult class"""

        # Initialize members of the class
        self.end_time_msecs = end_time_msecs
        self.env_type = env_type
        self.job_id = job_id
        self.job_name = job_name
        self.job_run_id = job_run_id
        self.job_type = job_type
        self.start_time_msecs = start_time_msecs
        self.view_box_id = view_box_id

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
        end_time_msecs = dictionary.get('endTimeMsecs')
        env_type = dictionary.get('envType')
        job_id = dictionary.get('jobId')
        job_name = dictionary.get('jobName')
        job_run_id = dictionary.get('jobRunId')
        job_type = dictionary.get('jobType')
        start_time_msecs = dictionary.get('startTimeMsecs')
        view_box_id = dictionary.get('viewBoxId')

        # Return an object of this model
        return cls(
            end_time_msecs,
            env_type,
            job_id,
            job_name,
            job_run_id,
            job_type,
            start_time_msecs,
            view_box_id
)