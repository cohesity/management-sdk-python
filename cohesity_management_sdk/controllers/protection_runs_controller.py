# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.protection_run_instance import ProtectionRunInstance
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class ProtectionRunsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(ProtectionRunsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_protection_runs(self,
                            job_id=None,
                            include_rpo_snapshots=None,
                            started_time_usecs=None,
                            start_time_usecs=None,
                            end_time_usecs=None,
                            num_runs=None,
                            exclude_tasks=None,
                            source_id=None,
                            run_types=None,
                            exclude_error_runs=None,
                            exclude_non_restoreable_runs=None):
        """Does a GET request to /public/protectionRuns.

        If no parameters are specified, Job Runs currently
        on the Cohesity Cluster are returned. Both running and completed Job
        Runs
        are reported.
        Specifying parameters filters the results that are returned.

        Args:
            job_id (long|int, optional): Filter by a Protection Job that is
                specified by id. If not specified, all Job Runs for all
                Protection Jobs are returned.
            include_rpo_snapshots (bool, optional): If true, then the
                snapshots for Protection Sources protected by Rpo policies
                will also be returned.
            started_time_usecs (long|int, optional): Return a specific Job Run
                by specifying a time and a jobId. Specify the time when the
                Job Run started as a Unix epoch Timestamp (in microseconds).
                If this field is specified, jobId must also be specified.
            start_time_usecs (long|int, optional): Filter by a start time.
                Only Job Runs that started after the specified time are
                returned. Specify the start time as a Unix epoch Timestamp (in
                microseconds).
            end_time_usecs (long|int, optional): Filter by a end time
                specified as a Unix epoch Timestamp (in microseconds). Only
                Job Runs that completed before the specified end time are
                returned.
            num_runs (long|int, optional): Specify the number of Job Runs to
                return. The newest Job Runs are returned.
            exclude_tasks (bool, optional): If true, the individual backup
                status for all the objects protected by the Job Run are not
                populated in the response. For example in a VMware
                environment, the status of backing up each VM associated with
                a Job is not returned.
            source_id (long|int, optional): Filter by source id. Only Job Runs
                protecting the specified source (such as a VM or View) are
                returned. The source id is assigned by the Cohesity Cluster.
            run_types (list of string, optional): Filter by run type such as
                'kFull', 'kRegular' or 'kLog'. If not specified, Job Runs of
                all types are returned.
            exclude_error_runs (bool, optional): Filter out Jobs Runs with
                errors by setting this field to 'true'. If not set or set to
                'false', Job Runs with errors are returned.
            exclude_non_restoreable_runs (bool, optional): Filter out jobs
                runs that cannot be restored by setting this field to 'true'.
                If not set or set to 'false', Runs without any successful
                object will be returned. The default value is false.

        Returns:
            list of ProtectionRunInstance: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_runs called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_protection_runs.')
            _url_path = '/public/protectionRuns'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'jobId': job_id,
                'includeRpoSnapshots': include_rpo_snapshots,
                'startedTimeUsecs': started_time_usecs,
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs,
                'numRuns': num_runs,
                'excludeTasks': exclude_tasks,
                'sourceId': source_id,
                'runTypes': run_types,
                'excludeErrorRuns': exclude_error_runs,
                'excludeNonRestoreableRuns': exclude_non_restoreable_runs
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_protection_runs.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protection_runs.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_protection_runs')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_protection_runs.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ProtectionRunInstance.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_protection_runs(self, body):
        """Does a PUT request to /public/protectionRuns.

        Update the expiration date (retention period) for the specified
        Protection
        Job Runs and their snapshots.
        After an expiration time is reached, the Job Run and its snapshots are
        deleted.
        If an expiration time of 0 is specified, a Job Run and its snapshots
        are immediately deleted.

        Args:
            body (UpdateProtectionJobRunsParam): Request to update the
                expiration time of Protection Job Runs.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_protection_runs called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_protection_runs.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_protection_runs.')
            _url_path = '/public/protectionRuns'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_protection_runs.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_protection_runs.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_protection_runs')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_protection_runs.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_cancel_protection_job_run(self, id, body=None):
        """Does a POST request to /public/protectionRuns/cancel/{id}.

        Cancel a Protection Job run.

        Args:
            id (long|int): Specifies a unique id of the Protection Job.
            body (CancelProtectionJobRunParam, optional): TODO: type
                description here. Example:

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_cancel_protection_job_run called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_cancel_protection_job_run.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_cancel_protection_job_run.')
            _url_path = '/public/protectionRuns/cancel/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_cancel_protection_job_run.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_cancel_protection_job_run.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_cancel_protection_job_run')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_cancel_protection_job_run.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
