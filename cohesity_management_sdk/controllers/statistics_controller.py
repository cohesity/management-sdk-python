# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.metric_data_block import MetricDataBlock
from cohesity_management_sdk.models.entity_schema import EntitySchema
from cohesity_management_sdk.models.entity import Entity
from cohesity_management_sdk.exceptions.error_error_exception import ErrorErrorException

class StatisticsController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(StatisticsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_time_series_stats(self,
                              schema_name,
                              entity_id,
                              metric_name,
                              start_time_msecs,
                              rollup_function=None,
                              rollup_interval_secs=None,
                              end_time_msecs=None):
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
            entity_id (string): Specifies the id of the entity represented as
                a string. Get the entityId by running the GET
                public/statistics/entities operation.
            metric_name (string): Specifies the name of the metric such as the
                'kDiskAwaitTimeMsecs' which is displayed as 'Disk Health' in
                Advanced Diagnostics of the Cohesity Dashboard.
            start_time_msecs (long|int): Specifies the start time for the
                series of metric data. Specify the start time as a Unix epoch
                Timestamp (in milliseconds).
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
            end_time_msecs (long|int, optional): Specifies the end time for
                the series of metric data. Specify the end time as a Unix
                epoch Timestamp (in milliseconds). If not specified, the data
                points up to the current time are returned.

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
            self.logger.info('Validating required parameters for get_time_series_stats.')
            self.validate_parameters(schema_name=schema_name,
                                     entity_id=entity_id,
                                     metric_name=metric_name,
                                     start_time_msecs=start_time_msecs)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_time_series_stats.')
            _url_path = '/public/statistics/timeSeriesStats'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'schemaName': schema_name,
                'entityId': entity_id,
                'metricName': metric_name,
                'startTimeMsecs': start_time_msecs,
                'rollupFunction': rollup_function,
                'rollupIntervalSecs': rollup_interval_secs,
                'endTimeMsecs': end_time_msecs
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_time_series_stats.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_time_series_stats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_time_series_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_time_series_stats.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, MetricDataBlock.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_entity_schema_by_name(self,
                                  schema_name):
        """Does a GET request to /public/statistics/entitiesSchema/{schemaName}.

        An entity schema specifies the meta-data associated with entity such
        as the
        list of attributes and a time series of data.
        For example for a Disk entity, the entity schema specifies the Node
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
            list of EntitySchema: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_entity_schema_by_name called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for get_entity_schema_by_name.')
            self.validate_parameters(schema_name=schema_name)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_entity_schema_by_name.')
            _url_path = '/public/statistics/entitiesSchema/{schemaName}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'schemaName': schema_name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_entity_schema_by_name.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_entity_schema_by_name.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_entity_schema_by_name')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_entity_schema_by_name.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, EntitySchema.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_entities(self,
                     schema_name,
                     include_aggr_metric_sources=None,
                     metric_names=None):
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

        Returns:
            list of Entity: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_entities called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for get_entities.')
            self.validate_parameters(schema_name=schema_name)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_entities.')
            _url_path = '/public/statistics/entities'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'schemaName': schema_name,
                'includeAggrMetricSources': include_aggr_metric_sources,
                'metricNames': metric_names
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_entities.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_entities.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_entities')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_entities.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, Entity.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_entities_schema(self,
                            schema_names=None,
                            metric_names=None):
        """Does a GET request to /public/statistics/entitiesSchema.

        An entity schema specifies the meta-data associated with entity such
        as
        the list of attributes and a time series of data.
        For example for a Disk entity, the entity schema specifies the Node
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
            list of EntitySchema: Response from the API. Success

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
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'schemaNames': schema_names,
                'metricNames': metric_names
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_entities_schema.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_entities_schema.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_entities_schema')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_entities_schema.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, EntitySchema.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
