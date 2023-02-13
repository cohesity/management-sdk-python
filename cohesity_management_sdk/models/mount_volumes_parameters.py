# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MountVolumesParameters(object):

    """Implementation of the 'MountVolumesParameters' model.

    Specifies the information required for mounting volumes.
    Only required for Restore Tasks of type 'kMountVolumes'.
    At a minimum, the targetSourceId must be specified for 'kMountVolumes'
    Restore Tasks. If only targetSourceId is specified, all disks are
    attached but may not be mounted.
    The mount target must be registered on the Cohesity Cluster.
    If the mount target is a VM, VMware Tools must be installed.
    If the mount target is a physical server, a Cohesity Agent must be
    be installed. See the Cohesity Dashboard help documentation for details.
    In the username and password fields, specify the credentials to
    access the mount target.

    Attributes:
        bring_disks_online (bool): Optional setting that determines if the
            volumes are brought online on the mount target after attaching the
            disks. This field is only set for VMs. The Cohesity Cluster always
            attempts to mount Physical servers. If true and the mount target
            is a VM, to mount the volumes VMware Tools must be installed on
            the guest operating system of the VM and login credentials to the
            mount target must be specified. NOTE: If automount is configured
            for a Windows system, the volumes may be automatically brought
            online.
        password (string): Specifies password of the username to access the
            target source.
        target_source_id (long|int): Specifies the target Protection Source id
            where the volumes will be mounted. NOTE: The source that was
            backed up and the mount target must be the same type, for example
            if the source is a VMware VM, then the mount target must also be a
            VMware VM. The mount target must be registered on the Cohesity
            Cluster.
        username (string): Specifies username to access the target source.
        volume_names (list of string): Array of Volume Names.  Optionally
            specify the names of volumes to mount. If none are specified, all
            volumes of the Server are mounted on the target. To get the names
            of the volumes, call the GET
            /public/restore/vms/volumesInformation operation.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bring_disks_online":'bringDisksOnline',
        "password":'password',
        "target_source_id":'targetSourceId',
        "username":'username',
        "volume_names":'volumeNames'
    }

    def __init__(self,
                 bring_disks_online=None,
                 password=None,
                 target_source_id=None,
                 username=None,
                 volume_names=None):
        """Constructor for the MountVolumesParameters class"""

        # Initialize members of the class
        self.bring_disks_online = bring_disks_online
        self.password = password
        self.target_source_id = target_source_id
        self.username = username
        self.volume_names = volume_names


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
        password = dictionary.get('password')
        target_source_id = dictionary.get('targetSourceId')
        username = dictionary.get('username')
        volume_names = dictionary.get('volumeNames')

        # Return an object of this model
        return cls(bring_disks_online,
                   password,
                   target_source_id,
                   username,
                   volume_names)


