# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.one_drive_env_job_parameters
import cohesity_management_sdk.models.outlook_env_job_parameters

class Office365EnvJobParameters(object):

    """Implementation of the 'Office365EnvJobParameters' model.

    Specifies Office365 parameters applicable for all Office365 Environment
    type Protection Sources in a Protection Job. This encapsulates both
    OneDrive
    & Mailbox parameters.

    Attributes:
        onedrive_parameters (OneDriveEnvJobParameters): Specifies OneDrive job
            parameters applicable for all Office365 Environment type
            Protection Sources in a Protection Job.
        outlook_parameters (OutlookEnvJobParameters): Specifies Outlook job
            parameters applicable for all Office365 Environment type
            Protection Sources in a Protection Job.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "onedrive_parameters":'onedriveParameters',
        "outlook_parameters":'outlookParameters'
    }

    def __init__(self,
                 onedrive_parameters=None,
                 outlook_parameters=None):
        """Constructor for the Office365EnvJobParameters class"""

        # Initialize members of the class
        self.onedrive_parameters = onedrive_parameters
        self.outlook_parameters = outlook_parameters


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
        onedrive_parameters = cohesity_management_sdk.models.one_drive_env_job_parameters.OneDriveEnvJobParameters.from_dictionary(dictionary.get('onedriveParameters')) if dictionary.get('onedriveParameters') else None
        outlook_parameters = cohesity_management_sdk.models.outlook_env_job_parameters.OutlookEnvJobParameters.from_dictionary(dictionary.get('outlookParameters')) if dictionary.get('outlookParameters') else None

        # Return an object of this model
        return cls(onedrive_parameters,
                   outlook_parameters)


