# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.role import Role
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class RolesController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(RolesController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def delete_roles(self, body=None):
        """Does a DELETE request to /public/roles.

        Returns Success if all the specified Roles are deleted.

        Args:
            body (RoleDeleteParameters, optional): Request to delete one or
                more Roles.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_roles called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_roles.')
            _url_path = '/public/roles'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_roles.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_roles.')
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_roles')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_roles.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_roles(self, name=None, tenant_ids=None, all_under_hierarchy=None):
        """Does a GET request to /public/roles.

        If the 'name' parameter is not specified, all roles defined on the
        Cohesity Cluster are returned. In addition, information about each
        role
        is returned such as the name, description, assigned privileges, etc.
        If an exact role name (such as COHESITY_VIEWER) is specified in the
        'name' parameter, only information about that single role is
        returned.

        Args:
            name (string, optional): Specifies the name of the role.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            list of Role: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_roles called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_roles.')
            _url_path = '/public/roles'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'name': name,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_roles.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_roles.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_roles')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_roles.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Role.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_role(self, body=None):
        """Does a POST request to /public/roles.

        Returns the new custom role that was created.
        A custom role is a user-defined role that is created using the REST
        API,
        the Cohesity Cluster or the CLI.

        Args:
            body (RoleCreateParameters, optional): Request to create a new
                custom Role.

        Returns:
            Role: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_role called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_role.')
            _url_path = '/public/roles'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_role.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_role.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_role')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_role.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Role.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_role(self, name, body=None):
        """Does a PUT request to /public/roles/{name}.

        For example, you could update the privileges assigned to a Role.
        Returns the updated role.

        Args:
            name (string): Specifies the name of the role to update.
            body (RoleUpdateParameters, optional): Request to update a custom
                role.

        Returns:
            Role: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_role called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for update_role.')
            self.validate_parameters(name=name)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_role.')
            _url_path = '/public/roles/{name}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'name': name})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_role.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_role.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_role')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_role.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Role.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
