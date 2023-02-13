# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CifsShareInfo(object):

    """Implementation of the 'CifsShareInfo' model.

    Specifies information about a CIFS share of a NetApp volume.

    Attributes:
        acls (list of string): Array of Access Control Lists.  Specifies the
            ACLs for this share.
        name (string): Specifies the name of the CIFS share. This can be
            different from the volume name that this share belongs to. A
            single volume can export multiple CIFS shares, each with unique
            settings such as permissions.
        path (string): Specifies the path of this share under the Vserver's
            root.
        server_name (string): Specifies the CIFS server name (such as
            'NETAPP-01') specified by the system administrator. This name is
            searchable within the active directory domain.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "acls":'acls',
        "name":'name',
        "path":'path',
        "server_name":'serverName'
    }

    def __init__(self,
                 acls=None,
                 name=None,
                 path=None,
                 server_name=None):
        """Constructor for the CifsShareInfo class"""

        # Initialize members of the class
        self.acls = acls
        self.name = name
        self.path = path
        self.server_name = server_name


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
        acls = dictionary.get('acls')
        name = dictionary.get('name')
        path = dictionary.get('path')
        server_name = dictionary.get('serverName')

        # Return an object of this model
        return cls(acls,
                   name,
                   path,
                   server_name)


