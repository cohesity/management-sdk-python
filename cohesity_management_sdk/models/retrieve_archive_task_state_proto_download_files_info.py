# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

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
        file_path_vec (list of string): The file paths to be retrieved from
            the archive. For example, if the file paths are /foo/bar and
            /foo2/bar and target_dir_path is "downloaded_files". The retrieved
            files will have the full path structure maintained in
            target_dir_path such as downloaded_files/foo/bar and
            /downloaded_files/foo2/bar.
        magneto_instance_id (MagnetoInstanceId): Instance from which the
            requested files will be restored.
        object_id (MagnetoObjectId): Object from which the requested files
            will be restored.
        skip_restore_in_stub_view (bool): Ask Icebox to only create the stub
            view and skip restoring files in the stub view.
        target_dir_path (string): Path to the directory under which the
            downloaded files will be placed.
        target_view_name (string): Target view name where the downloaded files
            will be placed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_path_vec":'filePathVec',
        "magneto_instance_id":'magnetoInstanceId',
        "object_id":'objectId',
        "skip_restore_in_stub_view":'skipRestoreInStubView',
        "target_dir_path":'targetDirPath',
        "target_view_name":'targetViewName'
    }

    def __init__(self,
                 file_path_vec=None,
                 magneto_instance_id=None,
                 object_id=None,
                 skip_restore_in_stub_view=None,
                 target_dir_path=None,
                 target_view_name=None):
        """Constructor for the RetrieveArchiveTaskStateProtoDownloadFilesInfo class"""

        # Initialize members of the class
        self.file_path_vec = file_path_vec
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
        file_path_vec = dictionary.get('filePathVec')
        magneto_instance_id = cohesity_management_sdk.models.magneto_instance_id.MagnetoInstanceId.from_dictionary(dictionary.get('magnetoInstanceId')) if dictionary.get('magnetoInstanceId') else None
        object_id = cohesity_management_sdk.models.magneto_object_id.MagnetoObjectId.from_dictionary(dictionary.get('objectId')) if dictionary.get('objectId') else None
        skip_restore_in_stub_view = dictionary.get('skipRestoreInStubView')
        target_dir_path = dictionary.get('targetDirPath')
        target_view_name = dictionary.get('targetViewName')

        # Return an object of this model
        return cls(file_path_vec,
                   magneto_instance_id,
                   object_id,
                   skip_restore_in_stub_view,
                   target_dir_path,
                   target_view_name)


