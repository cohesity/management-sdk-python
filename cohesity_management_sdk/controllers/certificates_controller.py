# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.list_cert_response import ListCertResponse
from cohesity_management_sdk.models.certificate_details import CertificateDetails
from cohesity_management_sdk.models.ssl_certificate_config import SslCertificateConfig
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class CertificatesController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(CertificatesController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_certificate_list(self):
        """Does a GET request to /public/certificates/global.

        Returns the all certificate and their details generated from this
        cluster.

        Returns:
            ListCertResponse: Response from the API. List Host Certificate
                Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_certificate_list called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_certificate_list.')
            _url_path = '/public/certificates/global'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_certificate_list.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_certificate_list.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_certificate_list')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_certificate_list.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ListCertResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_deploy_host_certificate(self, body=None):
        """Does a POST request to /public/certificates/global.

        Returns the global certificate for a single or multiple hosts.

        Args:
            body (DeployCertParameters, optional): Request to generate and
                deploy a new certificate.

        Returns:
            CertificateDetails: Response from the API. Host Certificate
                Download Response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_deploy_host_certificate called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_deploy_host_certificate.')
            _url_path = '/public/certificates/global'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_deploy_host_certificate.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_deploy_host_certificate.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_deploy_host_certificate')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_deploy_host_certificate.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, CertificateDetails.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_web_server_certificate(self):
        """Does a DELETE request to /public/certificates/webServer.

        Returns delete status upon completion.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_web_server_certificate called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for delete_web_server_certificate.')
            _url_path = '/public/certificates/webServer'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_web_server_certificate.'
            )
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='delete_web_server_certificate')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for delete_web_server_certificate.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_web_server_certificate(self):
        """Does a GET request to /public/certificates/webServer.

        Returns the Server Certificate configured on the cluster.

        Returns:
            SslCertificateConfig: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_web_server_certificate called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_web_server_certificate.')
            _url_path = '/public/certificates/webServer'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_web_server_certificate.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_web_server_certificate.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_web_server_certificate')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_web_server_certificate.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                SslCertificateConfig.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_web_server_certificate(self, body=None):
        """Does a PUT request to /public/certificates/webServer.

        Returns the updated Web Server Certificate on the cluster.

        Args:
            body (SslCertificateConfig, optional): TODO: type description
                here. Example:

        Returns:
            SslCertificateConfig: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_web_server_certificate called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_web_server_certificate.')
            _url_path = '/public/certificates/webServer'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_web_server_certificate.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_web_server_certificate.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='update_web_server_certificate')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_web_server_certificate.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                SslCertificateConfig.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
