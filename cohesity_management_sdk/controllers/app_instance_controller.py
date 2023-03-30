# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.models.app_instance import AppInstance
from cohesity_management_sdk.models.launch_app_instance import LaunchAppInstance
from cohesity_management_sdk.models.app_instance_id_parameter import AppInstanceIdParameter
from cohesity_management_sdk.models.update_app_instance_state_parameters import UpdateAppInstanceStateParameters


class AppInstanceController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(AppInstanceController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def update_app_instance_settings(self, app_instance_id, body):
        """Does a PUT request to /public/appInstanceSettings/{appInstanceId}.

        Changes the settings of the app instance.

        Args:
            app_instance_id (string): Specifies the app instance Id.
            body (UpdateAppInstanceSettingsParameters): Request to update app
                instance settings.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_app_instance_settings called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_app_instance_settings.')
            self.validate_parameters(app_instance_id=app_instance_id, body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_app_instance_settings.')
            _url_path = '/public/appInstanceSettings/{appInstanceId}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'appInstanceId': app_instance_id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_app_instance_settings.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_app_instance_settings.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_app_instance_settings')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_app_instance_settings.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_app_instances(self):
        """Does a GET request to /public/appInstances.

        Api provides the list of the app instances. Instances can be in
        different states including stopped.

        Returns:
            AppInstance: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_app_instances called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_app_instances.')
            _url_path = '/public/appInstances'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
            # Prepare headers
            self.logger.info('Preparing headers for get_app_instances.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_app_instances.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_app_instances')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_app_instances.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              AppInstance.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def launch_app_instance(self, body):
        """Does a POST request to /public/appInstances.

        Starts the application instance launch on the cluster.
        Only installed apps can be launched.

        Args:
            body (LaunchAppInstance): TODO: type description
                here. Example:

        Returns:
            AppInstanceIdParameter: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('launch_app_instance called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for launch_app_instance.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for launch_app_instance.')
            _url_path = '/public/appInstances'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for launch_app_instance.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for launch_app_instance.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='launch_app_instance')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for launch_app_instance.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                AppInstanceIdParameter.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_app_instance_state(self, app_instance_id, body):
        """Does a PUT request to /public/appInstances/{appInstanceId}/states.

        Changes the state of the app instances.

        Args:
            app_instance_id (int): Specifies the app instance Id.
            body (UpdateAppInstanceStateParameters): Request to update app
            instance state.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_app_instance_state called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_app_instance_state.')
            self.validate_parameters(app_instance_id=app_instance_id, body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_app_instance_state.')
            _url_path = '/public/appInstances/{appInstanceId}/states'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'appInstanceId': app_instance_id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_app_instance_state.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_app_instance_state.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_app_instance_state')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_app_instance_state.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

