# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SystemAppStatusResult(object):

    """Implementation of the 'SystemAppStatusResult' model.

    Specifies the result of getting the status of System Apps.


    Attributes:

        available_replicas (int): Required field.
        configured_replicas (int): Required field.
        name (string): Required field.
        ready_replicas (int): Required field.
        service_endpoint (string): Required field.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "available_replicas":'availableReplicas',
        "configured_replicas":'configuredReplicas',
        "name":'name',
        "ready_replicas":'readyReplicas',
        "service_endpoint":'serviceEndpoint',
    }
    def __init__(self,
                 available_replicas=None,
                 configured_replicas=None,
                 name=None,
                 ready_replicas=None,
                 service_endpoint=None,
            ):

        """Constructor for the SystemAppStatusResult class"""

        # Initialize members of the class
        self.available_replicas = available_replicas
        self.configured_replicas = configured_replicas
        self.name = name
        self.ready_replicas = ready_replicas
        self.service_endpoint = service_endpoint

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
        available_replicas = dictionary.get('availableReplicas')
        configured_replicas = dictionary.get('configuredReplicas')
        name = dictionary.get('name')
        ready_replicas = dictionary.get('readyReplicas')
        service_endpoint = dictionary.get('serviceEndpoint')

        # Return an object of this model
        return cls(
            available_replicas,
            configured_replicas,
            name,
            ready_replicas,
            service_endpoint
)