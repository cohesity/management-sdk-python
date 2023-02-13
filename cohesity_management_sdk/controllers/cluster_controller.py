# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.apps_config import AppsConfig
from cohesity_management_sdk.models.basic_cluster_info import BasicClusterInfo
from cohesity_management_sdk.models.cluster import Cluster
from cohesity_management_sdk.models.cluster_status_result import ClusterStatusResult
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class ClusterController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(ClusterController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_basic_cluster_info(self):
        """Does a GET request to /public/basicClusterInfo.

        All Active Directory domains that are currently joined to the
        Cohesity
        Cluster are returned. In addition, the default LOCAL domain on the
        Cohesity Cluster is returned as the first element of the domains array
        in
        the response.

        Returns:
            BasicClusterInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_basic_cluster_info called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_basic_cluster_info.')
            _url_path = '/public/basicClusterInfo'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_basic_cluster_info.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_basic_cluster_info.')
            _request = self.http_client.get(_query_url, headers=_headers)
            _context = self.execute_request(_request,
                                            name='get_basic_cluster_info')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_basic_cluster_info.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              BasicClusterInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_cluster(self,
                    fetch_stats=None,
                    fetch_time_series_schema=None,
                    include_minimum_nodes_info=None):
        """Does a GET request to /public/cluster.

        Returns information about this Cohesity Cluster.

        Args:
            fetch_stats (bool, optional): If 'true', also get statistics about
                the Cohesity Cluster.
            fetch_time_series_schema (bool, optional): Specifies whether to
                get time series schema info of the cluster.
            include_minimum_nodes_info (bool, optional): Specifies whether to
                include info about minimum failure domains needed to support
                based on fault tolerance configured and EC configuration on all
                storage domains.

        Returns:
            Cluster: Response from the API. Successful Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_cluster called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_cluster.')
            _url_path = '/public/cluster'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'fetchStats': fetch_stats,
                'fetchTimeSeriesSchema': fetch_time_series_schema,
                'includeMinimumNodesInfo': include_minimum_nodes_info
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_cluster.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_cluster.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_cluster')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_cluster.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Cluster.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_cluster(self, body=None):
        """Does a PUT request to /public/cluster.

        Returns the updated Cluster configuration.

        Args:
            body (UpdateClusterParams, optional): Update Cluster Parameter.

        Returns:
            Cluster: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_cluster called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_cluster.')
            _url_path = '/public/cluster'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_cluster.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_cluster.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_cluster')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_cluster.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Cluster.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_app_settings(self):
        """Does a GET request to /public/cluster/appSettings.

        Returns the app settings for the cluster.

        Returns:
            AppsConfig: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_app_settings called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_app_settings.')
            _url_path = '/public/cluster/appSettings'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_app_settings.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_app_settings.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_app_settings')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_app_settings.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                AppsConfig.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_app_settings(self, body=None):
        """Does a PUT request to /public/cluster/appSettings.

        Returns the updated app settings.

        Args:
            body (AppsConfig): Update App Settings Parameter.

        Returns:
            AppsConfig: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_app_settings called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_app_settings.')
            _url_path = '/public/cluster/appSettings'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_app_settings.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_app_settings.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_app_settings')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_app_settings.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                AppsConfig.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_cluster_status(self):
        """Does a GET request to /public/cluster/status.

        Sends a request to get the status of every node that is part of the
        current
        Cluster.

        Returns:
            ClusterStatusResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_cluster_status called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_cluster_status.')
            _url_path = '/public/cluster/status'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_cluster_status.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_cluster_status.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_cluster_status')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_cluster_status.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ClusterStatusResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
