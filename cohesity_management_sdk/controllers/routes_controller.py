# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.route import Route
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class RoutesController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(RoutesController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def delete_route(self, body=None):
        """Does a DELETE request to /public/routes.

        Returns the delete status upon completion.

        Args:
            body (DeleteRouteParam, optional): TODO: type description here.
                Example:

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_route called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_route.')
            _url_path = '/public/routes'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_route.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_route.')
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_route')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_route.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_routes(self):
        """Does a GET request to /public/routes.

        Returns the Static Routes for the Cohesity Cluster.

        Returns:
            list of Route: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_routes called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_routes.')
            _url_path = '/public/routes'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_routes.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_routes.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_routes')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_routes.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Route.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def add_route(self, body=None):
        """Does a POST request to /public/routes.

        Returns the create status upon completion.

        Args:
            body (Route, optional): TODO: type description here. Example:

        Returns:
            Route: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('add_route called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for add_route.')
            _url_path = '/public/routes'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for add_route.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for add_route.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='add_route')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for add_route.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Route.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
