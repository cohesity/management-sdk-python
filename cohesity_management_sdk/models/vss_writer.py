# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VssWriter(object):

    """Implementation of the 'VssWriter' model.

    Specifies vss writer information about a Physical Protection Source.

    Attributes:
        is_writer_excluded (bool): If true, the writer will be excluded by
            default.
        writer_name (string): Specifies the name of the writer.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_writer_excluded": 'isWriterExcluded',
        "writer_name": 'writerName'
    }

    def __init__(self,
                 is_writer_excluded=None,
                 writer_name=None):
        """Constructor for the VssWriter class"""

        # Initialize members of the class
        self.is_writer_excluded = is_writer_excluded
        self.writer_name = writer_name


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
        is_writer_excluded = dictionary.get('isWriterExcluded', None)
        writer_name = dictionary.get('writerName', None)

        # Return an object of this model
        return cls(is_writer_excluded,
                   writer_name)


