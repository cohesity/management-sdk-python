# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.specifies_the_external_client_subnets_that_can_communicate_with_this_cluster import SpecifiesTheExternalClientSubnetsThatCanCommunicateWithThisCluster
from cohesity_management_sdk.models.cluster_public_keys import ClusterPublicKeys
from cohesity_management_sdk.exceptions.error_error_exception import ErrorErrorException

class ClustersController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(ClustersController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_external_client_subnets(self):
        """Does a GET request to /public/externalClientSubnets.

        Returns the external Client Subnets for the cluster.

        Returns:
            SpecifiesTheExternalClientSubnetsThatCanCommunicateWithThisCluster:
                Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_external_client_subnets called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_external_client_subnets.')
            _url_path = '/public/externalClientSubnets'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_external_client_subnets.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_external_client_subnets.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_external_client_subnets')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_external_client_subnets.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, SpecifiesTheExternalClientSubnetsThatCanCommunicateWithThisCluster.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_cluster_keys(self):
        """Does a GET request to /public/cluster/keys.

        Returns the Public Keys for the cluster.

        Returns:
            ClusterPublicKeys: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_cluster_keys called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_cluster_keys.')
            _url_path = '/public/cluster/keys'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_cluster_keys.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_cluster_keys.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_cluster_keys')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_cluster_keys.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, ClusterPublicKeys.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update_external_client_subnets(self,
                                       body=None):
        """Does a PUT request to /public/externalClientSubnets.

        Returns the updated external Client Subnets of the cluster.

        Args:
            body (SpecifiesTheExternalClientSubnetsThatCanCommunicateWithThisCl
                uster, optional): TODO: type description here. Example:

        Returns:
            SpecifiesTheExternalClientSubnetsThatCanCommunicateWithThisCluster:
                Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_external_client_subnets called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_external_client_subnets.')
            _url_path = '/public/externalClientSubnets'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_external_client_subnets.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_external_client_subnets.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_external_client_subnets')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_external_client_subnets.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, SpecifiesTheExternalClientSubnetsThatCanCommunicateWithThisCluster.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
