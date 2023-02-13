# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.group import Group
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class GroupsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(GroupsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def delete_groups(self, body=None):
        """Does a DELETE request to /public/groups.

        If the group on the Cohesity Cluster was added for an Active Directory
        user,
        the referenced principal group on the Active Directory domain is NOT
        deleted.
        Only the group on the Cohesity Cluster is deleted.
        Returns Success if the specified groups are deleted.

        Args:
            body (GroupDeleteParameters, optional): Request to delete one or
                more groups on the Cohesity Cluster.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_groups called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_groups.')
            _url_path = '/public/groups'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_groups.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_groups.')
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_groups')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_groups.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_groups(self,
                   name=None,
                   domain=None,
                   filter_by_owned_domains=None,
                   tenant_ids=None,
                   all_under_hierarchy=None):
        """Does a GET request to /public/groups.

        If no parameters are specified, all groups currently on the Cohesity
        Cluster
        are returned. Specifying parameters filters the results that are
        returned.

        Args:
            name (string, optional): Optionally specify a group name to filter
                by. All groups containing name will be returned.
            domain (string, optional): If no domain is specified, all groups
                on the Cohesity Cluster are searched. If a domain is
                specified, only groups on the Cohesity Cluster associated with
                that domain are searched.
            filter_by_owned_domains (bool, optional): If FilterByOwnedDomains
                is set to true, then the groups are filtered to show only the
                ones that are in the domains owned by the current tenant or
                user.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            list of Group: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_groups called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_groups.')
            _url_path = '/public/groups'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'name': name,
                'domain': domain,
                'filterByOwnedDomains': filter_by_owned_domains,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_groups.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_groups.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_groups')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_groups.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Group.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_group(self, body=None):
        """Does a POST request to /public/groups.

        If an Active Directory domain is specified, a new group is added to
        the
        Cohesity Cluster for the specified Active Directory group principal.
        If the LOCAL domain is specified, a new group is created directly in
        the default LOCAL domain on the Cohesity Cluster.
        Returns the created or added group.

        Args:
            body (GroupParameters, optional): Request to add or create a
                Group.

        Returns:
            Group: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_group called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_group.')
            _url_path = '/public/groups'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_group.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_group.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_group')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_group.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Group.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_group(self, body=None):
        """Does a PUT request to /public/groups.

        Returns the group that was updated on the Cohesity Cluster.

        Args:
            body (GroupParameters, optional): Request to update a group.

        Returns:
            Group: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_group called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_group.')
            _url_path = '/public/groups'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_group.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_group.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_group')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_group.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Group.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
