# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.smb_active_file_opens_response import SmbActiveFileOpensResponse
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class SMBFileOpensController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(SMBFileOpensController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_smb_file_opens(self,
                           file_path=None,
                           view_name=None,
                           page_count=None,
                           cookie=None):
        """Does a GET request to /public/smbFileOpens.

        If no parameters are specified, all active SMB file opens currently on
        the
        Cohesity Cluster are returned. Specifying parameters filters the
        results that
        are returned.

        Args:
            file_path (string, optional): Specifies the filepath in the view
                relative to the root filesystem. If this field is specified,
                viewName field must also be specified.
            view_name (string, optional): Specifies the name of the View in
                which to search. If a view name is not specified, all the
                views in the Cluster is searched. This field is mandatory if
                filePath field is specified.
            page_count (int, optional): Specifies the maximum number of active
                opens to return in the response. This field cannot be set
                above 1000. If this is not set, maximum of 1000 entries are
                returned.
            cookie (string, optional): Specifies the opaque string returned in
                the previous response. If this is set, next set of active
                opens just after the previous response are returned. If this
                is not set, first set of active opens are returned.

        Returns:
            SmbActiveFileOpensResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_smb_file_opens called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_smb_file_opens.')
            _url_path = '/public/smbFileOpens'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'filePath': file_path,
                'viewName': view_name,
                'pageCount': page_count,
                'cookie': cookie
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_smb_file_opens.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_smb_file_opens.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_smb_file_opens')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_smb_file_opens.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                SmbActiveFileOpensResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_close_smb_file_open(self, body):
        """Does a POST request to /public/smbFileOpens.

        Returns nothing upon success.

        Args:
            body (CloseSmbFileOpenParameters): Request to close an active SMB
                file open.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_close_smb_file_open called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_close_smb_file_open.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_close_smb_file_open.')
            _url_path = '/public/smbFileOpens'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_close_smb_file_open.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_close_smb_file_open.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_close_smb_file_open')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_close_smb_file_open.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
