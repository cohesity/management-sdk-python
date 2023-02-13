# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.exceptions.error_exception import ErrorException
from cohesity_management_sdk.models.agent_deployment_status_response import AgentDeploymentStatusResponse
from cohesity_management_sdk.models.cloud_archive_summary import CloudArchiveSummary
from cohesity_management_sdk.models.data_transfer_from_vaults_summary_response import DataTransferFromVaultsSummaryResponse
from cohesity_management_sdk.models.data_transfer_to_vaults_summary_response import DataTransferToVaultsSummaryResponse
from cohesity_management_sdk.models.object_information import ObjectInformation
from cohesity_management_sdk.models.protection_trend import ProtectionTrend
from cohesity_management_sdk.models.protection_sources_job_runs_report_element import ProtectionSourcesJobRunsReportElement
from cohesity_management_sdk.models.protection_sources_jobs_summary_report_response_wrapper import ProtectionSourcesJobsSummaryReportResponseWrapper

class ReportsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(ReportsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_agent_deployment_report(self,
                                    host_os_type=None,
                                    compact_version=None,
                                    output_format=None,
                                    health_status=None):
        """Does a GET request to /public/reports/agents.

        Get the list of all the installed agents which includes the health
        status and upgradability of the agent.

        Args:
            host_os_type (HostOsTypeEnum, optional):  Specifies the host type
                on which the Cohesity agent is installed.
            compact_version (string, optional): Specifies the compact version
                of Cohesity agent. For example, 6.0.1.
                Setting this parameter will filter the response based on
                installed agent version.
            output_format (string):  Specifies the format for the
                output such as 'csv' or 'json'.
                If not specified, the json format is returned.
                If 'csv' is specified, a comma-separated list with a heading
                row is returned.
            health_status (HealthStatusEnum): Specifies the health status of
                the Cohesity agent.

        Returns:
            list of AgentDeploymentStatusResponse: Response from the API.
                Successful Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_agent_deployment_report called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_agent_deployment_report.')
            _url_path = '/public/reports/agents'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'hostOsType': host_os_type,
                'compactVersion': compact_version,
                'outputFormat':output_format,
                'healthStatus':health_status
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_agent_deployment_report.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_agent_deployment_report.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_agent_deployment_report')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_agent_deployment_report.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              AgentDeploymentStatusResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_data_transfer_from_vaults_report_request(self,
                                                    start_time_msecs=None,
                                                    end_time_msecs=None,
                                                    vault_ids=None,
                                                    output_format=None,
                                                    group_by=None):
        """Does a GET request to /public/reports/dataTransferFromVaults.

        A Vault can provide an additional Cloud Tier where cold data of the
        Cohesity Cluster is stored in the Cloud.
        A Vault can also provide archive storage for backup data.
        This archive data is stored on Tapes and in Cloud Vaults.

        Args:
            start_time_msecs (int|long, optional): Filter by a start time.
                Specify the start time as a Unix epoch Timestamp (in
                milliseconds).
                If startTimeMsecs and endTimeMsecs are not specified, the time
                period is the last 7 days.
            end_time_msecs (int|long, optional): Filter by end time.
                Specify the end time as a Unix epoch Timestamp (in
                milliseconds).
                If startTimeMsecs and endTimeMsecs are not specified,
                the time period is the last 7 days.
            vault_ids (list of int, required): Filter by a list of Vault ids.
            output_format (string, optional): Specifies the format for the
                output such as 'csv' or 'json'.
                If not specified, the json format is returned.
                If 'csv' is specified, a comma-separated list with a heading
                row is returned.
            group_by (string, optional): Specifies wheather the report should
                be grouped by target when scheduled or downloaded. If not set
                or set to false, report is grouped by protection jobs. It is
                ignored if outformat is not "csv" and response contains whole
                report.

        Returns:
            list of DataTransferFromVaultsSummaryResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_data_transfer_from_vaults_report_request called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_data_transfer_from_vaults_report_request.')
            _url_path = '/public/reports/dataTransferFromVaults'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'startTimeMsecs': start_time_msecs,
                'endTimeMsecs': end_time_msecs,
                'vaultIds':vault_ids,
                'outputFormat': output_format,
                'groupBy': group_by
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_data_transfer_from_vaults_report_request.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_data_transfer_from_vaults_report_request.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_data_transfer_from_vaults_report_request')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_data_transfer_from_vaults_report_request.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              DataTransferFromVaultsSummaryResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_data_transfer_to_vaults_report_request(self,
                                                    start_time_msecs=None,
                                                    end_time_msecs=None,
                                                    vault_ids=None,
                                                    output_format=None,
                                                    group_by=None):
        """Does a GET request to /public/reports/dataTransferToVaults.

        A Vault can provide an additional Cloud Tier where cold data of the
        Cohesity Cluster can be stored in the Cloud.
        A Vault can also provide archive storage for backup data.
        This archive data is stored on Tapes and in Cloud Vaults.

        Args:
            start_time_msecs (int|long, optional): Filter by a start time.
                Specify the start time as a Unix epoch Timestamp (in
                milliseconds).
                If startTimeMsecs and endTimeMsecs are not specified, the time
                period is the last 7 days.
            end_time_msecs (int|long, optional): Filter by end time.
                Specify the end time as a Unix epoch Timestamp (in
                milliseconds).
                If startTimeMsecs and endTimeMsecs are not specified,
                the time period is the last 7 days.
            vault_ids (list of int, required): Filter by a list of Vault ids.
            output_format (string, optional): Specifies the format for the
                output such as 'csv' or 'json'.
                If not specified, the json format is returned.
                If 'csv' is specified, a comma-separated list with a heading
                row is returned.
            group_by (string, optional): Specifies wheather the report should
                be grouped by target when scheduled or downloaded. If not set
                or set to false, report is grouped by protection jobs. It is
                ignored if outformat is not "csv" and response contains whole
                report.

        Returns:
            list of DataTransferToVaultsSummaryResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_data_transfer_to_vaults_report_request called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_data_transfer_to_vaults_report_request.')
            _url_path = '/public/reports/dataTransferToVaults'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'startTimeMsecs': start_time_msecs,
                'endTimeMsecs': end_time_msecs,
                'vaultIds':vault_ids,
                'outputFormat': output_format,
                'groupBy': group_by
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_data_transfer_to_vaults_report_request.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_data_transfer_to_vaults_report_request.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_data_transfer_to_vaults_report_request')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_data_transfer_to_vaults_report_request.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              DataTransferToVaultsSummaryResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_gdpr_report(self,
                   id=None,
                   accessible_users=None,
                   parent_source_id=None,
                   output_format=None,
                   actions=None,
                   search=None,
                   start_time_usecs=None,
                   end_time_usecs=None):
        """Does a GET request to /public/reports/gdpr.

        Returns the GDPR report information.

        Args:
            id (list of int|long): Specifies the objects for which to
                get the gdpr information.
            accessible_users (list of string, optional): Specifies the users
                for which to get the accessible objects.
            parent_source_id (list of int|long, optional): Specifies the
                parent sources of objects for which to get info for.
            output_format (string, optional): Specifies the format for
                the output such as 'csv' or 'json'.
                If not specified, the json format is returned.
                If 'csv' is specified, a comma-separated list with a heading
                row is returned.
            actions (list of string, optional): Specifies the action for the
                audit logs.
            search (string, optional): Specifies the search string for the
                audit logs.
            start_time_usecs (long|int, optional): Specifies the start time
                for the audit logs as a Unix epoch Timestamp (in
                microseconds).
            end_time_usecs (long|int, optional): Specifies the end time for
                the audit logsas a Unix epoch Timestamp (in microseconds).

        Returns:
            list of ObjectInformation: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_gdpr_report called.')


            # Prepare query URL
            self.logger.info('Preparing query URL for get_gdpr_report.')
            _url_path = '/public/reports/gdpr'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'id': id,
                'accessibleUsers': accessible_users,
                'parentSourceId': parent_source_id,
                'outputFormat': output_format,
                'actions': actions,
                'search': search,
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_gdpr_report.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_gdpr_report.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_gdpr_report')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_gdpr_report.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ObjectInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protected_objects_trends_report_request(self,
                             job_ids=None,
                             start_time_usecs=None,
                             timezone=None,
                             end_time_usecs=None,
                             environments=None,
                             protected_object_ids=None,
                             registered_source_id=None,
                             rollup=None,
                             tenant_ids=None,
                             all_under_hierarchy=None):
        """Does a GET request to /public/reports/protectedObjectsTrends.

        This gives a summary of protection trend for protected resources
        during the given time range.
        If no roll up is specified, then the trends will be grouped by days.

        Args:
            job_ids (list of int|long, optional): Filter by a list of Job ids.
                Snapshots summary statistics for the specified Protection Jobs
                are reported.
            start_time_usecs (int|long, optional): Filter by a start time.
                Snapshot summary statistics for Job Runs that started after
                the specified time are reported. Specify the start time as a
                Unix epoch Timestamp (in microseconds).
            timezone (string, required): Specifies the timezone to use when
                calculating day/week/month Specify the timezone in the
                following format: "Area/Location", for example:"America/New_York".
            end_time_usecs (int|long, optional): Filter by end time.
                Snapshot summary statistics
            environments (EnvironmentEnum, optional): Filter by a list of
                environment types suchas 'kVMware', 'kView', etc.
                Supported environment types such as 'kView', 'kSQL',
                'kVMware', etc.
                NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.
                'kVMware' indicates the VMware Protection Source environment.
                'kHyperV' indicates the HyperV Protection Source environment.
                'kSQL' indicates the SQL Protection Source environment.
                'kView' indicates the View Protection Source environment.
                'kPuppeteer' indicates the Cohesity's Remote Adapter.
                'kPhysical' indicates the physical Protection Source
                environment.
                'kPure' indicates the Pure Storage Protection Source
                environment.
                'kNimble' indicates the Nimble Storage Protection Source
                environment.
                'kAzure' indicates the Microsoft's Azure Protection Source
                environment.
                'kNetapp' indicates the Netapp Protection Source environment.
                'kAgent' indicates the Agent Protection Source environment.
                'kGenericNas' indicates the Generic Network Attached Storage
                Protection
                Source environment.
                'kAcropolis' indicates the Acropolis Protection Source
                environment.
                'kPhsicalFiles' indicates the Physical Files Protection Source
                environment.
                'kIsilon' indicates the Dell EMC's Isilon Protection Source
                environment.
                'kGPFS' indicates IBM's GPFS Protection Source environment.
                'kKVM' indicates the KVM Protection Source environment.
                'kAWS' indicates the AWS Protection Source environment.
                'kExchange' indicates the Exchange Protection Source environment.
                'kHyperVVSS' indicates the HyperV VSS Protection Source
                environment.
                'kOracle' indicates the Oracle Protection Source environment.
                'kGCP' indicates the Google Cloud Platform Protection Source
                environment.
                'kFlashBlade' indicates the Flash Blade Protection Source
                environment.
                'kAWSNative' indicates the AWS Native Protection Source
                environment.
                'kO365' indicates the Office 365 Protection Source
                environment.
                'kO365Outlook' indicates Office 365 outlook Protection Source
                environment.
                'kHyperFlex' indicates the Hyper Flex Protection Source
                environment.
                'kGCPNative' indicates the GCP Native Protection Source
                environment.
                'kAzureNative' indicates the Azure Native Protection Source
                environment.
                'kKubernetes' indicates a Kubernetes Protection Source
                environment.
                'kElastifile' indicates Elastifile Protection Source
                environment.
                'kAD' indicates Active Directory Protection Source
                environment.
                'kRDSSnapshotManager' indicates AWS RDS Protection Source
                environment.
                'kCassandra' indicates Cassandra Protection Source environment.
                'kMongoDB' indicates MongoDB Protection Source environment.
                'kCouchbase' indicates Couchbase Protection Source environment.
                'kHdfs' indicates Hdfs Protection Source environment.
                'kHive' indicates Hive Protection Source environment.
                'kHBase' indicates HBase Protection Source environment.
                'kUDA' indicates Universal Data Adapter Protection Source
                environment.
                'kO365Teams' indicates the Office365 Teams Protection Source
                environment.
                'kO365Group' indicates the Office365 Groups Protection Source
                environment.
                'kO365Exchange' indicates the Office365 Mailbox Protection
                Source environment.
                'kO365OneDrive' indicates the Office365 OneDrive Protection
                Source environment.
                'kO365Sharepoint' indicates the Office365 SharePoint Protection
                Source environment.
                'kO365PublicFolders' indicates the Office365 PublicFolders
                Protection Source environment.

            protected_object_ids (list of int|long, optional): Filter by a
                list of leaf Protection Sources Objects (such as VMs).
            registered_source_id (int|long, optional): Specifies an id of a
                top level Registered Source such as a vCenter Server. If
                specified, Snapshot summary statistics for all the leaf
                Protection Sources (such as VMs) that are children of this
                Registered Source are reported.
                NOTE: If specified, filtering by other fields is not
                supported.
            rollup (string, optional): Roll up type for grouping. Valid values
                are day, week, month
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            list of ProtectionTrend: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protected_objects_trends_report_request called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_protected_objects_trends_report_request.')
            _url_path = '/public/reports/protectedObjectsTrends'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'jobIds': job_ids,
                'startTimeUsecs': start_time_usecs,
                'timezone': timezone,
                'endTimeUsecs': end_time_usecs,
                'environments': environments,
                'protectedObjectIds': protected_object_ids,
                'registeredSourceId': registered_source_id,
                'rollup': rollup,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_protected_objects_trends_report_request.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protected_objects_trends_report_request.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_protected_objects_trends_report_request')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_protected_objects_trends_report_request.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionTrend.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protection_sources_job_runs_report_request(self,
                                tenant_ids=None,
                                all_under_hierarchy=None,
                                job_ids=None,
                                start_time_usecs=None,
                                end_time_usecs=None,
                                environments=None,
                                protection_source_ids=None,
                                output_format=None,
                                page_count=None,
                                run_status=None):
        """Does a GET request to /public/reports/protectionSourcesJobRuns.

        Returns the Snapshots that contain backups of the specified
        Protection Source Objects and match the specified filter criteria.

        Args:
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.
            job_ids (list of int|long, optional): Filter by a list of Job ids.
                Snapshots for the specified Protection Jobs are listed.
            start_time_usecs (int|long, optional): Filter by a start time.
                Snapshots that started after the specified time are returned.
                Specify the end time as a Unix epoch Timestamp (in
                microseconds).
            end_time_usecs (int|long, optional): Filter by a end time.
                Snapshots that ended before the specified time are returned.
                Specify the end time as a Unix epoch Timestamp (in
                microseconds).
            environments (EnvironmentEnum, optional): Filter by a list of
                environment types such as 'kVMware', 'kView', etc.
            protection_source_ids (int|long, required): Filter by a list of
                leaf Protection Sources Objects (such as VMs). Snapshots of
                the specified Protection Source Objects are returned.
            output_format (string, optional): Specifies the format for the
                output such as 'cvs' or 'json'.
                If not specified, the json format is returned.
                If 'csv' is specified, a comma-separated list with a heading
                row is returned.
            page_count (int, optional): Specifies the number of Snapshots to
                return in the response for pagination purposes. Used in
                combination with the paginationCookie in the response to
                return multiple sets of Snapshots.
            run_status (RunStatusEnum, optional): Filter by a list of run
                statuses such as 'kRunning',
                'kSuccess', 'kFailure' etc.
                Snapshots of Job Runs with the specified run statuses are
                reported.
                'kSuccess' indicates that the Job Run was successful.
                'kRunning' indicates that the Job Run is currently running.
                'kWarning' indicates that the Job Run was successful but
                warnings were issued.
                'kCancelled' indicates that the Job Run was canceled.
                'kError' indicates the Job Run encountered an error and did
                not run to completion.

        Returns:
            list of ProtectionSourcesJobRunsReportElement: Response from the
                API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_sources_job_runs_report_request called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_protection_sources_job_runs_report_request.')
            _url_path = '/public/reports/protectionSourcesJobRuns'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'tenantIds':tenant_ids,
                'allUnderHierarchy':all_under_hierarchy,
                'jobIds': job_ids,
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs,
                'environments': environments,
                'protectionSourceIds': protection_source_ids,
                'outputFormat':output_format,
                'pageCount':page_count,
                'runStatus': run_status
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_protection_sources_job_runs_report_request.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protection_sources_job_runs_report_request.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_protection_sources_job_runs_report_request')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_protection_sources_job_runs_report_request.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ProtectionSourcesJobRunsReportElement.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protection_sources_jobs_summary_report_request(
                  self,
                  job_ids=None,
                  start_time_usecs=None,
                  end_time_usecs=None,
                  environments=None,
                  protection_source_ids=None,
                  statuses=None,
                  output_format=None,
                  registered_source_id=None,
                  consecutive_failures=None,
                  report_name=None,
                  report_type=None,
                  tenant_ids=None,
                  all_under_hierarchy=None):
        """Does a GET request to /public/reports/protectionSourcesJobsSummary.

        For example, if two Job ids are passed in, Snapshot summary statistics
        about all the leaf Objects that have been protected by the two
        specified Jobs are reported.
        For example, if a top level registered Source id is passed in, summary
        statistics about all the Snapshots backing up leaf Objects in
        the specified Source are reported.

        Args:
            job_ids (list of int|long, optional): Filter by a list of Job ids.
                Snapshots summary statistics for the specified Protection Jobs
                are reported.
            start_time_usecs (int|long, optional): Filter by a start time.
                Snapshot summary statistics for Job Runs that started after
                the specified time are reported. Specify the start time as a
                Unix epoch Timestamp (in microseconds).
            end_time_usecs (int|long, optional): Filter by end time. Snapshot
                summary statistics for Job Runs that ended before the
                specified time are returned. Specify the end time as a Unix
                epoch Timestamp (in microseconds).
            environments (EnvironmentEnum, optional): Filter by a list of
                environment types such as 'kVMware', 'kView', etc.
                NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.
            protection_source_ids (list of long|int, optional): Filter by a list of
                leaf Protection Sources Objects (such as VMs). Snapshot
                summary statistics for the listed Protection Source Objects
                are reported.
            statuses (RunStatusEnum, optional): Filter by a list of run
                statuses.
                'kSuccess' indicates that the Job Run was successful.
                'kRunning' indicates that the Job Run is currently running.
                'kWarning' indicates that the Job Run was successful but
                warnings were issued.
                'kCancelled' indicates that the Job Run was canceled.
                'kError' indicates the Job Run encountered an error and did
                not run to completion.
            output_format (string, optional): Specifies the format for
                the output such as 'csv' or 'json'.
                If not specified, the json format is returned.
                If 'csv' is specified, a comma-separated list with a heading
                row is returned.
            registered_source_id (int, optional): Specifies an id of a top level
                Registered Source such as a vCenter Server. If specified,
                Snapshot summary statistics for allthe leaf Protection
                Sources (such as VMs) that are children of this Registered
                Source are reported.
                NOTE: If specified, filtering by other fields is not
                supported.
            consecutive_failures (int, optional): Filters out those jobs
                which have number of consecutive run failures less than
                consecutiveFailures.
            report_name (string, optional): Specifies the custom report name
                the user wants to set for this report.
            report_type (int, optional): Specifies the report type that will
                be used to set the right label & subject line for the report
                when downloaded or emailed because same API is used for 3
                reports currently
                1. kAvailableLocalSnapshotsReport
                2. kFailedObjectsReport
                3. kProtectionSummaryByObjectTypeReport
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            ProtectionSourcesJobsSummaryReportResponseWrapper: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_sources_jobs_summary_report_request called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_protection_sources_jobs_summary_report_request.')
            _url_path = '/public/reports/protectionSourcesJobsSummary'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'jobIds': job_ids,
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs,
                'environments': environments,
                'protectionSourceIds': protection_source_ids,
                'statuses': statuses,
                'outputFormat': output_format,
                'registeredSourceId': registered_source_id,
                'consecutiveFailures': consecutive_failures,
                'reportName': report_name,
                'reportType': report_type,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_protection_sources_jobs_summary_report_request.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_protection_sources_jobs_summary_report_request.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_protection_sources_jobs_summary_report_request')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_protection_sources_jobs_summary_report_request.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionSourcesJobsSummaryReportResponseWrapper.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_cloud_archive_report_request(self):
        """Does a GET request to /public/reports/cloudArchiveReport.

        last run status by each protection job.
        Cohesity Cluster to Vaults (External Targets).

        Returns:
            CloudArchiveSummary: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_cloud_archive_report_request called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_cloud_archive_report_request.')
            _url_path = '/public/reports/cloudArchiveReport'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_cloud_archive_report_request.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_cloud_archive_report_request.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_cloud_archive_report_request')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_cloud_archive_report_request.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              CloudArchiveSummary.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
