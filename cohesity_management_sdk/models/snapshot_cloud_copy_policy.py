# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cloud_deploy_target_details
import cohesity_management_sdk.models.data_lock_config


class SnapshotCloudCopyPolicy(object):

    """Implementation of the 'SnapshotCloudCopyPolicy' model.

    Specifies settings for copying Snapshots to Cloud. This also specifies the
    retention policy that should be applied to Snapshots after they have been
    copied to Cloud.


    Attributes:

        id (string): Specified the Id for a snapshot copy policy. This is
            generated when the policy is created.
        copy_partial (bool): Specifies if Snapshots are copied from the first
            completely successful Job Run or the first partially successful Job
            Run occurring at the start of the replication schedule. If true,
            Snapshots are copied from the first Job Run occurring at the start
            of the replication schedule, even if first Job Run was not
            completely successful i.e. Snapshots were not captured for all
            Objects in the Job. If false, Snapshots are copied from the first
            Job Run occurring at the start of the replication schedule that was
            completely successful i.e. Snapshots for all the Objects in the Job
            were successfully captured.
        datalock_config (DataLockConfig): Specifies WORM retention type for the
            copy target snapshots. When a WORM retention type is specified, the
            snapshots of the Protection Groups using this policy will be kept
            for the last N days as specified in the duration of the datalock.
            During that time, the snapshots cannot be deleted.
        days_to_keep (long|int): Specifies the number of days to retain copied
            Snapshots on the target.
        multiplier (int): Specifies a factor to multiply the periodicity by, to
            determine the copy schedule. For example if set to 2 and the
            periodicity is hourly, then Snapshots from the first eligible Job
            Run for every 2 hour period is copied.
        periodicity (PeriodicityEnum): Specifies the frequency that Snapshots
            should be copied to the specified target. Used in combination with
            multiplier. 'kEvery' means that the Snapshot copy occurs after the
            number of Job Runs equals the number specified in the multiplier.
            'kHour' means that the Snapshot copy occurs hourly at the frequency
            set in the multiplier, for example if multiplier is 2, the copy
            occurs every 2 hours. 'kDay' means that the Snapshot copy occurs
            daily at the frequency set in the multiplier. 'kWeek' means that
            the Snapshot copy occurs weekly at the frequency set in the
            multiplier. 'kMonth' means that the Snapshot copy occurs monthly at
            the frequency set in the multiplier. 'kYear' means that the
            Snapshot copy occurs yearly at the frequency set in the multiplier.
        target (CloudDeployTargetDetails): Specifies the details about
            CloudDeploy target where backup snapshots may be converted and
            stored.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "id":'Id',
        "copy_partial":'copyPartial',
        "datalock_config":'datalockConfig',
        "days_to_keep":'daysToKeep',
        "multiplier":'multiplier',
        "periodicity":'periodicity',
        "target":'target',
    }
    def __init__(self,
                 id=None,
                 copy_partial=None,
                 datalock_config=None,
                 days_to_keep=None,
                 multiplier=None,
                 periodicity=None,
                 target=None,
            ):

        """Constructor for the SnapshotCloudCopyPolicy class"""

        # Initialize members of the class
        self.id = id
        self.copy_partial = copy_partial
        self.datalock_config = datalock_config
        self.days_to_keep = days_to_keep
        self.multiplier = multiplier
        self.periodicity = periodicity
        self.target = target

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
        id = dictionary.get('Id')
        copy_partial = dictionary.get('copyPartial')
        datalock_config = cohesity_management_sdk.models.data_lock_config.DataLockConfig.from_dictionary(dictionary.get('datalockConfig')) if dictionary.get('datalockConfig') else None
        days_to_keep = dictionary.get('daysToKeep')
        multiplier = dictionary.get('multiplier')
        periodicity = dictionary.get('periodicity')
        target = cohesity_management_sdk.models.cloud_deploy_target_details.CloudDeployTargetDetails.from_dictionary(dictionary.get('target')) if dictionary.get('target') else None

        # Return an object of this model
        return cls(
            id,
            copy_partial,
            datalock_config,
            days_to_keep,
            multiplier,
            periodicity,
            target
)