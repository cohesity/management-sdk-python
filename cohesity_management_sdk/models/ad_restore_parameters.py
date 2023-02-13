# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_restore_options
import cohesity_management_sdk.models.credentials

class AdRestoreParameters(object):

    """Implementation of the 'AdRestoreParameters' model.

    Specifies the parameters specific to Application domain controller.

    Attributes:
        ad_options (AdRestoreOptions): Specifies the Active Directory options for the
            Restore task.
        credentials (Credentials): Specifies credentials to access a target
            source.
        mount_and_restore (bool): Specifies the option to mount the AD snapshot
            database and restore the AD objects in a single restore task.
            AdOptions must be set if this is set to true.
        port (int): Specifies the port on which the AD domain controller's
            NTDS database will be mounted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ad_options":'adOptions',
        "credentials":'credentials',
        "mount_and_restore":'mountAndRestore',
        "port":'port'
    }

    def __init__(self,
                 ad_options=None,
                 credentials=None,
                 mount_and_restore=None,
                 port=None):
        """Constructor for the AdRestoreParameters class"""

        # Initialize members of the class
        self.ad_options = ad_options
        self.credentials = credentials
        self.mount_and_restore = mount_and_restore
        self.port = port


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
        ad_options = cohesity_management_sdk.models.ad_restore_options.AdRestoreOptions.from_dictionary(dictionary.get("adOptions")) if dictionary.get("adOptions") else None
        credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('credentials')) if dictionary.get('credentials') else None
        mount_and_restore = dictionary.get('mountAndRestore')
        port = dictionary.get('port')

        # Return an object of this model
        return cls(ad_options,
                   credentials,
                   mount_and_restore,
                   port)


