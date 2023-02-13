# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.models.tags_operation_parameters import TagsOperationParameters
from cohesity_management_sdk.models.tags_operation_result import TagsOperationResult

class TagsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(TagsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config


    def apply_tags(self, body=None):
        """Does a PUT request to /public/tags/apply.

        Apply Tags on existing objects in the Cohesity Cluster.

        Args:
            body (TagsOperationParameters, optional): Request to add or update
            document tags.

        Returns:
            TagsOperationResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('apply_tags called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for apply_tags.')
            _url_path = '/public/tags/apply'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for apply_tags.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for apply_tags.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='apply_tags')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for apply_tags.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              TagsOperationResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def remove_tags(self, body=None):
        """Does a PUT request to /public/tags/remove.

        Remove Tags on existing objects in the Cohesity Cluster.

        Args:
            body (TagsOperationParameters, optional): Request to add or update
                document tags.

        Returns:
            TagsOperationResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('remove_tags called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for remove_tags.')
            _url_path = '/public/tags/remove'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for remove_tags.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for remove_tags.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='remove_tags')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for remove_tags.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              TagsOperationResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

