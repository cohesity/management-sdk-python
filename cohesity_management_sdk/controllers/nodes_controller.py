# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.free_node_information import FreeNodeInformation
from cohesity_management_sdk.models.node_status_result import NodeStatusResult
from cohesity_management_sdk.models.node import Node
from cohesity_management_sdk.models.upgrade_node_result import UpgradeNodeResult
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class NodesController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(NodesController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def list_free_nodes(self):
        """Does a GET request to /public/freeNodes.

        Sends a request to any Node to list all of the free Nodes that are
        present on
        the network.

        Returns:
            list of FreeNodeInformation: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_free_nodes called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for list_free_nodes.')
            _url_path = '/public/freeNodes'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_free_nodes.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_free_nodes.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='list_free_nodes')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for list_free_nodes.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                FreeNodeInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_node_status(self):
        """Does a GET request to /public/node/status.

        Sends a request to a Node to get the status of that node.

        Returns:
            NodeStatusResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_node_status called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_node_status.')
            _url_path = '/public/node/status'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_node_status.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_node_status.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_node_status')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_node_status.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              NodeStatusResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_nodes(self,
                  ids=None, 
                  include_marked_for_removal=None,
                  include_only_unassigned_nodes=None,
                  cluster_partition_ids=None,
                  fetch_stats=None,
                  show_system_disks=None):
        """Does a GET request to /public/nodes.

        If no parameters are specified, all Nodes currently on the Cohesity
        Cluster are
        returned.
        Specifying parameters filters the results that are returned.
        Args:
            ids (long|int, optional): IdList is the ids of nodes to be
                returned. If empty, all nodes are returned.
            include_marked_for_removal (bool, optional):
                IncludeMarkedForRemoval is used to specify whether to
                include nodes marked for removal.
            include_only_unassigned_nodes (bool, optional):
                IncludeOnlyUnassignedNodes will return nodes that are not yet
                assigned to any cluster partition. If this parameter is
                specified as true and ClusterPartitionIdList is also non-empty,
                then no nodes will be returned.
            cluster_partition_ids (long|int, optional):  ClusterPartitionIdList
                specifies the list of Ids used to filter the nodes by specified
                cluster partition.
            fetch_stats (bool, optional): FetchStats is used to specify whether
                to call Stats service to fetch the stats for the nodes.
            show_system_disks (bool, optional): ShowSystemdisks is used to
                specify whether to display system disks for the nodes.

        Returns:
            list of Node: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_nodes called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_nodes.')
            _url_path = '/public/nodes'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'ids': ids,
                'includeMarkedForRemoval': include_marked_for_removal,
                'includeOnlyUnassignedNodes': include_only_unassigned_nodes,
                'clusterPartitionIds': cluster_partition_ids,
                'fetchStats': fetch_stats,
                'showSystemDisks': show_system_disks
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_nodes.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_nodes.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_nodes')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_nodes.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Node.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_upgrade_node(self, body):
        """Does a PUT request to /public/nodes/software.

        Sends a request to upgrade the software version of a Node. By default,
        the
        Node that the request is sent to is the only one upgraded, but the
        user can
        specify if they want to attempt to upgrade all free nodes on the
        network.
        Before using this, you need to upload a new package to the Node you
        want to
        upgrade by using the /public/packages endpoint.

        Args:
            body (UpgradeNodeParameters): TODO: type description here.
                Example:

        Returns:
            UpgradeNodeResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_upgrade_node called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_upgrade_node.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_upgrade_node.')
            _url_path = '/public/nodes/software'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_upgrade_node.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_upgrade_node.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_upgrade_node')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_upgrade_node.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, UpgradeNodeResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_node_by_id(self, id):
        """Does a GET request to /public/nodes/{id}.

        Returns the Node corresponding to the specified Node Id.

        Args:
            id (long|int): Id of the Node

        Returns:
            list of Node: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_node_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_node_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_node_by_id.')
            _url_path = '/public/nodes/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_node_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_node_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_node_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_node_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Node.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
