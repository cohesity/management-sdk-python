# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.interface import Interface
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class InterfaceController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(InterfaceController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def update_interface(self, body=None):
        """Does a PUT request to /public/interface.

        Returns the update status upon completion.

        Args:
            body (Interface, optional): TODO: type description here. Example:

        Returns:
            Interface: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_interface called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_interface.')
            _url_path = '/public/interface'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_interface.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_interface.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_interface')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_interface.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Interface.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_interface(self,
                       node_id=None,
                       cache=None,
                       bond_interface_only=None,
                       iface_group_assigned_only=None,
                       include_uplink_switch_info=None,
                       include_bond_slave_details=None,
                       include_stats=None):
        """Does a GET request to /public/interface.

        Show network interfaces.

        Args:
            node_id (int, optional): Specifies the id of the node.
            cache (bool, optional): Specifies if interface is cached info.
            bond_interface_only (bool, optional): Specifies if only show bond
                interface info.
            iface_group_assigned_only (bool, optional): Specifies if only show
                interface group assigned interface info.
            include_uplink_switch_info (bool, optional): Specifies if include
                uplink switch info.
            include_bond_slave_details (bool, optional): Specifies if include
                bond secondary detailed info.
            include_stats (bool, optional): Specifies if include stats.

        Returns:
            Interface: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_interface called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for list_interface.')
            _url_path = '/public/interface'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'nodeId': node_id,
                'cache': cache,
                'bondInterfaceOnly': bond_interface_only,
                'ifaceGroupAssignedOnly': iface_group_assigned_only,
                'includeUplinkSwitchInfo': include_uplink_switch_info,
                'includeBondSlaveDetails': include_bond_slave_details,
                'includeStats': include_stats
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)
            
            # Prepare headers
            self.logger.info('Preparing headers for list_interface.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_interface.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='list_interface')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for list_interface.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Interface.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
