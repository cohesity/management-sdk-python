# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.externally_triggered_sbt_parameters

class ExternallyTriggeredEnvJobParameters(object):

    """Implementation of the 'ExternallyTriggeredEnvJobParameters' model.

    Attributes:
        client_type (ClientTypeEnum): Specifies the client type of the
            externally triggered job
            kGeneric implies generic externally triggered backups.
            kSbt implies externally triggered backups for SBT.
        sbt_params (ExternallyTriggeredSbtParameters): Specifies the catalog
            view associated with this job.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_type": 'clientType',
        "sbt_params": 'sbtParams'
    }

    def __init__(self,
                 client_type=None,
                 sbt_params=None):
        """Constructor for the ExternallyTriggeredEnvJobParameters class"""

        # Initialize members of the class
        self.client_type = client_type
        self.sbt_params = sbt_params


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
        client_type = dictionary.get('clientType')
        sbt_params = cohesity_management_sdk.models.externally_triggered_sbt_parameters.ExternallyTriggeredSbtParameters.from_dictionary(dictionary.get('sbtParams')) if dictionary.get('sbtParams') else None

        # Return an object of this model
        return cls(client_type,
                   sbt_params)


