# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.iscsi_san_port

class PureStorageArray(object):

    """Implementation of the 'PureStorageArray' model.

    Specifies a Pure Storage Array.

    Attributes:
        id (string): Specifies a unique id of a Pure Storage Array. The id is
            unique across Cohesity Clusters.
        ports (list of IscsiSanPort): Specifies the SAN ports of the Pure
            Storage Array.
        revision (string): Specifies the revision of the Pure Storage Array.
        version (string): Specifies the version of the Pure Storage Array.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "ports":'ports',
        "revision":'revision',
        "version":'version'
    }

    def __init__(self,
                 id=None,
                 ports=None,
                 revision=None,
                 version=None):
        """Constructor for the PureStorageArray class"""

        # Initialize members of the class
        self.id = id
        self.ports = ports
        self.revision = revision
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
        id = dictionary.get('id')
        ports = None
        if dictionary.get('ports') != None:
            ports = list()
            for structure in dictionary.get('ports'):
                ports.append(cohesity_management_sdk.models.iscsi_san_port.IscsiSanPort.from_dictionary(structure))
        revision = dictionary.get('revision')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(id,
                   ports,
                   revision,
                   version)


