# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PstParameters(object):

    """Implementation of the 'PstParameters' model.

    Specifies PST conversion details.

    Attributes:
        create_pst (bool): Specifies if create a PST or MSG for input items.
          For 6.6 we always set this to true.
        pst_password (string): Specifies Password to be set for generated PSTs.
        pst_size_threshold (long|int): Specifies PST size threshold in bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "create_pst":'createPst',
        "pst_password":'pstPassword',
        "pst_size_threshold":'pstSizeThreshold'
    }

    def __init__(self,
                 create_pst=None,
                 pst_password=None,
                 pst_size_threshold=None):
        """Constructor for the PstParameters class"""

        # Initialize members of the class
        self.create_pst = create_pst
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
        pst_password = dictionary.get('pstPassword')
        pst_size_threshold = dictionary.get('pstSizeThreshold')

        # Return an object of this model
        return cls(create_pst,
                   pst_password,
                   pst_size_threshold)


