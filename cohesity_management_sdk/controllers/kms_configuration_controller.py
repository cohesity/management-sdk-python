# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.kms_configuration_response import KmsConfigurationResponse
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class KmsConfigurationController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(KmsConfigurationController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config


    def get_kms_config(self, id=None, include_rpaas_kms=None):
        """Does a GET request to /public/kmsConfig.

        List KMS configurations in the cluster.

        Args:
            id (int, optional): The Id of a KMS server.
            include_rpaas_kms(bool, optional): Include RPaaS KMS, if true
                returns RPaaS keys

        Returns:
            list of KmsConfigurationResponse: Response from the API. Specifies
                a list of KMS configurations.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_kms_config called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_kms_config.')
            _url_path = '/public/kmsConfig'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'id': id,
                'includeRpaasKms': include_rpaas_kms
                }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_kms_config.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_kms_config.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_kms_config')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_kms_config.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                KmsConfigurationResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise


    def update_kms_config(self, body=None):
        """Does a PUT request to /public/kmsConfig.

        Update KMS configurations in the cluster.

        Args:
            body (KmsUpdateRequestParameters, optional): TODO: type description here.
                Example:

        Returns:
            KmsConfigurationResponse: Response from the API. Response after
                KMS has been updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_kms_config called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_kms_config.')
            _url_path = '/public/kmsConfig'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_kms_config.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_kms_config.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_kms_config')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_kms_config.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                KmsConfigurationResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise


    def create_kms_config(self, body=None):
        """Does a POST request to /public/kmsConfig.

        Returns the created KMS config.

        Args:
            body (KmsCreateRequestParameters, optional): TODO: type description here.
                Example:

        Returns:
            KmsConfigurationResponse: Response from the API. Response after
                KMS has been created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_kms_config called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_kms_config.')
            _url_path = '/public/kmsConfig'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_kms_config.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_kms_config.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_kms_config')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_kms_config.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                KmsConfigurationResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_kms_config(self, id, body):
        """Does a DELETE request to /public/kmsConfig/{id}.

        Specifies a unique id of the KMS config.

        Args:
            id (long|int): Specifies a unique id of the Protection Job.
            body (KmsDeleteParams): Request to delete kms config.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_kms_config called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_kms_config.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_kms_config.')
            _url_path = '/public/kmsConfig/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_kms_config.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_kms_config.')
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='delete_kms_config')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_kms_config.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
