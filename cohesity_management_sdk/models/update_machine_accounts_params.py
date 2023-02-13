# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpdateMachineAccountsParams(object):

    """Implementation of the 'UpdateMachineAccountsParams' model.

    Specifies the parameters required to update the machine accounts of an
    active directory.

    Attributes:
        machine_accounts (list of string): Array of Machine Accounts.
            Specifies an array of computer names used to identify the Cohesity
            Cluster on the domain.
        overwrite_existing_accounts (bool): Specifies whether the specified
            machine accounts should overwrite the existing machine accounts in
            this domain.
        password (string): Specifies the password for the specified userName.
        user_name (string): Specifies a userName that has administrative
            privileges in the domain.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "machine_accounts":'machineAccounts',
        "overwrite_existing_accounts":'overwriteExistingAccounts',
        "password":'password',
        "user_name":'userName'
    }

    def __init__(self,
                 machine_accounts=None,
                 overwrite_existing_accounts=None,
                 password=None,
                 user_name=None):
        """Constructor for the UpdateMachineAccountsParams class"""

        # Initialize members of the class
        self.machine_accounts = machine_accounts
        self.overwrite_existing_accounts = overwrite_existing_accounts
        self.password = password
        self.user_name = user_name


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
        machine_accounts = dictionary.get('machineAccounts')
        overwrite_existing_accounts = dictionary.get('overwriteExistingAccounts')
        password = dictionary.get('password')
        user_name = dictionary.get('userName')

        # Return an object of this model
        return cls(machine_accounts,
                   overwrite_existing_accounts,
                   password,
                   user_name)


