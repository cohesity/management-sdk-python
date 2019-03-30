# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.user_preferences_proto_user_preferences_preference import UserPreferencesProtoUserPreferencesPreference
from cohesity_management_sdk.exceptions.error_error_exception import ErrorErrorException

class PreferencesController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(PreferencesController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_user_preferences(self):
        """Does a GET request to /public/sessionUser/preferences.

        List the preferences of the session user.

        Returns:
            list of UserPreferencesProtoUserPreferencesPreference: Response
                from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_user_preferences called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_user_preferences.')
            _url_path = '/public/sessionUser/preferences'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_user_preferences.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_user_preferences.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_user_preferences')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_user_preferences.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, UserPreferencesProtoUserPreferencesPreference.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update_user_preferences(self,
                                body=None):
        """Does a PUT request to /public/sessionUser/preferences.

        Returns the updated user preferences.

        Args:
            body (list of UserPreferencesProtoUserPreferencesPreference,
                optional): Request to create or update User Preferences

        Returns:
            list of UserPreferencesProtoUserPreferencesPreference: Response
                from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_user_preferences called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_user_preferences.')
            _url_path = '/public/sessionUser/preferences'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_user_preferences.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_user_preferences.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_user_preferences')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_user_preferences.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, UserPreferencesProtoUserPreferencesPreference.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
