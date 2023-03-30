# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.protected_object import ProtectedObject
from cohesity_management_sdk.models.protection_job import ProtectionJob
from cohesity_management_sdk.models.protection_object_summary import ProtectionObjectSummary
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class ProtectionObjectsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(ProtectionObjectsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def delete_unprotect_object(self, body=None):
        """Does a DELETE request to /public/protectionObjects.

        Unprotect a Protected Object.

        Args:
            body (UnprotectObjectParams, optional): TODO: type description
                here. Example:

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_unprotect_object called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for delete_unprotect_object.')
            _url_path = '/public/protectionObjects'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_unprotect_object.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_unprotect_object.')
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='delete_unprotect_object')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for delete_unprotect_object.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_protect_object(self, body=None):
        """Does a POST request to /public/protectionObjects.

        Returns the Protected Object and its corresponding Protection Job
        information.

        Args:
            body (ProtectObjectParameters, optional): TODO: type description
                here. Example:

        Returns:
            list of ProtectedObject: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_protect_object called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_protect_object.')
            _url_path = '/public/protectionObjects'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_protect_object.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_protect_object.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_protect_object')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_protect_object.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectedObject.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_protection_object(self, body=None):
        """Does a PUT request to /public/protectionObjects.

        Returns the Updated Protected Object.

        Args:
            body (UpdateProtectionObjectParameters, optional): TODO: type
                description here. Example:

        Returns:
            ProtectionJob: Response from the API.
                UpdateProtectionObjectRequest is the response of updating a
                Protection
Object.
Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_protection_object called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_protection_object.')
            _url_path = '/public/protectionObjects'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_protection_object.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_protection_object.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_protection_object')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_protection_object.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionJob.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protection_object_summary(self, protection_source_id):
        """Does a GET request to /public/protectionObjects/summary.

        Returns the Protected Object and its corresponding Protection Job
        information.

        Args:
            protection_source_id (long|int): Specifies the id of the
                Protection Source.

        Returns:
            ProtectionObjectSummary: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_object_summary called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_protection_object_summary.'
            )
            self.validate_parameters(protection_source_id=protection_source_id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_protection_object_summary.')
            _url_path = '/public/protectionObjects/summary'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'protectionSourceId': protection_source_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_protection_object_summary.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protection_object_summary.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_protection_object_summary')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_protection_object_summary.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ProtectionObjectSummary.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
