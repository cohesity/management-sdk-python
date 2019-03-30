# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.dashboard_response import DashboardResponse
from cohesity_management_sdk.exceptions.error_error_exception import ErrorErrorException

class DashboardController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(DashboardController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_dashboard(self,
                      cluster_id=None,
                      all_clusters=None,
                      refresh=None,
                      tile_types=None):
        """Does a GET request to /public/dashboard.

        If no parameters are specified, dashboard for the local cluster is
        returned.

        Args:
            cluster_id (long|int, optional): Id of the remote cluster for
                which to fetch the data. If value is not specified, it is
                assumed to be local cluster.
            all_clusters (bool, optional): Summary data for all clusters. If
                this is set to true, all other parameters will be ignored.
            refresh (bool, optional): Specifies whether to refresh the tiles
                selected.
            tile_types (list of TileTypesEnum, optional): Specifies the types
                of the tiles to be returned. If this is not specified, all the
                tiles are returned. This is ignored when allClusters is set to
                true. 'kHealth' is the tile that shows health of the cluster
                and the alerts in the past 24 hours. 'kJobRuns' is the tile
                that shows job runs in the past 24 hours. 'kRecoveries' is the
                tile that shows recoveries done in the past 30 days.
                'kProtectedObjects' is the tile that shows the protected
                objects details. 'kProtection' is the tile that shows the
                protection information in the past 24 hours. 'kAuditLogs' is
                the tile that shows the recent audit logs. 'kIops' is the tile
                that shows IP performance in the past 24 hours. 'kThroughput'
                is the tile that shows job runs in the past 24 hours.
                'kStorageEfficiency' is the tile that shows job runs in the
                past 7 days.

        Returns:
            DashboardResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_dashboard called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_dashboard.')
            _url_path = '/public/dashboard'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'clusterId': cluster_id,
                'allClusters': all_clusters,
                'refresh': refresh,
                'tileTypes': tile_types
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_dashboard.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_dashboard.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_dashboard')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_dashboard.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, DashboardResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
