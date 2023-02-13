# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NasMountCredentialParams(object):

    """Implementation of the 'NasMountCredentialParams' model.

    Specifies the credentials to mount a volume on a NetApp server.

    Attributes:
        domain (string): Specifies the domain in which this credential is
            valid.
        domain_controller (string): Specifies the domain controller for the
            selected domain
        manage_password_by_cohesity (bool): Specifies if Cohesity can manage
            the password after registration
        nas_protocol (NasProtocolEnum): Specifies the protocol used by the NAS
            server. Specifies the protocol used by a NAS server. 'kNfs3'
            indicates NFS v3 protocol. 'kCifs1' indicates CIFS v1.0 protocol.
        nas_type (NasTypeEnum): Specifies the type of a NAS Object such as
            'kGroup', or 'kHost'. Specifies the kind of NAS mount. 'kGroup'
            indicates top level node that holds individual NAS hosts. 'kHost'
            indicates a single NAS path that can be mounted. 'kDfsGroup'
            indicates a DFS group containing top level directories mapped to
            different servers. 'kDfsTopDir' indicates a top level directory
            inside a DFS group, discovered when registering a DFS group.
        password (string): Specifies the password for the username to use for
            mounting the NAS.
        skip_validation (bool): Specifies the flag to disable mount point
            validation during registration process.
        username (string): Specifies a username to use for mounting the NAS.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain":'domain',
        "domain_controller":'domainController',
        "manage_password_by_cohesity":'managePasswordByCohesity',
        "nas_protocol":'nasProtocol',
        "nas_type":'nasType',
        "password":'password',
        "skip_validation":'skipValidation',
        "username":'username'
    }

    def __init__(self,
                 domain=None,
                 domain_controller=None,
                 manage_password_by_cohesity=None,
                 nas_protocol=None,
                 nas_type=None,
                 password=None,
                 skip_validation=None,
                 username=None):
        """Constructor for the NasMountCredentialParams class"""

        # Initialize members of the class
        self.domain = domain
        self.domain_controller = domain_controller
        self.manage_password_by_cohesity = manage_password_by_cohesity
        self.nas_protocol = nas_protocol
        self.nas_type = nas_type
        self.password = password
        self.skip_validation = skip_validation
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
        domain_controller = dictionary.get('domainController')
        manage_password_by_cohesity = dictionary.get('managePasswordByCohesity')
        nas_protocol = dictionary.get('nasProtocol')
        nas_type = dictionary.get('nasType')
        password = dictionary.get('password')
        skip_validation = dictionary.get('skipValidation')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(domain,
                   domain_controller,
                   manage_password_by_cohesity,
                   nas_protocol,
                   nas_type,
                   password,
                   skip_validation,
                   username)


