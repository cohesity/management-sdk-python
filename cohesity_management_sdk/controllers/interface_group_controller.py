# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.interface_group import InterfaceGroup
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class InterfaceGroupController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(InterfaceGroupController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_interface_groups(self):
        """Does a GET request to /public/interfaceGroups.

        Returns the interface groups for the Cohesity Cluster.

        Returns:
            list of InterfaceGroup: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_interface_groups called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_interface_groups.')
            _url_path = '/public/interfaceGroups'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_interface_groups.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_interface_groups.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_interface_groups')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_interface_groups.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              InterfaceGroup.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_interface_group(self, body=None):
        """Does a POST request to /public/interfaceGroups.

        Returns the create status upon completion.

        Args:
            body (InterfaceGroup, optional): TODO: type description here.
                Example:

        Returns:
            InterfaceGroup: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_interface_group called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_interface_group.')
            _url_path = '/public/interfaceGroups'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_interface_group.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_interface_group.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_interface_group')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_interface_group.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              InterfaceGroup.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_interface_group(self, body=None):
        """Does a PUT request to /public/interfaceGroups.

        Returns the update status upon completion.

        Args:
            body (InterfaceGroup, optional): TODO: type description here.
                Example:

        Returns:
            InterfaceGroup: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_interface_group called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_interface_group.')
            _url_path = '/public/interfaceGroups'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_interface_group.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_interface_group.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_interface_group')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_interface_group.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              InterfaceGroup.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_interface_group(self, name):
        """Does a DELETE request to /public/interfaceGroups/{name}.

        Returns the delete status upon completion.

        Args:
            name (string): Request to delete one interface group.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_interface_group called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_interface_group.')
            self.validate_parameters(name=name)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_interface_group.')
            _url_path = '/public/interfaceGroups/{name}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'name': name})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_interface_group.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='delete_interface_group')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_interface_group.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
