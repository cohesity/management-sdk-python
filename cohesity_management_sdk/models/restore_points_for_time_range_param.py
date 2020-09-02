# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.universal_id

class RestorePointsForTimeRangeParam(object):

    """Implementation of the 'RestorePointsForTimeRangeParam' model.

    Specifies the request parameters to restore points for time range API.

    Attributes:
        end_time_usecs (long|int): Specifies the end time specified as a Unix
            epoch Timestamp (in microseconds).
        environment (EnvironmentRestorePointsForTimeRangeParamEnum): Specifies
            the protection source environment type. Supported environment
            types such as 'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer'
            refers to Cohesity's Remote Adapter. 'kVMware' indicates the
            VMware Protection Source environment. 'kHyperV' indicates the
            HyperV Protection Source environment. 'kSQL' indicates the SQL
            Protection Source environment. 'kView' indicates the View
            Protection Source environment. 'kPuppeteer' indicates the
            Cohesity's Remote Adapter. 'kPhysical' indicates the physical
            Protection Source environment. 'kPure' indicates the Pure Storage
            Protection Source environment. 'Nimble' indicates the Nimble
            Storage Protection Source environment. 'kAzure' indicates the
            Microsoft's Azure Protection Source environment. 'kNetapp'
            indicates the Netapp Protection Source environment. 'kAgent'
            indicates the Agent Protection Source environment. 'kGenericNas'
            indicates the Generic Network Attached Storage Protection Source
            environment. 'kAcropolis' indicates the Acropolis Protection
            Source environment. 'kPhsicalFiles' indicates the Physical Files
            Protection Source environment. 'kIsilon' indicates the Dell EMC's
            Isilon Protection Source environment. 'kGPFS' indicates IBM's GPFS
            Protection Source environment. 'kKVM' indicates the KVM Protection
            Source environment. 'kAWS' indicates the AWS Protection Source
            environment. 'kExchange' indicates the Exchange Protection Source
            environment. 'kHyperVVSS' indicates the HyperV VSS Protection
            Source environment. 'kOracle' indicates the Oracle Protection
            Source environment. 'kGCP' indicates the Google Cloud Platform
            Protection Source environment. 'kFlashBlade' indicates the Flash
            Blade Protection Source environment. 'kAWSNative' indicates the
            AWS Native Protection Source environment.  'kO365' indicates the
            Office 365 Protection Source environment. 'kO365Outlook' indicates
            Office 365 outlook Protection Source environment. 'kHyperFlex'
            indicates the Hyper Flex Protection Source environment.
            'kGCPNative' indicates the GCP Native Protection Source
            environment. 'kAzureNative' indicates the Azure Native Protection
            Source environment. 'kKubernetes' indicates a Kubernetes
            Protection Source environment. 'kElastifile' indicates Elastifile
            Protection Source environment. 'kAD' indicates Active Directory
            Protection Source environment. 'kRDSSnapshotManager' indicates AWS
            RDS Protection Source environment.
        job_uids (list of UniversalId): Specifies the jobs for which to get
            the full snapshot information.
        protection_source_id (long|int): Specifies the id of the Protection
            Source which is to be restored.
        start_time_usecs (long|int): Specifies the start time specified as a
            Unix epoch Timestamp (in microseconds).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "job_uids":'jobUids',
        "end_time_usecs":'endTimeUsecs',
        "environment":'environment',
        "protection_source_id":'protectionSourceId',
        "start_time_usecs":'startTimeUsecs'
    }

    def __init__(self,
                 job_uids=None,
                 end_time_usecs=None,
                 environment=None,
                 protection_source_id=None,
                 start_time_usecs=None):
        """Constructor for the RestorePointsForTimeRangeParam class"""

        # Initialize members of the class
        self.end_time_usecs = end_time_usecs
        self.environment = environment
        self.job_uids = job_uids
        self.protection_source_id = protection_source_id
        self.start_time_usecs = start_time_usecs


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
        job_uids = None
        if dictionary.get('jobUids') != None:
            job_uids = list()
            for structure in dictionary.get('jobUids'):
                job_uids.append(cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(structure))
        end_time_usecs = dictionary.get('endTimeUsecs')
        environment = dictionary.get('environment')
        protection_source_id = dictionary.get('protectionSourceId')
        start_time_usecs = dictionary.get('startTimeUsecs')

        # Return an object of this model
        return cls(job_uids,
                   end_time_usecs,
                   environment,
                   protection_source_id,
                   start_time_usecs)


