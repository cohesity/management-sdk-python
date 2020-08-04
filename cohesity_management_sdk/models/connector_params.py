# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.additional_connector_params
import cohesity_management_sdk.models.credentials
import cohesity_management_sdk.models.entity_proto

class ConnectorParams(object):

    """Implementation of the 'ConnectorParams' model.

    Message that encapsulates the various params required to establish a
    connection with a particular environment.

    Attributes:
        additional_params(AdditionalConnectorParams): Optional additional
            connector params might be needed to connect to an environment.
        agent_endpoint (string): For some of the environments connection to
            endpoint is done through an agent. This captures the agent
            endpoint information.
        agent_port (int): Optional agent port to use when connecting to the
            server. If this is not specified, then environment specific
            default port will be used.
        credentials (Credentials): Specifies credentials to access a target
            source.
        endpoint (string): The endpoint URL of the environment (such as the
            address of the vCenter instance for a VMware environment, etc).
        entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        host_type (int): The host environment type. This is set for kPhysical
            type environment.
        id (long|int): A unique id associated with this connector params. This
            is a convenience field and is used to maintain an index to
            different connection params. This is generated at the time when
            the source is registered with Magneto.
        populate_subnet_for_all_cluster_nodes (bool): If set to true, inter
            agent communcation will be enabled and for every GetAgentInfo call
            we will fill subnet information of all the nodes in clustered
            entity.
        port (int): Optional port to use when connecting to the server. If
            this is not specified, then environment specific default port will
            be used.
        tenant_id (string): The tenant_id for the environment. This is used to
            remotely access connectors and executors via bifrost.
        mtype (int): The type of environment to connect to.
        version (long|int): A version that is associated with the params. This
            is updated anytime any of the params change. This is used to
            discard older connector params.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_params":'additionalParams',
        "agent_endpoint":'agentEndpoint',
        "agent_port":'agentPort',
        "credentials":'credentials',
        "endpoint":'endpoint',
        "entity":'entity',
        "host_type":'hostType',
        "id":'id',
        "populate_subnet_for_all_cluster_nodes":'populateSubnetForAllClusterNodes',
        "port":'port',
        "tenant_id":'tenantId',
        "mtype":'type',
        "version":'version'
    }

    def __init__(self,
                 additional_params=None,
                 agent_endpoint=None,
                 agent_port=None,
                 credentials=None,
                 endpoint=None,
                 entity=None,
                 host_type=None,
                 id=None,
                 populate_subnet_for_all_cluster_nodes=None,
                 port=None,
                 tenant_id=None,
                 mtype=None,
                 version=None):
        """Constructor for the ConnectorParams class"""

        # Initialize members of the class
        self.additional_params = additional_params
        self.agent_endpoint = agent_endpoint
        self.agent_port = agent_port
        self.credentials = credentials
        self.endpoint = endpoint
        self.entity = entity
        self.host_type = host_type
        self.id = id
        self.populate_subnet_for_all_cluster_nodes = populate_subnet_for_all_cluster_nodes
        self.port = port
        self.tenant_id = tenant_id
        self.mtype = mtype
        self.version = version


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
        additional_params = cohesity_management_sdk.models.additional_connector_params.AdditionalConnectorParams.from_dictionary(dictionary.get('additionalParams')) if dictionary.get('additionalParams') else None
        agent_endpoint = dictionary.get('agentEndpoint')
        agent_port = dictionary.get('agentPort')
        credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('credentials')) if dictionary.get('credentials') else None
        endpoint = dictionary.get('endpoint')
        entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('entity')) if dictionary.get('entity') else None
        host_type = dictionary.get('hostType')
        id = dictionary.get('id')
        populate_subnet_for_all_cluster_nodes = dictionary.get('populateSubnetForAllClusterNodes', None)
        port = dictionary.get('port')
        tenant_id = dictionary.get('tenantId')
        mtype = dictionary.get('type')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(additional_params,
                   agent_endpoint,
                   agent_port,
                   credentials,
                   endpoint,
                   entity,
                   host_type,
                   id,
                   populate_subnet_for_all_cluster_nodes,
                   port,
                   tenant_id,
                   mtype,
                   version)


