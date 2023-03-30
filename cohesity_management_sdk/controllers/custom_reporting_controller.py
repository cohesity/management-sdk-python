# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.postgres_node_info import PostgresNodeInfo
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class CustomReportingController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(CustomReportingController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_postgres(self):
        """Does a GET request to /public/postgres.

        Returns the list of node information running postgres database.

        Returns:
            list of PostgresNodeInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_postgres called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_postgres.')
            _url_path = '/public/postgres'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_postgres.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_postgres.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_postgres')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_postgres.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              PostgresNodeInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
