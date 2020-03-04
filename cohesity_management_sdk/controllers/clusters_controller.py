# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.cluster_public_keys import ClusterPublicKeys
from cohesity_management_sdk.models.create_cluster_result import CreateClusterResult
from cohesity_management_sdk.models.cluster_creation_progress_result import ClusterCreationProgressResult
from cohesity_management_sdk.models.service_gflags import ServiceGflags
from cohesity_management_sdk.models.io_preferential_tier import IoPreferentialTier
from cohesity_management_sdk.models.service_state_result import ServiceStateResult
from cohesity_management_sdk.models.change_service_state_result import ChangeServiceStateResult
from cohesity_management_sdk.models.upgrade_cluster_result import UpgradeClusterResult
from cohesity_management_sdk.models.external_client_subnets import ExternalClientSubnets
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.exceptions.error_exception import ErrorException


class ClustersController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, client=None, call_back=None):
        super(ClustersController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_cluster_keys(self):
        """Does a GET request to /public/cluster/keys.

        Returns the Public Keys for the cluster.

        Returns:
            ClusterPublicKeys: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_cluster_keys called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_cluster_keys.')
            _url_path = '/public/cluster/keys'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_cluster_keys.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_cluster_keys.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name='get_cluster_keys')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_cluster_keys.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, ClusterPublicKeys.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def destroy_cluster(self):
        """Does a DELETE request to /public/clusters.

        Sends a request to destroy a Cohesity Cluster and returns some
        information
        about the operation and each Node.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('destroy_cluster called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for destroy_cluster.')
            _url_path = '/public/clusters'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for destroy_cluster.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name='destroy_cluster')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for destroy_cluster.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_cloud_cluster(self, body):
        """Does a POST request to /public/clusters/cloudEdition.

        Sends a request to create a new Cloud Edition Cohesity Cluster and
        returns
        the IDs, name, and software version of the new cluster. Also returns
        the
        status of each node.

        Args:
            body (CreateCloudClusterParameters): TODO: type description here.
                Example:

        Returns:
            CreateClusterResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_cloud_cluster called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_cloud_cluster.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_cloud_cluster.')
            _url_path = '/public/clusters/cloudEdition'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_cloud_cluster.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_cloud_cluster.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request,
                                            name='create_cloud_cluster')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_cloud_cluster.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                CreateClusterResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_expand_cloud_cluster(self, body):
        """Does a POST request to /public/clusters/cloudEdition/nodes.

        Sends a request to expand a Cloud Edition Cohesity Cluster and returns
        some
        information about the request and each new Node.

        Args:
            body (ExpandCloudClusterParameters): TODO: type description here.
                Example:

        Returns:
            CreateClusterResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_expand_cloud_cluster called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_expand_cloud_cluster.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_expand_cloud_cluster.')
            _url_path = '/public/clusters/cloudEdition/nodes'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_expand_cloud_cluster.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_expand_cloud_cluster.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request,
                                            name='create_expand_cloud_cluster')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_expand_cloud_cluster.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                CreateClusterResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_cluster_creation_progress(self):
        """Does a GET request to /public/clusters/creationProgress.

        Sends a request to check the progress of the creation of a new
        Cohesity
        Cluster and returns some information about the creation process along
        with an estimated time remaining and completion percentage.

        Returns:
            ClusterCreationProgressResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_cluster_creation_progress called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_cluster_creation_progress.')
            _url_path = '/public/clusters/creationProgress'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_cluster_creation_progress.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_cluster_creation_progress.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(
                _request, name='get_cluster_creation_progress')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_cluster_creation_progress.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ClusterCreationProgressResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_service_gflag(self, service_name=None, gflags_name_list=None):
        """Does a GET request to /public/clusters/gflag.

        Sends a request to get the gflags of the current Cluster.

        Args:
            service_name (ServiceNameGetServiceGflagEnum, optional): Specifies
                the service name. If specified, only gflags matching the
                service name will be returned. 'kApollo' is a service for
                reclaiming freed disk sectors on Nodes in the SnapFS
                distributed file system. 'kBridge' is a service for managing
                the SnapFS distributed file system. 'kGenie' is a service that
                is responsible for monitoring hardware health on the Cluster.
                'kGenieGofer' is a service that links the Genie service to
                other services on the Cluster. 'kMagneto' is the data
                protection service of the Cohesity Data Platform. 'kIris' is
                the service which serves REST API calls to the UI, CLI, and
                any scripts written by customers. 'kIrisProxy' is a service
                that links the Iris service to other services on the Cluster.
                'kScribe' is the service responsible for storing filesystem
                metadata. 'kStats' is the service that is responsible for
                retrieving and aggregating disk metrics across the Cluster.
                'kYoda' is an elastic search indexing service. 'kAlerts' is a
                publisher and subscribing service for alerts. 'kKeychain' is a
                service for managing disk encryption keys. 'kLogWatcher' is a
                service that scans the log directory and reduces the number of
                logs if required. 'kStatsCollector' is a service that
                periodically logs system stats. 'kGandalf' is a distributed
                lock service and coordination manager. 'kNexus' indicates the
                Nexus service. This is the service that is responsible for
                creation of Clusters and configuration of Nodes and
                networking. 'kNexusProxy' is a service that links the Nexus
                service to other services on the Cluster. 'kStorageProxy' is a
                service for accessing data on external entities. 'kTricorder'
                is a diagnostic health testing service for Clusters.
                'kRtClient' is a reverse tunneling client service.
                'kVaultProxy' is a service for managing external targets that
                Clusters can be backed up to. 'kSmbProxy' is an SMB protocol
                service. 'kBridgeProxy' is the service that links the Bridge
                service to other services on the Cluster. 'kLibrarian' is an
                elastic search indexing service. 'kGroot' is a service for
                managing replication of SQL databases across multiple nodes in
                a Cluster. 'kEagleAgent' is a service that is responsible for
                retrieving information on Cluster health. 'kAthena' is a
                service for running distributed containerized applications on
                the Cohesity Data Platform. 'kBifrostBroker' is a service for
                communicating with the Cohesity proxies for multitenancy.
                'kSmb2Proxy' is a new SMB protocol service. 'kOs' can be
                specified in order to do a full reboot.
            gflags_name_list (list of string, optional): Specifies a list of
                gflag names. If specified, only gflags matching the gflag name
                list will be returned.

        Returns:
            list of ServiceGflags: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_service_gflag called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_service_gflag.')
            _url_path = '/public/clusters/gflag'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'serviceName': service_name,
                'gflagsNameList': gflags_name_list
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_service_gflag.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_service_gflag.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name='get_service_gflag')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_service_gflag.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ServiceGflags.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_service_gflag(self, body):
        """Does a PUT request to /public/clusters/gflag.

        Sends a request to update the gflags of the current Cluster.

        Args:
            body (UpdateGflagParameters): TODO: type description here.
                Example:

        Returns:
            list of ServiceGflags: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_service_gflag called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_service_gflag.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_service_gflag.')
            _url_path = '/public/clusters/gflag'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_service_gflag.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_service_gflag.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request,
                                            name='update_service_gflag')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_service_gflag.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ServiceGflags.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_io_preferential_tier(self):
        """Does a GET request to /public/clusters/ioPreferentialTier.

        Get the IO preferential tiers of the cluster.

        Returns:
            IoPreferentialTier: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_io_preferential_tier called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_io_preferential_tier.')
            _url_path = '/public/clusters/ioPreferentialTier'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_io_preferential_tier.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_io_preferential_tier.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request,
                                            name='get_io_preferential_tier')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_io_preferential_tier.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException(Error, _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, IoPreferentialTier.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def put_io_preferential_tier(self, body):
        """Does a PUT request to /public/clusters/ioPreferentialTier.

        Update the IO preferential tiers of the cluster.

        Args:
            body (IoPreferentialTier): TODO: type description here. Example:

        Returns:
            IoPreferentialTier: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('put_io_preferential_tier called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for put_io_preferential_tier.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for put_io_preferential_tier.')
            _url_path = '/public/clusters/ioPreferentialTier'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for put_io_preferential_tier.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for put_io_preferential_tier.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request,
                                            name='put_io_preferential_tier')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for put_io_preferential_tier.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException(Error, _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, IoPreferentialTier.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def remove_node(self, id):
        """Does a DELETE request to /public/clusters/nodes/{id}.

        Sends a request to remove a Node from a Cohesity Cluster.

        Args:
            id (long|int): Specifies the ID of the node being removed.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('remove_node called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for remove_node.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for remove_node.')
            _url_path = '/public/clusters/nodes/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for remove_node.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name='remove_node')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for remove_node.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_physical_cluster(self, body):
        """Does a POST request to /public/clusters/physicalEdition.

        Sends a request to create a new Physical Edition Cohesity Cluster and
        returns
        the IDs, name, and software version of the new cluster. Also returns
        the
        status of each node.

        Args:
            body (CreatePhysicalClusterParameters): TODO: type description
                here. Example:

        Returns:
            CreateClusterResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_physical_cluster called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_physical_cluster.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_physical_cluster.')
            _url_path = '/public/clusters/physicalEdition'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_physical_cluster.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_physical_cluster.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request,
                                            name='create_physical_cluster')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_physical_cluster.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                CreateClusterResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_expand_physical_cluster(self, body):
        """Does a POST request to /public/clusters/physicalEdition/nodes.

        Sends a request to expand a Physical Edition Cohesity Cluster and
        returns some
        information about the request and each new Node.

        Args:
            body (ExpandPhysicalClusterParameters): TODO: type description
                here. Example:

        Returns:
            CreateClusterResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_expand_physical_cluster called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_expand_physical_cluster.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_expand_physical_cluster.')
            _url_path = '/public/clusters/physicalEdition/nodes'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_expand_physical_cluster.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_expand_physical_cluster.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(
                _request, name='create_expand_physical_cluster')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_expand_physical_cluster.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                CreateClusterResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_service_states(self):
        """Does a GET request to /public/clusters/services/states.

        Sends a request to list the states of all of the services on a
        Cluster.

        Returns:
            list of ServiceStateResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_service_states called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for list_service_states.')
            _url_path = '/public/clusters/services/states'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_service_states.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_service_states.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request,
                                            name='list_service_states')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for list_service_states.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, ServiceStateResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def change_service_state(self, body):
        """Does a POST request to /public/clusters/services/states.

        Sends a request to either stop, start, or restart one or more of the
        services
        on a Cohesity Cluster and returns a message describing the result.

        Args:
            body (ChangeServiceStateParameters): TODO: type description here.
                Example:

        Returns:
            ChangeServiceStateResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('change_service_state called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for change_service_state.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for change_service_state.')
            _url_path = '/public/clusters/services/states'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for change_service_state.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for change_service_state.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request,
                                            name='change_service_state')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for change_service_state.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ChangeServiceStateResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_upgrade_cluster(self, body):
        """Does a PUT request to /public/clusters/software.

        Sends a request to upgrade the software version of a Cohesity Cluster
        and returns a message specifying the result. Before using this, you
        need to
        use the /public/packages endpoint to upload a new package to the
        Cluster.

        Args:
            body (UpgradeClusterParameters): TODO: type description here.
                Example:

        Returns:
            UpgradeClusterResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_upgrade_cluster called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_upgrade_cluster.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_upgrade_cluster.')
            _url_path = '/public/clusters/software'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_upgrade_cluster.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_upgrade_cluster.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request,
                                            name='update_upgrade_cluster')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_upgrade_cluster.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                UpgradeClusterResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_virtual_cluster(self, body):
        """Does a POST request to /public/clusters/virtualEdition.

        Sends a request to create a new Virtual Edition Cohesity Cluster and
        returns
        the IDs, name and software version of the new cluster.

        Args:
            body (CreateVirtualClusterParameters): TODO: type description
                here. Example:

        Returns:
            CreateClusterResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_virtual_cluster called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_virtual_cluster.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_virtual_cluster.')
            _url_path = '/public/clusters/virtualEdition'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_virtual_cluster.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_virtual_cluster.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request,
                                            name='create_virtual_cluster')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_virtual_cluster.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                CreateClusterResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_external_client_subnets(self):
        """Does a GET request to /public/externalClientSubnets.

        Returns the external Client Subnets for the cluster.

        Returns:
            ExternalClientSubnets: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_external_client_subnets called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_external_client_subnets.')
            _url_path = '/public/externalClientSubnets'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_external_client_subnets.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_external_client_subnets.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request,
                                            name='get_external_client_subnets')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_external_client_subnets.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ExternalClientSubnets.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_external_client_subnets(self, body=None):
        """Does a PUT request to /public/externalClientSubnets.

        Returns the updated external Client Subnets of the cluster.

        Args:
            body (ExternalClientSubnets, optional): TODO: type description
                here. Example:

        Returns:
            ExternalClientSubnets: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_external_client_subnets called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_external_client_subnets.')
            _url_path = '/public/externalClientSubnets'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_external_client_subnets.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_external_client_subnets.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(
                _request, name='update_external_client_subnets')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_external_client_subnets.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ExternalClientSubnets.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
