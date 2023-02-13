# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VaultProviderStatsByEnv(object):

    """Implementation of the 'VaultProviderStatsByEnv' model.

    Specifies the Vault stats by environments.

    Attributes:
        count (long|int): Specifies the count of the objects of the specified
            environment.
        environment (EnvironmentVaultProviderStatsByEnvEnum): Specifies the
            environment type.
        size (long|int): Specifies the size of the entities of the specified
            environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count":'count',
        "environment":'environment',
        "size":'size'
    }

    def __init__(self,
                 count=None,
                 environment=None,
                 size=None):
        """Constructor for the VaultProviderStatsByEnv class"""

        # Initialize members of the class
        self.count = count
        self.environment = environment
        self.size = size


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
        count = dictionary.get('count')
        environment = dictionary.get('environment')
        size = dictionary.get('size')

        # Return an object of this model
        return cls(count,
                   environment,
                   size)


