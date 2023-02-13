# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.notifications import Notifications
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class NotificationsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(NotificationsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_notifications(self):
        """Does a GET request to /public/sessionUser/notifications.

        List the notification of the session user.

        Returns:
            Notifications: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_notifications called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_notifications.')
            _url_path = '/public/sessionUser/notifications'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_notifications.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_notifications.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_notifications')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_notifications.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Notifications.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_notifications(self, body):
        """Does a PATCH request to /public/sessionUser/notifications.

        Returns success or failure.

        Args:
            body (UpdateNotifications): Specifies the list of notificationIds
                and the operation to be performed.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_notifications called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_notifications.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_notifications.')
            _url_path = '/public/sessionUser/notifications'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_notifications.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_notifications.')
            _request = self.http_client.patch(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_notifications')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_notifications.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
