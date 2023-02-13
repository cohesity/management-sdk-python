# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GroupDeleteParameters(object):

    """Implementation of the 'GroupDeleteParameters' model.

    Specifies the groups to delete on the Cohesity Cluster.

    Attributes:
        domain (string): Specifies the domain associated with the groups to
            delete. Only groups associated with the same domain can be deleted
            by a single request. If no domain is specified, the specified
            groups are deleted from the LOCAL domain on the Cohesity Cluster.
            If a non-LOCAL domain is specified, the specified groups are
            deleted on the Cohesity Cluster. However, the referenced group
            principals on the Active Directory are not deleted.
        names (list of string): Array of Groups.  Specifies the list of groups
            to delete on the Cohesity Cluster. Only groups from the same
            domain can be deleted by a single request.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain":'domain',
        "names":'names'
    }

    def __init__(self,
                 domain=None,
                 names=None):
        """Constructor for the GroupDeleteParameters class"""

        # Initialize members of the class
        self.domain = domain
        self.names = names


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
        domain = dictionary.get('domain')
        names = dictionary.get('names')

        # Return an object of this model
        return cls(domain,
                   names)


