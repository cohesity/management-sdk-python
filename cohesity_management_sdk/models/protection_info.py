# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ProtectionInfo(object):

    """Implementation of the 'ProtectionInfo' model.

    dataLocation defines data location related information.

    Attributes:
        end_time_usecs (long|int): Specifies the end time for object
            retention.
        location (string): Specifies the location of the object.
        policy_id (string): Specifies the id of the policy.
        protection_job_id (long|int): Specifies the id of the protection job.
        protection_job_name (string): Specifies the protection job name which
            protects this object.
        retention_period (long|int): Specifies the retention period.
        start_time_usecs (long|int): Specifies the start time for object
            retention.
        storage_domain (string): Specifies the storage domain name.
        total_snapshots (long|int): Specifies the total number of snapshots.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_time_usecs":'endTimeUsecs',
        "location":'location',
        "policy_id":'policyId',
        "protection_job_id":'protectionJobId',
        "protection_job_name":'protectionJobName',
        "retention_period":'retentionPeriod',
        "start_time_usecs":'startTimeUsecs',
        "storage_domain":'storageDomain',
        "total_snapshots":'totalSnapshots'
    }

    def __init__(self,
                 end_time_usecs=None,
                 location=None,
                 policy_id=None,
                 protection_job_id=None,
                 protection_job_name=None,
                 retention_period=None,
                 start_time_usecs=None,
                 storage_domain=None,
                 total_snapshots=None):
        """Constructor for the ProtectionInfo class"""

        # Initialize members of the class
        self.end_time_usecs = end_time_usecs
        self.location = location
        self.policy_id = policy_id
        self.protection_job_id = protection_job_id
        self.protection_job_name = protection_job_name
        self.retention_period = retention_period
        self.start_time_usecs = start_time_usecs
        self.storage_domain = storage_domain
        self.total_snapshots = total_snapshots


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
        end_time_usecs = dictionary.get('endTimeUsecs')
        location = dictionary.get('location')
        policy_id = dictionary.get('policyId')
        protection_job_id = dictionary.get('protectionJobId')
        protection_job_name = dictionary.get('protectionJobName')
        retention_period = dictionary.get('retentionPeriod')
        start_time_usecs = dictionary.get('startTimeUsecs')
        storage_domain = dictionary.get('storageDomain')
        total_snapshots = dictionary.get('totalSnapshots')

        # Return an object of this model
        return cls(end_time_usecs,
                   location,
                   policy_id,
                   protection_job_id,
                   protection_job_name,
                   retention_period,
                   start_time_usecs,
                   storage_domain,
                   total_snapshots)


