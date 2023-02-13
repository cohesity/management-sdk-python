# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class EwsToPstConversionParams(object):

    """Implementation of the 'EwsToPstConversionParams' model.

    Attributes:
        create_pst (bool): Create Msg files or Pst.
            false value indicates only create msg files.
            Default value is true.
        option_flags (int): ConvertEwsToPst flags of pstSizeThreshold
            ConvertEwsToPSTOptionFlags.
        pst_name_prefix (string): Name prefix for generated PST files.
        pst_password (string): Optional password to be set for the output PSTs.
        pst_size_threshold (long|int): PST rotation size in bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "create_pst":'createPst',
        "option_flags":'optionFlags',
        "pst_name_prefix":'pstNamePrefix',
        "pst_password":'pstPassword',
        "pst_size_threshold":'pstSizeThreshold'
    }

    def __init__(self,
                 create_pst=None,
                 option_flags=None,
                 pst_name_prefix=None,
                 pst_password=None,
                 pst_size_threshold=None):
        """Constructor for the EwsToPstConversionParams class"""

        # Initialize members of the class
        self.create_pst = create_pst
        self.option_flags = option_flags
        self.pst_name_prefix = pst_name_prefix
        self.pst_password = pst_password
        self.pst_size_threshold = pst_size_threshold


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
        create_pst = dictionary.get('createPst')
        option_flags = dictionary.get('optionFlags')
        pst_name_prefix = dictionary.get('pstNamePrefix')
        pst_size_threshold = dictionary.get('pstSizeThreshold')
        pst_password = dictionary.get('pstPassword')

        # Return an object of this model
        return cls(create_pst,
                   option_flags,
                   pst_name_prefix,
                   pst_password,
                   pst_size_threshold)


