# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NetworkRealmInfo(object):

    """Implementation of the 'NetworkRealmInfo' model.

    Contains mapping of network realms with adapter specific entities. This
    will be populated by IRIS for create/update source requests so that we can
    persist the mapping in the corresponding entity hierarchy.


    Attributes:

        connector_group_id (long|int): 'network_realm_id' maintains the
            collection of connector_group_id. Connector group id for the
            environment. If it is set, Magneto will fetch the bifrost server
            based on <network_realm_id, connector_group_id>.
        entity_id (long|int): Entity id to which the network_realm_id is mapped
            to. This can be a non root entity as well.
        network_realm_id (long|int): Network Realm id to use for the tenant.
            This realm could be a collection of Rigel/HyX.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "connector_group_id":'connectorGroupId',
        "entity_id":'entityId',
        "network_realm_id":'networkRealmId',
    }
    def __init__(self,
                 connector_group_id=None,
                 entity_id=None,
                 network_realm_id=None,
            ):

        """Constructor for the NetworkRealmInfo class"""

        # Initialize members of the class
        self.connector_group_id = connector_group_id
        self.entity_id = entity_id
        self.network_realm_id = network_realm_id

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
        connector_group_id = dictionary.get('connectorGroupId')
        entity_id = dictionary.get('entityId')
        network_realm_id = dictionary.get('networkRealmId')

        # Return an object of this model
        return cls(
            connector_group_id,
            entity_id,
            network_realm_id
)