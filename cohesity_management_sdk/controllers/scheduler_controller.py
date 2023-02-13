# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.exceptions.error_exception import ErrorException
from cohesity_management_sdk.models.scheduler_proto import SchedulerProto
from cohesity_management_sdk.models.scheduler_proto_scheduler_job import SchedulerProto_SchedulerJob
from cohesity_management_sdk.models.scheduler_proto_scheduler_job_schedule__parameter import SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter



class SchedulerController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(SchedulerController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_scheduler_jobs(self,
                       ids=None,
                       tenant_ids=None,
                       all_under_hierarchy=None):
        """Does a GET request to /public/scheduler.

        Returns all the email report scheduler jobs that are scheduled to run.
        An email report scheduler job generates a report with the specified
        parameters and sends that report to the specified email accounts
        according to the defined schedule.

        Args:
            ids (list of int|long, optional): Specifies ids of scheduler jobs
                to fetch.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            SchedulerProto: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_scheduler_jobs called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_scheduler_jobs.')
            _url_path = '/public/scheduler'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'ids': ids,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_scheduler_jobs.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_scheduler_jobs.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_scheduler_jobs')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_scheduler_jobs.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                SchedulerProto.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_scheduler_job(self, body):
        """Does a PUT request to /public/scheduler.

        Returns the updated email report scheduler job.

        Args:
            body (SchedulerProto_SchedulerJob): Update Job Parameter.

        Returns:
            SchedulerProto_SchedulerJob: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_scheduler_job called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_scheduler_job.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_scheduler_job.')
            _url_path = '/public/scheduler'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_scheduler_job.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_scheduler_job.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_scheduler_job')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_scheduler_job.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              SchedulerProto_SchedulerJob.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_scheduler_job(self, body=None):
        """Does a POST request to /public/scheduler.

        Returns the created email report scheduler job.
        An email report scheduler job generates a report with the specified
        parameters and sends that report to the specified email accounts
        according to the defined schedule.
        This operation may also be used to send a report once (with no
        schedule), by setting the EnableRecurring field to false.

        Args:
            body (SchedulerProto_SchedulerJob, optional): update user quota
                params.

        Returns:
            SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter: Response from the API. Success
            SchedulerProto_SchedulerJob: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_scheduler_job called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_scheduler_job.')
            _url_path = '/public/scheduler'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_scheduler_job.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_scheduler_job.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_scheduler_job')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_scheduler_job.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            if _context.response.status_code == 200:
                return APIHelper.json_deserialize(
                    _context.response.raw_body, SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter.from_dictionary)
            elif _context.response.status_code == 201:
                return APIHelper.json_deserialize(
                    _context.response.raw_body, SchedulerProto_SchedulerJob.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_scheduler_jobs(self, ids=None):
        """Does a DELETE request to /public/scheduler.

        Specify a list of email report schedule job ids to unschedule and
        delete.

        Args:
            ids (list<object, int|long>): Array of ids

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_scheduler_jobs called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_scheduler_jobs.')
            _url_path = '/public/scheduler'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_scheduler_jobs.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_scheduler_jobs.')
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(ids))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='delete_scheduler_jobs')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_scheduler_jobs.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

