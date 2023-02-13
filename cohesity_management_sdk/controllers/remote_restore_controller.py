# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.remote_vault_restore_task_status import RemoteVaultRestoreTaskStatus
from cohesity_management_sdk.models.universal_id import UniversalId
from cohesity_management_sdk.models.remote_vault_search_job_results import RemoteVaultSearchJobResults
from cohesity_management_sdk.models.remote_vault_search_job_information import RemoteVaultSearchJobInformation
from cohesity_management_sdk.models.created_remote_vault_search_job_uid import CreatedRemoteVaultSearchJobUid
from cohesity_management_sdk.models.vault_bandwidth_limits import VaultBandwidthLimits
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class RemoteRestoreController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(RemoteRestoreController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def upload_vault_encryption_keys(self, id, body=None):
        """Does a PUT request to /public/remoteVaults/encryptionKeys/{id}.

        This request contains multiple files stored as multipart mime data.
        Each file has a key used to encrypt data between a remote Cluster and
        the
        remote Vault.
        Content of the file should be same as the file downloaded from the
        remote
        Cluster.

        Args:
            id (long|int): Specifies a unique id of the Vault.
            body (list of VaultEncryptionKey, optional): Request to upload
                encryption keys of a remote Vault.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('upload_vault_encryption_keys called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for upload_vault_encryption_keys.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for upload_vault_encryption_keys.')
            _url_path = '/public/remoteVaults/encryptionKeys/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for upload_vault_encryption_keys.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for upload_vault_encryption_keys.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='upload_vault_encryption_keys')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for upload_vault_encryption_keys.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_remote_vault_restore_tasks(self):
        """Does a GET request to /public/remoteVaults/restoreTasks.

        A remote Vault restore task can restore archived data from a Vault
        (External Target) to this local Cluster.
        This is part of the CloudRetrieve functionality for finding and
        restoring
        archived data from remote Vaults to an alternative (non-original)
        Cluster.

        Returns:
            list of RemoteVaultRestoreTaskStatus: Response from the API.
                Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_remote_vault_restore_tasks called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for list_remote_vault_restore_tasks.')
            _url_path = '/public/remoteVaults/restoreTasks'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for list_remote_vault_restore_tasks.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_remote_vault_restore_tasks.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='list_remote_vault_restore_tasks')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for list_remote_vault_restore_tasks.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                RemoteVaultRestoreTaskStatus.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_remote_vault_restore_task(self, body):
        """Does a POST request to /public/remoteVaults/restoreTasks.

        Returns the id of the remote Vault restore Task that was created.
        After a Vault is searched by a search Job, this operation can be
        called to create a task that restores the indexes and/or the
        Snapshots
        of a Protection Job, which were archived on a remote Vault (External
        Target).
        This is part of the CloudRetrieve functionality for finding and
        restoring
        archived data from remote Vaults to an alternative (non-original)
        Cluster.

        Args:
            body (CreateRemoteVaultRestoreTaskParameters): Request to create a
                remote Vault restore task.

        Returns:
            UniversalId: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_remote_vault_restore_task called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_remote_vault_restore_task.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_remote_vault_restore_task.')
            _url_path = '/public/remoteVaults/restoreTasks'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_remote_vault_restore_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_remote_vault_restore_task.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_remote_vault_restore_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_remote_vault_restore_task.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              UniversalId.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_remote_vault_search_job_results(self,
                                            search_job_id,
                                            cluster_id,
                                            cluster_incarnation_id,
                                            page_count=None,
                                            cluster_name=None,
                                            cookie=None):
        """Does a GET request to /public/remoteVaults/searchJobResults.

        Specify a unique id of the search Job using a combination of the
        searchJobId, clusterId, and clusterIncarnationId parameters,
        which are all required.
        The results can be optionally filtered by the remote Cluster name.
        This is part of the CloudRetrieve functionality for finding and
        restoring
        archived data from a remote Vault.

        Args:
            search_job_id (long|int): Specifies the id of the remote Vault
                search Job assigned by the Cohesity Cluster. Used in
                combination with the clusterId and clusterIncarnationId to
                uniquely identify the search Job.
            cluster_id (long|int): Specifies the Cohesity Cluster id where the
                search Job was created. Used in combination with the
                searchJobId and clusterIncarnationId to uniquely identify the
                search Job.
            cluster_incarnation_id (long|int): Specifies the incarnation id of
                the Cohesity Cluster where the search Job was created. Used in
                combination with the searchJobId and clusterId to uniquely
                identify the search Job.
            page_count (int, optional): Specifies the number of Protection
                Jobs to return in the response to support pagination.
            cluster_name (string, optional): Optionally filter the result by
                the remote Cohesity Cluster name.
            cookie (string, optional): Specifies the opaque string cookie
                returned by the previous response, to get next set of results.
                Used in combination with pageCount to support pagination.

        Returns:
            RemoteVaultSearchJobResults: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_remote_vault_search_job_results called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_remote_vault_search_job_results.'
            )
            self.validate_parameters(
                search_job_id=search_job_id,
                cluster_id=cluster_id,
                cluster_incarnation_id=cluster_incarnation_id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_remote_vault_search_job_results.')
            _url_path = '/public/remoteVaults/searchJobResults'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'searchJobId': search_job_id,
                'clusterId': cluster_id,
                'clusterIncarnationId': cluster_incarnation_id,
                'pageCount': page_count,
                'clusterName': cluster_name,
                'cookie': cookie
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_remote_vault_search_job_results.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_remote_vault_search_job_results.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_remote_vault_search_job_results')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_remote_vault_search_job_results.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                RemoteVaultSearchJobResults.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_stop_remote_vault_search_job(self, body):
        """Does a DELETE request to /public/remoteVaults/searchJobs.

        This is part of the CloudRetrieve functionality for finding and
        restoring
        archived data from remote Vaults to an alternative (non-original)
        Cluster.

        Args:
            body (StopRemoteVaultSearchJobParameters): Request to stop a
                Remote Vault Search Job.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_stop_remote_vault_search_job called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_stop_remote_vault_search_job.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for delete_stop_remote_vault_search_job.')
            _url_path = '/public/remoteVaults/searchJobs'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for delete_stop_remote_vault_search_job.')
            _headers = {'content-type': 'application/json; charset=utf-8'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_stop_remote_vault_search_job.'
            )
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='delete_stop_remote_vault_search_job')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for delete_stop_remote_vault_search_job.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_remote_vault_search_jobs(self):
        """Does a GET request to /public/remoteVaults/searchJobs.

        List all the searches of remote Vaults (External Targets) that
        have run or are running on this Cohesity Cluster.
        A search finds Protection Jobs that have archived to a
        Vault (External Target).
        This is part of the CloudRetrieve functionality for finding and
        restoring
        archived data from remote Vaults to an alternative (non-original)
        Cluster.
        NOTE: A Vault is equivalent to an External Target in the Cohesity
        Dashboard.
        A search Job is equivalent to a search task in the Cohesity
        Dashboard.

        Returns:
            list of RemoteVaultSearchJobInformation: Response from the API.
                Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_remote_vault_search_jobs called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for list_remote_vault_search_jobs.')
            _url_path = '/public/remoteVaults/searchJobs'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for list_remote_vault_search_jobs.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_remote_vault_search_jobs.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='list_remote_vault_search_jobs')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for list_remote_vault_search_jobs.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                RemoteVaultSearchJobInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_remote_vault_search_job(self, body):
        """Does a POST request to /public/remoteVaults/searchJobs.

        A search Job finds Protection Jobs that archived data to a
        Vault (External Target) which also match the specified search
        criteria.
        The results can be optionally filtered by specifying a Cluster match
        string,
        a Protection Job match string, a start time and an end time.
        This is part of the CloudRetrieve functionality for finding and
        restoring
        archived data from remote Vaults to an alternative (non-original)
        Cluster.
        NOTE: A Vault is equivalent to an External Target in the Cohesity
        Dashboard.
        A search Job is equivalent to a search task in the Cohesity
        Dashboard.

        Args:
            body (CreateRemoteVaultSearchJobParameters): Request to create a
                search of a remote Vault.

        Returns:
            CreatedRemoteVaultSearchJobUid: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_remote_vault_search_job called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_remote_vault_search_job.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_remote_vault_search_job.')
            _url_path = '/public/remoteVaults/searchJobs'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_remote_vault_search_job.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_remote_vault_search_job.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_remote_vault_search_job')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_remote_vault_search_job.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                CreatedRemoteVaultSearchJobUid.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_remote_vault_search_job_by_id(self, id):
        """Does a GET request to /public/remoteVaults/searchJobs/{id}.

        Specify an id for a completed or running search Job.
        A search Job finds data that has been archived to a Vault (External
        Target).
        The returned results do not include Job Run (Snapshot) information.
        It is part of the CloudRetrieve functionality for finding and
        restoring
        archived data from remote Vaults to an alternative (non-original)
        Cluster.

        Args:
            id (long|int): Specifies the id of the remote Vault search Job to
                return.

        Returns:
            RemoteVaultSearchJobInformation: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_remote_vault_search_job_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for list_remote_vault_search_job_by_id.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for list_remote_vault_search_job_by_id.')
            _url_path = '/public/remoteVaults/searchJobs/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for list_remote_vault_search_job_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_remote_vault_search_job_by_id.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='list_remote_vault_search_job_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for list_remote_vault_search_job_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                RemoteVaultSearchJobInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_cloud_domain_migration(self, migration_uid=None):
        """Does a GET request to /public/remoteVaults/cloudDomainMigration.

        Returns the queried cloud domain response.

        Args:
            migration_uid (string): Specifies the Unique identifier of the
                domain migration request and can be used to query the status
                of the migration.

        Returns:
            VaultBandwidthLimits: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_cloud_domain_migration called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for list_cloud_domain_migration.')
            _url_path = '/public/remoteVaults/cloudDomainMigration'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'migrationUid': migration_uid
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_cloud_domain_migration.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_cloud_domain_migration.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='list_cloud_domain_migration')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for list_cloud_domain_migration.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              VaultBandwidthLimits.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_cloud_domain_migration_request(self):
        """Does a POST request to /public/remoteVaults/cloudDomainMigration.

        Returns the created cloud domain response.
        Args:
            body(CreateCloudDomainMigrationParameters): Request to schedule a
                cloud domain migration task.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_cloud_domain_migration_request called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_cloud_domain_migration_request.')
            _url_path = '/public/remoteVaults/cloudDomainMigration'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_cloud_domain_migration_request.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_cloud_domain_migration_request.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_cloud_domain_migration_request')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_cloud_domain_migration_request.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
