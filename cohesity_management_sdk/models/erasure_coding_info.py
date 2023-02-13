# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ErasureCodingInfo(object):

    """Implementation of the 'ErasureCodingInfo' model.

    Specifies information for erasure coding.

    Attributes:
        algorithm (AlgorithmEnum): Algorthm used for erasure coding.
            REED_SOLOMON indicates the algorithm used for erasure coding. LRC
            indicates the algorithm used for erasure coding.
        erasure_coding_enabled (bool): Specifies whether Erasure coding is
            enabled on the Storage Domain (View Box).
        inline_erasure_coding (bool): Specifies if erasure coding should occur
            inline (as the data is being written). This field is only relevant
            if erasure coding is enabled.
        num_coded_stripes (int): The number of coded stripes.
        num_data_stripes (int): The number of stripes containing data.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "algorithm":'algorithm',
        "erasure_coding_enabled":'erasureCodingEnabled',
        "inline_erasure_coding":'inlineErasureCoding',
        "num_coded_stripes":'numCodedStripes',
        "num_data_stripes":'numDataStripes'
    }

    def __init__(self,
                 algorithm=None,
                 erasure_coding_enabled=None,
                 inline_erasure_coding=None,
                 num_coded_stripes=None,
                 num_data_stripes=None):
        """Constructor for the ErasureCodingInfo class"""

        # Initialize members of the class
        self.algorithm = algorithm
        self.erasure_coding_enabled = erasure_coding_enabled
        self.inline_erasure_coding = inline_erasure_coding
        self.num_coded_stripes = num_coded_stripes
        self.num_data_stripes = num_data_stripes


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
        algorithm = dictionary.get('algorithm')
        erasure_coding_enabled = dictionary.get('erasureCodingEnabled')
        inline_erasure_coding = dictionary.get('inlineErasureCoding')
        num_coded_stripes = dictionary.get('numCodedStripes')
        num_data_stripes = dictionary.get('numDataStripes')

        # Return an object of this model
        return cls(algorithm,
                   erasure_coding_enabled,
                   inline_erasure_coding,
                   num_coded_stripes,
                   num_data_stripes)


