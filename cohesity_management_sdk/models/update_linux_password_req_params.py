# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpdateLinuxPasswordReqParams(object):

    """Implementation of the 'UpdateLinuxPasswordReqParams' model.

    Specifies the user input parameters.

    Attributes:
        linux_current_password (string): Specifies the current password.
        linux_password (string): Specifies the new linux password.
        linux_username (string): Specifies the linux username for which the
            password will be updated.
        verify_password (bool): True if request is only to verify if current
            password matches with set password.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "linux_password":'linuxPassword',
        "linux_username":'linuxUsername',
        "linux_current_password":'linuxCurrentPassword',
        "verify_password":'verifyPassword'
    }

    def __init__(self,
                 linux_password=None,
                 linux_username=None,
                 linux_current_password=None,
                 verify_password=None):
        """Constructor for the UpdateLinuxPasswordReqParams class"""

        # Initialize members of the class
        self.linux_current_password = linux_current_password
        self.linux_password = linux_password
        self.linux_username = linux_username
        self.verify_password = verify_password


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
        linux_password = dictionary.get('linuxPassword')
        linux_username = dictionary.get('linuxUsername')
        linux_current_password = dictionary.get('linuxCurrentPassword')
        verify_password = dictionary.get('verifyPassword')

        # Return an object of this model
        return cls(linux_password,
                   linux_username,
                   linux_current_password,
                   verify_password)


