# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class SpecifiesProtectionJobSummaryOfAnObject(object):

    """Implementation of the 'Specifies Protection Job summary of an object.' model.

    TODO: type model description here.

    Attributes:
        cluster_id (long|int): Specifies the id of the cluster on which object
            is protected.
        cluster_incarnation_id (long|int): Specifies the incarnation id of the
            cluster on which object is protected.
        job_id (long|int): Specifies the id of the Protection Job.
        job_name (string): Specifies the name of the Protection Job.
        last_protection_job_run_status (int): Specifies the last job run
            status.
        policy_id (string): Specifies the id of the policy that is used by a
            Protection Job. Format of policy id will be like following:
            clusterid:clusterincarnationid:policyid.
        policy_name (string): Specifies the name of the policy that is used by
            a Protection Job.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_id":'clusterId',
        "cluster_incarnation_id":'clusterIncarnationId',
        "job_id":'jobId',
        "job_name":'jobName',
        "last_protection_job_run_status":'lastProtectionJobRunStatus',
        "policy_id":'policyId',
        "policy_name":'policyName'
    }

    def __init__(self,
                 cluster_id=None,
                 cluster_incarnation_id=None,
                 job_id=None,
                 job_name=None,
                 last_protection_job_run_status=None,
                 policy_id=None,
                 policy_name=None):
        """Constructor for the SpecifiesProtectionJobSummaryOfAnObject class"""

        # Initialize members of the class
        self.cluster_id = cluster_id
        self.cluster_incarnation_id = cluster_incarnation_id
        self.job_id = job_id
        self.job_name = job_name
        self.last_protection_job_run_status = last_protection_job_run_status
        self.policy_id = policy_id
        self.policy_name = policy_name


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
        cluster_id = dictionary.get('clusterId')
        cluster_incarnation_id = dictionary.get('clusterIncarnationId')
        job_id = dictionary.get('jobId')
        job_name = dictionary.get('jobName')
        last_protection_job_run_status = dictionary.get('lastProtectionJobRunStatus')
        policy_id = dictionary.get('policyId')
        policy_name = dictionary.get('policyName')

        # Return an object of this model
        return cls(cluster_id,
                   cluster_incarnation_id,
                   job_id,
                   job_name,
                   last_protection_job_run_status,
                   policy_id,
                   policy_name)


