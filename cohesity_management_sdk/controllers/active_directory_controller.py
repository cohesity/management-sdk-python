# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.active_directory_entry import ActiveDirectoryEntry
from cohesity_management_sdk.models.list_centrify_zone import ListCentrifyZone
from cohesity_management_sdk.models.domain_controllers import DomainControllers
from cohesity_management_sdk.models.active_directory_principal import ActiveDirectoryPrincipal
from cohesity_management_sdk.models.added_active_directory_principal import AddedActiveDirectoryPrincipal
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class ActiveDirectoryController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(ActiveDirectoryController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def delete_active_directory_entry(self, body):
        """Does a DELETE request to /public/activeDirectory.

        Deletes the join of the Cohesity Cluster to the specified
        Active Directory domain. After the deletion, the Cohesity Cluster
        no longer has access to the principals on the Active Directory.
        For example, you can no longer log in to the Cohesity Cluster
        with a user defined in a principal group of the Active Directory
        domain.

        Args:
            body (ActiveDirectoryEntry): Request to delete a join with an
                Active Directory.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_active_directory_entry called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_active_directory_entry.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for delete_active_directory_entry.')
            _url_path = '/public/activeDirectory'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for delete_active_directory_entry.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_active_directory_entry.'
            )
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='delete_active_directory_entry')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for delete_active_directory_entry.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_active_directory_entry(self,
                                   domains=None,
                                   tenant_ids=None,
                                   all_under_hierarchy=None):
        """Does a GET request to /public/activeDirectory.

        After a Cohesity Cluster has been joined to an Active Directory
        domain,
        the users and groups in the domain can be authenticated on the
        Cohesity Cluster
        using their Active Directory credentials.
        NOTE: The userName and password fields are not populated by this
        operation.

        Args:
            domains (list of string, optional): Specifies the domains to fetch
                active directory entries.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            list of ActiveDirectoryEntry: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_active_directory_entry called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_active_directory_entry.')
            _url_path = '/public/activeDirectory'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'domains': domains,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_active_directory_entry.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_active_directory_entry.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_active_directory_entry')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_active_directory_entry.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ActiveDirectoryEntry.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_active_directory_entry(self, body):
        """Does a POST request to /public/activeDirectory.

        After a Cohesity Cluster has been joined to an Active Directory
        domain,
        the users and groups in the domain can be authenticated on the
        Cohesity Cluster
        using their Active Directory credentials.

        Args:
            body (CreateActiveDirectoryEntryParams): Request to join an Active
                Directory.

        Returns:
            ActiveDirectoryEntry: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_active_directory_entry called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_active_directory_entry.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_active_directory_entry.')
            _url_path = '/public/activeDirectory'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_active_directory_entry.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_active_directory_entry.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_active_directory_entry')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_active_directory_entry.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ActiveDirectoryEntry.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_centrify_zones(self, domain_name=None):
        """Does a GET request to /public/activeDirectory/centrifyZones.

        Fetches the list centrify zones of an active directory domain.

        Args:
            domain_name (string, optional): Specifies the fully qualified
                domain name (FQDN) of an Active Directory.

        Returns:
            list of ListCentrifyZone: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_centrify_zones called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for list_centrify_zones.')
            _url_path = '/public/activeDirectory/centrifyZones'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'domainName': domain_name}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_centrify_zones.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_centrify_zones.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='list_centrify_zones')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for list_centrify_zones.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ListCentrifyZone.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_active_directory_domain_controllers(self, domain_name=None):
        """Does a GET request to /public/activeDirectory/domainControllers.

        List the domain controllers for a domain.

        Args:
            domain_name (string, optional): Specifies the domain name

        Returns:
            DomainControllers: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_active_directory_domain_controllers called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_active_directory_domain_controllers.'
            )
            _url_path = '/public/activeDirectory/domainControllers'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'domainName': domain_name}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_active_directory_domain_controllers.'
            )
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_active_directory_domain_controllers.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_active_directory_domain_controllers')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_active_directory_domain_controllers.'
            )
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, DomainControllers.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def search_active_directory_principals(self,
                                           domain=None,
                                           object_class=None,
                                           search=None,
                                           sids=None,
                                           include_computers=None,
                                           include_service_accounts=None):
        """Does a GET request to /public/activeDirectory/principals.

        Optionally limit the search results by specifying security identifiers
        (SIDs),
        an object class (user or group) or a substring.
        You can specify SIDs or a substring but not both.

        Args:
            domain (string, optional): Specifies the domain name of the
                principals to search. If specified the principals in that
                domain are searched. Domain could be an Active Directory
                domain joined by the Cluster or any one of the trusted domains
                of the Active Directory domain or the LOCAL domain. If not
                specified, all the domains are searched.
            object_class (ObjectClassSearchActiveDirectoryPrincipalsEnum,
                optional): Optionally filter by a principal object class such
                as 'kGroup' or 'kUser'. If 'kGroup' is specified, only group
                principals are returned. If 'kUser' is specified, only user
                principals are returned. If not specified, both group and user
                principals are returned. 'kUser' specifies a user object
                class. 'kGroup' specifies a group object class. 'kComputer'
                specifies a computer object class. 'kWellKnownPrincipal'
                specifies a well known principal. 'kServiceAccount' specifies
                a service account object class.
            search (string, optional): Optionally filter by matching a
                substring. Only principals in the with a name or
                sAMAccountName that matches part or all of the specified
                substring are returned. If specified, a 'sids' parameter
                should not be specified.
            sids (list of string, optional): Optionally filter by a list of
                security identifiers (SIDs) found in the specified domain.
                Only principals matching the specified SIDs are returned. If
                specified, a 'search' parameter should not be specified.
            include_computers (bool, optional): Specifies if Computer/GMSA
                accounts need to be included in this search.
            include_service_accounts (bool, optional): Specifies if service
                accounts should be included in the search result.
                This field is true by default.

        Returns:
            list of ActiveDirectoryPrincipal: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('search_active_directory_principals called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for search_active_directory_principals.')
            _url_path = '/public/activeDirectory/principals'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'domain': domain,
                'objectClass': object_class,
                'search': search,
                'sids': sids,
                'includeComputers': include_computers,
                'includeServiceAccounts': include_service_accounts
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for search_active_directory_principals.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for search_active_directory_principals.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='search_active_directory_principals')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for search_active_directory_principals.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ActiveDirectoryPrincipal.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def add_active_directory_principals(self, body=None):
        """Does a POST request to /public/activeDirectory/principals.

        After a group or user has been added to a Cohesity Cluster,
        the referenced Active Directory principal can be used by the Cohesity
        Cluster.
        In addition, this operation maps Cohesity roles with a group or user
        and
        this mapping defines the privileges allowed on the Cohesity Cluster
        for the
        group or user.
        For example if an 'management' group is created on the Cohesity
        Cluster
        for the Active Directory 'management' principal group and is
        associated with the Cohesity 'View' role, all users in the
        referenced Active Directory 'management' principal group can log in to
        the
        Cohesity Dashboard but will only have view-only privileges.
        These users cannot create new Protection Jobs, Policies, Views, etc.
        NOTE: Local Cohesity users and groups cannot be created by this
        operation.
        Local Cohesity users or groups do not have an associated Active
        Directory
        principals and are created directly in the default LOCAL domain.

        Args:
            body (list of ActiveDirectoryPrincipalsAddParameters, optional):
                Request to add groups or users to the Cohesity Cluster.

        Returns:
            list of AddedActiveDirectoryPrincipal: Response from the API.
                Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('add_active_directory_principals called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for add_active_directory_principals.')
            _url_path = '/public/activeDirectory/principals'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for add_active_directory_principals.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for add_active_directory_principals.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='add_active_directory_principals')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for add_active_directory_principals.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                AddedActiveDirectoryPrincipal.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_enable_trusted_domain_discovery(self, body, name):
        """Does a POST request to /public/activeDirectory/{name}/enableTrustedDomainState.

        Updates the states of trusted domains discovery.

        Args:
            body (UpdateTrustedDomainEnableParams): Request to update enable
                trusted domains state of an Active Directory.
            name (string): Specifies the Active Directory Domain Name.

        Returns:
            ActiveDirectoryEntry: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_enable_trusted_domain_discovery called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_enable_trusted_domain_discovery.'
            )
            self.validate_parameters(body=body, name=name)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_enable_trusted_domain_discovery.'
            )
            _url_path = '/public/activeDirectory/{name}/enableTrustedDomainState'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'name': name})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_enable_trusted_domain_discovery.'
            )
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_enable_trusted_domain_discovery.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_enable_trusted_domain_discovery')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_enable_trusted_domain_discovery.'
            )
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ActiveDirectoryEntry.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_active_directory_id_mapping(self, body, name):
        """Does a PUT request to /public/activeDirectory/{name}/idMappingInfo.

        Updates the user id mapping info of an Active Directory.

        Args:
            body (IdMappingInfo): Request to update user id mapping of an
                Active Directory.
            name (string): Specifies the Active Directory Domain Name.

        Returns:
            ActiveDirectoryEntry: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_active_directory_id_mapping called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_active_directory_id_mapping.'
            )
            self.validate_parameters(body=body, name=name)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_active_directory_id_mapping.')
            _url_path = '/public/activeDirectory/{name}/idMappingInfo'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'name': name})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_active_directory_id_mapping.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_active_directory_id_mapping.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='update_active_directory_id_mapping')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_active_directory_id_mapping.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ActiveDirectoryEntry.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_active_directory_ignored_trusted_domains(self, body, name):
        """Does a PUT request to /public/activeDirectory/{name}/ignoredTrustedDomains.

        Updates the list of trusted domains to be ignored during trusted
        domain discovery of an Active Directory.

        Args:
            body (UpdateIgnoredTrustedDomainsParams): Request to update the
                list of ignored trusted domains of an AD.
            name (string): Specifies the Active Directory Domain Name.

        Returns:
            ActiveDirectoryEntry: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info(
                'update_active_directory_ignored_trusted_domains called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_active_directory_ignored_trusted_domains.'
            )
            self.validate_parameters(body=body, name=name)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_active_directory_ignored_trusted_domains.'
            )
            _url_path = '/public/activeDirectory/{name}/ignoredTrustedDomains'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'name': name})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_active_directory_ignored_trusted_domains.'
            )
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_active_directory_ignored_trusted_domains.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request,
                name='update_active_directory_ignored_trusted_domains')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_active_directory_ignored_trusted_domains.'
            )
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ActiveDirectoryEntry.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_active_directory_ldap_provider(self, body, name):
        """Does a PUT request to /public/activeDirectory/{name}/ldapProvider.

        Updates the LDAP provide Id for an Active Directory domain.

        Args:
            body (UpdateLdapProviderParams): Request to update the LDAP
                provider info.
            name (string): Specifies the Active Directory Domain Name.

        Returns:
            ActiveDirectoryEntry: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_active_directory_ldap_provider called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_active_directory_ldap_provider.'
            )
            self.validate_parameters(body=body, name=name)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_active_directory_ldap_provider.'
            )
            _url_path = '/public/activeDirectory/{name}/ldapProvider'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'name': name})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_active_directory_ldap_provider.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_active_directory_ldap_provider.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='update_active_directory_ldap_provider')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_active_directory_ldap_provider.'
            )
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ActiveDirectoryEntry.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_active_directory_machine_accounts(self, body, name):
        """Does a POST request to /public/activeDirectory/{name}/machineAccounts.

        Updates the machine accounts of an Active Directory.

        Args:
            body (UpdateMachineAccountsParams): Request to update machine
                accounts of an Active Directory.
            name (string): Specifies the Active Directory Domain Name.

        Returns:
            ActiveDirectoryEntry: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info(
                'update_active_directory_machine_accounts called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_active_directory_machine_accounts.'
            )
            self.validate_parameters(body=body, name=name)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_active_directory_machine_accounts.'
            )
            _url_path = '/public/activeDirectory/{name}/machineAccounts'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'name': name})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_active_directory_machine_accounts.'
            )
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_active_directory_machine_accounts.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='update_active_directory_machine_accounts')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_active_directory_machine_accounts.'
            )
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ActiveDirectoryEntry.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_preferred_domain_controllers(self, body, name):
        """Does a PUT request to /public/activeDirectory/{name}/preferredDomainControllers.

        Updates the preferred domain controllers of an Active Directory

        Args:
            body (list of PreferredDomainController): Request to update
                preferred domain controllers of an Active Directory.
            name (string): Specifies the Active Directory Domain Name.

        Returns:
            ActiveDirectoryEntry: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_preferred_domain_controllers called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_preferred_domain_controllers.'
            )
            self.validate_parameters(body=body, name=name)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_preferred_domain_controllers.')
            _url_path = '/public/activeDirectory/{name}/preferredDomainControllers'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'name': name})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_preferred_domain_controllers.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_preferred_domain_controllers.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='update_preferred_domain_controllers')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_preferred_domain_controllers.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ActiveDirectoryEntry.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
