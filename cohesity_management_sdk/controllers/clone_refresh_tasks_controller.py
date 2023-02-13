# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.restore_task_wrapper import RestoreTaskWrapper
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class CloneRefreshTasksController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(CloneRefreshTasksController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def create_clone_refresh_task(self, body):
        """Does a POST request to /public/restore/applicationsClone/refresh.

        Returns the created Clone Refresh Task which refreshes the clone with
        specified
        data.

        Args:
            body (CloneRefreshRequest): Request to create a Clone Refresh
                Task.

        Returns:
            RestoreTaskWrapper: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_clone_refresh_task called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_clone_refresh_task.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_clone_refresh_task.')
            _url_path = '/public/restore/applicationsClone/refresh'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_clone_refresh_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_clone_refresh_task.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_clone_refresh_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_clone_refresh_task.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, RestoreTaskWrapper.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
