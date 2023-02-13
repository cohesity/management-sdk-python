# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.remote_cluster import RemoteCluster
from cohesity_management_sdk.models.replication_encryption_key_reponse import ReplicationEncryptionKeyReponse
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class RemoteClusterController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(RemoteClusterController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_remote_clusters(self,
                            cluster_ids=None,
                            cluster_names=None,
                            purpose_replication=None,
                            purpose_remote_access=None,
                            verify_reverse_registration=None):
        """Does a GET request to /public/remoteClusters.

        Cohesity Clusters involved in replication, must be registered to each
        other.
        For example, if Cluster A is replicating Snapshots to Cluster B,
        Cluster
        B must be registered on Cluster A and Cluster B must be registered
        on Cluster A.

        Args:
            cluster_ids (list of long|int, optional): Filter by a list of
                Cluster ids.
            cluster_names (list of string, optional): Filter by a list of
                Cluster names.
            purpose_replication (bool, optional): Filter for purpose as
                Replication.
            purpose_remote_access (bool, optional): Filter for purpose as
                Remote Access.
            verify_reverse_registration (bool, optional): Verify anti
                connection if set to true.

        Returns:
            list of RemoteCluster: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_remote_clusters called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_remote_clusters.')
            _url_path = '/public/remoteClusters'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'clusterIds': cluster_ids,
                'clusterNames': cluster_names,
                'purposeReplication': purpose_replication,
                'purposeRemoteAccess': purpose_remote_access,
                'verifyReverseRegistration': verify_reverse_registration
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_remote_clusters.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_remote_clusters.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_remote_clusters')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_remote_clusters.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RemoteCluster.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_remote_cluster(self, body):
        """Does a POST request to /public/remoteClusters.

        For a Protection Job to replicate Snapshots from one Cluster
        to another Cluster, the Clusters must be paired together by
        registering each Cluster on the other Cluster.
        For example, Cluster A must be registered on Cluster B
        and Cluster B must be registered on Cluster A.

        Args:
            body (RegisterRemoteCluster): Request to register a remote
                Cluster.

        Returns:
            RemoteCluster: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_remote_cluster called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_remote_cluster.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_remote_cluster.')
            _url_path = '/public/remoteClusters'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_remote_cluster.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_remote_cluster.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_remote_cluster')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_remote_cluster.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RemoteCluster.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_remote_cluster(self, id):
        """Does a DELETE request to /public/remoteClusters/{id}.

        Delete the specified remote Cluster registration connection
        on this Cluster.

        Args:
            id (long|int): id of the remote Cluster

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_remote_cluster called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_remote_cluster.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_remote_cluster.')
            _url_path = '/public/remoteClusters/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_remote_cluster.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='delete_remote_cluster')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_remote_cluster.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_remote_cluster_by_id(self, id):
        """Does a GET request to /public/remoteClusters/{id}.

        Returns the details about the remote Cluster with the specified
        Cluster id
        that is registered on this local Cluster.

        Args:
            id (long|int): id of the remote Cluster

        Returns:
            list of RemoteCluster: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_remote_cluster_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_remote_cluster_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_remote_cluster_by_id.')
            _url_path = '/public/remoteClusters/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_remote_cluster_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_remote_cluster_by_id.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_remote_cluster_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_remote_cluster_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RemoteCluster.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_remote_cluster(self, id, body):
        """Does a PUT request to /public/remoteClusters/{id}.

        Update the connection settings of the specified remote Cluster that
        is
        registered on this Cluster.

        Args:
            id (long|int): id of the remote Cluster
            body (RegisterRemoteCluster): Request to update a remote Cluster.

        Returns:
            RemoteCluster: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_remote_cluster called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_remote_cluster.')
            self.validate_parameters(id=id, body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_remote_cluster.')
            _url_path = '/public/remoteClusters/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_remote_cluster.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_remote_cluster.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_remote_cluster')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_remote_cluster.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RemoteCluster.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_replication_encryption_key(self):
        """Does a GET request to /public/replicationEncryptionKey.

        Get the encryption key that is used for encrypting replication data
        between this Cluster and a remote Cluster.

        Returns:
            ReplicationEncryptionKeyReponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_replication_encryption_key called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_replication_encryption_key.')
            _url_path = '/public/replicationEncryptionKey'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_replication_encryption_key.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_replication_encryption_key.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_replication_encryption_key')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_replication_encryption_key.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ReplicationEncryptionKeyReponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
