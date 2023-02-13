# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.license_account_usage_rsp import LicenseAccountUsageRsp
from cohesity_management_sdk.models.cluster_status_result import ClusterStatusResult
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class LicenseController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(LicenseController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_license_usage(self):
        """Does a GET request to /public/licenseUsage.

        Sends a request to retrieve information about the current license
        usage
        of the cluster and the enitled license capacity of the Cohesity
        Account.

        Returns:
            LicenseAccountUsageRsp: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_license_usage called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_license_usage.')
            _url_path = '/public/licenseUsage'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_license_usage.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_license_usage.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_license_usage')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_license_usage.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)

            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              LicenseAccountUsageRsp.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    