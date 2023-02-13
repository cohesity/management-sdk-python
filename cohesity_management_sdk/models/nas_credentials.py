# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NasCredentials(object):

    """Implementation of the 'NasCredentials' model.

    Specifies the server credentials to connect to a NetApp server.

    Attributes:
        host (string): Specifies the hostname or IP address of the NAS
            server.
        mount_path (string): Specifies the mount path to the NAS server.
        password (string): If using the CIFS protocol and a Username was
            specified, specify the password for the username.
        share_type (ShareTypeEnum): Specifies the sharing protocol type used
            to mount the file system. Currently, only NFS is supported. 'kNFS'
            indicates use the NFS protocol to mount the file system. 'kCIFS'
            indicates use the CIFS protocol to mount the file system.
        username (string): If using the CIFS protocol, you can optional
            specify a username to use when mounting.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "host":'host',
        "mount_path":'mountPath',
        "password":'password',
        "share_type":'shareType',
        "username":'username'
    }

    def __init__(self,
                 host=None,
                 mount_path=None,
                 password=None,
                 share_type=None,
                 username=None):
        """Constructor for the NasCredentials class"""

        # Initialize members of the class
        self.host = host
        self.mount_path = mount_path
        self.password = password
        self.share_type = share_type
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
        host = dictionary.get('host')
        mount_path = dictionary.get('mountPath')
        password = dictionary.get('password')
        share_type = dictionary.get('shareType')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(host,
                   mount_path,
                   password,
                   share_type,
                   username)


