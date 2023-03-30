# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.package_details import PackageDetails
from cohesity_management_sdk.models.download_package_result import DownloadPackageResult
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class PackagesController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(PackagesController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def list_packages(self):
        """Does a GET request to /public/packages.

        Sends a request retrieve information about all packages which are
        currently
        installed on the Cluster.

        Returns:
            list of PackageDetails: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_packages called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for list_packages.')
            _url_path = '/public/packages'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_packages.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_packages.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='list_packages')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for list_packages.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              PackageDetails.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_download_package(self, body):
        """Does a POST request to /public/packages/url.

        Sends a request to download a package from a URL to the Cluster.

        Args:
            body (DownloadPackageParameters): TODO: type description here.
                Example:

        Returns:
            DownloadPackageResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_download_package called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_download_package.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_download_package.')
            _url_path = '/public/packages/url'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_download_package.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_download_package.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_download_package')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_download_package.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                DownloadPackageResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
