# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.analyse_jar_result import AnalyseJarResult
from cohesity_management_sdk.models.applications_wrapper import ApplicationsWrapper
from cohesity_management_sdk.models.map_reduce_info import MapReduceInfo
from cohesity_management_sdk.models.kill_map_reduce_instance_result import KillMapReduceInstanceResult
from cohesity_management_sdk.models.mappers_wrapper import MappersWrapper
from cohesity_management_sdk.models.mapper_info import MapperInfo
from cohesity_management_sdk.models.get_map_reduce_app_runs_params import GetMapReduceAppRunsParams
from cohesity_management_sdk.models.app_run_history import AppRunHistory
from cohesity_management_sdk.models.extract_file_range_result import ExtractFileRangeResult
from cohesity_management_sdk.models.reducer_info import ReducerInfo
from cohesity_management_sdk.models.map_reduce_file_formats import MapReduceFileFormats
from cohesity_management_sdk.models.reducers_wrapper import ReducersWrapper
from cohesity_management_sdk.models.run_map_reduce_params import RunMapReduceParams
from cohesity_management_sdk.models.run_map_reduce_instance_result import RunMapReduceInstanceResult
from cohesity_management_sdk.models.supported_pattern import SupportedPattern
from cohesity_management_sdk.models.upload_mr_jar_view_path_wrapper import UploadMRJarViewPathWrapper    
from cohesity_management_sdk.models.get_mr_jar_upload_path_result import GetMRJarUploadPathResult


class AnalyticsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(AnalyticsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def analyze_jar(self, body=None):
        """Does a POST request to /public/analytics/analyzeJar.

         Returns the result of the jar analysis.

        Args:
            body (AnalyseJarArg, optional): Create Notification Rule
                argument.

        Returns:
            AnalyseJarResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('analyze_jar called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for analyze_jar.')
            _url_path = '/public/analytics/analyzeJar'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for analyze_jar.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for analyze_jar.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='analyze_jar')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for analyze_jar.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              AnalyseJarResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_applications(self):
        """Does a GET request to /public/analytics/apps.

        If no parameters are specified, all Applications currently on
        the Cohesity Cluster are returned.
        Specifying parameters filters the results that are returned.

        List Applications filtered by the specified parameters.

        Returns:
            ApplicationsWrapper: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_applications called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_applications.')
            _url_path = '/public/analytics/apps'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_applications.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_applications.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_applications')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_applications.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)
            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, ApplicationsWrapper.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_application(self, body=None):
        """Does a POST request to /public/analytics/apps.

        Returns the created application.

        Args:
            body (MapReduceInfo): Create an Application.

        Returns:
            MapReduceInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_application called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_application.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_application.')
            _url_path = '/public/analytics/apps'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_application.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_application.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_application')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_application.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              MapReduceInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_application_by_id(self, id):
        """Does a GET request to /public/analytics/apps/{id}

        Returns the Application corresponding to the specified Application
        Id.
        
        List details about a single Application.

        Args:
            id (long|int): TODO: Type description here.

        Returns:
            MapReduceInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_application_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_application_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_application_by_id.')
            _url_path = '/public/analytics/apps/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_application_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_application_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_application_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_application_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              MapReduceInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_application(self, id, body=None):
        """Does a PUT request to /public/analytics/apps/{id}.

        Returns the updated Application.

        Args:
            id (long|int): TODO: Type description here.
            body (MapReduceInfo, optional): TODO: Type description here.

        Returns:
            MapReduceInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_application called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_application.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_application.')
            _url_path = '/public/analytics/apps/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_application.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_application.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_application')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_application.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              MapReduceInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_application(self, id):
        """Does a DELETE request to /public/analytics/apps/{id}.

        Returns delete status upon completion.

        Args:
            id (long|int): TODO: Type description here.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_application called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_application.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_application.')
            _url_path = '/public/analytics/apps/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_application.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_application')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_application.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def cancel_map_reduce_instance_run(self, id):
        """Does a PUT request to /public/analytics/cancelAppInstanceRun/{id}.

        Cancel a specific map reduce instance run.

        Args:
            id (long|int): TODO: Type description here.

        Returns:
            KillMapReduceInstanceResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('cancel_map_reduce_instance_run called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for cancel_map_reduce_instance_run.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for cancel_map_reduce_instance_run.')
            _url_path = '/public/analytics/cancelAppInstanceRun/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for cancel_map_reduce_instance_run.')

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for cancel_map_reduce_instance_run.')
            _request = self.http_client.put(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='cancel_map_reduce_instance_run')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for cancel_map_reduce_instance_run.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              KillMapReduceInstanceResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_mappers(self):
        """Does a GET request to /public/analytics/mappers.

        If no parameters are specified, all Mappers currently on the Cohesity
        Cluster are returned.
        Specifying parameters filters the results that are returned.
    
        List Mappers filtered by the specified parameters.

        Returns:
            list of MappersWrapper: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_mappers called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_mappers.')
            _url_path = '/public/analytics/mappers'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_mappers.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_mappers.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_mappers')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_mappers.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              MappersWrapper.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_mapper(self, body=None):
        """Does a POST request to /public/analytics/mappers.

        Returns the created mapper.

        Args:
            body (MapperInfo): Create an Application.

        Returns:
            MapperInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_mapper called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_mapper.')
            _url_path = '/public/analytics/mappers'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_mapper.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_mapper.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_mapper')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_mapper.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              MapperInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise


    def get_mapper_by_id(self, id):
        """Does a GET request to /public/analytics/mappers/{id}

        Returns the Mapper corresponding to the specified Mapper Id.

        Args:
            id (string): TODO: Type description here.

        Returns:
            MapperInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_mapper_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_mapper_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_mapper_by_id.')
            _url_path = '/public/analytics/mappers/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_mapper_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_mapper_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_mapper_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_mapper_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              MapperInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_mapper(self, id, body=None):
        """Does a PUT request to /public/analytics/apps/{id}.

        Returns the updated Application.

        Args:
            id (long|int): TODO: Type description here.
            body (MapperInfo): TODO: Type description here.

        Returns:
            MapperInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_mapper called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_mapper.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_mapper.')
            _url_path = '/public/analytics/apps/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_mapper.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_mapper.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_mapper')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_mapper.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              MapperInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_mapper(self, id):
        """Does a DELETE request to /public/analytics/mappers/{id}

        Returns delete status upon completion.

        Args:
            id (long|int): TODO: Type description here.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_mapper called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_mapper.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_mapper.')
            _url_path = '/public/analytics/mappers/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_mapper.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_mapper')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_mapper.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_map_reduce_instance_run(self, id):
        """Does a DELETE request to /public/analytics/mrAppRun/{id}

        Delete a Map-Reduce Application Instance Run.

        Returns delete status upon completion.

        Args:
            id (long|int): TODO: Type description here.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_map_reduce_instance_run called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_map_reduce_instance_run.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_map_reduce_instance_run.')
            _url_path = '/public/analytics/mrAppRun/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_map_reduce_instance_run.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_map_reduce_instance_run')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_map_reduce_instance_run.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_map_reduce_app_runs(self, body=None):
        """Does a GET request to /public/analytics/mrAppRuns.

        List map reduce application runs filtered by the specified parameters.

        If no parameters are specified, all map reduce application instance
        runs currently on the Cohesity Cluster are returned.
        Specifying parameters filters the results that are returned.

        Args:
            body(GetMapReduceAppRunsParams): TODO Type description here.

        Returns:
            list of AppRunHistory: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_map_reduce_app_runs called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_map_reduce_app_runs.')
            _url_path = '/public/analytics/mrAppRuns'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'body': body}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_map_reduce_app_runs.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_map_reduce_app_runs.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_map_reduce_app_runs')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_map_reduce_app_runs.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                AppRunHistory.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def download_mr_base_jar(self):
        """Does a GET request to /public/analytics/mrBaseJar.

        Returns a struct containing the map reduce base jar from the cluster.

        Returns:
            ExtractFileRangeResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('download_mr_base_jar called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for download_mr_base_jar.')
            _url_path = '/public/analytics/mrBaseJar'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for download_mr_base_jar.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for download_mr_base_jar.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='download_mr_base_jar')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for download_mr_base_jar.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ExtractFileRangeResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_map_reduce_file_formats(self,
                                    result_file_path=None,
                                    storage_domain_id=None,
                                    view_name=None):
        """Does a GET request to /public/analytics/mrFileFormats.

        The Analytics workbench generates output files from map reduce
        instances run for a particular application. This API returns the
        output file formats available to the user for download.

        Args:
            result_file_path (string, optional): Specifies the path where the
                map reduce instance has the result. file generated.
            storage_domain_id (int, optional): Specifies the ID of the storage
                domain.
            view_name (int, optional): Specifies the maximum number of NLM
                locks to return in the response. This field cannot be set
                above 1000. If this is not set, maximum of 1000 entries are
                returned.

        Returns:
            MapReduceFileFormats: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_map_reduce_file_formats called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_map_reduce_file_formats.')
            _url_path = '/public/analytics/mrFileFormats'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'resultFilePath': result_file_path,
                'storageDomainId': storage_domain_id,
                'viewName': view_name
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_map_reduce_file_formats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_map_reduce_file_formats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_map_reduce_file_formats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_map_reduce_file_formats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                MapReduceFileFormats.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def download_mr_output_files(self,
                                is_nfs_file=None,
                                partition_id=None,
                                view_box_id=None,
                                view_name=None,
                                file_path=None,
                                start_offset=None,
                                length_bytes=None):
        """Does a GET request to /public/analytics/mrOutputfiles.

        Returns a struct containing the map reduce instance run output
        files from Yoda.

        Download map reduce base instance run output files from Yoda.

        Args:
            is_nfs_file (bool, optional): If true, then extracts file from
                NFS, else from local file system.
            partition_id (int, optional): Cluster partition id for the file
                to be read.
            view_box_id (int, optional):  View box id for the file to be read.
                Required for nfs files only.
            view_name (string, optional): View name for the file to be read.
                Required for nfs files only.
            file_path (string, optional): filepath of the file on NFS.
            start_offset (int, optional): start offset from where bytes will
                be read.
            length_bytes (int, optional): Number of bytes to be read from
                start_offset.

        Returns:
            ExtractFileRangeResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('download_mr_output_files called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for download_mr_output_files.')
            _url_path = '/public/analytics/mrOutputfiles'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'isNfsFile': is_nfs_file,
                'partitionId': partition_id,
                'viewBoxId': view_box_id,
                'viewName': view_name,
                'filePath': file_path,
                'startOffset':start_offset,
                'lengthBytes': length_bytes
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for download_mr_output_files.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for download_mr_output_files.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='download_mr_output_files')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for download_mr_output_files.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ExtractFileRangeResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_reducers(self):
        """Does a GET request to /public/analytics/reducers.

        If no parameters are specified, all Reducers currently on the Cohesity
        Cluster are returned.
        Specifying parameters filters the results that are returned.

        Returns:
            ReducersWrapper: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_reducers called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_reducers.')
            _url_path = '/public/analytics/reducers'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_reducers.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_reducers.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_reducers')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_reducers.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ReducersWrapper.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_reducer(self, body=None):
        """Does a POST request to /public/analytics/reducers.

        Returns the created reducer.

        Args:
            body (ReducerInfo): Request to create a reducer

        Returns:
            ReducerInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_reducer called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_reducer.')
            _url_path = '/public/analytics/reducers'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_reducer.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_reducer.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_reducer')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_reducer.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ReducerInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_reducer_by_id(self, id):
        """Does a GET request to /public/analytics/reducers/{id}.

        Returns the Reducer corresponding to the specified Reducer Id.

        List details about a single Reducer.

        Args:
            id (long|int): Specifies the reducer id.

        Returns:
            ReducerInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_reducer_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_reducer_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_reducer_by_id.')
            _url_path = '/public/analytics/reducers/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_reducer_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_reducer_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_reducer_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_reducer_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ReducerInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_reducer(self, id, body=None):
        """Does a PUT request to /public/analytics/reducers/{id}.

        Update a Reducer.

        Args:
            id (long|int): TODO: Type description here.
            body (ReducerInfo): Request to update reducer.

        Returns:
            ReducerInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_reducer called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_reducer.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_reducer.')
            _url_path = '/public/analytics/reducers/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_reducer.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_reducer.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_reducer')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_reducer.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ReducerInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_reducer(self, id):
        """Does a DELETE request to /public/analytics/reducers/{id}.

        Returns delete status upon completion.

        Args:
            id (long|int): TODO: Type description here.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_reducer called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_reducer.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_reducer.')
            _url_path = '/public/analytics/reducers/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_reducer.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_reducer')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_reducer.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def run_map_reduce_app_instance(self, body=None):
        """Does a PUT request to /public/analytics/runAppInstance.

        Returns the updated Application.

        Args:
            body (RunMapReduceParams): Request to update a View.

        Returns:
            RunMapReduceInstanceResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('run_map_reduce_app_instance called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for run_map_reduce_app_instance.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for run_map_reduce_app_instance.')
            _url_path = '/public/analytics/runAppInstance'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for run_map_reduce_app_instance.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for run_map_reduce_app_instance.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='run_map_reduce_app_instance')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for run_map_reduce_app_instance.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RunMapReduceInstanceResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_supported_patterns(self, application_id, application_data_type=None):
        """Does a GET request to /public/analytics/supportedPatterns.

        The Analytics workbench has ability to search for patterns which can
        be system defined or can be user defined. This API returns the
        patterns available for search.

        Used to retrieve supported patterns available for search in an
        application.

        Args:
            application_id (list of long|int): Specifies the application Id.
            application_data_type (list of string, optional): Specifies the
                data type for which supported patterns can be fetched.

        Returns:
            list of SupportedPattern: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_supported_patterns called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_application.')
            self.validate_parameters(application_id=application_id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_supported_patterns.')
            _url_path = '/public/analytics/supportedPatterns'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'applicationId': application_id,
                'applicationDataType': application_data_type
                }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_supported_patterns.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_supported_patterns.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_supported_patterns')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_supported_patterns.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              SupportedPattern.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def save_pattern(self, body=None):
        """Does a PUT request to /public/analytics/supportedPatterns.

        The Analytics workbench has ability to search for patterns which can
        be system defined or can be user defined. This API enables the user to
        save patterns for searching.

        Used to save user patterns for search in an application.

        Args:
            body (PatternRequestBody): Request to update a View.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('save_pattern called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for save_pattern.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for save_pattern.')
            _url_path = '/public/analytics/supportedPatterns'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for save_pattern.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for save_pattern.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='save_pattern')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for save_pattern.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)


        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def upload_jar(self):
        """Does a POST request to /public/analytics/uploadJar.

        Returns a struct containing the jar name and local mount path where
        the jar will be uploaded.

        Upload a jar to pre-specified Yoda internal view.

        Returns:
            UploadMRJarViewPathWrapper: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('upload_jar called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for upload_jar.')
            _url_path = '/public/analytics/uploadJar'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for upload_jar.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for upload_jar.')
            _request = self.http_client.post(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='upload_jar')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for upload_jar.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              UploadMRJarViewPathWrapper.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_uploaded_jar(self, body):
        """Does a DELETE request to /public/analytics/uploadJar.

        Returns delete status upon completion.

        Args:
            body (UploadMRJarViewPathWrapper)

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_uploaded_jar called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_uploaded_jar.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_uploaded_jar.')
            _url_path = '/public/analytics/uploadJar'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_uploaded_jar.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_uploaded_jar.')
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='delete_uploaded_jar')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_uploaded_jar.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_mr_upload_jar_path(self):
        """Does a GET request to /public/analytics/uploadJarPath.

        Returns the mounted path to upload Jars.

        Returns:
            GetMRJarUploadPathResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_mr_upload_jar_path called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_mr_upload_jar_path.')
            _url_path = '/public/analytics/uploadJarPath'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_mr_upload_jar_path.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_mr_upload_jar_path.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_mr_upload_jar_path')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_mr_upload_jar_path.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                GetMRJarUploadPathResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
