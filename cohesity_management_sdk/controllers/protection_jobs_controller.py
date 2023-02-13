# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.protection_job import ProtectionJob
from cohesity_management_sdk.models.update_protection_jobs_state import UpdateProtectionJobsState
from cohesity_management_sdk.models.protection_job_audit_trail import ProtectionJobAuditTrail
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class ProtectionJobsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, config=None, client=None, call_back=None):
        super(ProtectionJobsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def change_protection_job_state(self, id, body=None):
        """Does a POST request to /public/protectionJobState/{id}.

        If the Protection Job is currently running (not paused) and true is
        passed in,
        this operation stops any new Runs of this Protection Job
        from stating and executing.
        However, any existing Runs that were already executing will continue
        to run.
        If this Projection Job is paused and false is passed in, this
        operation
        restores the Job to a running state and new Runs are started as
        defined
        by the schedule in the Policy associated with the Job.
        Returns success if the paused state is changed.

        Args:
            id (long|int): Specifies a unique id of the Protection Job.
            body (ChangeProtectionJobStateParam, optional): TODO: type
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
            self.logger.info('change_protection_job_state called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for change_protection_job_state.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for change_protection_job_state.')
            _url_path = '/public/protectionJobState/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for change_protection_job_state.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for change_protection_job_state.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='change_protection_job_state')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for change_protection_job_state.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protection_jobs(self,
                            ids=None,
                            names=None,
                            policy_ids=None,
                            environments=None,
                            is_active=None,
                            is_deleted=None,
                            only_return_basic_summary=None,
                            include_last_run_and_stats=None,
                            include_rpo_snapshots=None,
                            is_last_run_sla_violated=None,
                            only_return_data_migration_jobs=None,
                            prune_excluded_source_ids=None,
                            tenant_ids=None,
                            all_under_hierarchy=None):
        """Does a GET request to /public/protectionJobs.

        If no parameters are specified, all Protection Jobs currently
        on the Cohesity Cluster are returned.
        Specifying parameters filters the results that are returned.

        Args:
            ids (list of long|int, optional): Filter by a list of Protection
                Job ids.
            names (list of string, optional): Filter by a list of Protection
                Job names.
            policy_ids (list of string, optional): Filter by Policy ids that
                are associated with Protection Jobs. Only Jobs associated with
                the specified Policy ids, are returned.
            environments (list of EnvironmentGetProtectionJobsEnum, optional):
                Filter by environment types such as 'kVMware', 'kView', etc.
                Only Jobs protecting the specified environment types are
                returned. NOTE: 'kPuppeteer' refers to Cohesity's Remote
                Adapter.
            is_active (bool, optional): Filter by Inactive or Active Jobs. If
                not set, all Inactive and Active Jobs are returned. If true,
                only Active Jobs are returned. If false, only Inactive Jobs
                are returned. When you create a Protection Job on a Primary
                Cluster with a replication schedule, the Cluster creates an
                Inactive copy of the Job on the Remote Cluster. In addition,
                when an Active and running Job is deactivated, the Job becomes
                Inactive.
            is_deleted (bool, optional): If true, return only Protection Jobs
                that have been deleted but still have Snapshots associated
                with them. If false, return all Protection Jobs except those
                Jobs that have been deleted and still have Snapshots
                associated with them. A Job that is deleted with all its
                Snapshots is not returned for either of these cases.
            only_return_basic_summary (bool, optional): if true then only job
                descriptions and the most recent run of the job will be
                returned.
            include_last_run_and_stats (bool, optional): If true, return the
                last Protection Run of the Job and the summary stats.
            include_rpo_snapshots (bool, optional): If true, then the
                Protected Objects protected by RPO policies will also be
                returned.
            is_last_run_sla_violated (bool, optional): IsLastRunSlaViolated is
                the parameter to filter the Protection Jobs based on the SLA
                violation status of the last Protection Run.
            only_return_data_migration_jobs (bool, optional):
                OnlyReturnDataMigrationJobs specifies if only data migration
                jobs should be returned. If not set, no data migration job
                will be returned.
            prune_excluded_source_ids (bool, optional): If true, the list of
                exclusion sources will be omitted from the response. This can
                be used to improve performance when the exclusion sources are
                not needed.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            list of ProtectionJob: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_jobs called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_protection_jobs.')
            _url_path = '/public/protectionJobs'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'ids': ids,
                'names': names,
                'policyIds': policy_ids,
                'environments': environments,
                'isActive': is_active,
                'isDeleted': is_deleted,
                'onlyReturnBasicSummary': only_return_basic_summary,
                'includeLastRunAndStats': include_last_run_and_stats,
                'includeRpoSnapshots': include_rpo_snapshots,
                'isLastRunSlaViolated': is_last_run_sla_violated,
                'onlyReturnDataMigrationJobs': only_return_data_migration_jobs,
                'pruneExcludedSourceIds': prune_excluded_source_ids,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_protection_jobs.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protection_jobs.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_protection_jobs')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_protection_jobs.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionJob.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_protection_job(self, body):
        """Does a POST request to /public/protectionJobs.

        Returns the created Protection Job.

        Args:
            body (ProtectionJobRequestBody): Request to create a Protection
                Job.

        Returns:
            ProtectionJob: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_protection_job called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_protection_job.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_protection_job.')
            _url_path = '/public/protectionJobs'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_protection_job.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_protection_job.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_protection_job')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_protection_job.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionJob.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_run_protection_job(self, id, body):
        """Does a POST request to /public/protectionJobs/run/{id}.

        Immediately execute a single Job Run and ignore the schedule defined
        in the Policy.
        A Protection Policy associated with the Job may define up to three
        backup run types:
        1) Regular (CBT utilized), 2) Full (CBT not utilized) and 3) Log.
        The passed in run type defines what type of backup is done by the Job
        Run.
        The schedule defined in the Policy for the backup run type is ignored
        but
        other settings such as the snapshot retention and retry settings are
        used.
        Returns success if the Job Run starts.

        Args:
            id (long|int): Specifies a unique id of the Protection Job.
            body (RunProtectionJobParam): Specifies the type of backup. If not
                specified, the 'kRegular' backup is run.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_run_protection_job called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_run_protection_job.'
            )
            self.validate_parameters(id=id, body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_run_protection_job.')
            _url_path = '/public/protectionJobs/run/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_run_protection_job.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_run_protection_job.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_run_protection_job')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_run_protection_job.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_protection_jobs_state(self, body=None):
        """Does a POST request to /public/protectionJobs/states.

        Note that the pause or resume actions will take effect from next
        Protection
        Run. Also, user can specify only one type of action on all the
        Protection Jobs.
        Deactivate and activate actions are independent of pause and resume
        state.
        Deactivate and activate actions are useful in case of failover
        situations.
        Returns success if the state of all the Protection Jobs state is
        changed
        successfully.

        Args:
            body (UpdateProtectionJobsStateRequestBody, optional): TODO: type
                description here. Example:

        Returns:
            UpdateProtectionJobsState: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_protection_jobs_state called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_protection_jobs_state.')
            _url_path = '/public/protectionJobs/states'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_protection_jobs_state.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_protection_jobs_state.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='update_protection_jobs_state')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_protection_jobs_state.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                UpdateProtectionJobsState.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_protection_job(self, id, body=None):
        """Does a DELETE request to /public/protectionJobs/{id}.

        Returns Success if the Protection Job is deleted.

        Args:
            id (long|int): Specifies a unique id of the Protection Job.
            body (DeleteProtectionJobParam, optional): Request to delete a
                protection job.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_protection_job called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_protection_job.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_protection_job.')
            _url_path = '/public/protectionJobs/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_protection_job.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_protection_job.')
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='delete_protection_job')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_protection_job.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protection_job_by_id(self, id):
        """Does a GET request to /public/protectionJobs/{id}.

        Returns the Protection Job corresponding to the specified Job id.

        Args:
            id (long|int): Specifies a unique id of the Protection Job.

        Returns:
            ProtectionJob: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_job_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_protection_job_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_protection_job_by_id.')
            _url_path = '/public/protectionJobs/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_protection_job_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protection_job_by_id.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_protection_job_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_protection_job_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionJob.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_protection_job(self, body, id):
        """Does a PUT request to /public/protectionJobs/{id}.

        Returns the updated Protection Job.

        Args:
            body (ProtectionJobRequestBody): Request to update a protection
                job.
            id (long|int): Specifies a unique id of the Protection Job.

        Returns:
            ProtectionJob: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_protection_job called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_protection_job.')
            self.validate_parameters(body=body, id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_protection_job.')
            _url_path = '/public/protectionJobs/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_protection_job.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_protection_job.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_protection_job')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_protection_job.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionJob.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protection_job_audit(self, id):
        """Does a GET request to /public/protectionJobs/{id}/auditTrail.

        Returns the audit of specific protection job edit history.

        Args:
            id (long|int): Specifies a unique id of the Protection Job.

        Returns:
            list of ProtectionJobAuditTrail: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_job_audit called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_protection_job_audit.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_protection_job_audit.')
            _url_path = '/public/protectionJobs/{id}/auditTrail'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_protection_job_audit.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protection_job_audit.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_protection_job_audit')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_protection_job_audit.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ProtectionJobAuditTrail.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
