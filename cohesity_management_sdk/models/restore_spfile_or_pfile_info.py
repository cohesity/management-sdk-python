# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RestoreSpfileOrPfileInfo(object):

    """Implementation of the 'RestoreSpfileOrPfileInfo' model.

    Proto to hold pfile/spfile restore related information


    Attributes:

        file_location (string): Location where spfile/pfile will be restored.
            If this is empty and should_restore_spfile_or_pfile is true we
            restore at default location : $ORACLE_HOME/dbs
        should_restore_spfile_or_pfile (bool): If set to true we first try to
            restore spfile, if spfile is not available then we try to restore
            pfile. If set to false we dont restore spfile or pfile. Default
            value is false, as spfile and pfile contains a lot of system
            parameters also, so user might not wanna replace his spfile/pfile
            on overwrite restore.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "file_location":'fileLocation',
        "should_restore_spfile_or_pfile":'shouldRestoreSpfileOrPfile',
    }
    def __init__(self,
                 file_location=None,
                 should_restore_spfile_or_pfile=None,
            ):

        """Constructor for the RestoreSpfileOrPfileInfo class"""

        # Initialize members of the class
        self.file_location = file_location
        self.should_restore_spfile_or_pfile = should_restore_spfile_or_pfile

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
        file_location = dictionary.get('fileLocation')
        should_restore_spfile_or_pfile = dictionary.get('shouldRestoreSpfileOrPfile')

        # Return an object of this model
        return cls(
            file_location,
            should_restore_spfile_or_pfile
)