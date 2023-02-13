# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NasMountCredentials(object):

    """Implementation of the 'NasMountCredentials' model.

    Message that encapsulates the credentials for mounting a specific NAS type.

    Attributes:
        cohesity_managed_password (bool): Whether the password managed by
            cohesity during registration.
        domain_controller (string): Active Domain controller IP or hostname;
        domain_name (string): The  name of the domain which the NAS mount
            credentials belong to.
        encrypted_password (list of int): AES256 encrypted password. The key
            for encryption should be obtained from KMS.
        password (string): The password field is only populated in RPCs. On
            disk, instances of this proto should not have this field set,
            except for legacy records.
            TODO(oleg): Change this field type to bytes.j
        protocol (int): The protocol of the NAS mount.
        username (string): The username and password to use for mounting the
            NAS.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cohesity_managed_password": 'cohesityManagedPassword',
        "domain_controller": 'domainController',
        "domain_name": 'domainName',
        "encrypted_password":'encryptedPassword',
        "password":'password',
        "protocol":'protocol',
        "username":'username'
    }

    def __init__(self,
                 cohesity_managed_password=None,
                 domain_controller=None,
                 domain_name=None,
                 encrypted_password=None,
                 password=None,
                 protocol=None,
                 username=None
                 ):
        """Constructor for the NasMountCredentials class"""

        # Initialize members of the class
        self.cohesity_managed_password = cohesity_managed_password
        self.domain_controller = domain_controller
        self.domain_name = domain_name
        self.encrypted_password = encrypted_password
        self.password = password
        self.protocol = protocol
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
        cohesity_managed_password = dictionary.get('cohesityManagedPassword')
        domain_controller = dictionary.get('domainController')
        domain_name = dictionary.get('domainName')
        encrypted_password = dictionary.get('encryptedPassword')
        password = dictionary.get('password')
        protocol = dictionary.get('protocol')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(cohesity_managed_password,
                   domain_controller,
                   domain_name,
                   encrypted_password,
                   password,
                   protocol,
                   username)


