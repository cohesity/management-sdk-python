# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.create_bond_result import CreateBondResult
from cohesity_management_sdk.models.host_result import HostResult
from cohesity_management_sdk.models.host_entry import HostEntry
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class NetworkController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(NetworkController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def create_bond(self, body):
        """Does a POST request to /public/network/bonds.

        Sends a request to create a new network bond on the Cluster. This can
        only be
        performed on a Node before it is part of a Cluster.

        Args:
            body (CreateBondParameters): TODO: type description here. Example:

        Returns:
            CreateBondResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_bond called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_bond.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_bond.')
            _url_path = '/public/network/bonds'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_bond.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_bond.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_bond')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_bond.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              CreateBondResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_bond(self, name):
        """Does a DELETE request to /public/network/bonds/{name}.

        Sends a request to delete a network bond from the Cluster. This can
        only be
        performed on a Node before it is part of a Cluster.

        Args:
            name (string): Specifies the name of the bond being deleted.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_bond called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for delete_bond.')
            self.validate_parameters(name=name)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_bond.')
            _url_path = '/public/network/bonds/{name}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'name': name})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_bond.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_bond')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_bond.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_hosts(self, ips):
        """Does a DELETE request to /public/network/hosts.

        Sends a request to remove one or more entries from the Cluster's
        etc/hosts file.

        Args:
            ips (list of string): Specifies a list of the IP addresses of
                entries to remove from the Cluster's /etc/hosts file.

        Returns:
            HostResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_hosts called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_hosts.')
            self.validate_parameters(ips=ips)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_hosts.')
            _url_path = '/public/network/hosts'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'ips': ips}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_hosts.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_hosts.')
            _request = self.http_client.delete(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_hosts')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_hosts.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              HostResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_hosts(self):
        """Does a GET request to /public/network/hosts.

        Sends a request to get a list of the current entries in the hosts
        file
        on the Cluster.

        Returns:
            list of HostEntry: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_hosts called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for list_hosts.')
            _url_path = '/public/network/hosts'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_hosts.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info('Preparing and executing request for list_hosts.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='list_hosts')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for list_hosts.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              HostEntry.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_append_hosts(self, body):
        """Does a POST request to /public/network/hosts.

        Sends a request to add one or more new entries to the Cluster's
        /etc/hosts
        file.

        Args:
            body (AppendHostsParameters): TODO: type description here.
                Example:

        Returns:
            HostResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_append_hosts called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_append_hosts.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_append_hosts.')
            _url_path = '/public/network/hosts'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_append_hosts.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_append_hosts.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_append_hosts')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_append_hosts.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              HostResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_edit_hosts(self, body):
        """Does a PUT request to /public/network/hosts.

        Sends a request to edit one or more entries in the Cluster's
        /etc/hosts file.

        Args:
            body (EditHostsParameters): TODO: type description here. Example:

        Returns:
            HostResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_edit_hosts called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_edit_hosts.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_edit_hosts.')
            _url_path = '/public/network/hosts'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_edit_hosts.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_edit_hosts.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_edit_hosts')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_edit_hosts.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              HostResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

