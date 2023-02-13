# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.ldap_provider_response import LdapProviderResponse
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class LdapProviderController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(LdapProviderController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_ldap_provider(self,
                          ids=None,
                          tenant_ids=None,
                          all_under_hierarchy=None):
        """Does a GET request to /public/ldapProvider.

        Lists the LDAP providers.

        Args:
            ids (list of long|int, optional): Specifies the ids of the LDAP
                providers to fetch.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            list of LdapProviderResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_ldap_provider called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_ldap_provider.')
            _url_path = '/public/ldapProvider'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'ids': ids,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_ldap_provider.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_ldap_provider.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_ldap_provider')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_ldap_provider.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                LdapProviderResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_ldap_provider(self, body):
        """Does a POST request to /public/ldapProvider.

        Returns the created LDAP provider.

        Args:
            body (LdapProvider): Request to configure a LDAP provider.

        Returns:
            LdapProviderResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_ldap_provider called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_ldap_provider.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_ldap_provider.')
            _url_path = '/public/ldapProvider'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_ldap_provider.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_ldap_provider.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_ldap_provider')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_ldap_provider.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                LdapProviderResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_ldap_provider(self, body):
        """Does a PUT request to /public/ldapProvider.

        Returns the updated LDAP provider.

        Args:
            body (UpdateLdapProviderParam): Request to update a LDAP
                provider.

        Returns:
            LdapProviderResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_ldap_provider called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_ldap_provider.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_ldap_provider.')
            _url_path = '/public/ldapProvider'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_ldap_provider.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_ldap_provider.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_ldap_provider')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_ldap_provider.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                LdapProviderResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_ldap_provider(self, id):
        """Does a DELETE request to /public/ldapProvider/{id}.

        Delete an LDAP provider.

        Args:
            id (long|int): Specifies the LDAP Id.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_ldap_provider called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_ldap_provider.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_ldap_provider.')
            _url_path = '/public/ldapProvider/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_ldap_provider.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='delete_ldap_provider')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_ldap_provider.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_ldap_provider_status(self, id):
        """Does a GET request to /public/ldapProvider/{id}/status.

        Get the connection status of an LDAP provider.

        Args:
            id (long|int): Specifies the LDAP Id.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_ldap_provider_status called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_ldap_provider_status.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_ldap_provider_status.')
            _url_path = '/public/ldapProvider/{id}/status'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_ldap_provider_status.'
            )
            _request = self.http_client.get(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_ldap_provider_status')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_ldap_provider_status.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
