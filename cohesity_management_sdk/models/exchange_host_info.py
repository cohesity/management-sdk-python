# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ExchangeHostInfo(object):

    """Implementation of the 'ExchangeHostInfo' model.

    Specifies the Information about the Exchange host.

    Attributes:
        agent_status (AgentStatusExchangeHostInfoEnum): Specifies the status
            of the agent on the Exchange host.
            Specifies the status of agent on Exchange Application Server.
            'kSupported' indicates the agent is supported for Exchange data
            protection.
            'kUnSupported' indicates the agent is not supported for Exchange
            data protection.
            'kUpgrade' indicates the agent of server need to be upgraded.
        endpoint (string): Specifies the endpoint of the Exchange host.
        guid (string): Specifies the guid of the Exchange host.
        name (string): Specifies the display name of the Exchange host.
        protection_source_id (int): Specifies the Protection source id of the
            Physical Host if the Exchange application is already registered on
            the physical host with the above endpoint.
        status (StatusExchangeHostInfoEnum): Specifies the status of the
            registration of the Exchange Host.
            Specifies the status of registration of Exchange Application
            Server.
            'kUnknown' indicates the status is not known.
            'kHealthy' indicates the status is healty and is registered as
            Exchange Server.
            'kUnHealthy' indicates the exchange application is registered on
            the physical server but it is unreachable now.
            'kUnregistered' indicates the server is not registered as physical
            source.
            'kUnreachable' indicates the server is not reachable from the
            cohesity cluster or the cohesity protection server is not
            installed on the exchange server.
            'kDetached' indicates the server is removed from the ExchangeDAG.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "agent_status": 'agentStatus',
        "endpoint": 'endpoint',
        "guid": 'guid',
        "name": 'name',
        "protection_source_id":'protectionSourceId',
        "status":'status'
    }

    def __init__(self,
                 agent_status=None,
                 endpoint=None,
                 guid=None,
                 name=None,
                 protection_source_id=None,
                 status=None):
        """Constructor for the ExchangeHostInfo class"""

        # Initialize members of the class
        self.agent_status = agent_status
        self.endpoint = endpoint
        self.guid = guid
        self.name = name
        self.protection_source_id = protection_source_id
        self.status = status

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
        agent_status = dictionary.get('agentStatus')
        endpoint = dictionary.get('endpoint')
        guid = dictionary.get('guid')
        name = dictionary.get('name')
        protection_source_id = dictionary.get('protectionSourceId')
        status = dictionary.get('status')

        # Return an object of this model
        return cls(agent_status,
                   endpoint,
                   guid,
                   name,
                   protection_source_id,
                   status)


