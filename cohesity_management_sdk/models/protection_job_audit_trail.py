# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_job

class ProtectionJobAuditTrail(object):

    """Implementation of the 'ProtectionJobAuditTrail' model.

    Specifies the fields for Protection job audit Response.

    Attributes:
        after (ProtectionJob): Provides details about a Protection Job.
        before (ProtectionJob): Provides details about a Protection Job.
        changes (list of ChangeEnum): Specifies the list of changed values in
            a Protection Job. kProtectionJobName implies that protection job
            has change in the name field kProtectionJobDescription implies
            that protection job has change in the description field.
            kProtectionJobSources implies that protection job has change in
            the source field. kProtectionJobSchedule implies that protection
            job has change in the schedule field. kProtectionJobFullSchedule
            implies that protection job has change in the full schedule field.
            kProtectionJobRetrySettings implies that protection job has change
            in the retry settings. kProtectionJobRetentionPolicy implies that
            protection job has change in the retention policy.
            kProtectionJobIndexingPolicy implies that protection job has
            change in the indexing policy. kProtectionJobAlertingPolicy
            implies that protection job has change in the alerting policy.
            kProtectionJobPriority implies that protection job has change in
            the alerting policy. kProtectionJobQuiesce implies that protection
            job has change in the Quiesce. kProtectionJobSla implies that
            protection job has change in the SLA settings.
            kProtectionJobPolicyId implies that protection job has change in
            the poilcy Id settings. kProtectionJobTimezone implies that
            protection job has change in the timezone settings.
            kProtectionJobFutureRunsPaused implies that protection job has
            change in the future run settings. kProtectionJobFutureRunsResumed
            implies that protection job has change in the future run resume
            settings. kSnapshotTargetPolicy implies that protection job has
            change in the snapshot target policy settings. kProtectionJobQOS
            implies that protection job has change in QOS settings.
            kProtectionJobInvalidField implies that the changed field is
            invalid.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "after":'after',
        "before":'before',
        "changes":'changes'
    }

    def __init__(self,
                 after=None,
                 before=None,
                 changes=None):
        """Constructor for the ProtectionJobAuditTrail class"""

        # Initialize members of the class
        self.after = after
        self.before = before
        self.changes = changes


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
        after = cohesity_management_sdk.models.protection_job.ProtectionJob.from_dictionary(dictionary.get('after')) if dictionary.get('after') else None
        before = cohesity_management_sdk.models.protection_job.ProtectionJob.from_dictionary(dictionary.get('before')) if dictionary.get('before') else None
        changes = dictionary.get('changes')

        # Return an object of this model
        return cls(after,
                   before,
                   changes)


