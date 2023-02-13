# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.view_box import ViewBox
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.exceptions.api_exception import APIException


class ViewBoxesController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(ViewBoxesController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_view_boxes(self,
                       tenant_ids=None,
                       all_under_hierarchy=None,
                       ids=None,
                       names=None,
                       cluster_partition_ids=None,
                       fetch_stats=None,
                       fetch_time_series_schema=None,
                       template_id=None,
                       match_partial_names=None):
        """Does a GET request to /public/viewBoxes.

        If no parameters are specified, all Domains (View Boxes) currently on
        the Cohesity Cluster are returned.
        Specifying parameters filters the results that are returned.

        Args:
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.
            ids (list of long|int, optional): Filter by a list of Storage
                Domain (View Box) ids. If empty, View Boxes are not filtered
                by id.
            names (list of string, optional): Filter by a list of Storage
                Domain (View Box) Names. If empty, Storage Domains (View
                Boxes) are not filtered by Name.
            cluster_partition_ids (list of long|int, optional): Filter by a
                list of Cluster Partition Ids.
            fetch_stats (bool, optional): Specifies whether to include usage
                and performance statistics.
            fetch_time_series_schema (bool, optional): Specifies whether to
                get time series schema info of the view box.
            template_id (int|long, optional): Filter list of Storage Domain
                (View Box) by the properties of the template like dedup,
                compression. If empty, Storage Domains (View Boxes) are not
                filtered.
            match_partial_names (bool, optional): If true, the names in
                'names' field are matched by prefix rather than exactly
                matched.

        Returns:
            list of ViewBox: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_view_boxes called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_view_boxes.')
            _url_path = '/public/viewBoxes'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy,
                'ids': ids,
                'names': names,
                'clusterPartitionIds': cluster_partition_ids,
                'fetchStats': fetch_stats,
                'fetchTimeSeriesSchema': fetch_time_series_schema,
                'templateId': template_id,
                'matchPartialNames': match_partial_names
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_view_boxes.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_view_boxes.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_view_boxes')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_view_boxes.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ViewBox.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_view_box(self, body):
        """Does a POST request to /public/viewBoxes.

        Returns the created Domain (View Box).

        Args:
            body (CreateViewBoxParams): Request to create a Storage Domain
                (View Box) configuration.

        Returns:
            ViewBox: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_view_box called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_view_box.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_view_box.')
            _url_path = '/public/viewBoxes'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_view_box.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_view_box.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_view_box')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_view_box.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ViewBox.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_view_box(self, id):
        """Does a DELETE request to /public/viewBoxes/{id}.

        Returns delete status upon completion.

        Args:
            id (long|int): Id of the Storage Domain (View Box)

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_view_box called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_view_box.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_view_box.')
            _url_path = '/public/viewBoxes/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_view_box.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_view_box')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_view_box.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_view_box_by_id(self, id, fetch_stats=None):
        """Does a GET request to /public/viewBoxes/{id}.

        Returns the Domain (View Box) corresponding to the specified Domain
        (View Box)
        Id.

        Args:
            id (long|int): Id of the Storage Domain (View Box)
            fetch_stats (bool, optional): Specifies whether to include usage
                and performance statistics.

        Returns:
            ViewBox: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_view_box_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_view_box_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_view_box_by_id.')
            _url_path = '/public/viewBoxes/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'fetchStats': fetch_stats}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_view_box_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_view_box_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_view_box_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_view_box_by_id.')
            if _context.response.status_code == 404:
                raise APIException('Not Found', _context)
            elif (_context.response.status_code <
                  200) or (_context.response.status_code > 208):
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ViewBox.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_view_box(self, id, body):
        """Does a PUT request to /public/viewBoxes/{id}.

        Returns the updated Domain (View Box).

        Args:
            id (long|int): Id of the Storage Domain (View Box)
            body (CreateViewBoxParams): Request to update a Storage Domain
                (View Box) configuration.

        Returns:
            ViewBox: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_view_box called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_view_box.')
            self.validate_parameters(id=id, body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_view_box.')
            _url_path = '/public/viewBoxes/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_view_box.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_view_box.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_view_box')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_view_box.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ViewBox.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
