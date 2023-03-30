# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NasCredentials(object):

    """Implementation of the 'NasCredentials' model.

    Specifies the server credentials to connect to a NetApp server.


    Attributes:

        host (string): Specifies the hostname or IP address of the NAS server.
        kerberos_realm_name (string): If applicable and specified, the realm
            name of the Kerberos provider security the NFS share.
        mount_path (string): Specifies the mount path to the NAS server.
        nfs_security_type (NfsSecurityTypeEnum): If applicable and specified,
            the NFS security type of the NFS share.
        nfs_version_number (NfsVersionNumberEnum): If applicable and specified,
            the NFS version number of the NFS share.
        password (string): If using the CIFS protocol and a Username was
            specified, specify the password for the username.
        share_type (ShareTypeEnum): Specifies the sharing protocol type used to
            mount the file system. Currently, only NFS is supported. 'kNFS'
            indicates use the NFS protocol to mount the file system. 'kCIFS'
            indicates use the CIFS protocol to mount the file system.
        username (string): If using the CIFS protocol, you can optional specify
            a username to use when mounting.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "host":'host',
        "kerberos_realm_name":'kerberosRealmName',
        "mount_path":'mountPath',
        "nfs_security_type":'nfsSecurityType',
        "nfs_version_number":'nfsVersionNumber',
        "password":'password',
        "share_type":'shareType',
        "username":'username',
    }
    def __init__(self,
                 host=None,
                 kerberos_realm_name=None,
                 mount_path=None,
                 nfs_security_type=None,
                 nfs_version_number=None,
                 password=None,
                 share_type=None,
                 username=None,
            ):

        """Constructor for the NasCredentials class"""

        # Initialize members of the class
        self.host = host
        self.kerberos_realm_name = kerberos_realm_name
        self.mount_path = mount_path
        self.nfs_security_type = nfs_security_type
        self.nfs_version_number = nfs_version_number
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
        kerberos_realm_name = dictionary.get('kerberosRealmName')
        mount_path = dictionary.get('mountPath')
        nfs_security_type = dictionary.get('nfsSecurityType')
        nfs_version_number = dictionary.get('nfsVersionNumber')
        password = dictionary.get('password')
        share_type = dictionary.get('shareType')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(
            host,
            kerberos_realm_name,
            mount_path,
            nfs_security_type,
            nfs_version_number,
            password,
            share_type,
            username
)