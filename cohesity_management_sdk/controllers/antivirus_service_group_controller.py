# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.antivirus_service_group import AntivirusServiceGroup
from cohesity_management_sdk.models.antivirus_service_group_state_params import AntivirusServiceGroupStateParams
from cohesity_management_sdk.models.icap_connection_status_response import IcapConnectionStatusResponse
from cohesity_management_sdk.models.delete_infected_file_response import DeleteInfectedFileResponse
from cohesity_management_sdk.models.infected_files import InfectedFiles
from cohesity_management_sdk.models.update_infected_file_response import UpdateInfectedFileResponse
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class AntivirusServiceGroupController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(AntivirusServiceGroupController,
              self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_antivirus_service_group(self):
        """Does a GET request to /public/antivirusGroups.

        Returns all the antivirus service group.

        Returns:
            list of AntivirusServiceGroup: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_antivirus_service_group called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_antivirus_service_group.')
            _url_path = '/public/antivirusGroups'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_antivirus_service_group.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_antivirus_service_group.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_antivirus_service_group')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_antivirus_service_group.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                AntivirusServiceGroup.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_antivirus_service_group(self, body):
        """Does a POST request to /public/antivirusGroups.

        Returns the created Antivirus service group.

        Args:
            body (AntivirusServiceGroupParams): Request to create an Antivirus
                Service Group.

        Returns:
            AntivirusServiceGroup: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_antivirus_service_group called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_antivirus_service_group.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_antivirus_service_group.')
            _url_path = '/public/antivirusGroups'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_antivirus_service_group.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_antivirus_service_group.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_antivirus_service_group')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_antivirus_service_group.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                AntivirusServiceGroup.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_antivirus_service_group(self, body):
        """Does a PUT request to /public/antivirusGroups.

        Returns the updated antivirus service group.

        Args:
            body (UpdateAntivirusServiceGroupParams): Request to update an
                Antivirus Service Group.

        Returns:
            AntivirusServiceGroup: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_antivirus_service_group called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_antivirus_service_group.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_antivirus_service_group.')
            _url_path = '/public/antivirusGroups'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_antivirus_service_group.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_antivirus_service_group.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='update_antivirus_service_group')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_antivirus_service_group.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                AntivirusServiceGroup.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_antivirus_service_group_state(self, body=None):
        """Does a PUT request to /public/antivirusGroups/states.

        Returns the state of an antivirus service group upon completion.

        Args:
            body (AntivirusServiceGroupStateParams, optional): TODO: type
                description here. Example:

        Returns:
            AntivirusServiceGroupStateParams: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_antivirus_service_group_state called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_antivirus_service_group_state.'
            )
            _url_path = '/public/antivirusGroups/states'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_antivirus_service_group_state.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_antivirus_service_group_state.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='update_antivirus_service_group_state')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_antivirus_service_group_state.'
            )
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                AntivirusServiceGroupStateParams.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_antivirus_service_group(self, id):
        """Does a DELETE request to /public/antivirusGroups/{id}.

        Returns delete status upon completion.

        Args:
            id (long|int): Specifies the AntivirusServiceGroup Id.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_antivirus_service_group called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_antivirus_service_group.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for delete_antivirus_service_group.')
            _url_path = '/public/antivirusGroups/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_antivirus_service_group.'
            )
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='delete_antivirus_service_group')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for delete_antivirus_service_group.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_icap_connection_status(self, icap_uris=None):
        """Does a GET request to /public/icapConnectionStatus.

        Returns the list of succeeded and failed connection statuses of Icap
        servers.

        Args:
            icap_uris (list of string, optional): Specifies the list of icap
                uri.

        Returns:
            IcapConnectionStatusResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_icap_connection_status called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_icap_connection_status.')
            _url_path = '/public/icapConnectionStatus'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'icapUris': icap_uris}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_icap_connection_status.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_icap_connection_status.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_icap_connection_status')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_icap_connection_status.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                IcapConnectionStatusResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_infected_files(self, body):
        """Does a DELETE request to /public/infectedFiles.

        Returns the list of delete succeeded and delete failed infected
        files.

        Args:
            body (DeleteInfectedFileParams): Request to delete the list of
                infected files.

        Returns:
            DeleteInfectedFileResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_infected_files called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_infected_files.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_infected_files.')
            _url_path = '/public/infectedFiles'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_infected_files.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_infected_files.')
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='delete_infected_files')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_infected_files.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                DeleteInfectedFileResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_infected_files(self,
                           view_names=None,
                           include_quarantined_files=None,
                           include_unquarantined_files=None,
                           file_path=None,
                           page_count=None,
                           pagination_cookie=None):
        """Does a GET request to /public/infectedFiles.

        Returns all the infected files matching with query parameters.

        Args:
            view_names (list of string, optional): Filter by a list of View
                names.
            include_quarantined_files (bool, optional): Specifies whether to
                include quarantined files in the result.
            include_unquarantined_files (bool, optional): Specifies whether to
                include unquarantined files in the result.
            file_path (string, optional): Specifies the path of a file. If
                this is provided, infected file list would contain the scan
                and infection state of the file and pagination cookie will be
                ignored.
            page_count (long|int, optional): Specifies the number of items to
                return in the response for pagination purposes. Default value
                is 1000.
            pagination_cookie (string, optional): Pagination cookie should be
                used from previous call to list infected files. It resumes (or
                gives the next set of values) from the result of the previous
                call.

        Returns:
            InfectedFiles: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_infected_files called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_infected_files.')
            _url_path = '/public/infectedFiles'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'viewNames': view_names,
                'includeQuarantinedFiles': include_quarantined_files,
                'includeUnquarantinedFiles': include_unquarantined_files,
                'filePath': file_path,
                'pageCount': page_count,
                'paginationCookie': pagination_cookie
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_infected_files.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_infected_files.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_infected_files')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_infected_files.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              InfectedFiles.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_infected_files(self, body):
        """Does a PUT request to /public/infectedFiles.

        Returns the list of update succeeded and update failed infected
        files.

        Args:
            body (UpdateInfectedFileParams): Request to update the list of
                infected files.

        Returns:
            UpdateInfectedFileResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_infected_files called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_infected_files.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_infected_files.')
            _url_path = '/public/infectedFiles'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_infected_files.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_infected_files.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_infected_files')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_infected_files.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                UpdateInfectedFileResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
