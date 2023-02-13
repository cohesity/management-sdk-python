# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NisNetgroup(object):

    """Implementation of the 'NisNetgroup' model.

    Defines an NIS Netgroup.

    Attributes:
        description (string): Description of the netgroup.
        domain (string): Specifies the domain of the netgroup.
        name (string): Specifies the name of the netgroup.
        nfs_access (NfsAccessEnum): Specifies whether clients from this
            netgroup can mount using NFS protocol.
            Protocol access level.
            'kDisabled' indicates Protocol access level 'Disabled'
            'kReadOnly' indicates Protocol access level 'ReadOnly'
            'kReadWrite' indicates Protocol access level 'ReadWrite'
        nfs_squash (int): Specifies the NFS squash type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "domain": 'domain',
        "name": 'name',
        "nfs_access": 'nfsAccess',
        "nfs_squash":'nfsSquash'
    }

    def __init__(self,
                 description=None,
                 domain=None,
                 name=None,
                 nfs_access=None,
                 nfs_squash=None):
        """Constructor for the NisNetgroup class"""

        # Initialize members of the class
        self.description = description
        self.domain = domain
        self.name = name
        self.nfs_access = nfs_access
        self.nfs_squash = nfs_squash

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
        description = dictionary.get('description')
        domain = dictionary.get('domain')
        name = dictionary.get('name')
        nfs_access = dictionary.get('nfsAccess')
        nfs_squash = dictionary.get('nfsSquash')

        # Return an object of this model
        return cls(description,
                   domain,
                   name,
                   nfs_access,
                   nfs_squash)


