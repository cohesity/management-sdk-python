# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.tenant import Tenant
from cohesity_management_sdk.models.tenant_active_directory_update import TenantActiveDirectoryUpdate
from cohesity_management_sdk.models.tenant_entity_update import TenantEntityUpdate
from cohesity_management_sdk.models.group import Group
from cohesity_management_sdk.models.tenant_ldap_provider_update import TenantLdapProviderUpdate
from cohesity_management_sdk.models.tenant_protection_policy_update import TenantProtectionPolicyUpdate
from cohesity_management_sdk.models.tenant_protection_job_update import TenantProtectionJobUpdate
from cohesity_management_sdk.models.tenant_proxy import TenantProxy
from cohesity_management_sdk.models.user import User
from cohesity_management_sdk.models.tenant_view_update import TenantViewUpdate
from cohesity_management_sdk.models.tenant_view_box_update import TenantViewBoxUpdate
from cohesity_management_sdk.models.tenant_vlan_update import TenantVlanUpdate
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class TenantController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(TenantController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def delete_tenant(self, body=None):
        """Does a DELETE request to /public/tenants.

        Returns success if the specified tenant is deleted.

        Args:
            body (TenantIdData, optional): TODO: type description here.
                Example:

        Returns:
            list of Tenant: Response from the API. Get Tenants Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_tenant called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_tenant.')
            _url_path = '/public/tenants'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_tenant.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_tenant.')
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_tenant')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_tenant.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Tenant.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_tenants(self,
                    ids=None,
                    properties=None,
                    hierarchy=None,
                    include_self=None,
                    skip_invalid_ids=None,
                    status=None):
        """Does a GET request to /public/tenants.

        Returns the list of tenants.

        Args:
            ids (list of string, optional): TODO: type description here.
                Example:
            properties (list of PropertyEnum, optional): 'ViewBox' indicates
                view box data for tenant. 'Vlan' indicates vlan data for
                tenant. 'ProtectionPolicy' indicates protection policy for
                tenant. 'ProtectionJob' indicates protection job for tenant.
                'Entity' indicates entity data for tenant. 'Views' indicates
                view data for tenant. 'ActiveDirectory' indicates active
                directory for tenant. 'LdapProvider' indicates ldap provider
                for tenant. 'SwiftConfig' indicates Swift configuration for
                tenant.
            hierarchy (bool, optional): TODO: type description here. Example:
                            include_self (bool, optional): TODO: type description here.
                Example:
            skip_invalid_ids (bool, optional): TODO: type description here.
                Example:
            status (list of StatusGetTenantsEnum, optional): Filter by tenant
                status.

        Returns:
            list of Tenant: Response from the API. Get Tenants Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_tenants called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_tenants.')
            _url_path = '/public/tenants'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'ids': ids,
                'properties': properties,
                'hierarchy': hierarchy,
                'includeSelf': include_self,
                'skipInvalidIds': skip_invalid_ids,
                'status': status
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_tenants.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_tenants.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_tenants')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_tenants.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Tenant.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_tenant(self, body=None):
        """Does a POST request to /public/tenants.

        A Vault can provide an additional Cloud Tier where cold data of the
        Cohesity Cluster is stored in the Cloud.
        A Vault can also provide archive storage for backup data.
        This archive data is stored on Tapes and in Cloud Vaults.

        Args:
            body (TenantCreateParameters, optional): Request to add or create
                a new tenant.

        Returns:
            Tenant: Response from the API. Create Tenants response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_tenant called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_tenant.')
            _url_path = '/public/tenants'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_tenant.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_tenant.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_tenant')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_tenant.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Tenant.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_tenant(self, body=None):
        """Does a PUT request to /public/tenants.

        Returns the tenant that was updated on the Cohesity Cluster.

        Args:
            body (TenantUpdate, optional): Request to update existing tenant.

        Returns:
            Tenant: Response from the API. Update Tenants Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_tenant called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_tenant.')
            _url_path = '/public/tenants'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_tenant.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_tenant.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_tenant')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_tenant.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Tenant.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_tenant_active_directory(self, body=None):
        """Does a PUT request to /public/tenants/activeDirectory.

        Returns success if the update for Active Directory is successful for
        specified
        tenant.

        Args:
            body (TenantActiveDirectoryUpdateParameters, optional): Request to
                update existing active directories.

        Returns:
            TenantActiveDirectoryUpdate: Response from the API. Tenant Active
                Directory Mapping Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_tenant_active_directory called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_tenant_active_directory.')
            _url_path = '/public/tenants/activeDirectory'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_tenant_active_directory.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_tenant_active_directory.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='update_tenant_active_directory')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_tenant_active_directory.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                TenantActiveDirectoryUpdate.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_tenant_entity(self, body=None):
        """Does a PUT request to /public/tenants/entity.

        Returns success if the update for entity permission data is successful
        for
        specified tenant.

        Args:
            body (TenantEntityUpdateParameters, optional): Request to
                associate entity for tenant.

        Returns:
            TenantEntityUpdate: Response from the API. Tenant Entity Update
                Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_tenant_entity called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_tenant_entity.')
            _url_path = '/public/tenants/entity'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_tenant_entity.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_tenant_entity.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_tenant_entity')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_tenant_entity.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, TenantEntityUpdate.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_tenant_groups(self, body=None):
        """Does a PUT request to /public/tenants/groups.

        Returns success if the update for groups is successful for specified
        tenant.

        Args:
            body (TenantGroupUpdateParameters, optional): Request to update
                existing tenant groups.

        Returns:
            list of Group: Response from the API. Tenant Group Mapping
                Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_tenant_groups called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_tenant_groups.')
            _url_path = '/public/tenants/groups'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_tenant_groups.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_tenant_groups.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_tenant_groups')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_tenant_groups.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Group.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_tenant_ldap_provider(self, body=None):
        """Does a PUT request to /public/tenants/ldapProvider.

        Returns success if the update for Ldap Providers is successful for
        specified
        tenant.

        Args:
            body (TenantLdapProviderUpdateParameters, optional): Request to
                update existing ldap providers.

        Returns:
            TenantLdapProviderUpdate: Response from the API. Tenant Ldap
                Provider Mapping Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_tenant_ldap_provider called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_tenant_ldap_provider.')
            _url_path = '/public/tenants/ldapProvider'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_tenant_ldap_provider.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_tenant_ldap_provider.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_tenant_ldap_provider')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_tenant_ldap_provider.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                TenantLdapProviderUpdate.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_tenant_protection_policy(self, body=None):
        """Does a PUT request to /public/tenants/policy.

        Returns success if the update for protection policy permission data
        is
        successful for the specified tenant.

        Args:
            body (TenantProtectionPolicyUpdateParameters, optional): Request
                to update existing protection policies.

        Returns:
            TenantProtectionPolicyUpdate: Response from the API. Tenant
                Protection Policy Mapping Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_tenant_protection_policy called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_tenant_protection_policy.')
            _url_path = '/public/tenants/policy'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_tenant_protection_policy.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_tenant_protection_policy.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='update_tenant_protection_policy')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_tenant_protection_policy.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                TenantProtectionPolicyUpdate.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_tenant_protection_job(self, body=None):
        """Does a PUT request to /public/tenants/protectionJob.

        Returns success if the update for protection job is successful for
        specified
        tenant.

        Args:
            body (TenantProtectionJobUpdateParameters, optional): Request to
                update existing protection jobs.

        Returns:
            TenantProtectionJobUpdate: Response from the API. Tenant
                Protection Job Mapping Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_tenant_protection_job called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_tenant_protection_job.')
            _url_path = '/public/tenants/protectionJob'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_tenant_protection_job.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_tenant_protection_job.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='update_tenant_protection_job')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_tenant_protection_job.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                TenantProtectionJobUpdate.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_tenants_proxies(self, ids=None):
        """Does a GET request to /public/tenants/proxies.

        Returns the list of proxies.

        Args:
            ids (list of string, optional): TODO: type description here.
                Example:

        Returns:
            list of TenantProxy: Response from the API. Get Tenants Proxies
                Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_tenants_proxies called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_tenants_proxies.')
            _url_path = '/public/tenants/proxies'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'ids': ids}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_tenants_proxies.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_tenants_proxies.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_tenants_proxies')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_tenants_proxies.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              TenantProxy.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise


    def get_download_tenants_proxy(self, id=None):
        """Does a GET request to /public/tenants/proxy/image.

        Returns the tenant proxy to be downloaded.

        Args:
            id (string, optional): Specifies the id of the tenant.

        Returns:
            list of int: Response from the API. Tenants Proxy Download
                Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_download_tenants_proxy called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_download_tenants_proxy.')
            _url_path = '/public/tenants/proxy/image'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'id': id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_download_tenants_proxy.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_download_tenants_proxy.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_download_tenants_proxy')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_download_tenants_proxy.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise


    def get_tenants_proxy_config(self,
                                 id=None,
                                 validate_only=None,
                                 connection_id=None):
        """Does a GET request to /public/tenants/proxy/config.

        Returns the config for tenants proxy.

        Args:
            id (string, optional): Specifies the id of the tenant.
            validate_only (bool, optional): Specifies whether to only validate
                the config request.
            connection_id (long|int, optional): Specifies the id of the
                connection.

        Returns:
            list of int: Response from the API. Get Tenants Proxy Config
                Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_tenants_proxy_config called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_tenants_proxy_config.')
            _url_path = '/public/tenants/proxy/config'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'id': id,
                'validateOnly': validate_only,
                'connectionId': connection_id
                }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_tenants_proxy_config.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_tenants_proxy_config.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_tenants_proxy_config')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_tenants_proxy_config.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_tenant_users(self, body=None):
        """Does a PUT request to /public/tenants/users.

        Returns success if the update for users data is successful for
        specified tenant.

        Args:
            body (TenantUserUpdateParameters, optional): Request to update
                existing users.

        Returns:
            list of User: Response from the API. Tenant Users Mapping
                Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_tenant_users called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_tenant_users.')
            _url_path = '/public/tenants/users'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_tenant_users.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_tenant_users.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_tenant_users')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_tenant_users.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              User.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_tenant_view(self, body=None):
        """Does a PUT request to /public/tenants/view.

        Returns success if the update for views permission data is successful
        for
        specified tenant.

        Args:
            body (TenantViewUpdateParameters, optional): Request to update
                existing views.

        Returns:
            TenantViewUpdate: Response from the API. Tenant View Mapping
                Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_tenant_view called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_tenant_view.')
            _url_path = '/public/tenants/view'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_tenant_view.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_tenant_view.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_tenant_view')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_tenant_view.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              TenantViewUpdate.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_tenant_view_box(self, body=None):
        """Does a PUT request to /public/tenants/viewBox.

        Returns success if the update for view box data is successful for
        specified
        tenant.

        Args:
            body (TenantViewBoxUpdateParameters, optional): Request to update
                existing tenant view box.

        Returns:
            TenantViewBoxUpdate: Response from the API. Tenant View Box Update
                Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_tenant_view_box called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_tenant_view_box.')
            _url_path = '/public/tenants/viewBox'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_tenant_view_box.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_tenant_view_box.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_tenant_view_box')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_tenant_view_box.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                TenantViewBoxUpdate.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_tenant_vlan(self, body=None):
        """Does a PUT request to /public/tenants/vlan.

        Returns success if the update for vlan data is successful for
        specified tenant.

        Args:
            body (TenantVlanUpdateParameters, optional): Request to update
                existing tenant vlan.

        Returns:
            TenantVlanUpdate: Response from the API. Tenant Vlan Update
                Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_tenant_vlan called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_tenant_vlan.')
            _url_path = '/public/tenants/vlan'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_tenant_vlan.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_tenant_vlan.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_tenant_vlan')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_tenant_vlan.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              TenantVlanUpdate.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
