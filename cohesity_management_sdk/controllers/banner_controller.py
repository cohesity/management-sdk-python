# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.exceptions.error_exception import ErrorException
from cohesity_management_sdk.models.banner import Banner
from cohesity_management_sdk.models.banner_update_parameters import BannerUpdateParameters



class BannerController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(BannerController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_banner(self):
        """Does a GET request to /public/banners.

        Currently it returns a cluster specific banner for all requests.
        Later, depending on who is requesting it (which can be inferred from
        the URL), we would like to return most appropriate banner if set by
        the cluster admin (or Service Provider).

        Returns:
            Banner: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_banner called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_banner.')
            _url_path = '/public/banners'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_banner.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_banner.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_banner')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_banner.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, Banner.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_banner(self, body=None):
        """Does a PUT request to /public/banners.

        Returns the banner that was updated on the Cohesity Cluster.

        Args:
            body (BannerUpdateParameters): Request to update a View.

        Returns:
            Banner: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_banner called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_banner.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_banner.')
            _url_path = '/public/banners'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_banner.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_banner.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_banner')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_banner.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)

            self.validate_response(_context)
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Banner.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

