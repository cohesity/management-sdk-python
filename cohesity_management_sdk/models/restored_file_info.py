# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RestoredFileInfo(object):

    """Implementation of the 'RestoredFileInfo' model.

    TODO: type model description here.

    Attributes:
        absolute_path (string): Full path of the file being restored: the
            actual file path without the disk. E.g.: \Program
            Files\App\file.txt
        attached_disk_id (int): Disk information of where the source file is
            currently located.
        disk_partition_id (int): Disk partition to which the file belongs to.
        fs_uuid (string): File system UUID on which file resides.
        inode_number (long|int): Inode number of the file.
            This is needed for snapmirror restore workflow.
        is_directory (bool): Whether the path points to a directory.
        is_non_simple_ldm_vol (bool): This will be set to true for recovery
            workflows for non-simple volumes on Windows Dynamic Disks. In that
            case, we will use VolumeInfo instead of some of the details
            captured here (e.g. virtual_disk_file) for determining disk and
            volume related details.
        restore_base_directory (string): This must be set to a directory path
            if restore_to_original_paths is false and restore task has
            multiple files which are not desired to be restore to one common
            location. If this filed is populated, 'absolute_path' will be
            restored under this location. If this field is not populated all
            files in restore task will be restored to location specified in
            RestoreFilesPreferences.
        restore_mount_point (string): Mount point of the volume on which the
            file to be restored is located. E.g.: c:\temp\vhd_mount_1234
        size_bytes (long|int): Size of the file in bytes. Required in FLR in
            GCP using Cloud Functions.
        virtual_disk_file (string): Virtual disk file to which this file
            belongs to.
        volume_id (string): Id of the volume.
        volume_path (string): Original volume name (or drive letter). This is
            used while performing the copy to the original paths. E.g.: c:

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "absolute_path":'absolutePath',
        "attached_disk_id":'attachedDiskId',
        "disk_partition_id":'diskPartitionId',
        "fs_uuid":'fsUuid',
        "inode_number":'inodeNumber',
        "is_directory":'isDirectory',
        "is_non_simple_ldm_vol":'isNonSimpleLdmVol',
        "restore_base_directory":'restoreBaseDirectory',
        "restore_mount_point":'restoreMountPoint',
        "size_bytes":'sizeBytes',
        "virtual_disk_file":'virtualDiskFile',
        "volume_id":'volumeId',
        "volume_path":'volumePath'
    }

    def __init__(self,
                 absolute_path=None,
                 attached_disk_id=None,
                 disk_partition_id=None,
                 fs_uuid=None,
                 inode_number=None,
                 is_directory=None,
                 is_non_simple_ldm_vol=None,
                 restore_base_directory=None,
                 restore_mount_point=None,
                 size_bytes=None,
                 virtual_disk_file=None,
                 volume_id=None,
                 volume_path=None):
        """Constructor for the RestoredFileInfo class"""

        # Initialize members of the class
        self.absolute_path = absolute_path
        self.attached_disk_id = attached_disk_id
        self.disk_partition_id = disk_partition_id
        self.fs_uuid = fs_uuid
        self.inode_number = inode_number
        self.is_directory = is_directory
        self.is_non_simple_ldm_vol = is_non_simple_ldm_vol
        self.restore_base_directory = restore_base_directory
        self.restore_mount_point = restore_mount_point
        self.size_bytes = size_bytes
        self.virtual_disk_file = virtual_disk_file
        self.volume_id = volume_id
        self.volume_path = volume_path


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
        absolute_path = dictionary.get('absolutePath')
        attached_disk_id = dictionary.get('attachedDiskId')
        disk_partition_id = dictionary.get('diskPartitionId')
        fs_uuid = dictionary.get('fsUuid')
        inode_number = dictionary.get('inodeNumber')
        is_directory = dictionary.get('isDirectory')
        is_non_simple_ldm_vol = dictionary.get('isNonSimpleLdmVol')
        restore_base_directory = dictionary.get('restoreBaseDirectory')
        restore_mount_point = dictionary.get('restoreMountPoint')
        size_bytes = dictionary.get('sizeBytes')
        virtual_disk_file = dictionary.get('virtualDiskFile')
        volume_id = dictionary.get('volumeId')
        volume_path = dictionary.get('volumePath')

        # Return an object of this model
        return cls(absolute_path,
                   attached_disk_id,
                   disk_partition_id,
                   fs_uuid,
                   inode_number,
                   is_directory,
                   is_non_simple_ldm_vol,
                   restore_base_directory,
                   restore_mount_point,
                   size_bytes,
                   virtual_disk_file,
                   volume_id,
                   volume_path)


