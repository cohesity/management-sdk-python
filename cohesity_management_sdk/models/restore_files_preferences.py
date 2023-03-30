# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RestoreFilesPreferences(object):

    """Implementation of the 'RestoreFilesPreferences' model.

    This message captures preferences from the user while restoring the files
    on the target.


    Attributes:

        alternate_restore_base_directory (string): This must be set to a
            directory path if restore_to_original_paths is false. All the files
            and directories restored will be restored under this location.
        continue_on_error (bool): Whether to continue with the copy in case of
            encountering an error.
        encryption_enabled (bool): Whether to enable encryption for NFS and SMB
            restores.
        generate_ssh_keys (bool): In case of GCP Linux restores, whether to
            generate ssh keys to connect to the customer's instance.
        override_originals (bool): This is relevant only if
            restore_to_original_paths is true. If this is true, then already
            existing files will be overridden, otherwise new files will be
            skipped.
        preserve_acls (bool): Whether to preserve the ACLs of the original
            file.
        preserve_attributes (bool): Whether to preserve the original
            attributes.
        preserve_timestamps (bool): Whether to preserve the original time
            stamps.
        restore_entities (int): Option to select whether to restore everything
            or ACLs only.
        restore_to_original_paths (bool): If this is true, then files will be
            restored to original paths.
        save_success_files (bool): Whether to save success files for FLR.
        skip_estimation (bool): Whether to skip the estimation step.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "alternate_restore_base_directory":'alternateRestoreBaseDirectory',
        "continue_on_error":'continueOnError',
        "encryption_enabled":'encryptionEnabled',
        "generate_ssh_keys":'generateSshKeys',
        "override_originals":'overrideOriginals',
        "preserve_acls":'preserveAcls',
        "preserve_attributes":'preserveAttributes',
        "preserve_timestamps":'preserveTimestamps',
        "restore_entities":'restoreEntities',
        "restore_to_original_paths":'restoreToOriginalPaths',
        "save_success_files":'saveSuccessFiles',
        "skip_estimation":'skipEstimation',
    }
    def __init__(self,
                 alternate_restore_base_directory=None,
                 continue_on_error=None,
                 encryption_enabled=None,
                 generate_ssh_keys=None,
                 override_originals=None,
                 preserve_acls=None,
                 preserve_attributes=None,
                 preserve_timestamps=None,
                 restore_entities=None,
                 restore_to_original_paths=None,
                 save_success_files=None,
                 skip_estimation=None,
            ):

        """Constructor for the RestoreFilesPreferences class"""

        # Initialize members of the class
        self.alternate_restore_base_directory = alternate_restore_base_directory
        self.continue_on_error = continue_on_error
        self.encryption_enabled = encryption_enabled
        self.generate_ssh_keys = generate_ssh_keys
        self.override_originals = override_originals
        self.preserve_acls = preserve_acls
        self.preserve_attributes = preserve_attributes
        self.preserve_timestamps = preserve_timestamps
        self.restore_entities = restore_entities
        self.restore_to_original_paths = restore_to_original_paths
        self.save_success_files = save_success_files
        self.skip_estimation = skip_estimation

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
        alternate_restore_base_directory = dictionary.get('alternateRestoreBaseDirectory')
        continue_on_error = dictionary.get('continueOnError')
        encryption_enabled = dictionary.get('encryptionEnabled')
        generate_ssh_keys = dictionary.get('generateSshKeys')
        override_originals = dictionary.get('overrideOriginals')
        preserve_acls = dictionary.get('preserveAcls')
        preserve_attributes = dictionary.get('preserveAttributes')
        preserve_timestamps = dictionary.get('preserveTimestamps')
        restore_entities = dictionary.get('restoreEntities')
        restore_to_original_paths = dictionary.get('restoreToOriginalPaths')
        save_success_files = dictionary.get('saveSuccessFiles')
        skip_estimation = dictionary.get('skipEstimation')

        # Return an object of this model
        return cls(
            alternate_restore_base_directory,
            continue_on_error,
            encryption_enabled,
            generate_ssh_keys,
            override_originals,
            preserve_acls,
            preserve_attributes,
            preserve_timestamps,
            restore_entities,
            restore_to_original_paths,
            save_success_files,
            skip_estimation
)