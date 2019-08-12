# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.magneto_instance_id
import cohesity_management_sdk.models.magneto_object_id

class RetrieveArchiveTaskStateProtoDownloadFilesInfo(object):

    """Implementation of the 'RetrieveArchiveTaskStateProto_DownloadFilesInfo' model.

    Information required for Icebox when downloading files from an archived
    entity. This proto is specifically just for the current temporary
    solution
    for downloading a single from an archive, where we let icebox download
    the
    file for us. In the future once the new Yoda APIs for downloading files
    from archive stub views are ready, we will just discard this proto and
    make field 20 reserved.

    Attributes:
        file_path (string): The file to download from the archive.
            TODO(zheng): Right now we only support single file download.
            Adjust accordingly once we support downloading multiple
            files/directories.
        magneto_instance_id (MagnetoInstanceId): TODO: type description here.
        object_id (MagnetoObjectId): TODO(apurv): This message type should be
            moved to the Yoda namespace.
        skip_restore_in_stub_view (bool): Ask Icebox to only create the stub
            view and skip restoring files in the stub view.
        target_dir_path (string): Path to the directory under which the
            downloaded files will be placed.
        target_view_name (string): Target view name where the downloaded files
            will be placed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_path":'filePath',
        "magneto_instance_id":'magnetoInstanceId',
        "object_id":'objectId',
        "skip_restore_in_stub_view":'skipRestoreInStubView',
        "target_dir_path":'targetDirPath',
        "target_view_name":'targetViewName'
    }

    def __init__(self,
                 file_path=None,
                 magneto_instance_id=None,
                 object_id=None,
                 skip_restore_in_stub_view=None,
                 target_dir_path=None,
                 target_view_name=None):
        """Constructor for the RetrieveArchiveTaskStateProtoDownloadFilesInfo class"""

        # Initialize members of the class
        self.file_path = file_path
        self.magneto_instance_id = magneto_instance_id
        self.object_id = object_id
        self.skip_restore_in_stub_view = skip_restore_in_stub_view
        self.target_dir_path = target_dir_path
        self.target_view_name = target_view_name


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
        file_path = dictionary.get('filePath')
        magneto_instance_id = cohesity_management_sdk.models.magneto_instance_id.MagnetoInstanceId.from_dictionary(dictionary.get('magnetoInstanceId')) if dictionary.get('magnetoInstanceId') else None
        object_id = cohesity_management_sdk.models.magneto_object_id.MagnetoObjectId.from_dictionary(dictionary.get('objectId')) if dictionary.get('objectId') else None
        skip_restore_in_stub_view = dictionary.get('skipRestoreInStubView')
        target_dir_path = dictionary.get('targetDirPath')
        target_view_name = dictionary.get('targetViewName')

        # Return an object of this model
        return cls(file_path,
                   magneto_instance_id,
                   object_id,
                   skip_restore_in_stub_view,
                   target_dir_path,
                   target_view_name)


