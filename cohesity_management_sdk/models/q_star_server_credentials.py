# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class QStarServerCredentials(object):

    """Implementation of the 'QStarServerCredentials' model.

    Specifies the server credentials to connect to a QStar service
    to manage the media Vault.

    Attributes:
        host (string): Specifies the IP address or DNS name of the server
            where QStar service is running.
        integral_volume_names (list of string): Array of Integral Volume
            Names.  Specifies a list of existing Integral Volume names
            available on the QStar server for storing objects.
        password (string): Specifies the password used to access the QStar
            host.
        port (int): Specifies the listening port where QStar WEB API service
            is running.
        share_type (string): Specifies the sharing protocol type used by QStar
            to mount the integral volume. See the Cohesity online help for the
            recommended protocol for your environment.
        use_https (bool): Specifies whether to use http or https to connect to
            the service. If true, a secure connection (https) is used.
        username (string): Specifies the account name used to access the QStar
            host.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "host":'host',
        "integral_volume_names":'integralVolumeNames',
        "password":'password',
        "port":'port',
        "share_type":'shareType',
        "use_https":'useHttps',
        "username":'username'
    }

    def __init__(self,
                 host=None,
                 integral_volume_names=None,
                 password=None,
                 port=None,
                 share_type=None,
                 use_https=None,
                 username=None):
        """Constructor for the QStarServerCredentials class"""

        # Initialize members of the class
        self.host = host
        self.integral_volume_names = integral_volume_names
        self.password = password
        self.port = port
        self.share_type = share_type
        self.use_https = use_https
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
        integral_volume_names = dictionary.get('integralVolumeNames')
        password = dictionary.get('password')
        port = dictionary.get('port')
        share_type = dictionary.get('shareType')
        use_https = dictionary.get('useHttps')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(host,
                   integral_volume_names,
                   password,
                   port,
                   share_type,
                   use_https,
                   username)


