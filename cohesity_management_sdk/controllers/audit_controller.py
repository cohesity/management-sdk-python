# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.cluster_audit_logs_search_result import ClusterAuditLogsSearchResult
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class AuditController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(AuditController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_audit_logs_actions(self):
        """Does a GET request to /public/auditLogs/actions.

        A string array of all the actions used to filter audit logs.

        Returns:
            list of string: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_audit_logs_actions called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_audit_logs_actions.')
            _url_path = '/public/auditLogs/actions'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_audit_logs_actions.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_audit_logs_actions.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_audit_logs_actions')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_audit_logs_actions.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_audit_logs_categories(self):
        """Does a GET request to /public/auditLogs/categories.

        A string array of all the categories used to filter audit logs.

        Returns:
            list of string: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_audit_logs_categories called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_audit_logs_categories.')
            _url_path = '/public/auditLogs/categories'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_audit_logs_categories.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_audit_logs_categories.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_audit_logs_categories')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_audit_logs_categories.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def search_cluster_audit_logs(self,
                                  user_names=None,
                                  domains=None,
                                  entity_types=None,
                                  actions=None,
                                  search=None,
                                  start_time_usecs=None,
                                  end_time_usecs=None,
                                  start_index=None,
                                  page_count=None,
                                  output_format=None,
                                  tenant_id=None,
                                  all_under_hierarchy=None):
        """Does a GET request to /public/auditLogs/cluster.

        When actions (such as a login or a Job being paused) occur on the
        Cohesity Cluster, the Cluster generates Audit Logs.
        If no parameters are specified, all logs currently on the Cohesity
        Cluster
        are returned. Specifying parameters filters the results that are
        returned.

        Args:
            user_names (list of string, optional): Filter by user names who
                cause the actions that generate Cluster Audit Logs.
            domains (list of string, optional): Filter by domains of users who
                cause the actions that trigger Cluster audit logs.
            entity_types (list of string, optional): Filter by entity types
                involved in the actions that generate the Cluster audit logs,
                such as User, Protection Job, View, etc. For a complete list,
                see the Category drop-down in the Admin > Audit Logs page of
                the Cohesity Dashboard.
            actions (list of string, optional): Filter by the actions that
                generate Cluster audit logs such as Activate, Cancel, Clone,
                Create, etc. For a complete list, see the Actions drop-down in
                the Admin > Audit Logs page of the Cohesity Dashboard.
            search (string, optional): Filter by matching a substring in
                entity name or details of the Cluster audit log.
            start_time_usecs (long|int, optional): Filter by a start time.
                Only Cluster audit logs that were generated after the
                specified time are returned. Specify the start time as a Unix
                epoch Timestamp (in microseconds).
            end_time_usecs (long|int, optional): Filter by a end time
                specified as a Unix epoch Timestamp (in microseconds). Only
                Cluster audit logs that were generated before the specified
                end time are returned.
            start_index (long|int, optional): Specifies an index number that
                can be used to return subsets of items in multiple requests.
                Break up the items to return into multiple requests by setting
                pageCount and startIndex to return a subsets of items in the
                search result. For example, set startIndex to 0 to get the
                first set of pageCount items for the first request. Increment
                startIndex by pageCount to get the next set of pageCount items
                for a next request. Continue until all items are returned and
                therefore the total number of returned items is equal to
                totalCount. Default value is 0.
            page_count (long|int, optional): Limit the number of items to
                return in the response for pagination purposes. Default value
                is 1000.
            output_format (string, optional): Specifies the format of the
                output such as csv and json. If not specified, the json format
                is returned. If csv is specified, a comma-separated list with
                a heading row is returned.
            tenant_id (string, optional): TenantId specifies the tenant whose
                action resulted in the audit log.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if logs of all the tenants under the hierarchy of tenant with
                id TenantId should be returned.

        Returns:
            ClusterAuditLogsSearchResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('search_cluster_audit_logs called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for search_cluster_audit_logs.')
            _url_path = '/public/auditLogs/cluster'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'userNames': user_names,
                'domains': domains,
                'entityTypes': entity_types,
                'actions': actions,
                'search': search,
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs,
                'startIndex': start_index,
                'pageCount': page_count,
                'outputFormat': output_format,
                'tenantId': tenant_id,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for search_cluster_audit_logs.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for search_cluster_audit_logs.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='search_cluster_audit_logs')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for search_cluster_audit_logs.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ClusterAuditLogsSearchResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
