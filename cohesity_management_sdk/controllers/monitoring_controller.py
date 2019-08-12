# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException

class MonitoringController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(MonitoringController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_all_job_runs(self,
                         start_time,
                         end_time,
                         job_types=None,
                         page=None,
                         page_size=None):
        """Does a GET request to /public/monitoring/jobs.

        Specifying parameters can alter the results that are returned.

        Args:
            start_time (long|int): Specifies the start time of the time range
                of interest.
            end_time (long|int): Specifies the end time of the time range of
                interest.
            job_types (list of string, optional): Specifies the job types for
                which runs are needed.
            page (int, optional): Specifies the page number in case of
                pagination of response.
            page_size (int, optional): Specifies the size of the page in case
                of pagination of response.

        Returns:
            void: Response from the API. Specifies the common result structure
                of the response of all runs info (
protection, replication,
                archival etc.).

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_all_job_runs called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for get_all_job_runs.')
            self.validate_parameters(start_time=start_time,
                                     end_time=end_time)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_all_job_runs.')
            _url_path = '/public/monitoring/jobs'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'startTime': start_time,
                'endTime': end_time,
                'jobTypes': job_types,
                'page': page,
                'pageSize': page_size
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_all_job_runs.')
            _request = self.http_client.get(_query_url)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_all_job_runs')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_all_job_runs.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
