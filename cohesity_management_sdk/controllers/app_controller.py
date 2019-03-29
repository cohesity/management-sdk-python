# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.app_information import AppInformation
from cohesity_management_sdk.exceptions.error_error_exception import ErrorErrorException

class AppController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(AppController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def upload_app(self):
        """Does a POST request to /public/apps.

        Api provides the list of the apps which are available for the user to
        install
        or are already installed. App object provides basic app information
        along with
        app metadata.

        Returns:
            AppInformation: Response from the API. Success

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
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for upload_app.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for upload_app.')
            _request = self.http_client.post(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'upload_app')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for upload_app.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, AppInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def delete_uninstall_app(self,
                             app_uid,
                             version):
        """Does a DELETE request to /public/apps/{appUid}/versions/{version}.

        App must already been installed for this api to work.

        Args:
            app_uid (long|int): Specifies the app Id.
            version (long|int): Specifies the app version.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_uninstall_app called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for delete_uninstall_app.')
            self.validate_parameters(app_uid=app_uid,
                                     version=version)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_uninstall_app.')
            _url_path = '/public/apps/{appUid}/versions/{version}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'appUid': app_uid,
                'version': version
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info('Preparing and executing request for delete_uninstall_app.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'delete_uninstall_app')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_uninstall_app.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_install_app(self,
                           app_uid,
                           version):
        """Does a POST request to /public/apps/{appUid}/versions/{version}.

        Only purchased apps can be installed using this api.

        Args:
            app_uid (long|int): Specifies the app Id.
            version (long|int): Specifies the app version.

        Returns:
            AppInformation: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_install_app called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_install_app.')
            self.validate_parameters(app_uid=app_uid,
                                     version=version)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_install_app.')
            _url_path = '/public/apps/{appUid}/versions/{version}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'appUid': app_uid,
                'version': version
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_install_app.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_install_app.')
            _request = self.http_client.post(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_install_app')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_install_app.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, AppInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_apps(self):
        """Does a GET request to /public/apps.

        Api provides the list of the apps which are available for the user to
        install
        or are already installed. App object provides basic app information
        along with
        app metadata.

        Returns:
            list of AppInformation: Response from the API. GetAppsResponse
                specifies response for getting apps

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_apps called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_apps.')
            _url_path = '/public/apps'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_apps.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_apps.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_apps')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_apps.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, AppInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
