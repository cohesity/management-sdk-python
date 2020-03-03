# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import logging
from cohesity_management_sdk.exceptions.api_exception import APIException
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.models.access_token import AccessToken
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class AccessTokensController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, client=None, call_back=None):
        super(AccessTokensController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def create_generate_access_token(self, body):
        """Does a POST request to /public/accessTokens.

        Before making other REST API requests, your REST client must make a
        'POST /public/accessToken' request with a valid Cohesity username and
        password. This POST request returns an access token and type
        in the response that is generated by the Cohesity Cluster.
        Subsequent requests to other Cohesity REST API operations must
        specify the returned access token and type by setting 'Authorization'
        in the http header in the following format:
        Authorization: token_type access_token
        The generated token is valid for 24 hours. If a request is made with
        an expired token, the 'Token expired' error message is returned.
        Add code to your REST client to check for this error and request
        another access token before reissuing the request.

        Args:
            body (AccessTokenCredential): Request to generate access token.

        Returns:
            AccessToken: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_generate_access_token called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_generate_access_token.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_generate_access_token.')
            _url_path = '/public/accessTokens'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_generate_access_token.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_generate_access_token.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            _context = self.execute_request(
                _request, name='create_generate_access_token')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_generate_access_token.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              AccessToken.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise APIException("error", _context)
