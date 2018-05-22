# coding: utf-8

"""
    Cohesity REST API

    This API provides operations for interfacing with the Cohesity Cluster. NOTE: To view the documentation on the responses, click 'Model' next to 'Example Value' and keep clicking to expand the hierarchy.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AuditApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def search_cluster_audit_logs(self, **kwargs):
        """
        List the cluster audit logs on the Cohesity Cluster that match the filter criteria specified using parameters.
        When actions (such as a login or a Job being paused) occur on the Cohesity Cluster, the Cluster generates Audit Logs. If no parameters are specified, all logs currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_cluster_audit_logs(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Filter by matching a substring in entity name or details of the Cluster audit log.
        :param int start_index: Specifies an index number that can be used to return subsets of items in multiple requests. Break up the items to return into multiple requests by setting pageCount and startIndex to return a subsets of items in the search result. For example, set startIndex to 0 to get the first set of pageCount items for the first request. Increment startIndex by pageCount to get the next set of pageCount items for a next request. Continue until all items are returned and therefore the total number of returned items is equal to totalCount. Default value is 0.
        :param list[str] user_names: Filter by user names who cause the actions that generate Cluster Audit Logs.
        :param list[str] entity_types: Filter by entity types involved in the actions that generate the Cluster audit logs, such as User, Protection Job, View, etc. For a complete list, see the Category drop-down in the Admin > Audit Logs page of the Cohesity Dashboard.
        :param int start_time_usecs: Filter by a start time. Only Cluster audit logs that were generated after the specified time are returned. Specify the start time as a Unix epoch Timestamp (in microseconds).
        :param int end_time_usecs: Filter by a end time specified as a Unix epoch Timestamp (in microseconds). Only Cluster audit logs that were generated before the specified end time are returned.
        :param int page_count: Limit the number of items to return in the response for pagination purposes. Default value is 1000.
        :param str output_format: Specifies the format of the output such as csv and json. If not specified, the json format is returned. If csv is specified, a comma-separated list with a heading row is returned.
        :param list[str] domains: Filter by domains of users who cause the actions that trigger Cluster audit logs.
        :param list[str] actions: Filter by the actions that generate Cluster audit logs such as Activate, Cancel, Clone, Create, etc. For a complete list, see the Actions drop-down in the Admin > Audit Logs page of the Cohesity Dashboard.
        :return: ClusterAuditLogsSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.search_cluster_audit_logs_with_http_info(**kwargs)
        else:
            (data) = self.search_cluster_audit_logs_with_http_info(**kwargs)
            return data

    def search_cluster_audit_logs_with_http_info(self, **kwargs):
        """
        List the cluster audit logs on the Cohesity Cluster that match the filter criteria specified using parameters.
        When actions (such as a login or a Job being paused) occur on the Cohesity Cluster, the Cluster generates Audit Logs. If no parameters are specified, all logs currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_cluster_audit_logs_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Filter by matching a substring in entity name or details of the Cluster audit log.
        :param int start_index: Specifies an index number that can be used to return subsets of items in multiple requests. Break up the items to return into multiple requests by setting pageCount and startIndex to return a subsets of items in the search result. For example, set startIndex to 0 to get the first set of pageCount items for the first request. Increment startIndex by pageCount to get the next set of pageCount items for a next request. Continue until all items are returned and therefore the total number of returned items is equal to totalCount. Default value is 0.
        :param list[str] user_names: Filter by user names who cause the actions that generate Cluster Audit Logs.
        :param list[str] entity_types: Filter by entity types involved in the actions that generate the Cluster audit logs, such as User, Protection Job, View, etc. For a complete list, see the Category drop-down in the Admin > Audit Logs page of the Cohesity Dashboard.
        :param int start_time_usecs: Filter by a start time. Only Cluster audit logs that were generated after the specified time are returned. Specify the start time as a Unix epoch Timestamp (in microseconds).
        :param int end_time_usecs: Filter by a end time specified as a Unix epoch Timestamp (in microseconds). Only Cluster audit logs that were generated before the specified end time are returned.
        :param int page_count: Limit the number of items to return in the response for pagination purposes. Default value is 1000.
        :param str output_format: Specifies the format of the output such as csv and json. If not specified, the json format is returned. If csv is specified, a comma-separated list with a heading row is returned.
        :param list[str] domains: Filter by domains of users who cause the actions that trigger Cluster audit logs.
        :param list[str] actions: Filter by the actions that generate Cluster audit logs such as Activate, Cancel, Clone, Create, etc. For a complete list, see the Actions drop-down in the Admin > Audit Logs page of the Cohesity Dashboard.
        :return: ClusterAuditLogsSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'start_index', 'user_names', 'entity_types', 'start_time_usecs', 'end_time_usecs', 'page_count', 'output_format', 'domains', 'actions']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_cluster_audit_logs" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/public/auditLogs/cluster'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'search' in params:
            query_params['search'] = params['search']
        if 'start_index' in params:
            query_params['startIndex'] = params['start_index']
        if 'user_names' in params:
            query_params['userNames'] = params['user_names']
        if 'entity_types' in params:
            query_params['entityTypes'] = params['entity_types']
        if 'start_time_usecs' in params:
            query_params['startTimeUsecs'] = params['start_time_usecs']
        if 'end_time_usecs' in params:
            query_params['endTimeUsecs'] = params['end_time_usecs']
        if 'page_count' in params:
            query_params['pageCount'] = params['page_count']
        if 'output_format' in params:
            query_params['outputFormat'] = params['output_format']
        if 'domains' in params:
            query_params['domains'] = params['domains']
        if 'actions' in params:
            query_params['actions'] = params['actions']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ClusterAuditLogsSearchResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
