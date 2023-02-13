# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FileExtensionFilter(object):

    """Implementation of the 'FileExtensionFilter' model.

    TODO: type model description here.

    Attributes:
        file_extensions_list (list of string): The list of file extensions to
            apply
        is_enabled (bool): If set, it enables the file extension filter
        mode (ModeFileExtensionFilterEnum): The mode applied to the list of
            file extensions 'kWhitelist' indicates a whitelist extension
            filter. 'kBlacklist' indicates a blacklist extension filter.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_extensions_list":'fileExtensionsList',
        "is_enabled":'isEnabled',
        "mode":'mode'
    }

    def __init__(self,
                 file_extensions_list=None,
                 is_enabled=None,
                 mode=None):
        """Constructor for the FileExtensionFilter class"""

        # Initialize members of the class
        self.file_extensions_list = file_extensions_list
        self.is_enabled = is_enabled
        self.mode = mode


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
        file_extensions_list = dictionary.get('fileExtensionsList')
        is_enabled = dictionary.get('isEnabled')
        mode = dictionary.get('mode')

        # Return an object of this model
        return cls(file_extensions_list,
                   is_enabled,
                   mode)


