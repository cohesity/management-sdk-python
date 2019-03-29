# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.vlan import VLAN
from cohesity_management_sdk.exceptions.error_error_exception import ErrorErrorException
from cohesity_management_sdk.exceptions.api_exception import APIException

class VlanController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(VlanController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def update_vlan(self,
                    id,
                    body=None):
        """Does a PUT request to /public/vlans/{id}.

        Returns the created or updated VLAN on the Cohesity Cluster.

        Args:
            id (int): Specifies the id of the VLAN.
            body (VLAN, optional): TODO: type description here. Example:

        Returns:
            VLAN: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_vlan called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for update_vlan.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_vlan.')
            _url_path = '/public/vlans/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'id': id
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_vlan.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_vlan.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_vlan')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_vlan.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, VLAN.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def remove_vlan(self,
                    id):
        """Does a DELETE request to /public/vlans/{id}.

        Returns the delete status upon completion.

        Args:
            id (int): Specifies the id of the VLAN.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('remove_vlan called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for remove_vlan.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for remove_vlan.')
            _url_path = '/public/vlans/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'id': id
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info('Preparing and executing request for remove_vlan.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'remove_vlan')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for remove_vlan.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_vlans(self,
                  all_under_hierarchy=None,
                  tenant_ids=None):
        """Does a GET request to /public/vlans.

        Returns the VLANs for the Cohesity Cluster.

        Args:
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.

        Returns:
            list of VLAN: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_vlans called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_vlans.')
            _url_path = '/public/vlans'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'allUnderHierarchy': all_under_hierarchy,
                'tenantIds': tenant_ids
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_vlans.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_vlans.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_vlans')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_vlans.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, VLAN.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_vlan(self):
        """Does a POST request to /public/vlans.

        Returns the created VLAN on the Cohesity Cluster.

        Returns:
            VLAN: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_vlan called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_vlan.')
            _url_path = '/public/vlans'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_vlan.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_vlan.')
            _request = self.http_client.post(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_vlan')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_vlan.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, VLAN.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_vlan_by_id(self,
                       id):
        """Does a GET request to /public/vlans/{id}.

        Returns the VLAN corresponding to the specified VLAN ID or a
        specified
        InterfaceName.<VLAN ID>.
        Example 1: /public/vlans/10
        Example 2: /public/vlans/bond0.20
        Example 3: /public/vlans/bond1.20

        Args:
            id (int): Specifies the id of the VLAN.

        Returns:
            VLAN: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_vlan_by_id called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for get_vlan_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_vlan_by_id.')
            _url_path = '/public/vlans/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'id': id
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_vlan_by_id.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_vlan_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_vlan_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_vlan_by_id.')
            if _context.response.status_code == 404:
                raise APIException('Not Found', _context)
            elif (_context.response.status_code < 200) or (_context.response.status_code > 208):
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, VLAN.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
