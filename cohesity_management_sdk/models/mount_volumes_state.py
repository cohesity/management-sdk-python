# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.mount_volume_result_details
import cohesity_management_sdk.models.request_error

class MountVolumesState(object):

    """Implementation of the 'MountVolumesState' model.

    Specifies the states of mounting all the volumes onto a mount target
    for a 'kRecoverVMs' Restore Task.

    Attributes:
        bring_disks_online (bool): Optional setting that determines if the
            volumes are brought online on the mount target after attaching the
            disks. This option is only significant for VMs.
        mount_volume_results (list of MountVolumeResultDetails): Array of
            Mount Volume Results.  Specifies the results of mounting each
            specified volume.
        other_error (RequestError): Specifies an error that did not occur
            during the mount operation.
        target_source_id (long|int): Specifies the target Protection Source Id
            where the volumes will be mounted. NOTE: The source that was
            backed up and the mount target must be the same type, for example
            if the source is a VMware VM, then the mount target must also be a
            VMware VM. The mount target must be registered on the Cohesity
            Cluster.
        username (string): Specifies the username to access the mount target.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bring_disks_online":'bringDisksOnline',
        "mount_volume_results":'mountVolumeResults',
        "other_error":'otherError',
        "target_source_id":'targetSourceId',
        "username":'username'
    }

    def __init__(self,
                 bring_disks_online=None,
                 mount_volume_results=None,
                 other_error=None,
                 target_source_id=None,
                 username=None):
        """Constructor for the MountVolumesState class"""

        # Initialize members of the class
        self.bring_disks_online = bring_disks_online
        self.mount_volume_results = mount_volume_results
        self.other_error = other_error
        self.target_source_id = target_source_id
        self.username = username


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
        bring_disks_online = dictionary.get('bringDisksOnline')
        mount_volume_results = None
        if dictionary.get('mountVolumeResults') != None:
            mount_volume_results = list()
            for structure in dictionary.get('mountVolumeResults'):
                mount_volume_results.append(cohesity_management_sdk.models.mount_volume_result_details.MountVolumeResultDetails.from_dictionary(structure))
        other_error = cohesity_management_sdk.models.request_error.RequestError.from_dictionary(dictionary.get('otherError')) if dictionary.get('otherError') else None
        target_source_id = dictionary.get('targetSourceId')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(bring_disks_online,
                   mount_volume_results,
                   other_error,
                   target_source_id,
                   username)


