# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.active_alerts_stats import ActiveAlertsStats
from cohesity_management_sdk.models.get_consumer_stats_result import GetConsumerStatsResult
from cohesity_management_sdk.models.file_distribution_stats import FileDistributionStats
from cohesity_management_sdk.models.protection_runs_stats import ProtectionRunsStats
from cohesity_management_sdk.models.last_protection_run_stats import LastProtectionRunStats
from cohesity_management_sdk.models.protected_objects_summary import ProtectedObjectsSummary
from cohesity_management_sdk.models.restore_stats import RestoreStats
from cohesity_management_sdk.models.storage_stats import StorageStats
from cohesity_management_sdk.models.get_tenant_stats_result import GetTenantStatsResult
from cohesity_management_sdk.models.vault_stats import VaultStats
from cohesity_management_sdk.models.vault_provider_stats_info import VaultProviderStatsInfo
from cohesity_management_sdk.models.vault_run_stats_summary import VaultRunStatsSummary
from cohesity_management_sdk.models.get_view_box_stats_result import GetViewBoxStatsResult
from cohesity_management_sdk.models.view_stats_snapshot import ViewStatsSnapshot
from cohesity_management_sdk.models.view_protocol_stats import ViewProtocolStats
from cohesity_management_sdk.exceptions.error_exception import ErrorException
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class StatsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(StatsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_active_alerts_stats(self, start_time_usecs, end_time_usecs):
        """Does a GET request to /public/stats/alerts.

        Compute the statistics on the active Alerts generated on the cluster
        based on the provided time interval.

        Args:
            start_time_usecs (long|int): Specifies the start time Unix time
                epoch in microseconds from which the active alerts stats are
                computed.
            end_time_usecs (long|int): Specifies the end time Unix time epoch
                in microseconds to which the active alerts stats are
                computed.

        Returns:
            ActiveAlertsStats: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_active_alerts_stats called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_active_alerts_stats.')
            self.validate_parameters(start_time_usecs=start_time_usecs,
                                     end_time_usecs=end_time_usecs)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_active_alerts_stats.')
            _url_path = '/public/stats/alerts'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_active_alerts_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_active_alerts_stats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_active_alerts_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_active_alerts_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, ActiveAlertsStats.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_consumer_stats(self,
                           consumer_type=None,
                           consumer_id_list=None,
                           consumer_entity_id_list=None,
                           fetch_view_box_name=None,
                           fetch_tenant_name=None,
                           fetch_protection_policy=None,
                           fetch_protection_environment=None,
                           view_boxes_id_list=None,
                           organizations_id_list=None,
                           tenant_ids=None,
                           include_service_provider=None,
                           msecs_before_current_time_to_compare=None,
                           max_count=None,
                           cookie=None):
        """Does a GET request to /public/stats/consumers.

        Gets the statistics of consumers.

        Args:
            consumer_type (ConsumerTypeGetConsumerStatsEnum, optional):
                Specifies the consumer type. Type of the consumer can be one
                of the following three,  'kViews', indicates the stats info of
                Views used per organization (tenant) per view box (storage
                domain). 'kProtectionRuns', indicates the stats info of
                Protection Runs used per organization (tenant) per view box
                (storage domain). 'kReplicationRuns', indicates the stats info
                of Replication In used per organization (tenant) per view box
                (storage domain).
            consumer_id_list (list of long|int, optional): Specifies a list of
                consumer ids.
            consumer_entity_id_list (list of string, optional): Specifies a
                list of consumer entity ids. If this field is specified, each
                entity id must corresponds to the id in 'ConsumerIdList' in
                the same index, and the length of 'ConsumerEntityIdList' and
                'ConsumerIdList' must be the same.
            fetch_view_box_name (bool, optional): Specifies whether to fetch
                view box (storage domain) name for each consumer.
            fetch_tenant_name (bool, optional): Specifies whether to fetch
                tenant (organization) name for each consumer.
            fetch_protection_policy (bool, optional): Specifies whether to
                fetch protection policy for each consumer. This field is
                applicable only if 'consumerType' is 'kProtectionRuns' or
                'kReplicationRuns'.
            fetch_protection_environment(bool, optional): Specifies whether
                to fetch protection environment for each consumer. This field
                is applicable only if 'consumerType' is 'kProtectionRuns' or
                'kReplicationRuns'.
            view_boxes_id_list (list of long|int, optional): Specifies a list
                of view boxes (storage domain) id.
            organizations_id_list (list of string, optional): Specifies a list
                of organizations (tenant) id.
            tenant_ids (list of string, optional): Specifies a list of
                organizations (tenant) id. This field is added to allow
                tenantIds json tag. This list will be concatenated with
                TenantsIdList to form full list of tenantsIdList.
            include_service_provider(bool, optional): Specifies whether to
                fetch the consumption of external service providers. These
                information will be listed as a unique organization (tenant) in
                response. By default it is false.
            msecs_before_current_time_to_compare (long|int, optional): Specifies
                the time in msecs before current time to compare with.
            max_count (long|int, optional): Specifies a limit on the number of
                stats groups returned.
            cookie (string, optional): Specifies the opaque string returned in
                the previous response. If this is set, next set of active
                opens just after the previous response are returned. If this
                is not set, first set of active opens are returned.

        Returns:
            GetConsumerStatsResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_consumer_stats called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_consumer_stats.')
            _url_path = '/public/stats/consumers'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'consumerType': consumer_type,
                'consumerIdList': consumer_id_list,
                'consumerEntityIdList': consumer_entity_id_list,
                'fetchViewBoxName': fetch_view_box_name,
                'fetchTenantName': fetch_tenant_name,
                'fetchProtectionPolicy': fetch_protection_policy,
                'fetchProtectionEnvironment': fetch_protection_environment,
                'viewBoxesIdList': view_boxes_id_list,
                'organizationsIdList': organizations_id_list,
                'tenantIds': tenant_ids,
                'includeServiceProvider': include_service_provider,
                'maxCount': max_count,
                'cookie': cookie,
                'msecsBeforeCurrentTimeToCompare': msecs_before_current_time_to_compare
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_consumer_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_consumer_stats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_consumer_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_consumer_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                GetConsumerStatsResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_file_distribution_stats(self, entity_type):
        """Does a GET request to /public/stats/files.

        Compute the file distribution statistics on a given entity like
        cluster or storage domain.

        Args:
            entity_type (EntityTypeGetFileDistributionStatsEnum): Specifies
                the entity type on which file distribution stats are
                computed.

        Returns:
            list of FileDistributionStats: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_file_distribution_stats called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_file_distribution_stats.'
            )
            self.validate_parameters(entity_type=entity_type)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_file_distribution_stats.')
            _url_path = '/public/stats/files'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'entityType': entity_type}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_file_distribution_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_file_distribution_stats.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_file_distribution_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_file_distribution_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                FileDistributionStats.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protection_runs_stats(self, status, start_time_usecs,
                                  end_time_usecs):
        """Does a GET request to /public/stats/protectionRuns.

        Compute the statistics of the Protection Runs based on the input
        filters. This endpoint provides a snapshot of count of Protection Runs
        of a specified status on a specified time interval.

        Args:
            status (StatusGetProtectionRunsStatsEnum): Specifies the
                Protection Run status for which stats has to be computed.
            start_time_usecs (long|int): Specifies the start time in Unix
                timestamp epoch in microseconds where the end time of the
                Protection Run is greater than the specified value.
            end_time_usecs (long|int): Specifies the end time in Unix
                timestamp epoch in microseconds where the end time of the
                Protection Run is lesser than the specified value.

        Returns:
            ProtectionRunsStats: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_runs_stats called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_protection_runs_stats.'
            )
            self.validate_parameters(status=status,
                                     start_time_usecs=start_time_usecs,
                                     end_time_usecs=end_time_usecs)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_protection_runs_stats.')
            _url_path = '/public/stats/protectionRuns'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'status': status,
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_protection_runs_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protection_runs_stats.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_protection_runs_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_protection_runs_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ProtectionRunsStats.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_last_protection_run_stats(self,
                                      from_time_secs=None,
                                      to_time_secs=None):
        """Does a GET request to /public/stats/protectionRuns/lastRun.

        Compute stats on last Protection Run for every job.

        Args:
            from_time_secs (long|int, optional): Specifies the time in Unix
                timestamp epoch in microsecond which filters all the runs
                started after this value. If not specified, this will be set
                to 24 hours prior to toTimeUsecs parameter.
            to_time_secs (long|int, optional): Specifies the time in Unix
                timestamp epoch in microsecond which filters all the runs
                started before this value. If not specified, this will
                be set to 24 hours ahead of fromTimeUsecs parameter.

        Returns:
            LastProtectionRunStats: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_last_protection_run_stats called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_last_protection_run_stats.')
            _url_path = '/public/stats/protectionRuns/lastRun'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'fromTimeUsecs': from_time_secs,
                'toTimeUsecs': to_time_secs
                }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_last_protection_run_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_last_protection_run_stats.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_last_protection_run_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_last_protection_run_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                LastProtectionRunStats.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protected_objects_summary(self, exclude_types=None):
        """Does a GET request to /public/stats/protectionSummary.

        Computes the protected objects summary on the cluster.

        Args:
            exclude_types (list of ExcludeTypeGetProtectedObjectsSummaryEnum,
                optional): Specifies the environment types to exclude.

        Returns:
            ProtectedObjectsSummary: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protected_objects_summary called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_protected_objects_summary.')
            _url_path = '/public/stats/protectionSummary'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'excludeTypes': exclude_types}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_protected_objects_summary.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protected_objects_summary.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_protected_objects_summary')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_protected_objects_summary.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ProtectedObjectsSummary.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_restore_stats(self, start_time_usecs, end_time_usecs):
        """Does a GET request to /public/stats/restores.

        Compute the statistics on the Restore tasks on the cluster based on
        the provided time interval.

        Args:
            start_time_usecs (long|int): Specifies the start time Unix time
                epoch in microseconds from which the restore stats are
                computed.
            end_time_usecs (long|int): Specifies the end time Unix time epoch
                in microseconds to which the restore stats are computed.

        Returns:
            RestoreStats: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_restore_stats called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_restore_stats.')
            self.validate_parameters(start_time_usecs=start_time_usecs,
                                     end_time_usecs=end_time_usecs)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_restore_stats.')
            _url_path = '/public/stats/restores'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_restore_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_restore_stats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_restore_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_restore_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RestoreStats.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_storage_stats(self):
        """Does a GET request to /public/stats/storage.

        Computes the storage stats on the cluster.

        Returns:
            StorageStats: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_storage_stats called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_storage_stats.')
            _url_path = '/public/stats/storage'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_storage_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_storage_stats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_storage_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_storage_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              StorageStats.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_tenant_stats(self,
                         consumer_type=None,
                         skip_group_by_tenant=None,
                         max_count=None,
                         cookie=None,
                         output_format=None,
                         view_boxes_id_list=None,
                         organizations_id_list=None,
                         tenant_ids=None,
                         include_service_provider=None):
        """Does a GET request to /public/stats/tenants.

        Gets the statistics of organizations (tenant).

        Args:
            consumer_type (ConsumerTypeGetTenantStatsEnum, optional):
                Specifies the consumer type. Type of the consumer can be one
                of the following three,  'kViews', indicates the stats info of
                Views used per organization (tenant) per view box (storage
                domain). 'kProtectionRuns', indicates the stats info of
                Protection Runs used per organization (tenant) per view box
                (storage domain). 'kReplicationRuns', indicates the stats info
                of Replication In used per organization (tenant) per view box
                (storage domain). 'kViewProtectionRuns', indicates the stats
                info of View Protection Runs used per organization (tenant)
                per view box (storage domain).
            skip_group_by_tenant (bool, optional): Specifies if we should skip
                grouping by tenant. If false, and tenant has multiple storage
                domains, then the stats for the storage domains will be
                aggregated. If true, then the response will return each
                storage domain cross tenant independently.
            max_count (long|int, optional): Specifies a limit on the number of
                stats groups returned.
            cookie (string, optional): Specifies the opaque string returned in
                the previous response. If this is set, next set of active
                opens just after the previous response are returned. If this
                is not set, first set of active opens are returned.
            output_format (string, optional): Specifies what format to return
                the data in. Defaults to proto, but can select other options
                like csv.
            view_boxes_id_list (list of long|int, optional): Specifies a list
                of view boxes (storage domain) id.
            organizations_id_list (list of string, optional): Specifies a list
                of organizations (tenant) id.
            tenant_ids (list of string, optional): Specifies a list of
                organizations (tenant) id. This field is added to allow
                tenantIds json tag. This list will be concatenated with
                TenantsIdList to form full list of tenantsIdList.
            include_service_provider(bool, optional): Specifies whether to
                fetch the consumption of external service providers. These
                information will be listed as a unique organization (tenant) in
                response. By default it is false.

        Returns:
            GetTenantStatsResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_tenant_stats called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_tenant_stats.')
            _url_path = '/public/stats/tenants'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'consumerType': consumer_type,
                'skipGroupByTenant': skip_group_by_tenant,
                'maxCount': max_count,
                'cookie': cookie,
                'outputFormat': output_format,
                'viewBoxesIdList': view_boxes_id_list,
                'organizationsIdList': organizations_id_list,
                'tenantIds': tenant_ids,
                'includeServiceProvider': include_service_provider
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_tenant_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_tenant_stats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_tenant_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_tenant_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                GetTenantStatsResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_vault_stats(self):
        """Does a GET request to /public/stats/vaults.

        Compute the statistics on vaults.

        Returns:
            VaultStats: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_vault_stats called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_vault_stats.')
            _url_path = '/public/stats/vaults'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_vault_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_vault_stats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_vault_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_vault_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              VaultStats.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_vault_provider_stats(self, run_type):
        """Does a GET request to /public/stats/vaults/providers.

        Compute the size and count of entities on vaults.

        Args:
            run_type (RunTypeGetVaultProviderStatsEnum): Specifies the type of
                the runs.

        Returns:
            list of VaultProviderStatsInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_vault_provider_stats called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_vault_provider_stats.')
            self.validate_parameters(run_type=run_type)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_vault_provider_stats.')
            _url_path = '/public/stats/vaults/providers'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'runType': run_type}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_vault_provider_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_vault_provider_stats.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_vault_provider_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_vault_provider_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                VaultProviderStatsInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_vault_run_stats(self, run_type, start_time_usecs, end_time_usecs,
                            interval):
        """Does a GET request to /public/stats/vaults/runs.

        Compute the statistics on protection runs to or from a vault and
        return a trend line of the result.

        Args:
            run_type (RunTypeGetVaultRunStatsEnum): Specifies the type of the
                run.
            start_time_usecs (long|int): Specifies the start time Unix time
                epoch in microseconds from which the vault run stats are
                computed.
            end_time_usecs (long|int): Specifies the end time Unix time epoch
                in microseconds to which the vault run stats are computed.
            interval (IntervalEnum): Specifies the interval by which runs will
                be grouped together in the returned trend line.

        Returns:
            VaultRunStatsSummary: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_vault_run_stats called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_vault_run_stats.')
            self.validate_parameters(run_type=run_type,
                                     start_time_usecs=start_time_usecs,
                                     end_time_usecs=end_time_usecs,
                                     interval=interval)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_vault_run_stats.')
            _url_path = '/public/stats/vaults/runs'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'runType': run_type,
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs,
                'interval': interval
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_vault_run_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_vault_run_stats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_vault_run_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_vault_run_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                VaultRunStatsSummary.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_view_box_stats(self,
                           view_boxes_id_list=None,
                           organizations_id_list=None,
                           tenant_ids=None,
                           include_service_provider=None):
        """Does a GET request to /public/stats/viewBoxes.

        Gets the statistics of view boxes (storage domain).

        Args:
            view_boxes_id_list (list of long|int, optional): Specifies a list
                of view boxes (storage domain) id.
            organizations_id_list (list of string, optional): Specifies a list
                of organizations (tenant) id.
            tenant_ids (list of string, optional): Specifies a list of
                organizations (tenant) id. This field is added to allow
                tenantIds json tag. This list will be concatenated with
                TenantsIdList to form full list of tenantsIdList.
            include_service_provider(bool, optional): Specifies whether to
                fetch the consumption of external service providers. These
                information will be listed as a unique organization (tenant) in
                response. By default it is false.

        Returns:
            GetViewBoxStatsResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_view_box_stats called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_view_box_stats.')
            _url_path = '/public/stats/viewBoxes'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'viewBoxesIdList': view_boxes_id_list,
                'organizationsIdList': organizations_id_list,
                'tenantIds': tenant_ids,
                'includeServiceProvider': include_service_provider
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_view_box_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_view_box_stats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_view_box_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_view_box_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                GetViewBoxStatsResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_view_stats(self,
                       metric=None,
                       num_top_views=None,
                       protocol=None,
                       last_hours=None):
        """Does a GET request to /public/stats/views.

        Compute the statistics on Views.

        Args:
            metric (MetricEnum, optional): Specifies the metric to which stats
                has to be sorted.
            num_top_views (long|int, optional): Specifies the number of views
                for which stats has to be computed. Specifying this field will
                return the Views sorted in the descending order on the metric
                specified. If specified, minimum value is 1. If not specified,
                all views will be returned. If metric is not specified, this
                parameter must also not be specified.
            last_hours (long|int, optional): Specifies the last hours of stats
                to sort.
            protocol (ProtocolViewStatsEnum, optional): Specifies the protocol
                to sort.

        Returns:
            ViewStatsSnapshot: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_view_stats called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_view_stats.')
            _url_path = '/public/stats/views'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'metric': metric,
                'numTopViews': num_top_views,
                'lastHours': last_hours,
                'protocol': protocol
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_view_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_view_stats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_view_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_view_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, ViewStatsSnapshot.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_view_protocol_stats(self):
        """Does a GET request to /public/stats/views/protocols.

        Compute the protocol statistics on Views.

        Returns:
            list of ViewProtocolStats: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_view_protocol_stats called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_view_protocol_stats.')
            _url_path = '/public/stats/views/protocols'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_view_protocol_stats.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_view_protocol_stats.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_view_protocol_stats')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_view_protocol_stats.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, ViewProtocolStats.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
