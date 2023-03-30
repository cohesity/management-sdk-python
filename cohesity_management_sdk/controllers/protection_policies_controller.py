# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.protection_policy import ProtectionPolicy
from cohesity_management_sdk.models.protection_policy_summary import ProtectionPolicySummary
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class ProtectionPoliciesController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(ProtectionPoliciesController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_protection_policies(self,
                                ids=None,
                                names=None,
                                environments=None,
                                vault_ids=None,
                                origin=None,
                                types=None,
                                tenant_ids=None,
                                all_under_hierarchy=None):
        """Does a GET request to /public/protectionPolicies.

        If no parameters are specified, all Protection Policies currently on
        the
        Cohesity Cluster are returned.
        Specifying parameters filters the results that are returned.

        Args:
            ids (list of string, optional): Filter by a list of Protection
                Policy ids.
            names (list of string, optional): Filter by a list of Protection
                Policy names.
            environments (list of EnvironmentGetProtectionPoliciesEnum,
                optional): Filter by Environment type such as 'kVMware',
                'kView', etc. Only Policies protecting the specified
                environment type are returned. NOTE: 'kPuppeteer' refers to
                Cohesity's Remote Adapter.
            vault_ids (list of long|int, optional): Filter by a list of Vault
                ids. Policies archiving to any of the specified vaults will be
                returned.
            origin (OriginEnum, optional): Specifies the origin of the
                protection policy. 'kHelios' means a global policy which was
                created on Helios. 'kLocal' means a local policy which was
                created on the cluster.
            types (TypeProtectionPolicyRequestEnum, optional): Specifies the
                type of the protection policy. 'kRegular' means a regular
                Protection Policy. 'kRPO' means an RPO Protection Policy.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            list of ProtectionPolicy: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_policies called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_protection_policies.')
            _url_path = '/public/protectionPolicies'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'ids': ids,
                'names': names,
                'environments': environments,
                'vaultIds': vault_ids,
                'origin': origin,
                'types': types,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_protection_policies.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protection_policies.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_protection_policies')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_protection_policies.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionPolicy.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_protection_policy(self, body):
        """Does a POST request to /public/protectionPolicies.

        Returns the created Protection Policy.

        Args:
            body (ProtectionPolicyRequest): Request to create a Protection
                Policy.

        Returns:
            ProtectionPolicy: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_protection_policy called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_protection_policy.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_protection_policy.')
            _url_path = '/public/protectionPolicies'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_protection_policy.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_protection_policy.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_protection_policy')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_protection_policy.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionPolicy.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_protection_policy(self, id):
        """Does a DELETE request to /public/protectionPolicies/{id}.

        Returns Success if the Protection Policy is deleted.

        Args:
            id (string): Specifies a unique id of the Protection Policy to
                return.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_protection_policy called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_protection_policy.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for delete_protection_policy.')
            _url_path = '/public/protectionPolicies/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_protection_policy.'
            )
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='delete_protection_policy')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for delete_protection_policy.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protection_policy_by_id(self, id):
        """Does a GET request to /public/protectionPolicies/{id}.

        Returns the Protection Policy corresponding to the specified Policy
        Id.

        Args:
            id (string): Specifies a unique id of the Protection Policy to
                return.

        Returns:
            ProtectionPolicy: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_policy_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_protection_policy_by_id.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_protection_policy_by_id.')
            _url_path = '/public/protectionPolicies/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_protection_policy_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protection_policy_by_id.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_protection_policy_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_protection_policy_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionPolicy.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_protection_policy(self, body, id):
        """Does a PUT request to /public/protectionPolicies/{id}.

        Returns the updated Protection Policy.

        Args:
            body (ProtectionPolicyRequest): Request to update a Protection
                Policy.
            id (string): Specifies a unique id of the Protection Policy to
                return.

        Returns:
            ProtectionPolicy: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_protection_policy called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_protection_policy.')
            self.validate_parameters(body=body, id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_protection_policy.')
            _url_path = '/public/protectionPolicies/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_protection_policy.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_protection_policy.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_protection_policy')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_protection_policy.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionPolicy.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protection_policy_summary(self,
                                      id,
                                      include_aggregated_last_run_summary=None,
                                      include_aggregated_runs_summary=None,
                                      start_time_usecs=None,
                                      end_time_usecs=None,
                                      page_count=None,
                                      pagination_cookie=None):
        """Does a GET request to /public/protectionPolicySummary.

        List Protection Policy Summary.

        Args:
            id (string): Specifies the id of the policy whose summary should
                be retrieved. If this is not set, the API will return error.
            include_aggregated_last_run_summary (bool, optional): Specifies
                whether to include summary of the last Protection Run of each
                Protection Source.
            include_aggregated_runs_summary (bool, optional): Specifies
                whether to include summary of all Protection Runs of the
                Protection Source or Protection Jobs. If this is set to true,
                then only the Protection Runs from the provided
                'startTimeUsecs' and 'endTimeUsecs' are processed.
            start_time_usecs (long|int, optional): Filter by a start time
                specified as a Unix epoch Timestamp (in microseconds). Only
                Job Runs that started after the specified time are included in
                the aggregated runs summary result.
            end_time_usecs (long|int, optional): Filter by a end time
                specified as a Unix epoch Timestamp (in microseconds). Only
                Job Runs that completed before the specified end time are
                included int he aggregated runs summary result.
            page_count (long|int, optional): Specifies the limit of the number
                of Protection Sources or Protection Jobs to be returned as a
                part of the Protection Policy Summary.
            pagination_cookie (string, optional): If set, i.e. there are more
                results to display, use this value to get the next set of
                results, by using this value in paginationCookie param for the
                next request to GetProtectionPolicySummary.

        Returns:
            ProtectionPolicySummary: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_policy_summary called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_protection_policy_summary.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_protection_policy_summary.')
            _url_path = '/public/protectionPolicySummary'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'id': id,
                'includeAggregatedLastRunSummary':
                include_aggregated_last_run_summary,
                'includeAggregatedRunsSummary':
                include_aggregated_runs_summary,
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs,
                'pageCount': page_count,
                'paginationCookie': pagination_cookie
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_protection_policy_summary.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protection_policy_summary.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_protection_policy_summary')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_protection_policy_summary.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ProtectionPolicySummary.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
