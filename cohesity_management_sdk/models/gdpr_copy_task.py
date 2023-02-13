# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GdprCopyTask(object):

    """Implementation of the 'GdprCopyTask' model.

    CopyTask defines the copy tasks of a job.

    Attributes:
        job_id (long|int): Specifies the job with which this copy task is tied
            to. Note: this is only used for internal aggregation.
        cloud_target_type (string): Specifies the cloud deploy target type.
            For example 'kAzure','kAWS', 'kGCP'
        expiry_time_usecs (long|int): Specifies the expiry of the copy task.
        target_id (long|int): Specifies the id for the target.
        target_name (string): Specifies the target of the replication or
            archival tasks.
        total_snapshots (long|int): Specifies the total number of snapshots.
        mtype (string): Specifies details about the Copy Run of a Job Run. A
            Copy task copies snapshots resulted from a backup run to an
            external target which could be 'kLocal', 'kArchival', or
            'kRemote'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "job_id":'JobId',
        "cloud_target_type":'cloudTargetType',
        "expiry_time_usecs":'expiryTimeUsecs',
        "target_id":'targetId',
        "target_name":'targetName',
        "total_snapshots":'totalSnapshots',
        "mtype":'type'
    }

    def __init__(self,
                 job_id=None,
                 cloud_target_type=None,
                 expiry_time_usecs=None,
                 target_id=None,
                 target_name=None,
                 total_snapshots=None,
                 mtype=None):
        """Constructor for the GdprCopyTask class"""

        # Initialize members of the class
        self.job_id = job_id
        self.cloud_target_type = cloud_target_type
        self.expiry_time_usecs = expiry_time_usecs
        self.target_id = target_id
        self.target_name = target_name
        self.total_snapshots = total_snapshots
        self.mtype = mtype


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
        job_id = dictionary.get('JobId')
        cloud_target_type = dictionary.get('cloudTargetType')
        expiry_time_usecs = dictionary.get('expiryTimeUsecs')
        target_id = dictionary.get('targetId')
        target_name = dictionary.get('targetName')
        total_snapshots = dictionary.get('totalSnapshots')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(job_id,
                   cloud_target_type,
                   expiry_time_usecs,
                   target_id,
                   target_name,
                   total_snapshots,
                   mtype)


