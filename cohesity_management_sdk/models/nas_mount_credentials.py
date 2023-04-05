# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NasMountCredentials(object):

    """Implementation of the 'NasMountCredentials' model.

    TODO: type description here.


    Attributes:

        domain_name (string): The name of the domain which the NAS mount
            credentials belong to.
        encrypted_password (list of long|int): AES256 encrypted password. The
            key for encryption should be obtained from KMS.
        kdc (string): KDC hostname or IP for krb5 authentication. KDC stores
            secret keys for a smb user and provides the krb5 tickets for
            authentication.
        password (string): The password field is only populated in RPCs. On
            disk, instances of this proto should not have this field set,
            except for legacy records.  TODO(oleg): Change this field type to
            bytes.j
        protocol (int): The protocol of the NAS mount.
        username (string): The username and password to use for mounting the
            NAS.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "domain_name":'domainName',
        "encrypted_password":'encryptedPassword',
        "kdc":'kdc',
        "password":'password',
        "protocol":'protocol',
        "username":'username',
    }
    def __init__(self,
                 domain_name=None,
                 encrypted_password=None,
                 kdc=None,
                 password=None,
                 protocol=None,
                 username=None,
            ):

        """Constructor for the NasMountCredentials class"""

        # Initialize members of the class
        self.domain_name = domain_name
        self.encrypted_password = encrypted_password
        self.kdc = kdc
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
        domain_name = dictionary.get('domainName')
        encrypted_password = dictionary.get("encryptedPassword")
        kdc = dictionary.get('kdc')
        password = dictionary.get('password')
        protocol = dictionary.get('protocol')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(
            domain_name,
            encrypted_password,
            kdc,
            password,
            protocol,
            username
)