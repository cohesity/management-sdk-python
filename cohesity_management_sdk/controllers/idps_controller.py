# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.added_idp_principal import AddedIdpPrincipal
from cohesity_management_sdk.models.idp_service_configuration import IdpServiceConfiguration
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class IdpsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(IdpsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def add_active_idp_principals(self):
        """Does a POST request to /public/idps/principals.

        After a group or user has been added to a Cohesity Cluster,
        the referenced Idp principal can be used by the Cohesity Cluster.
        In addition, this operation maps Cohesity roles with a group or user
        and
        this mapping defines the privileges allowed on the Cohesity Cluster
        for the
        group or user.
        For example if an 'management' group is created on the Cohesity
        Cluster
        for the Idp 'management' principal group and is associated with the
        Cohesity 'View' role, all users in the referenced Idp
        'management' principal group can log in to the Cohesity Dashboard but
        will only have view-only privileges. These users cannot create new
        Protection Jobs, Policies, Views, etc.
        NOTE: Local Cohesity users and groups cannot be created by this
        operation.
        Local Cohesity users or groups do not have an associated Idp
        principals and are created directly in the default LOCAL domain.

        Returns:
            list of AddedIdpPrincipal: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('add_active_idp_principals called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for add_active_idp_principals.')
            _url_path = '/public/idps/principals'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for add_active_idp_principals.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for add_active_idp_principals.'
            )
            _request = self.http_client.post(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='add_active_idp_principals')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for add_active_idp_principals.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, AddedIdpPrincipal.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_idps(self,
                 tenant_ids=None,
                 all_under_hierarchy=None,
                 names=None,
                 ids=None,
                 domains=None):
        """Does a GET request to /public/idps.

        Returns the Idps configured on the Cohesity Cluster corresponding to
        the filter
        parameters. If no filter is given, all Idp configurations are
        returned.

        Args:
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.
            names (list of string, optional): Specifies the names of the IdP
                vendors like Okta. If specified, returns IdP configurations of
                the vendors matching the names in the parameters.
            ids (list of long|int, optional): Specifies the Ids of the IdP
                configuration. If specified, returns IdP configurations of the
                matching Ids in the IdP configuration.
            domains (list of string, optional): Specifies the domains of the
                IdP configurations. If specified, returns IdP configurations
                matching the domains in the parameters.

        Returns:
            list of IdpServiceConfiguration: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_idps called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_idps.')
            _url_path = '/public/idps'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy,
                'names': names,
                'ids': ids,
                'domains': domains
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_idps.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_idps.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_idps')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_idps.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                IdpServiceConfiguration.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_idp(self, body=None):
        """Does a POST request to /public/idps.

        Returns the newly created IdP configuration.

        Args:
            body (CreateIdpConfigurationRequest, optional): Request to create
                a new IdP Configuration.

        Returns:
            IdpServiceConfiguration: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_idp called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_idp.')
            _url_path = '/public/idps'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_idp.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_idp.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_idp')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_idp.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                IdpServiceConfiguration.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_idp_login(self, tenant_id=None):
        """Does a GET request to /public/idps/login.

        Redirects the client to the IdP site with the URI to login.

        Args:
            tenant_id (string, optional): Specifies an optional tenantId for
                which the SSO login should be done. If this is not specified,
                Cluster SSO login is done.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_idp_login called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_idp_login.')
            _url_path = '/public/idps/login'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'tenantId': tenant_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_idp_login.')
            _request = self.http_client.get(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_idp_login')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_idp_login.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_idp(self, id):
        """Does a DELETE request to /public/idps/{id}.

        Returns Success if the IdP configuration is deleted.

        Args:
            id (long|int): Specifies the Id assigned for the IdP Service by
                the Cluster.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_idp called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for delete_idp.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_idp.')
            _url_path = '/public/idps/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info('Preparing and executing request for delete_idp.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_idp')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_idp.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_idp(self, id, body=None):
        """Does a PUT request to /public/idps/{id}.

        Returns the updated IdP configuration.

        Args:
            id (long|int): Specifies the Id assigned for the IdP Service by
                the Cluster.
            body (UpdateIdpConfigurationRequest, optional): Request to update
                an Idp Configuration.

        Returns:
            IdpServiceConfiguration: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_idp called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for update_idp.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_idp.')
            _url_path = '/public/idps/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_idp.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_idp.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_idp')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_idp.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                IdpServiceConfiguration.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
