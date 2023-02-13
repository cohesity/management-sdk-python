# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SystemAppStatusResult(object):

    """Implementation of the 'SystemAppStatusResult' model.

    Specifies the result of getting the status of System Apps.

    Attributes:
        available_replicas (int): Required field.
        name (string): Required field.
        configured_replicas (int): Required field.
        ready_replicas (int): Required field.
        service_endpoint (string): Required field.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "available_replicas":'availableReplicas',
        "name":'name',
        "configured_replicas":'configuredReplicas',
        "ready_replicas":'readyReplicas',
        "service_endpoint":'serviceEndpoint'
    }

    def __init__(self,
                 available_replicas=None,
                 name=None,
                 configured_replicas=None,
                 ready_replicas=None,
                 service_endpoint=None):
        """Constructor for the SystemAppStatusResult class"""

        # Initialize members of the class
        self.available_replicas = available_replicas
        self.name = name
        self.configured_replicas = configured_replicas
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
        name = dictionary.get('name')
        configured_replicas = dictionary.get('configuredReplicas')
        service_endpoint = dictionary.get('serviceEndpoint')
        ready_replicas = dictionary.get('readyReplicas')

        # Return an object of this model
        return cls(available_replicas,
                   name,
                   configured_replicas,
                   ready_replicas,
                   service_endpoint)


