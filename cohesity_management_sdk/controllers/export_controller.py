# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.exceptions.error_error_exception import ErrorErrorException

class ExportController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(ExportController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def create_export_config(self,
                             body):
        """Does a POST request to /public/export/config.

        Export metadata into Json files

        Args:
            body (ExportParameters): Request to open an exported config file
                to prepare for importing.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_export_config called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_export_config.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_export_config.')
            _url_path = '/public/export/config'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_export_config.')
            _headers = {
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_export_config.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_export_config')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_export_config.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
