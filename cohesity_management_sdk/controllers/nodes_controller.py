# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.node import Node
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException

class NodesController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(NodesController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_nodes(self):
        """Does a GET request to /public/nodes.

        If no parameters are specified, all Nodes currently on the Cohesity
        Cluster are returned. Specifying parameters filters the results that
        are returned.

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
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_nodes.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_nodes.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_nodes')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_nodes.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, Node.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_node_by_id(self,
                       id):
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
            self.logger.info('Validating required parameters for get_node_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_node_by_id.')
            _url_path = '/public/nodes/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'id': id
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_node_by_id.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_node_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_node_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_node_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, Node.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
