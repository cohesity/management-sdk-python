# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.view import View
from cohesity_management_sdk.models.file_lock_status import FileLockStatus
from cohesity_management_sdk.models.get_views_result import GetViewsResult
from cohesity_management_sdk.models.view_user_quotas import ViewUserQuotas
from cohesity_management_sdk.models.user_quota_and_usage import UserQuotaAndUsage
from cohesity_management_sdk.models.user_quota_settings import UserQuotaSettings
from cohesity_management_sdk.models.get_views_and_aliases_by_share_result import GetViewsAndAliasesByShareResult
from cohesity_management_sdk.models.activate_view_aliases_result import ActivateViewAliasesResult
from cohesity_management_sdk.models.view_alias import ViewAlias
from cohesity_management_sdk.exceptions.error_error_exception import ErrorErrorException

class ViewsController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(ViewsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_view_by_name(self,
                         name):
        """Does a GET request to /public/views/{name}.

        Returns the View corresponding to the specified View name.

        Args:
            name (string): Specifies the View name.

        Returns:
            View: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_view_by_name called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for get_view_by_name.')
            self.validate_parameters(name=name)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_view_by_name.')
            _url_path = '/public/views/{name}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'name': name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_view_by_name.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_view_by_name.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_view_by_name')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_view_by_name.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, View.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update_view_by_name(self,
                            name,
                            body):
        """Does a PUT request to /public/views/{name}.

        Returns the updated View.

        Args:
            name (string): Specifies the View name.
            body (View1): Request to update a view.

        Returns:
            View: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_view_by_name called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for update_view_by_name.')
            self.validate_parameters(name=name,
                                     body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_view_by_name.')
            _url_path = '/public/views/{name}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'name': name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_view_by_name.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_view_by_name.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_view_by_name')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_view_by_name.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, View.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def delete_view(self,
                    name):
        """Does a DELETE request to /public/views/{name}.

        Returns delete status upon completion.

        Args:
            name (string): Specifies the View name.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_view called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for delete_view.')
            self.validate_parameters(name=name)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_view.')
            _url_path = '/public/views/{name}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'name': name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info('Preparing and executing request for delete_view.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'delete_view')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_view.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_file_lock_status(self,
                             name):
        """Does a GET request to /public/views/{name}/fileLocks.

        Returns error if op fails.

        Args:
            name (string): Specifies the View name.

        Returns:
            FileLockStatus: Response from the API. Get lock file status
                response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_file_lock_status called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for get_file_lock_status.')
            self.validate_parameters(name=name)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_file_lock_status.')
            _url_path = '/public/views/{name}/fileLocks'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'name': name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_file_lock_status.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_file_lock_status.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_file_lock_status')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_file_lock_status.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, FileLockStatus.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_lock_file(self,
                         name,
                         body=None):
        """Does a POST request to /public/views/{name}/fileLocks.

        Returns error if op fails.

        Args:
            name (string): Specifies the View name.
            body (LockFileParameters, optional): Request to lock a file.

        Returns:
            FileLockStatus: Response from the API. Get lock file status
                response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_lock_file called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_lock_file.')
            self.validate_parameters(name=name)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_lock_file.')
            _url_path = '/public/views/{name}/fileLocks'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'name': name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_lock_file.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_lock_file.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_lock_file')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_lock_file.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, FileLockStatus.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_views(self,
                  view_names=None,
                  view_box_names=None,
                  match_partial_names=None,
                  max_count=None,
                  max_view_id=None,
                  include_inactive=None,
                  tenant_ids=None,
                  all_under_hierarchy=None,
                  view_box_ids=None,
                  job_ids=None,
                  sort_by_logical_usage=None,
                  match_alias_names=None):
        """Does a GET request to /public/views.

        If no parameters are specified, all Views on the Cohesity Cluster are
        returned.
        Specifying parameters filters the results that are returned.
        NOTE: If maxCount is set and the number of Views returned exceeds the
        maxCount,
        there are more Views to return.
        To get the next set of Views, send another request and specify the id
        of the
        last View returned in viewList from the previous response.

        Args:
            view_names (list of string, optional): Filter by a list of View
                names.
            view_box_names (list of string, optional): Filter by a list of
                View Box names.
            match_partial_names (bool, optional): If true, the names in
                viewNames are matched by prefix rather than exactly matched.
            max_count (int, optional): Specifies a limit on the number of
                Views returned.
            max_view_id (long|int, optional): If the number of Views to return
                exceeds the maxCount specified in the original request,
                specify the id of the last View from the viewList in the
                previous response to get the next set of Views.
            include_inactive (bool, optional): Specifies if inactive Views on
                this Remote Cluster (which have Snapshots copied by
                replication) should also be returned. Inactive Views are not
                counted towards the maxCount. By default, this field is set to
                false.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.
            view_box_ids (list of long|int, optional): Filter by a list of
                Storage Domains (View Boxes) specified by id.
            job_ids (list of long|int, optional): Filter by Protection Job
                ids. Return Views that are being protected by listed Jobs,
                which are specified by ids.
            sort_by_logical_usage (bool, optional): If set to true, the list
                is sorted descending by logical usage.
            match_alias_names (bool, optional): If true, view aliases are also
                matched with the names in viewNames.

        Returns:
            GetViewsResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_views called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_views.')
            _url_path = '/public/views'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'viewNames': view_names,
                'viewBoxNames': view_box_names,
                'matchPartialNames': match_partial_names,
                'maxCount': max_count,
                'maxViewId': max_view_id,
                'includeInactive': include_inactive,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy,
                'viewBoxIds': view_box_ids,
                'jobIds': job_ids,
                'SortByLogicalUsage': sort_by_logical_usage,
                'matchAliasNames': match_alias_names
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_views.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_views.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_views')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_views.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, GetViewsResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_clone_view(self,
                          body):
        """Does a POST request to /public/views/clone.

        Returns the cloned View.

        Args:
            body (CloneViewRequest): Request to clone a View.

        Returns:
            View: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_clone_view called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_clone_view.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_clone_view.')
            _url_path = '/public/views/clone'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_clone_view.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_clone_view.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_clone_view')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_clone_view.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, View.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_clone_directory(self,
                               body):
        """Does a POST request to /public/views/cloneDirectory.

        Returns error if op fails.

        Args:
            body (CloneDirectoryRequestParams): Request to clone a directory.

        Returns:
            void: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_clone_directory called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_clone_directory.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_clone_directory.')
            _url_path = '/public/views/cloneDirectory'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_clone_directory.')
            _headers = {
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_clone_directory.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_clone_directory')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_clone_directory.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_overwrite_view(self,
                              body):
        """Does a POST request to /public/views/overwrite.

        Specifies source and target view names as params.
        Returns the modified Target View.

        Args:
            body (OverwriteViewParameters): Request to overwrite a Target view
                with contents of a Source view.

        Returns:
            View: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_overwrite_view called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_overwrite_view.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_overwrite_view.')
            _url_path = '/public/views/overwrite'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_overwrite_view.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_overwrite_view.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_overwrite_view')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_overwrite_view.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, View.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_rename_view(self,
                           body,
                           name):
        """Does a POST request to /public/views/rename/{name}.

        Specify original name of the View in the 'name' parameter.
        Returns the renamed View.

        Args:
            body (RenameViewParameters): Request to rename a View.
            name (string): Specifies the View name.

        Returns:
            View: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_rename_view called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_rename_view.')
            self.validate_parameters(body=body,
                                     name=name)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_rename_view.')
            _url_path = '/public/views/rename/{name}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'name': name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_rename_view.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_rename_view.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_rename_view')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_rename_view.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, View.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_view_user_quotas(self,
                             exclude_users_within_alert_threshold=None,
                             sid=None,
                             summary_only=None,
                             page_count=None,
                             max_view_id=None,
                             cookie=None,
                             view_name=None,
                             include_usage=None,
                             unix_uid=None,
                             user_unix_ids_for_view=None,
                             user_sids_for_view=None,
                             view_names_for_user=None,
                             output_format=None):
        """Does a GET request to /public/viewUserQuotas.

        Returns error if op fails.

        Args:
            exclude_users_within_alert_threshold (bool, optional): This field
                can be set only when includeUsage is set to true. By default,
                all the users with logical usage > 0 will be returned in the
                result. If this field is set to true, only the list of users
                who has exceeded the alert threshold will be returned.
            sid (string, optional): If interested in a user via smb_client,
                include SID. Otherwise, If valid unix-id to SID mappings are
                available (i.e., when mixed mode is enabled) the server will
                perform the necessary id mapping and return the correct usage
                irrespective of whether the unix id / SID is provided. The
                string is of following format -
                S-1-IdentifierAuthority-SubAuthority1-SubAuthority2-...-SubAuth
                orityn.
            summary_only (bool, optional): Specifies a flag to just return a
                summary. If set to true, and if ViewName is not nil, it
                returns the summary of users for a view. Otherwise if UserId
                not nil, and ViewName is nil then it fetches the summary for a
                user in his views.  By default, it is set to false.
            page_count (long|int, optional): Specifies the max entries that
                should be returned in the result.
            max_view_id (long|int, optional): Related to fetching a particular
                user's quota and usage in all his views. It only pertains to
                the scenario where either UnixUid or Sid is specified, and
                ViewName is nil. Specify the maxViewId for All the views
                returned would have view_id's less than or equal to the given
                MaxViewId if it is >= 0.
            cookie (string, optional): Cookie should be used from previous
                call to list user quota overrides. It resumes (or gives the
                next set of values) from the result of the previous call.
            view_name (string, optional): Specifies the name of the input
                view. If given, there could be three scenarios with the
                viewName input parameter: It gives the user quota overrides
                for this view, and the user quota settings. Returns
                'usersQuotaAndUsage'. If given along with the user id, it
                returns the quota policy for this user on this view. Returns
                'usersQuotaAndUsage'. If given along with SummaryOnly as true,
                a user quota summary for this view would be returned. Returns
                'summaryForView'. If not given, then the user id is checked.
            include_usage (bool, optional): If set to true, the logical usage
                info is included only for users with quota overrides. By
                default, it is set to false.
            unix_uid (int, optional): If interested in a user via
                unix-identifier, include UnixUid. Otherwise, If valid unix-id
                to SID mappings are available (i.e., when mixed mode is
                enabled) the server will perform the necessary id mapping and
                return the correct usage irrespective of whether the unix id /
                SID is provided.
            user_unix_ids_for_view (list of int, optional): While making a
                query for a view, this specifies a list of specific users with
                their unix uid for the result.
            user_sids_for_view (list of string, optional): While making a
                query for a view, this specifies a list of specific users with
                their Sid for the result.
            view_names_for_user (list of string, optional): While making a
                query for a user, this specifies a list of specific views for
                the result.
            output_format (string, optional): OutputFormat is the Output
                format for the output. If it is not specified, default is
                json.

        Returns:
            ViewUserQuotas: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_view_user_quotas called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_view_user_quotas.')
            _url_path = '/public/viewUserQuotas'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'excludeUsersWithinAlertThreshold': exclude_users_within_alert_threshold,
                'sid': sid,
                'summaryOnly': summary_only,
                'pageCount': page_count,
                'maxViewId': max_view_id,
                'cookie': cookie,
                'viewName': view_name,
                'includeUsage': include_usage,
                'unixUid': unix_uid,
                'userUnixIdsForView': user_unix_ids_for_view,
                'userSidsForView': user_sids_for_view,
                'viewNamesForUser': view_names_for_user,
                'outputFormat': output_format
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_view_user_quotas.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_view_user_quotas.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_view_user_quotas')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_view_user_quotas.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, ViewUserQuotas.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update_view_user_quota(self,
                               body=None):
        """Does a PUT request to /public/viewUserQuotas.

        Returns error if op fails.

        Args:
            body (ViewUserQuotaParameters, optional): update user quota
                params.

        Returns:
            UserQuotaAndUsage: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_view_user_quota called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_view_user_quota.')
            _url_path = '/public/viewUserQuotas'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_view_user_quota.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_view_user_quota.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_view_user_quota')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_view_user_quota.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, UserQuotaAndUsage.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_view_user_quota(self,
                               body=None):
        """Does a POST request to /public/viewUserQuotas.

        Returns error if op fails.

        Args:
            body (ViewUserQuotaParameters, optional): update user quota
                params.

        Returns:
            UserQuotaAndUsage: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_view_user_quota called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_view_user_quota.')
            _url_path = '/public/viewUserQuotas'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_view_user_quota.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_view_user_quota.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_view_user_quota')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_view_user_quota.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, UserQuotaAndUsage.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def delete_view_users_quota(self,
                                body=None):
        """Does a DELETE request to /public/viewUserQuotas.

        Returns error if op fails.

        Args:
            body (DeleteViewUsersQuotaParameters, optional): update user quota
                params.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_view_users_quota called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_view_users_quota.')
            _url_path = '/public/viewUserQuotas'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_view_users_quota.')
            _headers = {
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for delete_view_users_quota.')
            _request = self.http_client.delete(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'delete_view_users_quota')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_view_users_quota.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update_user_quota_settings(self,
                                   body=None):
        """Does a PUT request to /public/viewUserQuotasSettings.

        Returns error if op fails.

        Args:
            body (UpdateUserQuotaSettingsForView, optional): update user quota
                metadata params.

        Returns:
            UserQuotaSettings: Response from the API. The User Quota settings
                applied to a view.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_user_quota_settings called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_user_quota_settings.')
            _url_path = '/public/viewUserQuotasSettings'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_user_quota_settings.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_user_quota_settings.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_user_quota_settings')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_user_quota_settings.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, UserQuotaSettings.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update_view(self,
                    body):
        """Does a PUT request to /public/views.

        Returns the updated View.

        Args:
            body (View1): Request to update a view.

        Returns:
            View: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_view called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for update_view.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_view.')
            _url_path = '/public/views'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_view.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_view.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_view')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_view.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, View.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_view(self,
                    body):
        """Does a POST request to /public/views.

        Returns the created View.

        Args:
            body (CreateViewRequest): Request to create a View.

        Returns:
            View: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_view called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_view.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_view.')
            _url_path = '/public/views'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_view.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_view.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_view')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_view.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, View.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_views_by_share_name(self,
                                tenant_ids=None,
                                all_under_hierarchy=None,
                                share_name=None,
                                max_count=None,
                                pagination_cookie=None):
        """Does a GET request to /public/shares.

        If no parameters are specified, all shares on the Cohesity Cluster
        are
        returned. Specifying share name/prefix filters the results that are
        returned.
        NOTE: If maxCount is set and the number of Views returned exceeds the
        maxCount,
        there are more Views to return.
        To get the next set of Views, send another request and specify the
        pagination
        cookie from the previous response.

        Args:
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.
            share_name (string, optional): The share name(substring) that
                needs to be searched against existing views and aliases.
            max_count (int, optional): Specifies a limit on the number of
                Views returned.
            pagination_cookie (string, optional): Expected to be empty in the
                first call to GetViewsByShareName. To get the next set of
                results, set this value to the pagination cookie value
                returned  in the response of the previous call.

        Returns:
            GetViewsAndAliasesByShareResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_views_by_share_name called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_views_by_share_name.')
            _url_path = '/public/shares'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy,
                'shareName': share_name,
                'maxCount': max_count,
                'paginationCookie': pagination_cookie
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_views_by_share_name.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_views_by_share_name.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_views_by_share_name')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_views_by_share_name.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, GetViewsAndAliasesByShareResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_activate_view_aliases(self,
                                     name):
        """Does a POST request to /public/viewAliases/{name}/activate.

        Returns error if op fails.

        Args:
            name (string): Specifies the View name.

        Returns:
            ActivateViewAliasesResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_activate_view_aliases called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_activate_view_aliases.')
            self.validate_parameters(name=name)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_activate_view_aliases.')
            _url_path = '/public/viewAliases/{name}/activate'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'name': name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_activate_view_aliases.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_activate_view_aliases.')
            _request = self.http_client.post(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_activate_view_aliases')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_activate_view_aliases.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, ActivateViewAliasesResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_view_alias(self,
                          body):
        """Does a POST request to /public/viewAliases.

        Returns the created View Alias.

        Args:
            body (ViewAlias): Request to create a View.

        Returns:
            ViewAlias: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_view_alias called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_view_alias.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_view_alias.')
            _url_path = '/public/viewAliases'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_view_alias.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_view_alias.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_view_alias')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_view_alias.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, ViewAlias.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def delete_view_alias(self,
                          name):
        """Does a DELETE request to /public/viewAliases/{name}.

        Returns delete status upon completion.

        Args:
            name (string): Specifies the View Alias name.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_view_alias called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for delete_view_alias.')
            self.validate_parameters(name=name)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_view_alias.')
            _url_path = '/public/viewAliases/{name}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'name': name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info('Preparing and executing request for delete_view_alias.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'delete_view_alias')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_view_alias.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
