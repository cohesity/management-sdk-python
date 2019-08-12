# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class DeployCertParameters(object):

    """Implementation of the 'DeployCertParameters' model.

    Specifies the parameters used to generate and deploy a certificate.

    Attributes:
        cert_file_name (string): Specifies the filename of the certificate.
        password (list of string): Specifies the passsword of the host to
            establish SSH connection. The certificate is copied to the host
            after generating the certificate on the cluster.
        server_name (list of string): Specifies the servername of the host
            where certificate is to be deployed.
        target (list of string): Specifies the target location on the host
            where the certificate is deployed.
        user_name (list of string): TODO(Sai Akhil S): Accept credentials for
            the cluster instead of each each node and copy certificate to all
            nodes. Specifies the username of the host.
        valid_days (long|int): Specifies the number of days after which the
            certificate will expire. The user has to input the number of days
            (from the current date) till when the certificate is valid.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cert_file_name":'certFileName',
        "password":'password',
        "server_name":'serverName',
        "target":'target',
        "user_name":'userName',
        "valid_days":'validDays'
    }

    def __init__(self,
                 cert_file_name=None,
                 password=None,
                 server_name=None,
                 target=None,
                 user_name=None,
                 valid_days=None):
        """Constructor for the DeployCertParameters class"""

        # Initialize members of the class
        self.cert_file_name = cert_file_name
        self.password = password
        self.server_name = server_name
        self.target = target
        self.user_name = user_name
        self.valid_days = valid_days


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
        cert_file_name = dictionary.get('certFileName')
        password = dictionary.get('password')
        server_name = dictionary.get('serverName')
        target = dictionary.get('target')
        user_name = dictionary.get('userName')
        valid_days = dictionary.get('validDays')

        # Return an object of this model
        return cls(cert_file_name,
                   password,
                   server_name,
                   target,
                   user_name,
                   valid_days)


