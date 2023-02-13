# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UserDeleteParameters(object):

    """Implementation of the 'UserDeleteParameters' model.

    Specifies the users to delete on the Cohesity Cluster.

    Attributes:
        domain (string): Specifies the domain associated with the users to
            delete. Only users associated with the same domain can be deleted
            by a single request. If no domain is specified, the specified
            users are deleted from the LOCAL domain on the Cohesity Cluster.
            If a non-LOCAL domain is specified, the specified users are
            deleted on the Cohesity Cluster. However, the referenced user
            principals on the Active Directory are not deleted.
        tenant_id (string): Specifies the tenant for which the the users are
            to be deleted.
        users (list of string): Array of Users.  Specifies the list of users
            to delete on Cohesity Cluster. Only users from the same domain can
            be deleted by a single request.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain":'domain',
        "tenant_id":'tenantId',
        "users":'users'
    }

    def __init__(self,
                 domain=None,
                 tenant_id=None,
                 users=None):
        """Constructor for the UserDeleteParameters class"""

        # Initialize members of the class
        self.domain = domain
        self.tenant_id = tenant_id
        self.users = users


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
        tenant_id = dictionary.get('tenantId')
        users = dictionary.get('users')

        # Return an object of this model
        return cls(domain,
                   tenant_id,
                   users)


