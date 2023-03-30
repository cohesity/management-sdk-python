# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import sys
import logging

from cohesity_management_sdk.api_helper import APIHelper
#CohesityPatch
logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)


class Configuration(object):

    """A class used for configuring the SDK by a user.
    This class need not be instantiated and all properties and methods
    are accessible without instance creation.
    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "csv"

    # True if the client should skip verification of SSL certificates
    skip_ssl_verification = True

    # Set the global timeout value for http requests inside the SDK.
    http_request_timeout = 60
    
    # An enum for SDK environments
    class Environment(object):
        PRODUCTION = 0

    # An enum for API servers
    class Server(object):
        DEFAULT_HOST = 0

    # The environment in which the SDK is running
    environment = Environment.PRODUCTION

    # TODO: Set an appropriate value
    cluster_vip = 'prod-cluster.eng.cohesity.com'

    # Specifies the login name of the Cohesity user.
    # TODO: Set an appropriate value
    username = None

    # Specifies the password of the Cohesity user account.
    # TODO: Set an appropriate value
    password = None

    # Specifies the domain the user is logging in to. For a Local user model,
    # the domain is always LOCAL. For LDAP / AD user models, the domain will
    # map to an LDAP connection string. A user is uniquely identified by a
    # combination of username and domain. If this is not set, LOCAL is
    # assumed.
    # TODO: Set an appropriate value
    domain = None


    # AccessToken object, containing the fields access_token, privileges and token_type
    auth_token = None

    # API Key patch
    api_key = None

    # Session-Id.
    session_id = None

    # Open Id token.
    open_id_token = None

    # Optional: OTP support
    otp_type = None
    otp_code = None

    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.DEFAULT_HOST: 'https://{cluster_vip}/irisservices/api/v1',
        },
    }

    def get_base_uri(self, server=Server.DEFAULT_HOST):
        """Generates the appropriate base URI for the environment and the server.
        Args:
            server (Configuration.Server): The server enum for which the base URI is required.
        Returns:
            String: The base URI.
        """
        parameters = {
            "cluster_vip": self.cluster_vip,
        }
        return APIHelper.append_url_with_template_parameters(
            self.environments[self.environment][server], parameters, False)

    @classmethod
    def disable_logging(cls):
        """Disable all logging in the SDK
        """
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    @classmethod
    def enable_logging(cls, filename=None, filemode='a',
                       stream=sys.stdout, level=logging.INFO):
        """Enable logging in the SDK
        Args:
            filename: Specifies that a FileHandler be created, using the specified
                filename, rather than a StreamHandler.
            filemode: If filename is specified, open the file in this mode.
                Defaults to 'a'.
            stream: Use the specified stream to initialize the StreamHandler.
            level: Set the root logger level to the specified level.
        """

        cls.disable_logging()   # clear previously set logging info

        if filename is None:
            logging.basicConfig(stream=stream, level=level)
        else:
            logging.basicConfig(filename=filename, filemode=filemode,
                                level=level)
