# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DagApplicationServerInfo(object):

    """Implementation of the 'DagApplicationServerInfo' model.

    Specifies the information about the status of the Exchange Application
    Server which is a member of the DAG.

    Attributes:
        fqdn (string): Specifies the fully qualified domain name of the
            Exchange Server.
        guid (string): Specifies the Guid of the Exchange Application Server.
            keyspapce, only valid for an entity of type kKeyspace.
        id (string): Specifies the entity id of the Exchange Application
            server.
        name (string): Specifies the display name of the Exchange
            Application Server.
        owner_id (int): Specifies the entity id of the owner entity of the
            Exchange Application Server.
        status (StatusDagApplicationServerInfoEnum):  Specifies the status of
            the registration of the Exchange Application Server.
            Specifies the status of registration of Exchange Application Server.
            'kUnknown' indicates the status is not known.
            'kHealthy' indicates the status is healty and is registered as
            Exchange Server.
            'kUnHealthy' indicates the exchange application is registered on
            the physical server but it is unreachable now.
            'kUnregistered' indicates the server is not registered as physical
            source.
            'kUnreachable' indicates the server is not reachable from the
            cohesity cluster or the cohesity protection server is not installed
            on the exchange server.
            'kDetached' indicates the server is removed from the ExchangeDAG.
        total_size_bytes (int):  Specifies the total size of all Exchange
            database copies in all the Exchange Application Servers that are
            part of the DAG.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fqdn": 'fqdn',
        "guid": 'guid',
        "id":'id',
        "name": 'name',
        "owner_id": 'ownerId',
        "status":'status',
        "total_size_bytes":'totalSizeBytes'
    }

    def __init__(self,
                 fqdn=None,
                 guid=None,
                 id=None,
                 name=None,
                 owner_id=None,
                 status=None,
                 total_size_bytes=None):
        """Constructor for the DagApplicationServerInfo class"""

        # Initialize members of the class
        self.fqdn = fqdn
        self.guid = guid
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.status = status
        self.total_size_bytes = total_size_bytes

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
        fqdn = dictionary.get('fqdn')
        guid = dictionary.get('guid')
        id = dictionary.get('id')
        name = dictionary.get('name')
        owner_id = dictionary.get('ownerId')
        status = dictionary.get('status')
        total_size_bytes = dictionary.get('totalSizeBytes')

        # Return an object of this model
        return cls(fqdn,
                   guid,
                   id,
                   name,
                   owner_id,
                   status,
                   total_size_bytes)


