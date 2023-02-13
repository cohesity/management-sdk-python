# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AMQPTargetConfig(object):

    """Implementation of the 'AMQPTargetConfig' model.

    Specifies the AMQP target config.

    Attributes:
        certificate (string): Specifies the certificate.
        exchange (string): Specifies the exchange.
        filer_id (string): Specifies the filer id.
        password (string): Specifies the password.
        server_ip (string): Specifies the server ip.
        username (string): Specifies the username.
        virtual_host (string): Specifies the virtual host.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "certificate": 'certificate',
        "exchange": 'exchange',
        "filer_id": 'filerId',
        "password":'password',
        "server_ip":'serverIp',
        "username":'username',
        "virtual_host":'virtualHost'
    }

    def __init__(self,
                 certificate=None,
                 exchange=None,
                 filer_id=None,
                 password=None,
                 server_ip=None,
                 username=None,
                 virtual_host=None
                 ):
        """Constructor for the AMQPTargetConfig class"""

        # Initialize members of the class
        self.certificate = certificate
        self.exchange = exchange
        self.filer_id = filer_id
        self.password = password
        self.server_ip = server_ip
        self.username = username
        self.virtual_host = virtual_host

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
        certificate = dictionary.get('certificate')
        exchange = dictionary.get('exchange')
        filer_id = dictionary.get('filerId')
        password = dictionary.get('password')
        server_ip = dictionary.get('serverIp')
        username = dictionary.get('username')
        virtual_host = dictionary.get('virtualHost')

        # Return an object of this model
        return cls(certificate,
                   exchange,
                   filer_id,
                   password,
                   server_ip,
                   username,
                   virtual_host)


