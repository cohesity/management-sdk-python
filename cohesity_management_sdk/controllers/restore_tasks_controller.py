# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.ad_root_topology_object import AdRootTopologyObject
from cohesity_management_sdk.models.compared_ad_object import ComparedADObject
from cohesity_management_sdk.models.ad_object import ADObject
from cohesity_management_sdk.models.file_search_results import FileSearchResults
from cohesity_management_sdk.models.ad_objects_restore_status import AdObjectsRestoreStatus
from cohesity_management_sdk.models.restore_task import RestoreTask
from cohesity_management_sdk.models.file_fstat_result import FileFstatResult
from cohesity_management_sdk.models.file_snapshot_information import FileSnapshotInformation
from cohesity_management_sdk.models.object_search_results import ObjectSearchResults
from cohesity_management_sdk.models.list_org_vdc_networks_response import ListOrgVdcNetworksResponse
from cohesity_management_sdk.models.restore_points_for_time_range import RestorePointsForTimeRange
from cohesity_management_sdk.models.list_storage_profiles_response_body import ListStorageProfilesResponseBody
from cohesity_management_sdk.models.virtual_disk_information import VirtualDiskInformation
from cohesity_management_sdk.models.vm_directory_list_result import VmDirectoryListResult
from cohesity_management_sdk.models.vm_volumes_information import VmVolumesInformation
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class RestoreTasksController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(RestoreTasksController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_ad_domain_root_topology(self, restore_task_id):
        """Does a GET request to /public/restore/adDomainRootTopology.

        Returns the root topology for an AD domain.

        Args:
            restore_task_id (long|int): Specifies the restoreTaskId
                corresponding to which we need to get the ad topology.

        Returns:
            list of AdRootTopologyObject: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_ad_domain_root_topology called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_ad_domain_root_topology.'
            )
            self.validate_parameters(restore_task_id=restore_task_id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_ad_domain_root_topology.')
            _url_path = '/public/restore/adDomainRootTopology'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'restoreTaskId': restore_task_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_ad_domain_root_topology.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_ad_domain_root_topology.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_ad_domain_root_topology')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_ad_domain_root_topology.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                AdRootTopologyObject.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_compare_ad_objects(self, body):
        """Does a POST request to /public/restore/adObjectAttributes.

        Returns the list of AD Objects after comparing attributes of AD Object
        from
        both Snapshot and Production AD.

        Args:
            body (CompareAdObjectsRequest): Specifies the Request to compare
                the AD Objects from both Snapshot and Production AD.

        Returns:
            list of ComparedADObject: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_compare_ad_objects called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_compare_ad_objects.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_compare_ad_objects.')
            _url_path = '/public/restore/adObjectAttributes'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_compare_ad_objects.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_compare_ad_objects.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_compare_ad_objects')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_compare_ad_objects.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ComparedADObject.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def search_ad_objects(self,
                          restore_task_id,
                          num_objects=None,
                          search_base_dn=None,
                          subtree_search_scope=None,
                          compare_objects=None,
                          exclude_system_properties=None,
                          filter=None,
                          record_offset=None):
        """Does a GET request to /public/restore/adObjects.

        Returns the list of AD Objects along with status whether they are
        missing in
        Production AD, equal or not equal.

        Args:
            restore_task_id (long|int): Specifies the restoreTaskId
                corresponding to which we need to search AD objects.
            num_objects (int, optional): Specifies the number of AD Objects to
                be fetched.
            search_base_dn (string, optional): Specifies the search base
                distinguished name from where the search should begin in the
                hierarchy of the AD in both Production and Snapshot AD.
            subtree_search_scope (bool, optional): Specifies the search scope
                for the request. If subtree search scope is true all the
                children of Search Base DN are returned from given offset. If
                subtree search scope is false only all objects which are one
                level from the Search Base DN are returned.
            compare_objects (bool, optional): Specifies the option to compare
                the properties from Snapshot AD and Production AD if specifed
                and sets kNotEqual flag in the result when there is mismatch.
            exclude_system_properties (bool, optional): Specifies the option
                to exclude the system attributes while comparing the the
                objects from the Production AD and Snapshot AD.
            filter (string, optional): Specifies the filter which can be used
                for searching the AD Objects from given Search Base DN. There
                are two types of filters supported. They are: 1) If the string
                does not contain LDAP delimiters '(' and ')', then it is
                assumed to be ANR search "(anr=<ldap_filter>)" Eg: "a" will
                result in query to return all ANR fields with "a" characters
                (case insensitive) in them 2) Search with OR and AND
                combination: "(|(&(objectClass=user)(distinguishedName=CN=Jone
                Doe,OU=Users,DC=corp,DC=cohesity,DC=com))(&(objectClass=user)
                (sAMAccountName=jdoe)))"
            record_offset (int, optional): Specifies the offset from which AD
                objects should be searched in both the Snapshot and Production
                AD.

        Returns:
            list of ADObject: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('search_ad_objects called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for search_ad_objects.')
            self.validate_parameters(restore_task_id=restore_task_id)

            # Prepare query URL
            self.logger.info('Preparing query URL for search_ad_objects.')
            _url_path = '/public/restore/adObjects'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'restoreTaskId': restore_task_id,
                'numObjects': num_objects,
                'searchBaseDn': search_base_dn,
                'subtreeSearchScope': subtree_search_scope,
                'compareObjects': compare_objects,
                'excludeSystemProperties': exclude_system_properties,
                'filter': filter,
                'recordOffset': record_offset
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for search_ad_objects.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for search_ad_objects.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='search_ad_objects')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for search_ad_objects.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ADObject.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_search_production_ad_objects(self, body):
        """Does a POST request to /public/restore/adObjects.

        Returns the list of AD Objects that match the list of object guids,
        sam account names and distinguished names provided in the request.

        Args:
            body (SearchProductionAdObjectsRequest): Specifies the Request to
                search the AD Objects from Production AD.

        Returns:
            list of ADObject: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_search_production_ad_objects called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_search_production_ad_objects.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_search_production_ad_objects.')
            _url_path = '/public/restore/adObjects'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_search_production_ad_objects.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_search_production_ad_objects.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_search_production_ad_objects')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_search_production_ad_objects.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ADObject.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_ad_objects(self,
                       name=None,
                       sam_account_name=None,
                       object_type=None,
                       email=None,
                       registered_source_ids=None,
                       job_ids=None,
                       view_box_ids=None,
                       domain=None,
                       tenant_id=None,
                       all_under_hierarchy=None):
        """Does a GET request to /public/restore/adObjects/searchResults.

        Search for AD objects to recover that match the specified search and
        filter criterias
        provided in the request.

        Args:
            name (string, optional): Specifies the name of the AD object.
            sam_account_name (string, optional): Specifies the sam account
                name of the AD object.
            object_type (string, optional): Specifies the type of the AD
                Object. The type may be user, computer, group or
                ou(organizational unit).
            email (string, optional): Specifies the email of the AD object of
                type user or group.
            registered_source_ids (list of long|int, optional): Specifies the
                Active Directory Application Server Ids which contains the AD
                objects.
            job_ids (list of long|int, optional): Specifies the protection job
                Ids which have backed up Active Directory Application Server.
            view_box_ids (list of long|int, optional): Filter by a list of
                Domains (View Boxes) ids. Only items stored in the listed
                Domains (View Boxes) are returned.
            domain (string, optional): domain of the AD object.
            tenant_id (string, optional): TenantId specifies the tenant whose
                action resulted in the audit log.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if logs of all the tenants under the hierarchy of tenant with
                id TenantId should be returned.

        Returns:
            FileSearchResults: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_ad_objects called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_ad_objects.')
            _url_path = '/public/restore/adObjects/searchResults'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'name': name,
                'samAccountName': sam_account_name,
                'objectType': object_type,
                'email': email,
                'registeredSourceIds': registered_source_ids,
                'jobIds': job_ids,
                'viewBoxIds': view_box_ids,
                'domain': domain,
                'tenantId': tenant_id,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_ad_objects.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_ad_objects.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_ad_objects')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_ad_objects.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, FileSearchResults.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_one_drive_documents(self,
                                tenant_ids=None,
                                all_under_hierarchy=None,
                                document_name=None,
                                domain_ids=None,
                                mailbox_ids=None,
                                protection_job_ids=None):
        """Does a GET request to /public/restore/office365/onedrive/documents.

        Search for OneDrive files and folder to recover that match the
        specified
        search and filter criterias on the Cohesity cluster.

        Args:
            tenant_ids (string, optional): TenantId specifies the tenant
                whose action resulted in the audit log.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if logs of all the tenants under the hierarchy of tenant with
                id TenantId should be returned.
            document_name (string, optional): Specifies the document
                (file/folder) name.
            domain_ids (list of int, optional): Specifies the domain Ids in
                which Users' OneDrives are registered.
            mailbox_ids (list of int, optional): Specifies the Office365 User
                Ids which is the owner of the OneDrive.
            protection_job_ids (list of string, optional): Specifies the
                protection job Ids which have backed up mailbox(es) contianing
                emails/folders.

        Returns:
            FileSearchResults: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_one_drive_documents called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_one_drive_documents.')
            _url_path = '/public/restore/office365/onedrive/documents'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy,
                'documentName': document_name,
                'domainIds': domain_ids,
                'mailboxIds': mailbox_ids,
                'protectionJobIds': protection_job_ids
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_one_drive_documents.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_one_drive_documents.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_one_drive_documents')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_one_drive_documents.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                FileSearchResults.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise


    def get_ad_objects_restore_status(self, restore_task_id=None):
        """Does a GET request to /public/restore/adObjects/status.

        Returns the Restore status of the AD objects which were restored from
        the
        snapshot AD to production AD as part of the restore task id specified
        in the
        parameters.

        Args:
            restore_task_id (long|int, optional): Specifies the restoreTaskId
                corresponding to which we need to get information about the
                restore of the AD objects.

        Returns:
            AdObjectsRestoreStatus: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_ad_objects_restore_status called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_ad_objects_restore_status.')
            _url_path = '/public/restore/adObjects/status'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'restoreTaskId': restore_task_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_ad_objects_restore_status.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_ad_objects_restore_status.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_ad_objects_restore_status')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_ad_objects_restore_status.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                AdObjectsRestoreStatus.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_applications_clone_task(self, body):
        """Does a POST request to /public/restore/applicationsClone.

        Returns the created Restore Task.

        Args:
            body (ApplicationsRestoreTaskRequest): Request to create a Restore
                Task for cloning Applications like SQL DB.

        Returns:
            RestoreTask: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_applications_clone_task called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_applications_clone_task.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_applications_clone_task.')
            _url_path = '/public/restore/applicationsClone'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_applications_clone_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_applications_clone_task.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_applications_clone_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_applications_clone_task.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RestoreTask.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_applications_recover_task(self, body):
        """Does a POST request to /public/restore/applicationsRecover.

        Returns the created Restore Task.

        Args:
            body (ApplicationsRestoreTaskRequest): Request to create a Restore
                Task for recovering Applications like SQL DB. volumes to mount
                points.

        Returns:
            RestoreTask: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_applications_recover_task called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_applications_recover_task.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_applications_recover_task.')
            _url_path = '/public/restore/applicationsRecover'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_applications_recover_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_applications_recover_task.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_applications_recover_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_applications_recover_task.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RestoreTask.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_clone_task(self, body):
        """Does a POST request to /public/restore/clone.

        Returns the created Restore Task that clones VMs or a View.

        Args:
            body (CloneTaskRequest): Request to create a Restore Task for
                cloning VMs or a View.

        Returns:
            RestoreTask: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_clone_task called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_clone_task.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_clone_task.')
            _url_path = '/public/restore/clone'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_clone_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_clone_task.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_clone_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_clone_task.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RestoreTask.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_public_destroy_clone_task(self, id):
        """Does a DELETE request to /public/restore/clone/{id}.

        Destroy a clone task with specified id.

        Args:
            id (long|int): Specifies a unique id of the Clone Task to
                destroy.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_public_destroy_clone_task called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_public_destroy_clone_task.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for delete_public_destroy_clone_task.')
            _url_path = '/public/restore/clone/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_public_destroy_clone_task.'
            )
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='delete_public_destroy_clone_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for delete_public_destroy_clone_task.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_deploy_task(self, body):
        """Does a POST request to /public/restore/deploy.

        Returns the created Restore Task that deploys VMs on cloud. This
        operation
        returns the target where cloud is deployed. Currently, VMs can be
        deployed
        in either AWS target or Azure target.

        Args:
            body (DeployTaskRequest): Request to create a Restore Task for
                deploying VMs or a View on cloud.

        Returns:
            RestoreTask: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_deploy_task called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_deploy_task.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_deploy_task.')
            _url_path = '/public/restore/deploy'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_deploy_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_deploy_task.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_deploy_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_deploy_task.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RestoreTask.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_download_files_and_folders(self, body):
        """Does a POST request to /public/restore/downloadFilesAndFolders.

        Returns the created download Task information that downloads files and
        folders.

        Args:
            body (DownloadFilesAndFoldersParams): Request to create a task for
                downloading list of files or folders.

        Returns:
            RestoreTask: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_download_files_and_folders called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_download_files_and_folders.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_download_files_and_folders.')
            _url_path = '/public/restore/downloadFilesAndFolders'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_download_files_and_folders.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_download_files_and_folders.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_download_files_and_folders')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_download_files_and_folders.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RestoreTask.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def search_restored_files(self,
                              must_have_tags=None,
                              might_have_tags=None,
                              must_have_snapshot_tags=None,
                              might_have_snapshot_tags=None,
                              paginate=None,
                              page_size=None,
                              pagination_cookie=None,
                              search=None,
                              job_ids=None,
                              registered_source_ids=None,
                              view_box_ids=None,
                              environments=None,
                              start_time_usecs=None,
                              end_time_usecs=None,
                              start_index=None,
                              page_count=None,
                              source_ids=None,
                              folder_only=None,
                              tenant_id=None,
                              all_under_hierarchy=None):
        """Does a GET request to /public/restore/files.

        Use the files and folders returned by this operation to populate the
        list of files and folders to recover in the
        POST /public/restore/files operation.
        If no search pattern or filter parameters are specified, all files
        and folders currently found on the Cohesity Cluster are returned.
        Specify a search pattern or parameters to filter the results that
        are returned.
        The term "items" below refers to files and folders that are found
        in the source objects (such as VMs).

        Args:
            must_have_tags(list of string, optional): Specifies tags which must
                be all present in the document.
            might_have_tags(list of string, optional): Specifies list of tags,
                one of which might be present in the document. These are OR'ed
                together and the resulting criteria AND'ed with the rest of the
                query.
            must_have_snapshot_tags(list of string, optional): Specifies
                snapshot tags which must be all present in the document.
            might_have_snapshot_tags(list of string, optional): Specifies list
                of snapshot tags, one of which might be present in the
                document. These are OR'ed together and the resulting criteria
                AND'ed with the rest of the query.
            paginate(bool, optional): Specifies bool to control pagination of
                search results. Only valid for librarian queries. If this is
                set to true and a pagination cookie is provided, search will be
                resumed.
            page_size(int , optional): Specifies pagesize for pagination. Only
                valid for librarian queries. Effective only when Paginate is
                set to true.
            pagination_cookie(string, optional): Specifies cookie for resuming
                search if pagination is being used. Only valid for librarian
                queries. Effective only when Paginate is set to true.
            search (string, optional): Filter by searching for sub-strings in
                the item name. The specified string can match any part of the
                item name. For example: "vm" or "123" both match the item name
                of "vm-123".
            job_ids (list of long|int, optional): Filter by a list of
                Protection Job ids. Only items backed up by the specified Jobs
                are listed.
            registered_source_ids (list of long|int, optional): Filter by a
                list of Registered Sources ids. Only items from the listed
                Registered Sources are returned.
            view_box_ids (list of long|int, optional): Filter by a list of
                Domains (View Boxes) ids. Only items stored in the listed
                Domains (View Boxes) are returned.
            environments (list of EnvironmentSearchRestoredFilesEnum,
                optional): Filter by environment types such as 'kVMware',
                'kView', etc. Only items from the specified environment types
                are returned. NOTE: 'kPuppeteer' refers to Cohesity's Remote
                Adapter.
            start_time_usecs (long|int, optional): Filter by backup completion
                time by specifying a backup completion start and end times.
                Specified as a Unix epoch Timestamp (in microseconds). Only
                items created by backups that completed between the specified
                start and end times are returned.
            end_time_usecs (long|int, optional): Filter by backup completion
                time by specify a backup completion start and end times.
                Specified as a Unix epoch Timestamp (in microseconds). Only
                items created by backups that completed between the specified
                start and end times are returned.
            start_index (long|int, optional): Specifies an index number that
                can be used to return subsets of items in multiple requests.
                Break up the items to return into multiple requests by setting
                pageCount and using startIndex to return a subsets of items.
                For example, set startIndex to 0 to get the first set of items
                for the first request. Increment startIndex by pageCount to
                get the next set of items for a next request. Continue until
                all items are returned and therefore the total number of
                returned items is equal to totalCount.
            page_count (long|int, optional): Limit the number of items to
                return in the response for pagination purposes.
            source_ids (list of long|int, optional): Filter by source ids.
                Only files and folders found in the listed sources (such as
                VMs) are returned.
            folder_only (bool, optional): Filter by folders or files. If true,
                only folders are returned. If false, only files are returned.
                If not specified, both files and folders are returned.
            tenant_id (string, optional): TenantId specifies the tenant whose
                action resulted in the audit log.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if logs of all the tenants under the hierarchy of tenant with
                id TenantId should be returned.

        Returns:
            FileSearchResults: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('search_restored_files called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for search_restored_files.')
            _url_path = '/public/restore/files'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'mustHaveTags': must_have_tags,
                'mightHaveTags': might_have_tags,
                'mustHaveSnapshotTags': must_have_snapshot_tags,
                'mightHaveSnapshotTags': might_have_snapshot_tags,
                'paginate': paginate,
                'pageSize': page_size,
                'paginationCookie': pagination_cookie,
                'search': search,
                'jobIds': job_ids,
                'registeredSourceIds': registered_source_ids,
                'viewBoxIds': view_box_ids,
                'environments': environments,
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs,
                'startIndex': start_index,
                'pageCount': page_count,
                'sourceIds': source_ids,
                'folderOnly': folder_only,
                'tenantId': tenant_id,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for search_restored_files.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for search_restored_files.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='search_restored_files')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for search_restored_files.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, FileSearchResults.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_restore_files_task(self, body):
        """Does a POST request to /public/restore/files.

        Returns the created Restore Task that recovers files and folders.

        Args:
            body (RestoreFilesTaskRequest): Request to create a Restore Task
                for recovering files or folders.

        Returns:
            RestoreTask: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_restore_files_task called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_restore_files_task.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_restore_files_task.')
            _url_path = '/public/restore/files'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_restore_files_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_restore_files_task.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_restore_files_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_restore_files_task.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RestoreTask.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_file_fstat_information(self,
                                   job_id,
                                   job_uid_object_id,
                                   entity_id,
                                   job_instance_id,
                                   job_start_time_usecs,
                                   file_path,
                                   attempt_num=None,
                                   volume_name=None,
                                   view_box_id=None,
                                   view_name=None,
                                   volume_info_cookie=None,
                                   use_librarian=None):
        """Does a GET request to /public/restore/files/fstats.

        Get the fstat information about file provided using query parameters.

        Args:
            job_id (long|int): JobId is the id of the local job that took the
                snapshot, which may or may not match the JobUidObjectId below
                depending on whether the object originally belonged to this
                local job or to a different remote job.
            job_uid_object_id (long|int): JobUidObjectId is the globally
                unique id of the job that the object originally belonged to.
                If this object originally belonged to a job from a remote
                cluster, this field will contain the JobId of the remote job,
                else it will contain the JobId of the local job.
            entity_id (long|int): EntityId is the Id of the VM.
            job_instance_id (long|int): JobInstanceId is the Id of the job run
                that backed up the entity.
            job_start_time_usecs (long|int): JobStartTimeUsecs is the start
                time in usecs of the job run that backed up the entity.
            file_path (string): FilePath is the full path of the file or
                directory whose stat needed.
            attempt_num (long|int, optional): AttemptNum is the attempt number
                of the run that successfully created the snapshot.
            volume_name (string, optional): VolumeName is the name of the
                volume that needs to be browsed. This should match the name
                returned in VolumeInfo.
            view_box_id (long|int, optional): Id of the View Box if a View is
                being browsed.
            view_name (string, optional): Name of the View if a View is being
                browsed.
            volume_info_cookie (int, optional): VolumeInfoCookie is the cookie
                to be passed in calls to reading a VM dir for this volume.
            use_librarian (bool, optional): Specifies whether to use Librarian
                for file stat. This will be true if the browse is enabled via
                librarian.

        Returns:
            FileFstatResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_file_fstat_information called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_file_fstat_information.'
            )
            self.validate_parameters(job_id=job_id,
                                     job_uid_object_id=job_uid_object_id,
                                     entity_id=entity_id,
                                     job_instance_id=job_instance_id,
                                     job_start_time_usecs=job_start_time_usecs,
                                     file_path=file_path)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_file_fstat_information.')
            _url_path = '/public/restore/files/fstats'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'jobId': job_id,
                'jobUidObjectId': job_uid_object_id,
                'entityId': entity_id,
                'jobInstanceId': job_instance_id,
                'jobStartTimeUsecs': job_start_time_usecs,
                'filePath': file_path,
                'attemptNum': attempt_num,
                'volumeName': volume_name,
                'viewBoxId': view_box_id,
                'viewName': view_name,
                'volumeInfoCookie': volume_info_cookie,
                'useLibrarian': use_librarian
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_file_fstat_information.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_file_fstat_information.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_file_fstat_information')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_file_fstat_information.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              FileFstatResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_file_snapshots_information(self, job_id, cluster_id,
                                       cluster_incarnation_id, source_id,
                                       filename):
        """Does a GET request to /public/restore/files/snapshotsInformation.

        Get the information about snapshots that contain the specified file or
        folder. In addition, information about the file or folder is
        provided.

        Args:
            job_id (long|int): Specifies the id of the Job that captured the
                snapshots. These snapshots are searched for the specified
                files or folders. This field is required.
            cluster_id (long|int): Specifies the Cohesity Cluster id where the
                Job was created. This field is required.
            cluster_incarnation_id (long|int): Specifies the incarnation id of
                the Cohesity Cluster where the Job was created. An incarnation
                id is generated when a Cohesity Cluster is initially created.
                This field is required.
            source_id (long|int): Specifies the id of the Protection Source
                object (such as a VM) to search. When a Job Run executes,
                snapshots of the specified Protection Source object are
                captured. This operation searches the snapshots of the object
                for the file or folder. This field is required.
            filename (string): Specifies the name of the file or folder to
                find in the snapshots. This field is required.

        Returns:
            list of FileSnapshotInformation: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_file_snapshots_information called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_file_snapshots_information.'
            )
            self.validate_parameters(
                job_id=job_id,
                cluster_id=cluster_id,
                cluster_incarnation_id=cluster_incarnation_id,
                source_id=source_id,
                filename=filename)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_file_snapshots_information.')
            _url_path = '/public/restore/files/snapshotsInformation'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'jobId': job_id,
                'clusterId': cluster_id,
                'clusterIncarnationId': cluster_incarnation_id,
                'sourceId': source_id,
                'filename': filename
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_file_snapshots_information.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_file_snapshots_information.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_file_snapshots_information')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_file_snapshots_information.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                FileSnapshotInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def search_objects(self,
                       search=None,
                       job_ids=None,
                       registered_source_ids=None,
                       view_box_ids=None,
                       environments=None,
                       office365_source_types=None,
                       start_time_usecs=None,
                       end_time_usecs=None,
                       start_index=None,
                       page_count=None,
                       operating_systems=None,
                       application=None,
                       owner_entity_id=None,
                       tenant_id=None,
                       all_under_hierarchy=None):
        """Does a GET request to /public/restore/objects.

        If no search pattern or filter parameters are specified, all backup
        objects
        currently found on the Cohesity Cluster are returned.
        Only leaf objects that have been protected by a Job are returned such
        as VMs,
        Views and databases.
        Specify a search pattern or parameters to filter the results that
        are returned.
        The term "items" below refers to leaf backup objects such as VMs,
        Views and databases.

        Args:
            search (string, optional): Filter by searching for sub-strings in
                the item name. The specified string can match any part of the
                item name. For example: "vm" or "123" both match the item name
                of "vm-123".
            job_ids (list of long|int, optional): Filter by a list of
                Protection Job ids. Only items backed up by the specified Jobs
                are listed.
            registered_source_ids (list of long|int, optional): Filter by a
                list of Registered Sources ids. Only items from the listed
                Registered Sources are returned.
            view_box_ids (list of long|int, optional): Filter by a list of
                Domains (View Boxes) ids. Only items stored in the listed
                Domains (View Boxes) are returned.
            environments (list of EnvironmentSearchObjectsEnum, optional):
                Filter by environment types such as 'kVMware', 'kView', etc.
                Only items from the specified environment types are returned.
                NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.
            office365_source_types (Office365SourceTypesEnum, optional): Filter
                by Office365 types such as 'kUser', 'kSite', etc.
                Only items from the specified source types are returned.
            start_time_usecs (long|int, optional): Filter by backup completion
                time by specifying a backup completion start and end times.
                Specified as a Unix epoch Timestamp (in microseconds). Only
                items created by backups that completed between the specified
                start and end times are returned.
            end_time_usecs (long|int, optional): Filter by backup completion
                time by specify a backup completion start and end times.
                Specified as a Unix epoch Timestamp (in microseconds). Only
                items created by backups that completed between the specified
                start and end times are returned.
            start_index (long|int, optional): Specifies an index number that
                can be used to return subsets of items in multiple requests.
                Break up the items to return into multiple requests by setting
                pageCount and using startIndex to return a subsets of items.
                For example, set startIndex to 0 to get the first set of items
                for the first request. Increment startIndex by pageCount to
                get the next set of items for a next request. Continue until
                all items are returned and therefore the total number of
                returned items is equal to totalCount.
            page_count (long|int, optional): Limit the number of items to
                return in the response for pagination purposes.
            operating_systems (list of string, optional): Filter by the
                Operating Systems running on VMs and Physical Servers. This
                filter is applicable only to VMs and physical servers.
            application (string, optional): Filter by application when the
                environment type is kSQL. For example, if SQL is specified the
                SQL databases are returned.
            owner_entity_id (long|int, optional): Filter objects by the Entity
                id of the owner VM. For example, if a ownerEntityId is
                provided while searching for SQL databases, only SQL databases
                belonging to the VM with the specified id are returned.
                ownerEntityId is only significant if application is set to
                SQL.
            tenant_id (string, optional): TenantId specifies the tenant whose
                action resulted in the audit log.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if logs of all the tenants under the hierarchy of tenant with
                id TenantId should be returned.

        Returns:
            ObjectSearchResults: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('search_objects called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for search_objects.')
            _url_path = '/public/restore/objects'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'search': search,
                'jobIds': job_ids,
                'registeredSourceIds': registered_source_ids,
                'viewBoxIds': view_box_ids,
                'environments': environments,
                'office365SourceTypes': office365_source_types,
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs,
                'startIndex': start_index,
                'pageCount': page_count,
                'operatingSystems': operating_systems,
                'application': application,
                'ownerEntityId': owner_entity_id,
                'tenantId': tenant_id,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for search_objects.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for search_objects.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='search_objects')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for search_objects.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ObjectSearchResults.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_outlook_emails(self,
                           has_attachments=None,
                           sender_address=None,
                           recipient_addresses=None,
                           cc_recipient_addresses=None,
                           bcc_recipient_addresses=None,
                           sent_time_seconds=None,
                           received_time_seconds=None,
                           received_start_time=None,
                           received_end_time=None,
                           email_subject=None,
                           folder_name=None,
                           show_only_email_folders=None,
                           domain_ids=None,
                           mailbox_ids=None,
                           protection_job_ids=None,
                           tenant_id=None,
                           all_under_hierarchy=None):
        """Does a GET request to /public/restore/office365/outlook/emails.

        Search for Emails and Emails' folders to recover that match the
        specified
        search and filter criterias on the Cohesity cluster.

        Args:
            has_attachments (bool, optional): Specifies whether the emails
                have any attachments.
            sender_address (string, optional): Specifies the email address of
                the sender.
            recipient_addresses (list of string, optional): Specifies the
                email addresses of the recipients.
            cc_recipient_addresses (list of string, optional): Specifies the
                email addresses of the cc recipients.
            bcc_recipient_addresses (list of string, optional): Specifies the
                email addresses of the bcc recipients.
            sent_time_seconds (long|int, optional): Specifies the unix time
                when the email was sent.
            received_time_seconds (long|int, optional): Specifies the unix
                time when the email was received.
            received_start_time (long|int, optional): Specifies the unix start
                time for querying on email's received time.
            received_end_time (long|int, optional): Specifies the unix end
                time for querying on email's received time.
            email_subject (string, optional): Specifies the subject of the
                email.
            folder_name (string, optional): Specifies the parent folder name
                of the email.
            show_only_email_folders (bool, optional): Specifies whether the
                query result should include only Email folders.
            domain_ids (list of long|int, optional): Specifies the domain Ids
                in which mailboxes are registered.
            mailbox_ids (list of long|int, optional): Specifies the mailbox
                Ids which contains the emails/folders.
            protection_job_ids (list of long|int, optional): Specifies the
                protection job Ids which have backed up mailbox(es) continaing
                emails/folders.
            tenant_id (string, optional): TenantId specifies the tenant whose
                action resulted in the audit log.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if logs of all the tenants under the hierarchy of tenant with
                id TenantId should be returned.

        Returns:
            FileSearchResults: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_outlook_emails called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_outlook_emails.')
            _url_path = '/public/restore/office365/outlook/emails'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'hasAttachments': has_attachments,
                'senderAddress': sender_address,
                'recipientAddresses': recipient_addresses,
                'ccRecipientAddresses': cc_recipient_addresses,
                'bccRecipientAddresses': bcc_recipient_addresses,
                'sentTimeSeconds': sent_time_seconds,
                'receivedTimeSeconds': received_time_seconds,
                'receivedStartTime': received_start_time,
                'receivedEndTime': received_end_time,
                'emailSubject': email_subject,
                'folderName': folder_name,
                'showOnlyEmailFolders': show_only_email_folders,
                'domainIds': domain_ids,
                'mailboxIds': mailbox_ids,
                'protectionJobIds': protection_job_ids,
                'tenantId': tenant_id,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_outlook_emails.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_outlook_emails.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_outlook_emails')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_outlook_emails.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, FileSearchResults.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_sharepoint_documents(self,
                                tenant_id=None,
                                all_under_hierarchy=None,
                                document_name=None,
                                domain_ids=None,
                                site_ids=None,
                                protection_job_ids=None):
        """Does a GET request to /public/restore/office365/sharepoint/documents.

        Search for Sharepoint files and folder to recover that match the
        specified
        search and filter criterias on the Cohesity cluster.

        Args:
            tenant_id (string, optional): TenantId specifies the tenant whose
                action resulted in the audit log.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.
            document_name (string, optional): Specifies the document
                (file/folder) name.
            domain_ids (list of int|long, optional): Specifies the domain Ids
                in which Sharepoint Site's are registered.
            site_ids (list of int|long, optional): Specifies the Office365
                Sharepoint Site Id.
            protection_job_ids (list of int|long, optional): Specifies the
                protection job Ids which have backed up sites containing the
                documents.

        Returns:
            FileSearchResults: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_sharepoint_documents called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_sharepoint_documents.')
            _url_path = '/public/restore/office365/sharepoint/documents'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'tenantId': tenant_id,
                'allUnderHierarchy': all_under_hierarchy,
                'documentName': document_name,
                'domainIds': domain_ids,
                'siteIds': site_ids,
                'protectionJobIds': protection_job_ids
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_sharepoint_documents.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_sharepoint_documents.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_sharepoint_documents')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_sharepoint_documents.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                FileSearchResults.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_get_restore_points_for_time_range(self, body):
        """Does a POST request to /public/restore/pointsForTimeRange.

        Returns the snapshots in the time range specified.

        Args:
            body (RestorePointsForTimeRangeParam): TODO: type description
                here. Example:

        Returns:
            RestorePointsForTimeRange: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info(
                'create_get_restore_points_for_time_range called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_get_restore_points_for_time_range.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_get_restore_points_for_time_range.'
            )
            _url_path = '/public/restore/pointsForTimeRange'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_get_restore_points_for_time_range.'
            )
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_get_restore_points_for_time_range.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_get_restore_points_for_time_range')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_get_restore_points_for_time_range.'
            )
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                RestorePointsForTimeRange.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_recover_task(self, body):
        """Does a POST request to /public/restore/recover.

        Returns the created Restore Task. This operation returns the
        following
        types of Restore Tasks: 1) A Restore Task that recovers VMs back to
        the
        original location or a new location. 2) A Restore Task that mounts
        the
        volumes of a Server (such as a VM or Physical Server) onto the
        specified
        target system. The Snapshots of the Server that contains the volumes
        that are mounted is determined by Array of Objects.
        The content of the Server is available from the mount point
        for the Granular Level Recovery (GLR) of application data. For
        example
        recovering Microsoft Exchange data using Kroll Ontrack®
        PowerControls™.
        NOTE: Volumes are mounted "instantly" if the Snapshot is stored
        locally on the
        Cohesity Cluster. If the Snapshot is archival target, it will take
        longer
        because it must be retrieved.

        Args:
            body (RecoverTaskRequest): Request to create a Restore Task for
                recovering VMs or mounting volumes to mount points.

        Returns:
            RestoreTask: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_recover_task called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_recover_task.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_recover_task.')
            _url_path = '/public/restore/recover'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_recover_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_recover_task.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_recover_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_recover_task.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RestoreTask.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_restore_task(self, body):
        """Does a PUT request to /public/restore/recover.

        Updates an existing restore task with additional params which are
        needed for
        features like Hot-Standby.

        Args:
            body (UpdateRestoreTaskParams): TODO: type description here.
                Example:

        Returns:
            RestoreTask: Response from the API. Specifies the response of the
                UpdateRestoreTask API.
Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_restore_task called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_restore_task.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_restore_task.')
            _url_path = '/public/restore/recover'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_restore_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_restore_task.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_restore_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_restore_task.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RestoreTask.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_restore_tasks(self,
                          task_ids=None,
                          start_time_usecs=None,
                          end_time_usecs=None,
                          page_count=None,
                          task_types=None,
                          environment=None,
                          storage_domain_ids=None):
        """Does a GET request to /public/restore/tasks.

        If no parameters are specified, all Restore Tasks found
        on the Cohesity Cluster are returned. Both running and completed
        Restore Tasks are reported.
        Specifying parameters filters the results that are returned.

        Args:
            task_ids (list of long|int, optional): Filter by a list of Restore
                Task ids.
            start_time_usecs (long|int, optional): Filter by a start time
                specified as a Unix epoch Timestamp (in microseconds). All
                Restore Tasks (both completed and running) on the Cohesity
                Cluster that started after the specified start time but before
                the specified end time are returned. If not set, the start
                time is creation time of the Cohesity Cluster.
            end_time_usecs (long|int, optional): Filter by an end time
                specified as a Unix epoch Timestamp (in microseconds). All
                Restore Tasks (both completed and running) on the Cohesity
                Cluster that started after the specified start time but before
                the specified end time are returned. If not set, the end time
                is the current time.
            page_count (long|int, optional): Specifies the number of completed
                Restore Tasks to return in the response for pagination
                purposes. Running Restore Tasks are always returned. The
                newest completed Restore Tasks are returned.
            task_types (list of string, optional): Filter by the types of
                Restore Tasks such as 'kRecoverVMs', 'kCloneVMs', 'kCloneView'
                or 'kMountVolumes'.
            environment (EnvironmentGetRestoreTasksEnum, optional): Specifies
                the environment like VMware, SQL, where the Protection Source
                exists. Supported environment types such as 'kView', 'kSQL',
                'kVMware', etc. NOTE: 'kPuppeteer' refers to Cohesity's Remote
                Adapter. 'kVMware' indicates the VMware Protection Source
                environment. 'kHyperV' indicates the HyperV Protection Source
                environment. 'kSQL' indicates the SQL Protection Source
                environment. 'kView' indicates the View Protection Source
                environment. 'kPuppeteer' indicates the Cohesity's Remote
                Adapter. 'kPhysical' indicates the physical Protection Source
                environment. 'kPure' indicates the Pure Storage Protection
                Source environment. 'kNimble' indicates the Nimble Storage
                Protection Source environment. 'kAzure' indicates the
                Microsoft's Azure Protection Source environment. 'kNetapp'
                indicates the Netapp Protection Source environment. 'kAgent'
                indicates the Agent Protection Source environment.
                'kGenericNas' indicates the Generic Network Attached Storage
                Protection Source environment. 'kAcropolis' indicates the
                Acropolis Protection Source environment. 'kPhsicalFiles'
                indicates the Physical Files Protection Source environment.
                'kIsilon' indicates the Dell EMC's Isilon Protection Source
                environment. 'kGPFS' indicates IBM's GPFS Protection Source
                environment. 'kKVM' indicates the KVM Protection Source
                environment. 'kAWS' indicates the AWS Protection Source
                environment. 'kExchange' indicates the Exchange Protection
                Source environment. 'kHyperVVSS' indicates the HyperV VSS
                Protection Source environment. 'kOracle' indicates the Oracle
                Protection Source environment. 'kGCP' indicates the Google
                Cloud Platform Protection Source environment. 'kFlashBlade'
                indicates the Flash Blade Protection Source environment.
                'kAWSNative' indicates the AWS Native Protection Source
                environment. 'kO365' indicates the
                Office 365 Protection Source environment. 'kO365Outlook'
                indicates Office 365 outlook Protection Source environment.
                'kHyperFlex' indicates the Hyper Flex Protection Source
                environment. 'kGCPNative' indicates the GCP Native Protection
                Source environment. 'kAzureNative' indicates the Azure Native
                Protection Source environment. 'kKubernetes' indicates a
                Kubernetes Protection Source environment. 'kElastifile'
                indicates Elastifile Protection Source environment.
                'kAD' indicates Active Directory Protection Source environment.
                'kRDSSnapshotManager' indicates AWS RDS Protection Source
                environment. 'kCassandra' indicates Cassandra Protection Source
                environment. 'kMongoDB' indicates MongoDB Protection Source
                environment. 'kCouchbase' indicates Couchbase Protection Source
                environment. 'kHdfs' indicates Hdfs Protection Source
                environment. 'kHive' indicates Hive Protection Source
                environment. 'kHBase' indicates HBase Protection Source
                environment. 'kUDA' indicates Universal Data Adapter Protection
                Source environment.
                'kO365Teams' indicates the Office365 Teams Protection Source
                environment.
                'kO365Group' indicates the Office365 Groups Protection Source
                environment.
                'kO365Exchange' indicates the Office365 Mailbox Protection
                Source environment.
                'kO365OneDrive' indicates the Office365 OneDrive Protection
                Source environment.
                'kO365Sharepoint' indicates the Office365 SharePoint Protection
                Source environment.
                'kO365PublicFolders' indicates the Office365 PublicFolders
                Protection Source environment.
            storage_domain_ids (long|int): Filter by a list of Storage Domain
                IDs. This field applies only if 'TaskTypes' includes
                'kCloneView'. Only task writing data to these storage domains
                will be returned.

        Returns:
            list of RestoreTask: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_restore_tasks called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_restore_tasks.')
            _url_path = '/public/restore/tasks'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'taskIds': task_ids,
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs,
                'pageCount': page_count,
                'taskTypes': task_types,
                'environment': environment,
                'storageDomainIds': storage_domain_ids
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_restore_tasks.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_restore_tasks.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_restore_tasks')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_restore_tasks.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RestoreTask.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_cancel_restore_task(self, id):
        """Does a PUT request to /public/restore/tasks/cancel/{id}.

        Cancel a recover or clone task with specified id.

        Args:
            id (long|int): Specifies a unique id for the Restore Task.

        Returns:
            void: Response from the API. Success Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_cancel_restore_task called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_cancel_restore_task.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_cancel_restore_task.')
            _url_path = '/public/restore/tasks/cancel/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_cancel_restore_task.'
            )
            _request = self.http_client.put(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_cancel_restore_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_cancel_restore_task.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_restore_task_by_id(self, id):
        """Does a GET request to /public/restore/tasks/{id}.

        Returns the Restore Task corresponding to the specified Restore Task
        id.

        Args:
            id (long|int): Specifies a unique id for the Restore Task.

        Returns:
            RestoreTask: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_restore_task_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_restore_task_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_restore_task_by_id.')
            _url_path = '/public/restore/tasks/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_restore_task_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_restore_task_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_restore_task_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_restore_task_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RestoreTask.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_virtual_disk_information(self,
                                     cluster_id,
                                     cluster_incarnation_id,
                                     job_id,
                                     job_run_id,
                                     start_time_usecs,
                                     source_id,
                                     point_in_time_usecs=None,
                                     vault_id=None,
                                     vault_name=None,
                                     vault_type=None):
        """Does a GET request to /public/restore/virtualDiskInformation.

        Fetches information of virtual disk.

        Args:
            cluster_id (long|int): Specifies the Cohesity Cluster id where the
                Job was created.
            cluster_incarnation_id (long|int): Specifies the incarnation id of
                the Cohesity Cluster where the Job was created.
            job_id (long|int): Specifies the id of the Job that captured the
                snapshot.
            job_run_id (long|int): Specifies the id of the Job Run that
                captured the snapshot.
            start_time_usecs (long|int): Specifies the start time of the job
                run as a Unix epoch Timestamp in microseconds.
            source_id (long|int): Specifies the Id of the Protection Source
                object.
            point_in_time_usecs (long|int): PointInTimeUsecs is the time to
                get volume virtual disk info from previously available
                full/incremental snapshot.
            vault_id (int|long): Specifies the Id of the vault where snapshot
                was taken.
            vault_name (string): Specifies the name of the vault where snapshot
                was taken.
            vault_type (VaultTypeEnum): Specifes the type of the vault where
                snapshot was taken.

        Returns:
            list of VirtualDiskInformation: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_virtual_disk_information called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_virtual_disk_information.'
            )
            self.validate_parameters(
                cluster_id=cluster_id,
                cluster_incarnation_id=cluster_incarnation_id,
                job_id=job_id,
                job_run_id=job_run_id,
                start_time_usecs=start_time_usecs,
                source_id=source_id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_virtual_disk_information.')
            _url_path = '/public/restore/virtualDiskInformation'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'clusterId': cluster_id,
                'clusterIncarnationId': cluster_incarnation_id,
                'jobId': job_id,
                'jobRunId': job_run_id,
                'startTimeUsecs': start_time_usecs,
                'sourceId': source_id,
                "pointInTimeUsecs": point_in_time_usecs,
                'vaultId': vault_id,
                'vaultName': vault_name,
                'vaultType': vault_type
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_virtual_disk_information.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_virtual_disk_information.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_virtual_disk_information')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_virtual_disk_information.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                VirtualDiskInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_vm_directory_list(self,
                              job_id,
                              job_uid_object_id,
                              entity_id,
                              job_instance_id,
                              job_start_time_usecs,
                              dir_path,
                              attempt_num=None,
                              volume_name=None,
                              view_box_id=None,
                              view_name=None,
                              max_entries=None,
                              volume_info_cookie=None,
                              cookie=None,
                              stat_file_entries=None,
                              browse_indexed_data=None):
        """Does a GET request to /public/restore/vms/directoryList.

        Get the directory list based on the given directory name and other
        query parameters.

        Args:
            job_id (long|int): JobId is the id of the local job that took the
                snapshot, which may or may not match the JobUidObjectId below
                depending on whether the object originally belonged to this
                local job or to a different remote job.
            job_uid_object_id (long|int): JobUidObjectId is the globally
                unique id of the job that the object originally belonged to.
                If this object originally belonged to a job from a remote
                cluster, this field will contain the JobId of the remote job,
                else it will contain the JobId of the local job.
            entity_id (long|int): EntityId is the Id of the VM.
            job_instance_id (long|int): JobInstanceId is the Id of the job run
                that backed up the entity.
            job_start_time_usecs (long|int): JobStartTimeUsecs is the start
                time in usecs of the job run that backed up the entity.
            dir_path (string): DirPath is the full path of the directory whose
                contents need to be listed.
            attempt_num (long|int, optional): AttemptNum is the attempt number
                of the run that successfully created the snapshot.
            volume_name (string, optional): VolumeName is the name of the
                volume that needs to be browsed. This should match the name
                returned in VolumeInfo.
            view_box_id (long|int, optional): Id of the View Box if a View is
                being browsed.
            view_name (string, optional): Name of the View if a View is being
                browsed.
            max_entries (int, optional): MaxEntries is the maximum number of
                entries to return in this call. If there are more entries,
                server will return a cookie in the response that can be used
                to continue enumeration from the last call.
            volume_info_cookie (int, optional): VolumeInfoCookie is the cookie
                to be passed in calls to reading a VM dir for this volume.
            cookie (string, optional): Cookie is used for paginating results.
                If ReadDirResult returned partial results, it will also return
                a cookie that can be used to resume the listing. The value
                returned in ReadDirResult should be passed in the next call.
                The first call should not have this value set. Note that this
                value is only a suggestion and server is free to do a short
                read (return fewer entries along with a cookie).
            stat_file_entries (bool, optional): StatFileEntries specifies
                whether file stat data is returned.
            browse_indexed_data (bool, optional): Specifies whether to use
                indexed data in Librarian for browse.

        Returns:
            VmDirectoryListResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_vm_directory_list called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_vm_directory_list.')
            self.validate_parameters(job_id=job_id,
                                     job_uid_object_id=job_uid_object_id,
                                     entity_id=entity_id,
                                     job_instance_id=job_instance_id,
                                     job_start_time_usecs=job_start_time_usecs,
                                     dir_path=dir_path)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_vm_directory_list.')
            _url_path = '/public/restore/vms/directoryList'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'jobId': job_id,
                'jobUidObjectId': job_uid_object_id,
                'entityId': entity_id,
                'jobInstanceId': job_instance_id,
                'jobStartTimeUsecs': job_start_time_usecs,
                'dirPath': dir_path,
                'attemptNum': attempt_num,
                'volumeName': volume_name,
                'viewBoxId': view_box_id,
                'viewName': view_name,
                'maxEntries': max_entries,
                'volumeInfoCookie': volume_info_cookie,
                'cookie': cookie,
                'statFileEntries': stat_file_entries,
                'browseIndexedData': browse_indexed_data
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_vm_directory_list.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_vm_directory_list.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_vm_directory_list')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_vm_directory_list.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                VmDirectoryListResult.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_vm_volumes_information(self,
                                   job_id,
                                   cluster_id,
                                   cluster_incarnation_id,
                                   job_run_id,
                                   started_time_usecs,
                                   source_id,
                                   original_job_id,
                                   attempt_number=None,
                                   supported_volumes_only=None,
                                   compute_volume_info=None):
        """Does a GET request to /public/restore/vms/volumesInformation.

        All required fields must be specified for this operation.
        To get values for these fields, invoke the GET
        /public/restore/objects
        operation.
        A specific Job Run is defined by the jobRunId, startedTimeUsecs, and
        attemptNumber fields.

        Args:
            job_id (long|int): Specifies the Job id for the Protection Job
                that is currently associated with the object. If the object
                was backed up on current Cohesity Cluster, this field contains
                the id for the Job that captured this backup object. If the
                object was backed up on a Primary Cluster and replicated to
                this Cohesity Cluster, a new Inactive Job is created, the
                object is now associated with new Inactive Job, and this field
                contains the id of the new Inactive Job.
            cluster_id (long|int): Specifies the Cohesity Cluster id where the
                Job was created.
            cluster_incarnation_id (long|int): Specifies the incarnation id of
                the Cohesity Cluster where the Job was created. An incarnation
                id is generated when a Cohesity Cluster is initially created.
            job_run_id (long|int): Specifies the id of the Job Run that
                captured the snapshot.
            started_time_usecs (long|int): Specifies the time when the Job Run
                starts capturing a snapshot. Specified as a Unix epoch
                Timestamp (in microseconds).
            source_id (long|int): Specifies the id of the VM object to search
                for volumes.
            original_job_id (long|int): Specifies the id for the Protection
                Job that originally captured the snapshots of the original
                object. If the object was backed up on a Primary Cluster
                replicated to this Cohesity Cluster, and a new Inactive Job is
                created, this field still contains the id of the original Job
                and NOT the id of the new Inactive Job. This field is used in
                combination with the clusterId and clusterIncarnationId to
                uniquely identify a Job.
            attempt_number (long|int, optional): Specifies the number of the
                attempts made by the Job Run to capture a snapshot of the
                object. For example, if an snapshot is successfully captured
                after three attempts, this field equals 3.
            supported_volumes_only (bool, optional): Specifies to return only
                supported volumes information. Unsupported volumes are not
                returned if this flag is set to true. Default is false.
            compute_volume_info (bool, optional): Specifies whether to compute
                volume information if it is not found. If `ComputeVolumeInfo`
                is false and volume information is not found it skips
                computation of volume information and returns KNotFound.

        Returns:
            list of VmVolumesInformation: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_vm_volumes_information called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_vm_volumes_information.'
            )
            self.validate_parameters(
                job_id=job_id,
                cluster_id=cluster_id,
                cluster_incarnation_id=cluster_incarnation_id,
                job_run_id=job_run_id,
                started_time_usecs=started_time_usecs,
                source_id=source_id,
                original_job_id=original_job_id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_vm_volumes_information.')
            _url_path = '/public/restore/vms/volumesInformation'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'jobId': job_id,
                'clusterId': cluster_id,
                'clusterIncarnationId': cluster_incarnation_id,
                'jobRunId': job_run_id,
                'startedTimeUsecs': started_time_usecs,
                'sourceId': source_id,
                'originalJobId': original_job_id,
                'attemptNumber': attempt_number,
                'supportedVolumesOnly': supported_volumes_only,
                'computeVolumeInfo': compute_volume_info
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_vm_volumes_information.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_vm_volumes_information.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_vm_volumes_information')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_vm_volumes_information.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                VmVolumesInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_storage_profiles(self, id):
        """Does a GET request to /public/virtualDatacenters/{id}/storageProfiles.

        Fetches information of virtual disk.

        Args:
            id (int|long): Specifies a unique id for the VDC.

        Returns:
            ListStorageProfilesResponseBody: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_storage_profiles called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for list_storage_profiles.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for list_storage_profiles.')
            _url_path = '/public/virtualDatacenters/{id}/storageProfiles'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_storage_profiles.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_storage_profiles.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='list_storage_profiles')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for list_storage_profiles.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ListStorageProfilesResponseBody.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_org_vdc_networks(self, id):
        """Does a GET request to /public/virtualDatacenters/{id}/orgVdcNetworks.

        Returns the Org VDC Network under a VDC in a VMware environment.

        Args:
            id (long|int): Specifies the ID of the virtual datacenter.

        Returns:
            ListOrgVdcNetworksResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_org_vdc_networks called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_user_api_key_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for list_org_vdc_networks.')
            _url_path = '/public/virtualDatacenters/{id}/orgVdcNetworks'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for list_org_vdc_networks.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_org_vdc_networks.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='list_org_vdc_networks')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for list_org_vdc_networks.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ListOrgVdcNetworksResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
