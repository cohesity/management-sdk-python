# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.cluster_partition import ClusterPartition
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.exceptions.api_exception import APIException


class ClusterPartitionsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(ClusterPartitionsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_cluster_partitions(self, ids=None, names=None):
        """Does a GET request to /public/clusterPartitions.

        If no parameters are specified, all Cluster Partitions currently on
        the Cohesity Cluster are returned.
        Specifying parameters filters the results that are returned.

        Args:
            ids (list of long|int, optional): Array of Cluster Partition Ids.
                Filter by a list of Cluster Partition ids. If empty, the
                Cluster Partitions are not filtered by id.
            names (list of string, optional): Array of Cluster Partition
                Names.  Filter by a list of Cluster Partition Names. If empty,
                the Cluster Partitions are not filtered by names.

        Returns:
            list of ClusterPartition: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_cluster_partitions called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_cluster_partitions.')
            _url_path = '/public/clusterPartitions'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'ids': ids, 'names': names}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_cluster_partitions.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_cluster_partitions.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_cluster_partitions')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_cluster_partitions.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ClusterPartition.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_cluster_partition_by_id(self, id):
        """Does a GET request to /public/clusterPartitions/{id}.

        Returns the Cluster Partition corresponding to the specified Cluster
        Partition Id.

        Args:
            id (long|int): Specifies a unique id of the Cluster Partition to
                return.

        Returns:
            ClusterPartition: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_cluster_partition_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_cluster_partition_by_id.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_cluster_partition_by_id.')
            _url_path = '/public/clusterPartitions/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_cluster_partition_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_cluster_partition_by_id.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_cluster_partition_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_cluster_partition_by_id.')
            if _context.response.status_code == 404:
                raise APIException('Not Found', _context)
            elif (_context.response.status_code <
                  200) or (_context.response.status_code > 208):
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ClusterPartition.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
