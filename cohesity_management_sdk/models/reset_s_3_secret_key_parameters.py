# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ResetS3SecretKeyParameters(object):

    """Implementation of the 'ResetS3SecretKeyParameters' model.

    Specifies the parameters required to reset the S3 secret access key for
    the specified Cohesity user.

    Attributes:
        domain (string): Specifies the fully qualified domain name (FQDN) of
            an Active Directory or LOCAL for the default LOCAL domain on the
            Cohesity Cluster. If not specified, it is assumed to be LOCAL.
        tenant_id (string): Specifies the tenant for which the users are
            to be deleted.
        username (string): Specifies the Cohesity user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain":'domain',
        "tenant_id":'tenantId',
        "username":'username'
    }

    def __init__(self,
                 domain=None,
                 tenant_id=None,
                 username=None):
        """Constructor for the ResetS3SecretKeyParameters class"""

        # Initialize members of the class
        self.domain = domain
        self.tenant_id = tenant_id
        self.username = username


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
        username = dictionary.get('username')

        # Return an object of this model
        return cls(domain,
                   tenant_id,
                   username)


