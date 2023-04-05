# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.app import App
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class AppController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(AppController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_apps(self):
        """Does a GET request to /public/apps.

        Api provides the list of the apps which are available for the user to
        install or are already installed. App object provides basic app
        information along with app metadata.

        Returns:
            App: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_apps called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_apps.')
            _url_path = '/public/apps'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_apps.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_apps.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_apps')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_apps.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              App.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def upload_app(self, files, app_url=None):
        """Does a POST request to /public/apps.

        Api provides the list of the apps which are available for the user to
        install or are already installed. App object provides basic app
        information along with app metadata.

        Args:
            app_url (string, optional): Specifies the url of the app package

        Returns:
            App: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('upload_app called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for upload_app.')
            _url_path = '/public/apps'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'appUrl': app_url,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Read the file content.
            f = open(files, 'rb')
            files = {"file": (files, f)}

            # Prepare headers
            self.logger.info('Preparing headers for upload_app.')
            _headers = {
                'accept': '*/*',
                'content-type': 'multipart/form-data;'
                                'boundary=c7cbfdd911b4e720f1dd8f479c50bc7f'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for upload_app.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                files=files)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='upload_app')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for upload_app.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              App.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def install_app(self, version, app_uid):
        """Does a POST request to /public/apps/{appUid}/versions/{version}.

        Only purchased apps can be installed using this api.

        Args:
            version (long|int): Specifies the app version.
            app_uid (long|int): Specifies the app Id.

        Returns:
            App: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('install_app called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for install_app.')
            self.validate_parameters(id=id, app_uid=app_uid)

            # Prepare query URL
            self.logger.info('Preparing query URL for install_app.')
            _url_path = '/public/apps/{appUid}/versions/{version}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'appUid':app_uid, 'version': version})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for install_app.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for install_app.')
            _request = self.http_client.post(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='install_app')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for install_app.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              App.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def uninstall_app(self, version, app_uid):
        """Does a DELETE request to /public/apps/{appUid}/versions/{version}.

        Only purchased apps can be installed using this api.

        Args:
            version (long|int): Specifies the app version.
            app_uid (long|int): Specifies the app Id.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('uninstall_app called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for uninstall_app.')
            self.validate_parameters(id=id, app_uid=app_uid)

            # Prepare query URL
            self.logger.info('Preparing query URL for uninstall_app.')
            _url_path = '/public/apps/{appUid}/versions/{version}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'appUid':app_uid, 'version': version})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for uninstall_app.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for uninstall_app.')
            _request = self.http_client.delete(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='uninstall_app')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for uninstall_app.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
