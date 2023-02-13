# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.externally_triggered_job_params_externally_triggered_sbt_params

class ExternallyTriggeredJobParams(object):

    """Implementation of the 'ExternallyTriggeredJobParams' model.

    Message to capture any additional backup params specific to externally
    triggered backup job.

    Attributes:
        client_type (int): The client type for this job.
        sbt_params (ExternallyTriggeredJobParams_ExternallyTriggeredSbtParams):
            The SBT parameters.
        tags (list of string): All the tags populated in the runs of
            the externally triggered job. This field is only for the
            convenience of UI filtering the runs based on the tag. It
            should be populated only for the Iris query requests and
            should never be persisted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_type":'clientType',
        "sbt_params":'sbtParams',
        "tags":'tags'
    }

    def __init__(self,
                 client_type=None,
                 sbt_params=None,
                 tags=None):
        """Constructor for the ExternallyTriggeredJobParams class"""

        # Initialize members of the class
        self.client_type = client_type
        self.sbt_params = sbt_params
        self.tags = tags


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
        sbt_params = cohesity_management_sdk.models.externally_triggered_job_params_externally_triggered_sbt_params.ExternallyTriggeredJobParams_ExternallyTriggeredSbtParams.from_dictionary(dictionary.get('sbtParams')) if dictionary.get('sbtParams') else None
        tags = dictionary.get('tags')

        # Return an object of this model
        return cls(client_type,
                   sbt_params,
                   tags)


