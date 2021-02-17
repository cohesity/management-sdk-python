# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.access_tokens_controller import AccessTokensController
from cohesity_management_sdk.models.access_token_credential import AccessTokenCredential


class AuthManager:

    @classmethod
    def apply(cls, http_request, Configuration):
        """ Add authentication to the request.
        Args:
            http_request (HttpRequest): The HttpRequest object to which
                authentication header will be added.
        """
        # If this is API Key based authentication, we add the apiKey header
        if Configuration.api_key is not None:
            http_request.headers['apikey'] = Configuration.api_key
            return
        cls.check_auth(Configuration)
        token = Configuration.auth_token.access_token
        token_type = Configuration.auth_token.token_type
        http_request.headers['Authorization'] = token_type+" "+token

    @classmethod
    def check_auth(cls, Configuration):
        """ Checks if access token is valid."""
        if not Configuration.auth_token:
            cls.authorize(Configuration)

    @classmethod
    def authorize(cls, Configuration):
        """ Authorizes the client.
        Returns:
            AccessToken: The access token.
        """

        body = AccessTokenCredential()
        body.username = Configuration.username
        body.password = Configuration.password
        if Configuration.domain is not None:
            body.domain = Configuration.domain

        auth_controller = AccessTokensController(Configuration)
        token = auth_controller.create_generate_access_token(body)
        Configuration.auth_token = token
        return token