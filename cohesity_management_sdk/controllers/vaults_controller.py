# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.vault import Vault
from cohesity_management_sdk.models.tape_media_information import TapeMediaInformation
from cohesity_management_sdk.models.vault_bandwidth_limits import VaultBandwidthLimits
from cohesity_management_sdk.models.vault_encryption_key import VaultEncryptionKey
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class VaultsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(VaultsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_vaults(self,
                   id=None,
                   name=None,
                   global_id=None,
                   include_fort_knox_vault=None,
                   include_marked_for_removal=None,
                   tenant_ids=None):
        """Does a GET request to /public/vaults.

        If no parameters are specified, all Vaults (External Targets)
        currently
        registered on the Cohesity Cluster are returned.
        Specifying parameters filters the results that are returned.
        A Vault is equivalent to an External Target in the Cohesity
        Dashboard.

        Args:
            id (long|int, optional): Specifies the id of Vault to return. If
                empty, all Vaults are returned.
            name (string, optional): Specifies the name of the Vault to
                return. If empty, all Vaults are returned.
            global_id (string, optional): Specifies the global Identifier of
                the vault to be returned. If empty, all Vaults are returned.
            include_fort_knox_vault (bool, optional): Specifies if Vaults that
                are RPaaS vaults should be returned.
            include_marked_for_removal (bool, optional): Specifies if Vaults
                that are marked for removal should be returned.
            tenant_ids (list of string, optional): Specifies a list of tenant
                ids. Only vaults assigned to these tenants will be returned.

        Returns:
            list of Vault: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_vaults called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_vaults.')
            _url_path = '/public/vaults'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'id': id,
                'name': name,
                'globalId': global_id,
                'includeFortKnoxVault': include_fort_knox_vault,
                'includeMarkedForRemoval': include_marked_for_removal,
                'tenantIds': tenant_ids
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_vaults.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_vaults.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_vaults')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_vaults.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Vault.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_vault(self, body):
        """Does a POST request to /public/vaults.

        Returns the created Vault.
        A Vault is equivalent to an External Target in the Cohesity
        Dashboard.

        Args:
            body (Vault): Request to create a new Vault.

        Returns:
            Vault: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_vault called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_vault.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_vault.')
            _url_path = '/public/vaults'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_vault.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_vault.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_vault')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_vault.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Vault.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_archive_media_info(self,
                               cluster_id,
                               cluster_incarnation_id,
                               qstar_archive_job_id,
                               qstar_restore_task_id=None,
                               entity_ids=None):
        """Does a GET request to /public/vaults/archiveMediaInfo.

        Returns the media information about the specified archive service uid
        (such as a QStar tape archive service).
        An archive service uid is uniquely identified using a combination of
        the
        following fields: clusterIncarnationId, entityIds and clusterId.
        These are all required fields.

        Args:
            cluster_id (long|int): Specifies the id of the Cohesity Cluster
                that archived to a QStar media Vault.
            cluster_incarnation_id (long|int): Specifies the incarnation id of
                the Cohesity Cluster that archived to a QStar media Vault.
            qstar_archive_job_id (long|int): Specifies the id of the Job that
                archived to a QStar media Vault.
            qstar_restore_task_id (long|int, optional): Specifies the id of
                the restore task to optionally filter by. The restore task
                that is restoring data from the specified media Vault.
            entity_ids (list of long|int, optional): Specifies an array of
                entityIds to optionally filter by. An entityId is a unique id
                for a VM assigned by the Cohesity Cluster.

        Returns:
            list of TapeMediaInformation: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_archive_media_info called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_archive_media_info.')
            self.validate_parameters(
                cluster_id=cluster_id,
                cluster_incarnation_id=cluster_incarnation_id,
                qstar_archive_job_id=qstar_archive_job_id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_archive_media_info.')
            _url_path = '/public/vaults/archiveMediaInfo'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'clusterId': cluster_id,
                'clusterIncarnationId': cluster_incarnation_id,
                'qstarArchiveJobId': qstar_archive_job_id,
                'qstarRestoreTaskId': qstar_restore_task_id,
                'entityIds': entity_ids
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_archive_media_info.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_archive_media_info.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_archive_media_info')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_archive_media_info.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                TapeMediaInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_bandwidth_settings(self):
        """Does a GET request to /public/vaults/bandwidthSettings.

        Returns the upload and download bandwidth limits.

        Returns:
            VaultBandwidthLimits: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_bandwidth_settings called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_bandwidth_settings.')
            _url_path = '/public/vaults/bandwidthSettings'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_bandwidth_settings.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_bandwidth_settings.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_bandwidth_settings')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_bandwidth_settings.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                VaultBandwidthLimits.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_bandwidth_settings(self, body):
        """Does a PUT request to /public/vaults/bandwidthSettings.

        Returns the updated bandwidth limits.

        Args:
            body (VaultBandwidthLimits): Request to update global bandwidth
                limits settings.

        Returns:
            VaultBandwidthLimits: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_bandwidth_settings called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_bandwidth_settings.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_bandwidth_settings.')
            _url_path = '/public/vaults/bandwidthSettings'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_bandwidth_settings.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_bandwidth_settings.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_bandwidth_settings')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_bandwidth_settings.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                VaultBandwidthLimits.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_vault_encryption_key(self, id):
        """Does a GET request to /public/vaults/encryptionKey/{id}.

        Get encryption information (such as the encryption key)
        for the specified Vault (External Target).
        To restore data to a remote Cluster (for example to support a
        disaster
        recovery scenario), you must get the encryption key of the Vault
        and store it outside the local source Cluster, before disaster
        strikes.
        If you have the encryption key and the local source Cluster goes
        down,
        you can restore the data to a remote Cluster from the Vault.
        The local source Cluster is the Cluster that archived the data on the
        Vault.

        Args:
            id (long|int): Specifies a unique id of the Vault.

        Returns:
            VaultEncryptionKey: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_vault_encryption_key called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_vault_encryption_key.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_vault_encryption_key.')
            _url_path = '/public/vaults/encryptionKey/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_vault_encryption_key.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_vault_encryption_key.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_vault_encryption_key')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_vault_encryption_key.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, VaultEncryptionKey.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_vault_by_id(self, id):
        """Does a GET request to /public/vaults/{id}.

        Returns the Vault corresponding to the specified Vault Id.
        A Vault is equivalent to an External Target in the Cohesity
        Dashboard.

        Args:
            id (long|int): Specifies a unique id of the Vault.

        Returns:
            Vault: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_vault_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_vault_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_vault_by_id.')
            _url_path = '/public/vaults/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_vault_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_vault_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_vault_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_vault_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Vault.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_vault(self, id, body):
        """Does a PUT request to /public/vaults/{id}.

        Update the settings of a Vault.
        A Vault is equivalent to an External Target in the Cohesity
        Dashboard.
        Returns the updated Vault.

        Args:
            id (long|int): Specifies a unique id of the Vault.
            body (Vault): Request to update a Vault's settings.

        Returns:
            Vault: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_vault called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_vault.')
            self.validate_parameters(id=id, body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_vault.')
            _url_path = '/public/vaults/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_vault.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_vault.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_vault')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_vault.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Vault.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise


    def delete_vault(self, id, body):
        """Does a DELETE request to /public/vaults/{id}.

        Returns delete status upon completion.
        A Vault is equivalent to an External Target in the Cohesity Dashboard.

        Args:
            id (long|int): Specifies a unique id of the Vault.
            body (VaultDeleteParams): Request to delete vault.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_vault called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_vault.')
            self.validate_parameters(id=id, body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_vault.')
            _url_path = '/public/vaults/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_vault.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_vault.')
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='delete_vault')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_vault.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

