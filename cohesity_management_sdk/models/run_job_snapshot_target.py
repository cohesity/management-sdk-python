# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.archival_external_target
import cohesity_management_sdk.models.replication_target_settings

class RunJobSnapshotTarget(object):

    """Implementation of the 'RunJobSnapshotTarget' model.

    Specifies settings for a Copy Task when a Protection is run. It
    gives the target location for the Snapshot and its retention.

    Attributes:
        archival_target (ArchivalExternalTarget): Specifies settings about the
            Archival External Target (such as Tape or AWS).
        days_to_keep (long|int): Specifies the number of days to retain copied
            Snapshots on the target.
        hold_for_legal_purpose (bool): Specifies optionally whether to retain
            the snapshot for legal purpose. If set to true, the run cannot be
            deleted until the retention period. Note that using this option
            may cause the Cluster to run out of space. If set to false
            explicitly, the hold is removed, and the run will expire as
            specified in the policy of the Protection Job. If this field is
            not specified, there is no change to the hold of the run. This
            field can be set only by a User having Data Security Role.
        replication_target (ReplicationTargetSettings): Specifies settings
            about the Remote Cohesity Cluster where Snapshots are copied to.
        mtype (TypeRunJobSnapshotTargetEnum): Specifies the type of a Snapshot
            target such as 'kLocal', 'kRemote' or 'kArchival'. 'kLocal' means
            the Snapshot is stored on a local Cohesity Cluster. 'kRemote'
            means the Snapshot is stored on a Remote Cohesity Cluster. (It was
            copied to the Remote Cohesity Cluster using replication.)
            'kArchival' means the Snapshot is stored on a Archival External
            Target (such as Tape or AWS). 'kCloudDeploy' means the Snapshot is
            stored on a Cloud platform.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archival_target":'archivalTarget',
        "days_to_keep":'daysToKeep',
        "hold_for_legal_purpose":'holdForLegalPurpose',
        "replication_target":'replicationTarget',
        "mtype":'type'
    }

    def __init__(self,
                 archival_target=None,
                 days_to_keep=None,
                 hold_for_legal_purpose=None,
                 replication_target=None,
                 mtype=None):
        """Constructor for the RunJobSnapshotTarget class"""

        # Initialize members of the class
        self.archival_target = archival_target
        self.days_to_keep = days_to_keep
        self.hold_for_legal_purpose = hold_for_legal_purpose
        self.replication_target = replication_target
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
        archival_target = cohesity_management_sdk.models.archival_external_target.ArchivalExternalTarget.from_dictionary(dictionary.get('archivalTarget')) if dictionary.get('archivalTarget') else None
        days_to_keep = dictionary.get('daysToKeep')
        hold_for_legal_purpose = dictionary.get('holdForLegalPurpose')
        replication_target = cohesity_management_sdk.models.replication_target_settings.ReplicationTargetSettings.from_dictionary(dictionary.get('replicationTarget')) if dictionary.get('replicationTarget') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(archival_target,
                   days_to_keep,
                   hold_for_legal_purpose,
                   replication_target,
                   mtype)


