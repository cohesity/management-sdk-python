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


class SMBFileOpensApi(object):
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

    def close_smb_file_open(self, body, **kwargs):
        """
        Closes an active SMB file open.
        Returns nothing upon success.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.close_smb_file_open(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CloseSmbFileOpenParameters body: Request to close an active SMB file open. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.close_smb_file_open_with_http_info(body, **kwargs)
        else:
            (data) = self.close_smb_file_open_with_http_info(body, **kwargs)
            return data

    def close_smb_file_open_with_http_info(self, body, **kwargs):
        """
        Closes an active SMB file open.
        Returns nothing upon success.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.close_smb_file_open_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CloseSmbFileOpenParameters body: Request to close an active SMB file open. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method close_smb_file_open" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `close_smb_file_open`")

        resource_path = '/public/smbFileOpens'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

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

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_smb_file_opens(self, **kwargs):
        """
        List the active SMB file opens that match the filter criteria specified using parameters.
        If no parameters are specified, all active SMB file opens currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_smb_file_opens(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_path: Specifies the filepath in the view relative to the root filesystem. If this field is specified, viewName field must also be specified.
        :param str view_name: Specifies the name of the View in which to search. If a view name is not specified, all the views in the Cluster is searched. This field is mandatory if filePath field is specified.
        :param int page_count: Specifies the maximum number of active opens to return in the response. This field cannot be set above 1000. If this is not set, maximum of 1000 entries are returned.
        :param str cookie: Specifies the opaque string returned in the previous response. If this is set, next set of active opens just after the previous response are returned. If this is not set, first set of active opens are returned.
        :return: SmbActiveFileOpensResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_smb_file_opens_with_http_info(**kwargs)
        else:
            (data) = self.get_smb_file_opens_with_http_info(**kwargs)
            return data

    def get_smb_file_opens_with_http_info(self, **kwargs):
        """
        List the active SMB file opens that match the filter criteria specified using parameters.
        If no parameters are specified, all active SMB file opens currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_smb_file_opens_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_path: Specifies the filepath in the view relative to the root filesystem. If this field is specified, viewName field must also be specified.
        :param str view_name: Specifies the name of the View in which to search. If a view name is not specified, all the views in the Cluster is searched. This field is mandatory if filePath field is specified.
        :param int page_count: Specifies the maximum number of active opens to return in the response. This field cannot be set above 1000. If this is not set, maximum of 1000 entries are returned.
        :param str cookie: Specifies the opaque string returned in the previous response. If this is set, next set of active opens just after the previous response are returned. If this is not set, first set of active opens are returned.
        :return: SmbActiveFileOpensResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_path', 'view_name', 'page_count', 'cookie']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_smb_file_opens" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/public/smbFileOpens'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'file_path' in params:
            query_params['filePath'] = params['file_path']
        if 'view_name' in params:
            query_params['viewName'] = params['view_name']
        if 'page_count' in params:
            query_params['pageCount'] = params['page_count']
        if 'cookie' in params:
            query_params['cookie'] = params['cookie']

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
                                            response_type='SmbActiveFileOpensResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
