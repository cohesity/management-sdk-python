# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.get_job_run_info_result import GetJobRunInfoResult
from cohesity_management_sdk.models.get_all_job_runs_result import GetAllJobRunsResult
from cohesity_management_sdk.models.get_objects_details_result import GetObjectsDetailsResult
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class MonitoringController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, config=None, client=None, call_back=None):
        super(MonitoringController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_job_run_info(self, job_type, job_id, job_run_id):
        """Does a GET request to /public/monitoring/jobRunInfo.

        Returns the run details for the job run.

        Args:
            job_type (string): Specifies the job type of the needed run.
            job_id (long|int): Specifies the job id of the needed run.
            job_run_id (long|int): Specifies the job run id of the needed
                run.

        Returns:
            GetJobRunInfoResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_job_run_info called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_job_run_info.')
            self.validate_parameters(job_type=job_type,
                                     job_id=job_id,
                                     job_run_id=job_run_id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_job_run_info.')
            _url_path = '/public/monitoring/jobRunInfo'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'jobType': job_type,
                'jobId': job_id,
                'jobRunId': job_run_id
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_job_run_info.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_job_run_info.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_job_run_info')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_job_run_info.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                GetJobRunInfoResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_all_job_runs(self,
                         start_time_msecs,
                         end_time_msecs,
                         job_types=None,
                         env_types=None,
                         page=None,
                         page_size=None):
        """Does a GET request to /public/monitoring/jobs.

        Returns the job runs for the filters.
        Specifying parameters can alter the results that are returned.

        Args:
            start_time_msecs (long|int): Specifies the start time of the time
                range of interest.
            end_time_msecs (long|int): Specifies the end time of the time
                range of interest.
            job_types (list of string, optional): Specifies the job types for
                which runs are needed.
            env_types (list of EnvTypeGetAllJobRunsEnum, optional): Specifies
                the environment types of the job. Supported environment types
                such as 'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer'
                refers to Cohesity's Remote Adapter. 'kVMware' indicates the
                VMware Protection Source environment. 'kHyperV' indicates the
                HyperV Protection Source environment. 'kSQL' indicates the SQL
                Protection Source environment. 'kView' indicates the View
                Protection Source environment. 'kPuppeteer' indicates the
                Cohesity's Remote Adapter. 'kPhysical' indicates the physical
                Protection Source environment. 'kPure' indicates the Pure
                Storage Protection Source environment. 'kNimble' indicates the
                Nimble Storage Protection Source environment. 'kAzure'
                indicates the Microsoft's Azure Protection Source environment.
                'kNetapp' indicates the Netapp Protection Source environment.
                'kAgent' indicates the Agent Protection Source environment.
                'kGenericNas' indicates the Generic Network Attached Storage
                Protection Source environment. 'kAcropolis' indicates the
                Acropolis Protection Source environment. 'kPhsicalFiles'
                indicates the Physical Files Protection Source environment.
                'kIsilon' indicates the Dell EMC's Isilon Protection Source
                environment. 'kGPFS' indicates IBM's GPFS Protection Source
                environment. 'kKVM' indicates the KVM Protection Source
                environment. 'kAWS' indicates the AWS Protection Source
                environment. 'kExchange' indicates the Exchange Protection
                Source environment. 'kHyperVVSS' indicates the HyperV VSS
                Protection Source environment. 'kOracle' indicates the Oracle
                Protection Source environment. 'kGCP' indicates the Google
                Cloud Platform Protection Source environment. 'kFlashBlade'
                indicates the Flash Blade Protection Source environment.
                'kAWSNative' indicates the AWS Native Protection Source
                environment. 'kO365' indicates the Office 365 Protection Source
                environment. 'kO365Outlook' indicates Office 365 outlook
                Protection Source environment. 'kHyperFlex' indicates the Hyper
                Flex Protection Source environment. 'kGCPNative' indicates the
                GCP Native Protection Source environment. 'kAzureNative'
                indicates the Azure Native Protection Source environment.
                'kKubernetes' indicates a Kubernetes Protection Source
                environment. 'kElastifile' indicates Elastifile Protection
                Source environment. 'kAD' indicates Active Directory Protection
                Source environment. 'kRDSSnapshotManager' indicates AWS RDS
                Protection Source environment. 'kCassandra' indicates Cassandra
                Protection Source environment. 'kMongoDB' indicates MongoDB
                Protection Source environment. 'kCouchbase' indicates
                Couchbase Protection Source environment. 'kHdfs' indicates
                Hdfs Protection Source environment. 'kHive' indicates Hive
                Protection Source environment. 'kHBase' indicates HBase
                Protection Source environment. 'kUDA' indicates Universal
                Data Adapter Protection Source environment.
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
            page (int, optional): Specifies the page number in case of
                pagination of response.
            page_size (int, optional): Specifies the size of the page in case
                of pagination of response.

        Returns:
            list of GetAllJobRunsResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_all_job_runs called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_all_job_runs.')
            self.validate_parameters(start_time_msecs=start_time_msecs,
                                     end_time_msecs=end_time_msecs)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_all_job_runs.')
            _url_path = '/public/monitoring/jobs'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'startTimeMsecs': start_time_msecs,
                'endTimeMsecs': end_time_msecs,
                'jobTypes': job_types,
                'envTypes': env_types,
                'page': page,
                'pageSize': page_size
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_all_job_runs.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_all_job_runs.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_all_job_runs')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_all_job_runs.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                GetAllJobRunsResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_run_objects_details(self, job_type, job_id, job_run_id):
        """Does a GET request to /public/monitoring/objectDetails.

        Returns the objects details for the job run.

        Args:
            job_type (string): Specifies the job type of the needed run.
            job_id (long|int): Specifies the job id of the needed run.
            job_run_id (long|int): Specifies the job run id of the needed
                run.

        Returns:
            list of GetObjectsDetailsResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_run_objects_details called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_run_objects_details.')
            self.validate_parameters(job_type=job_type,
                                     job_id=job_id,
                                     job_run_id=job_run_id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_run_objects_details.')
            _url_path = '/public/monitoring/objectDetails'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'jobType': job_type,
                'jobId': job_id,
                'jobRunId': job_run_id
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_run_objects_details.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_run_objects_details.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_run_objects_details')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_run_objects_details.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                GetObjectsDetailsResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
