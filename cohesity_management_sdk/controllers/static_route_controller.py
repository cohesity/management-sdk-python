# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.static_route import StaticRoute
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException

class StaticRouteController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(StaticRouteController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_static_routes(self):
        """Does a GET request to /public/staticRoutes.

        Returns the Static Routes for the Cohesity Cluster.

        Returns:
            list of StaticRoute: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_static_routes called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_static_routes.')
            _url_path = '/public/staticRoutes'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_static_routes.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_static_routes.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_static_routes')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_static_routes.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, StaticRoute.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def remove_static_route(self,
                            ip):
        """Does a DELETE request to /public/staticRoutes/{ip}.

        Returns the delete status upon completion.

        Args:
            ip (string): Specifies the subnet IP of the route destination
                network.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('remove_static_route called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for remove_static_route.')
            self.validate_parameters(ip=ip)

            # Prepare query URL
            self.logger.info('Preparing query URL for remove_static_route.')
            _url_path = '/public/staticRoutes/{ip}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'ip': ip
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info('Preparing and executing request for remove_static_route.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'remove_static_route')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for remove_static_route.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update_static_route(self,
                            ip,
                            body=None):
        """Does a PUT request to /public/staticRoutes/{ip}.

        Returns the created or updated Static Route on the Cohesity Cluster.

        Args:
            ip (string): Specifies the subnet IP of the route destination
                network.
            body (StaticRoute, optional): TODO: type description here.
                Example:

        Returns:
            StaticRoute: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_static_route called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for update_static_route.')
            self.validate_parameters(ip=ip)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_static_route.')
            _url_path = '/public/staticRoutes/{ip}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'ip': ip
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_static_route.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_static_route.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_static_route')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_static_route.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, StaticRoute.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
