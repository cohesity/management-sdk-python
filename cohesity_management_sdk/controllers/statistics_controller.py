# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.entity_proto import EntityProto
from cohesity_management_sdk.models.entity_schema_proto import EntitySchemaProto
from cohesity_management_sdk.models.time_series_schema_response import TimeSeriesSchemaResponse
from cohesity_management_sdk.models.metric_data_block import MetricDataBlock
from cohesity_management_sdk.models.task import Task
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class StatisticsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(StatisticsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_entities(self,
                     schema_name,
                     include_aggr_metric_sources=None,
                     metric_names=None,
                     max_entities=None,
                     view_name=None):
        """Does a GET request to /public/statistics/entities.

        An entity is an object found on the Cohesity Cluster, such as a disk
        or a
        Node.
        In the Cohesity Dashboard, similar functionality is provided in
        Advanced
        Diagnostics.

        Args:
            schema_name (string): Specifies the entity schema to search for
                entities.
            include_aggr_metric_sources (bool, optional): Specifies whether to
                include the sources of aggregate metrics of an entity.
            metric_names (list of string, optional): Specifies the list of
                metric names to return such as 'kRandomIos' which corresponds
                to 'Random IOs' in Advanced Diagnostics of the Cohesity
                Dashboard.
            max_entities (int, optional): Specifies the maximum entities
                returned in the result. By default this field is 500.
            view_name (string, optional): Specifies a view name, only view
                entities which have name containing the specified name will
                be returned.

        Returns:
            list of EntityProto: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_entities called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_entities.')
            self.validate_parameters(schema_name=schema_name)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_entities.')
            _url_path = '/public/statistics/entities'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'schemaName': schema_name,
                'includeAggrMetricSources': include_aggr_metric_sources,
                'metricNames': metric_names,
                'maxEntities': max_entities,
                'viewName': view_name
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_entities.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_entities.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_entities')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_entities.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              EntityProto.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_entities_schema(self, schema_names=None, metric_names=None):
        """Does a GET request to /public/statistics/entitiesSchema.

        An entity schema specifies the meta-data associated with entity such
        as
        the list of attributes and a time series of data.
        For example, for a Disk entity, the entity schema specifies the Node
        that is
        using this Disk, the type of the Disk, and Metrics about the Disk such
        as Space
        Usage, Read IOs and Write IOs. Metrics define data points (time series
        data)
        to track over a period of time for a specific interval.
        If no parameters are specified, all entity schemas found on the
        Cohesity
        Cluster are returned.
        Specifying parameters filters the results that are returned.
        In the Cohesity Dashboard, similar functionality is provided in
        Advanced
        Diagnostics.

        Args:
            schema_names (list of string, optional): Specifies the list of
                schema names to filter by such as 'kIceboxJobVaultStats' which
                corresponds to 'External Target Job Stats' in Advanced
                Diagnostics of the Cohesity Dashboard.
            metric_names (list of string, optional): Specifies the list of
                metric names to filter by such as 'kRandomIos' which
                corresponds to 'Random IOs' in Advanced Diagnostics of the
                Cohesity Dashboard.

        Returns:
            list of EntitySchemaProto: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_entities_schema called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_entities_schema.')
            _url_path = '/public/statistics/entitiesSchema'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'schemaNames': schema_names,
                'metricNames': metric_names
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_entities_schema.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_entities_schema.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_entities_schema')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_entities_schema.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, EntitySchemaProto.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_entity_schema_by_name(self, schema_name):
        """Does a GET request to /public/statistics/entitiesSchema/{schemaName}.

        An entity schema specifies the meta-data associated with entity such
        as the
        list of attributes and a time series of data.
        For example, for a Disk entity, the entity schema specifies the Node
        that is
        using this Disk, the type of the Disk, and Metrics about the Disk such
        as
        Space Usage, Read IOs and Write IOs. Metrics define data points (time
        series
        data) to track over a period of time for a specific interval.
        In the Cohesity Dashboard, similar functionality is provided in
        Advanced
        Diagnostics.

        Args:
            schema_name (string): Name of the Schema

        Returns:
            list of EntitySchemaProto: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_entity_schema_by_name called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_entity_schema_by_name.'
            )
            self.validate_parameters(schema_name=schema_name)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_entity_schema_by_name.')
            _url_path = '/public/statistics/entitiesSchema/{schemaName}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'schemaName': schema_name})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_entity_schema_by_name.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_entity_schema_by_name.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_entity_schema_by_name')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_entity_schema_by_name.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, EntitySchemaProto.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_time_series_schema(self, entity_type, entity_id, entity_name):
        """Does a GET request to /public/statistics/timeSeriesSchema.

        Gets the Apollo schema information for an entity to list a series of
        data
        points.

        Args:
            entity_type (EntityTypeEnum): Specifies the type of the entity.
                The following entity types are available: cluster, viewbox.
                EntityType represents the various values for the entity type.
                'Cluster' indicates entity type of Cluster. 'StorageDomain'
                indicates entity type of Storage Domain.
            entity_id (long|int): Specifies the id of the entity.
            entity_name (string): Specifies the name of the entity.

        Returns:
            TimeSeriesSchemaResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_time_series_schema called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_time_series_schema.')
            self.validate_parameters(entity_type=entity_type,
                                     entity_id=entity_id,
                                     entity_name=entity_name)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_time_series_schema.')
            _url_path = '/public/statistics/timeSeriesSchema'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'entityType': entity_type,
                'entityId': entity_id,
                'entityName': entity_name
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_time_series_schema.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_time_series_schema.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_time_series_schema')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_time_series_schema.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                TimeSeriesSchemaResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_time_series_stats(self,
                              schema_name,
                              metric_name,
                              start_time_msecs,
                              entity_id=None,
                              entity_id_list=None,
                              end_time_msecs=None,
                              rollup_function=None,
                              rollup_interval_secs=None,
                              prorate_data_points=None):
        """Does a GET request to /public/statistics/timeSeriesStats.

        A Metric specifies a data point (such as CPU usage and IOPS) to track
        over a
        period of time.
        For example for a disk in the Cluster, you can report on the 'Disk
        Health'
        (kDiskAwaitTimeMsecs) Metric of the 'Disk Health Metrics'
        (kSentryDiskStats)
        Schema for the last week.
        You must specify the 'k' names as input and not the descriptive
        names.
        You must also specify the id of the entity that you are reporting on
        such as
        a Cluster, disk drive, job, etc.
        Get the entityId by running the GET /public/statistics/entities
        operation.
        In the Cohesity Dashboard, similar functionality is provided in
        Advanced
        Diagnostics.

        Args:
            schema_name (string): Specifies the name of entity schema such as
                'kIceboxJobVaultStats'.
            metric_name (string): Specifies the name of the metric such as the
                'kDiskAwaitTimeMsecs' which is displayed as 'Disk Health' in
                Advanced Diagnostics of the Cohesity Dashboard.
            start_time_msecs (long|int): Specifies the start time for the
                series of metric data. Specify the start time as a Unix epoch
                Timestamp (in milliseconds).
            entity_id (string, optional): Specifies the id of the entity
                represented as a string. Get the entityId by running the GET
                public/statistics/entities operation.
            entity_id_list (list of string, optional): Specifies an entity id
                list represented as a string. The stats result will be the sum
                over all these entities. If both EntityIdList and EntityId are
                specified, EntityId will be ignored.
            end_time_msecs (long|int, optional): Specifies the end time for
                the series of metric data. Specify the end time as a Unix
                epoch Timestamp (in milliseconds). If not specified, the data
                points up to the current time are returned.
            rollup_function (string, optional): Specifies the rollup function
                to apply to the data points for the time interval specified by
                rollupInternalSecs. The following rollup functions are
                available: sum, average, count, max, min, median,
                percentile95, latest, and rate. For more information about the
                functions, see the Advanced Diagnostics in the Cohesity online
                help. If not specified, raw data is returned.
            rollup_interval_secs (int, optional): Specifies the time interval
                granularity (in seconds) for the specified rollup function.
                Only specify a value if Rollup function is also specified.
            prorate_data_points (bool, optional): Specifies to create pro
                rated data point for every rollup interval instead of
                returning the actual raw data points. This should be used
                only when rollup function is provided.

        Returns:
            MetricDataBlock: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_time_series_stats called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_time_series_stats.')
            self.validate_parameters(schema_name=schema_name,
                                     metric_name=metric_name,
                                     start_time_msecs=start_time_msecs)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_time_series_stats.')
            _url_path = '/public/statistics/timeSeriesStats'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'schemaName': schema_name,
                'metricName': metric_name,
                'startTimeMsecs': start_time_msecs,
                'entityId': entity_id,
                'entityIdList': entity_id_list,
                'endTimeMsecs': end_time_msecs,
                'rollupFunction': rollup_function,
                'rollupIntervalSecs': rollup_interval_secs,
                'prorateDataPoints': prorate_data_points
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_time_series_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_time_series_stats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_time_series_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_time_series_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              MetricDataBlock.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_tasks(self,
                  task_paths=None,
                  include_finished_tasks=None,
                  start_time_seconds=None,
                  end_time_seconds=None,
                  max_tasks=None,
                  exclude_sub_tasks=None,
                  attributes=None):
        """Does a GET request to /public/tasks/status.

        Gets the progress and status of tasks.

        Args:
            task_paths (list of string, optional): Specifies a list of tasks
                path by which to filter the results. Otherwise all of the
                tasks will be returned.
            include_finished_tasks (bool, optional): Specifies whether or not
                to include finished tasks. By default, Pulse will only include
                unfinished tasks.
            start_time_seconds (long|int, optional): Specifies a start time by
                which to filter tasks. Including a value here will result in
                tasks only being included if they started after the time
                specified.
            end_time_seconds (long|int, optional): Specifies an end time by
                which to filter tasks. Including a value here will result in
                tasks only being included if the ended before this time.
            max_tasks (int, optional): Specifies the maximum number of tasks
                to display. Defaults to 100.
            exclude_sub_tasks (bool, optional): Specifies whether or not to
                include subtasks. By default all subtasks of any task matching
                a query will be returned.
            attributes (list of string, optional): If specified, tasks
                matching the current query are further filtered by these
                KeyValuePairs. This gives client an ability to search by
                custom attributes that they specified during the task
                creation. Only the Tasks having 'all' of the specified
                key=value pairs will be returned. Attributes passed in should
                be separated by commas and each must follow the pattern
                "name:type:value". Valid types are "kInt64", "kDouble",
                "kString", and "kBytes".

        Returns:
            list of Task: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_tasks called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_tasks.')
            _url_path = '/public/tasks/status'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'taskPaths': task_paths,
                'includeFinishedTasks': include_finished_tasks,
                'startTimeSeconds': start_time_seconds,
                'endTimeSeconds': end_time_seconds,
                'maxTasks': max_tasks,
                'excludeSubTasks': exclude_sub_tasks,
                'attributes': attributes
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_tasks.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_tasks.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_tasks')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_tasks.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Task.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
