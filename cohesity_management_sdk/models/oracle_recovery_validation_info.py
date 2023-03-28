# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class OracleRecoveryValidationInfo(object):

    """Implementation of the 'OracleRecoveryValidationInfo' model.

    TODO: type description here.


    Attributes:

        create_dummy_instance (bool): Boolean to tell whether we will be
            creating a dummy oracle instance to run recovery validations.
            Generally if we doing recovery validations on source host, we will
            do validations on the existing DB, else if validations are done on
            target different from source then we will be creating a dummy
            oracle instance to run validations.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "create_dummy_instance":'createDummyInstance',
    }
    def __init__(self,
                 create_dummy_instance=None,
            ):

        """Constructor for the OracleRecoveryValidationInfo class"""

        # Initialize members of the class
        self.create_dummy_instance = create_dummy_instance

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
        create_dummy_instance = dictionary.get('createDummyInstance')

        # Return an object of this model
        return cls(
            create_dummy_instance
)