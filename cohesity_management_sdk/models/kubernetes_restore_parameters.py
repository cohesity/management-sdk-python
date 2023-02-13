# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class KubernetesRestoreParameters(object):

    """Implementation of the 'KubernetesRestoreParameters' model.

    Specifies the information required for recovering kubernetes entities.

    Attributes:
        prefix (string): Specifies a prefix to prepended to the source object
            name to derive a new name for the recovered or cloned object. By
            default, cloned or recovered objects retain their original name.
            Length of this field is limited to 8 characters.
        suffix (string): Specifies a suffix to appended to the original source
            object name to derive a new name for the recovered or cloned
            object. By default, cloned or recovered objects retain their
            original name. Length of this field is limited to 8 characters.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prefix":'prefix',
        "suffix":'suffix'
    }

    def __init__(self,
                 prefix=None,
                 suffix=None):
        """Constructor for the KubernetesRestoreParameters class"""

        # Initialize members of the class
        self.prefix = prefix
        self.suffix = suffix


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
        prefix = dictionary.get('prefix')
        suffix = dictionary.get('suffix')

        # Return an object of this model
        return cls(prefix,
                   suffix)


