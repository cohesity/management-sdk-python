# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RunNowPhysicalParameters(object):

    """Implementation of the 'RunNowPhysicalParameters' model.

    Attributes:
        metadata_file_path (string): Specifies metadata file path during
            run-now requests for physical file based backups for some specific
            host entity. If specified, it will override any default
            metadata/directive file path set at the job level for the host.
            Also note that if the job default does not specify a
            metadata/directive file path for the host, then specifying this
            field for that host during run-now request will be rejected.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metadata_file_path":'metadataFilePath'
    }

    def __init__(self,
                 metadata_file_path=None):
        """Constructor for the RunNowPhysicalParameters class"""

        # Initialize members of the class
        self.metadata_file_path = metadata_file_path


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
        metadata_file_path = dictionary.get('metadataFilePath')

        # Return an object of this model
        return cls(metadata_file_path)


