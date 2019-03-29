# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.object_search_results import ObjectSearchResults
from cohesity_management_sdk.models.vm_volume_information import VMVolumeInformation
from cohesity_management_sdk.models.restore_task_1 import RestoreTask1
from cohesity_management_sdk.models.specifies_information_about_the_virtual_disk import SpecifiesInformationAboutTheVirtualDisk
from cohesity_management_sdk.models.file_folder_search_result_1 import FileFolderSearchResult1
from cohesity_management_sdk.models.file_folder_snapshot_information import FileFolderSnapshotInformation
from cohesity_management_sdk.exceptions.error_error_exception import ErrorErrorException

class RestoreTasksController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(RestoreTasksController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def search_objects(self,
                       search=None,
                       job_ids=None,
                       registered_source_ids=None,
                       environments=None,
                       start_time_usecs=None,
                       application=None,
                       owner_entity_id=None,
                       view_box_ids=None,
                       end_time_usecs=None,
                       start_index=None,
                       page_count=None,
                       operating_systems=None):
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
            environments (list of Environments1Enum, optional): Filter by
                environment types such as 'kVMware', 'kView', etc. Only items
                from the specified environment types are returned. NOTE:
                'kPuppeteer' refers to Cohesity's Remote Adapter.
            start_time_usecs (long|int, optional): Filter by backup completion
                time by specifying a backup completion start and end times.
                Specified as a Unix epoch Timestamp (in microseconds). Only
                items created by backups that completed between the specified
                start and end times are returned.
            application (string, optional): Filter by application when the
                environment type is kSQL. For example, if SQL is specified the
                SQL databases are returned.
            owner_entity_id (long|int, optional): Filter objects by the Entity
                id of the owner VM. For example, if a ownerEntityId is
                provided while searching for SQL databases, only SQL databases
                belonging to the VM with the specified id are returned.
                ownerEntityId is only significant if application is set to
                SQL.
            view_box_ids (list of long|int, optional): Filter by a list of
                Domains (View Boxes) ids. Only items stored in the listed
                Domains (View Boxes) are returned.
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
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'search': search,
                'jobIds': job_ids,
                'registeredSourceIds': registered_source_ids,
                'environments': environments,
                'startTimeUsecs': start_time_usecs,
                'application': application,
                'ownerEntityId': owner_entity_id,
                'viewBoxIds': view_box_ids,
                'endTimeUsecs': end_time_usecs,
                'startIndex': start_index,
                'pageCount': page_count,
                'operatingSystems': operating_systems
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for search_objects.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for search_objects.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'search_objects')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for search_objects.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, ObjectSearchResults.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_vm_volumes_information(self,
                                   started_time_usecs=None,
                                   attempt_number=None,
                                   supported_volumes_only=None,
                                   job_id=None,
                                   job_run_id=None,
                                   source_id=None,
                                   original_job_id=None,
                                   cluster_id=None,
                                   cluster_incarnation_id=None):
        """Does a GET request to /public/restore/vms/volumesInformation.

        All fields must be specified for this operation.
        To get values for these fields, invoke the GET
        /public/restore/objects
        operation.
        A specific Job Run is defined by the jobRunId, startedTimeUsecs, and
        attemptNumber fields.

        Args:
            started_time_usecs (long|int, optional): Specifies the time when
                the Job Run starts capturing a snapshot. Specified as a Unix
                epoch Timestamp (in microseconds).
            attempt_number (long|int, optional): Specifies the number of the
                attempts made by the Job Run to capture a snapshot of the
                object. For example, if an snapshot is successfully captured
                after three attempts, this field equals 3.
            supported_volumes_only (bool, optional): Specifies to return only
                supported volumes information. Unsupported volumes are not
                returned if this flag is set to true. Default is false.
            job_id (long|int, optional): Specifies the Job id for the
                Protection Job that is currently associated with the object.
                If the object was backed up on current Cohesity Cluster, this
                field contains the id for the Job that captured this backup
                object. If the object was backed up on a Primary Cluster and
                replicated to this Cohesity Cluster, a new Inactive Job is
                created, the object is now associated with new Inactive Job,
                and this field contains the id of the new Inactive Job.
            job_run_id (long|int, optional): Specifies the id of the Job Run
                that captured the snapshot.
            source_id (long|int, optional): Specifies the id of the VM object
                to search for volumes.
            original_job_id (long|int, optional): Specifies the id for the
                Protection Job that originally captured the snapshots of the
                original object. If the object was backed up on a Primary
                Cluster replicated to this Cohesity Cluster, and a new
                Inactive Job is created, this field still contains the id of
                the original Job and NOT the id of the new Inactive Job. This
                field is used in combination with the clusterId and
                clusterIncarnationId to uniquely identify a Job.
            cluster_id (long|int, optional): Specifies the Cohesity Cluster id
                where the Job was created.
            cluster_incarnation_id (long|int, optional): Specifies the
                incarnation id of the Cohesity Cluster where the Job was
                created. An incarnation id is generated when a Cohesity
                Cluster is initially created.

        Returns:
            list of VMVolumeInformation: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_vm_volumes_information called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_vm_volumes_information.')
            _url_path = '/public/restore/vms/volumesInformation'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'startedTimeUsecs': started_time_usecs,
                'attemptNumber': attempt_number,
                'supportedVolumesOnly': supported_volumes_only,
                'jobId': job_id,
                'jobRunId': job_run_id,
                'sourceId': source_id,
                'originalJobId': original_job_id,
                'clusterId': cluster_id,
                'clusterIncarnationId': cluster_incarnation_id
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_vm_volumes_information.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_vm_volumes_information.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_vm_volumes_information')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_vm_volumes_information.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, VMVolumeInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update_cancel_restore_task(self,
                                   id):
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
            self.logger.info('Validating required parameters for update_cancel_restore_task.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_cancel_restore_task.')
            _url_path = '/public/restore/tasks/cancel/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'id': id
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_cancel_restore_task.')
            _request = self.http_client.put(_query_url)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_cancel_restore_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_cancel_restore_task.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_restore_task_by_id(self,
                               id):
        """Does a GET request to /public/restore/tasks/{id}.

        Returns the Restore Task corresponding to the specified Restore Task
        id.

        Args:
            id (long|int): Specifies a unique id for the Restore Task.

        Returns:
            RestoreTask1: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_restore_task_by_id called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for get_restore_task_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_restore_task_by_id.')
            _url_path = '/public/restore/tasks/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'id': id
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_restore_task_by_id.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_restore_task_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_restore_task_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_restore_task_by_id.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, RestoreTask1.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_virtual_disk_information(self,
                                     source_id,
                                     cluster_id,
                                     cluster_incarnation_id,
                                     job_id,
                                     job_run_id,
                                     start_time_usecs):
        """Does a GET request to /public/restore/virtualDiskInformation.

        Fetches information of virtual disk.

        Args:
            source_id (long|int): Specifies the Id of the Protection Source
                object.
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

        Returns:
            list of SpecifiesInformationAboutTheVirtualDisk: Response from the
                API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_virtual_disk_information called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for get_virtual_disk_information.')
            self.validate_parameters(source_id=source_id,
                                     cluster_id=cluster_id,
                                     cluster_incarnation_id=cluster_incarnation_id,
                                     job_id=job_id,
                                     job_run_id=job_run_id,
                                     start_time_usecs=start_time_usecs)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_virtual_disk_information.')
            _url_path = '/public/restore/virtualDiskInformation'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'sourceId': source_id,
                'clusterId': cluster_id,
                'clusterIncarnationId': cluster_incarnation_id,
                'jobId': job_id,
                'jobRunId': job_run_id,
                'startTimeUsecs': start_time_usecs
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_virtual_disk_information.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_virtual_disk_information.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_virtual_disk_information')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_virtual_disk_information.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, SpecifiesInformationAboutTheVirtualDisk.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_restore_tasks(self,
                          task_ids=None,
                          start_time_usecs=None,
                          end_time_usecs=None,
                          page_count=None,
                          task_types=None,
                          environment=None):
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
            environment (Environment2Enum, optional): Specifies the
                environment like VMware, SQL, where the Protection Source
                exists. Supported environment types such as 'kView', 'kSQL',
                'kVMware', etc. NOTE: 'kPuppeteer' refers to Cohesity's Remote
                Adapter. 'kVMware' indicates the VMware Protection Source
                environment. 'kHyperV' indicates the HyperV Protection Source
                environment. 'kSQL' indicates the SQL Protection Source
                environment. 'kView' indicates the View Protection Source
                environment. 'kPuppeteer' indicates the Cohesity's Remote
                Adapter. 'kPhysical' indicates the physical Protection Source
                environment. 'kPure' indicates the Pure Storage Protection
                Source environment. 'kAzure' indicates the Microsoft's Azure
                Protection Source environment. 'kNetapp' indicates the Netapp
                Protection Source environment. 'kAgent' indicates the Agent
                Protection Source environment. 'kGenericNas' indicates the
                Genreric Network Attached Storage Protection Source
                environment. 'kAcropolis' indicates the Acropolis Protection
                Source environment. 'kPhsicalFiles' indicates the Physical
                Files Protection Source environment. 'kIsilon' indicates the
                Dell EMC's Isilon Protection Source environment. 'kKVM'
                indicates the KVM Protection Source environment. 'kAWS'
                indicates the AWS Protection Source environment. 'kExchange'
                indicates the Exchange Protection Source environment.
                'kHyperVVSS' indicates the HyperV VSS Protection Source
                environment. 'kOracle' indicates the Oracle Protection Source
                environment. 'kGCP' indicates the Google Cloud Platform
                Protection Source environment. 'kFlashBlade' indicates the
                Flash Blade Protection Source environment. 'kAWSNative'
                indicates the AWS Native Protection Source environment. 'kVCD'
                indicates the VMware's Virtual cloud Director Protection
                Source environment. 'kO365' indicates the Office 365
                Protection Source environment. 'kO365Outlook' indicates Office
                365 outlook Protection Source environment. 'kHyperFlex'
                indicates the Hyper Flex Protection Source environment.
                'kGCPNative' indicates the GCP Native Protection Source
                environment. 'kAzureNative' indicates the Azure Native
                Protection Source environment.

        Returns:
            list of RestoreTask1: Response from the API. Success

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
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'taskIds': task_ids,
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs,
                'pageCount': page_count,
                'taskTypes': task_types,
                'environment': environment
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_restore_tasks.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_restore_tasks.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_restore_tasks')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_restore_tasks.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, RestoreTask1.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_outlook_emails(self,
                           received_time_seconds=None,
                           show_only_email_folders=None,
                           received_end_time=None,
                           folder_name=None,
                           domain_ids=None,
                           mailbox_ids=None,
                           protection_job_ids=None,
                           sender_address=None,
                           sent_time_seconds=None,
                           email_subject=None,
                           recipient_addresses=None,
                           received_start_time=None,
                           bcc_recipient_addresses=None,
                           has_attachments=None,
                           cc_recipient_addresses=None):
        """Does a GET request to /public/restore/office365/outlook/emails.

        Search for Emails and Emails' folders to recover that match the
        specified
        search and filter criterias on the Cohesity cluster.

        Args:
            received_time_seconds (long|int, optional): Specifies the unix
                time when the email was received.
            show_only_email_folders (bool, optional): Specifies whether the
                query result should include only Email folders.
            received_end_time (long|int, optional): Specifies the unix end
                time for querying on email's received time.
            folder_name (string, optional): Specifies the parent folder name
                of the email.
            domain_ids (list of long|int, optional): Specifies the domain Ids
                in which mailboxes are registered.
            mailbox_ids (list of long|int, optional): Specifies the mailbox
                Ids which contains the emails/folders.
            protection_job_ids (list of long|int, optional): Specifies the
                protection job Ids which have backed up mailbox(es) continaing
                emails/folders.
            sender_address (string, optional): Specifies the email address of
                the sender.
            sent_time_seconds (long|int, optional): Specifies the unix time
                when the email was sent.
            email_subject (string, optional): Specifies the subject of the
                email.
            recipient_addresses (list of string, optional): Specifies the
                email addresses of the recipients.
            received_start_time (long|int, optional): Specifies the unix start
                time for querying on email's received time.
            bcc_recipient_addresses (list of string, optional): Specifies the
                email addresses of the bcc recipients.
            has_attachments (bool, optional): Specifies whether the emails
                have any attachments.
            cc_recipient_addresses (list of string, optional): Specifies the
                email addresses of the cc recipients.

        Returns:
            FileFolderSearchResult1: Response from the API. Success

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
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'receivedTimeSeconds': received_time_seconds,
                'showOnlyEmailFolders': show_only_email_folders,
                'receivedEndTime': received_end_time,
                'folderName': folder_name,
                'domainIds': domain_ids,
                'mailboxIds': mailbox_ids,
                'protectionJobIds': protection_job_ids,
                'senderAddress': sender_address,
                'sentTimeSeconds': sent_time_seconds,
                'emailSubject': email_subject,
                'recipientAddresses': recipient_addresses,
                'receivedStartTime': received_start_time,
                'bccRecipientAddresses': bcc_recipient_addresses,
                'hasAttachments': has_attachments,
                'ccRecipientAddresses': cc_recipient_addresses
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_outlook_emails.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_outlook_emails.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_outlook_emails')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_outlook_emails.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, FileFolderSearchResult1.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_file_snapshots_information(self,
                                       cluster_id,
                                       cluster_incarnation_id,
                                       source_id,
                                       filename,
                                       job_id):
        """Does a GET request to /public/restore/files/snapshotsInformation.

        Get the information about snapshots that contain the specified file or
        folder. In addition, information about the file or folder is
        provided.

        Args:
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
            job_id (long|int): Specifies the id of the Job that captured the
                snapshots. These snapshots are searched for the specified
                files or folders. This field is required.

        Returns:
            list of FileFolderSnapshotInformation: Response from the API.
                Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_file_snapshots_information called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for get_file_snapshots_information.')
            self.validate_parameters(cluster_id=cluster_id,
                                     cluster_incarnation_id=cluster_incarnation_id,
                                     source_id=source_id,
                                     filename=filename,
                                     job_id=job_id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_file_snapshots_information.')
            _url_path = '/public/restore/files/snapshotsInformation'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'clusterId': cluster_id,
                'clusterIncarnationId': cluster_incarnation_id,
                'sourceId': source_id,
                'filename': filename,
                'jobId': job_id
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_file_snapshots_information.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_file_snapshots_information.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_file_snapshots_information')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_file_snapshots_information.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, FileFolderSnapshotInformation.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_recover_task(self,
                            body):
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
            body (CreateRestoreTaskRequest): Request to create a Restore Task
                for recovering VMs or mounting volumes to mount points.

        Returns:
            RestoreTask1: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_recover_task called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_recover_task.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_recover_task.')
            _url_path = '/public/restore/recover'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_recover_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_recover_task.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_recover_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_recover_task.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, RestoreTask1.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def search_restored_files(self,
                              job_ids=None,
                              end_time_usecs=None,
                              start_index=None,
                              source_ids=None,
                              start_time_usecs=None,
                              page_count=None,
                              folder_only=None,
                              search=None,
                              registered_source_ids=None,
                              view_box_ids=None,
                              environments=None):
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
            job_ids (list of long|int, optional): Filter by a list of
                Protection Job ids. Only items backed up by the specified Jobs
                are listed.
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
            source_ids (list of long|int, optional): Filter by source ids.
                Only files and folders found in the listed sources (such as
                VMs) are returned.
            start_time_usecs (long|int, optional): Filter by backup completion
                time by specifying a backup completion start and end times.
                Specified as a Unix epoch Timestamp (in microseconds). Only
                items created by backups that completed between the specified
                start and end times are returned.
            page_count (long|int, optional): Limit the number of items to
                return in the response for pagination purposes.
            folder_only (bool, optional): Filter by folders or files. If true,
                only folders are returned. If false, only files are returned.
                If not specified, both files and folders are returned.
            search (string, optional): Filter by searching for sub-strings in
                the item name. The specified string can match any part of the
                item name. For example: "vm" or "123" both match the item name
                of "vm-123".
            registered_source_ids (list of long|int, optional): Filter by a
                list of Registered Sources ids. Only items from the listed
                Registered Sources are returned.
            view_box_ids (list of long|int, optional): Filter by a list of
                Domains (View Boxes) ids. Only items stored in the listed
                Domains (View Boxes) are returned.
            environments (list of Environments1Enum, optional): Filter by
                environment types such as 'kVMware', 'kView', etc. Only items
                from the specified environment types are returned. NOTE:
                'kPuppeteer' refers to Cohesity's Remote Adapter.

        Returns:
            FileFolderSearchResult1: Response from the API. Success

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
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'jobIds': job_ids,
                'endTimeUsecs': end_time_usecs,
                'startIndex': start_index,
                'sourceIds': source_ids,
                'startTimeUsecs': start_time_usecs,
                'pageCount': page_count,
                'folderOnly': folder_only,
                'search': search,
                'registeredSourceIds': registered_source_ids,
                'viewBoxIds': view_box_ids,
                'environments': environments
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for search_restored_files.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for search_restored_files.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'search_restored_files')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for search_restored_files.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, FileFolderSearchResult1.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_deploy_task(self,
                           body):
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
            RestoreTask1: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_deploy_task called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_deploy_task.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_deploy_task.')
            _url_path = '/public/restore/deploy'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_deploy_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_deploy_task.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_deploy_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_deploy_task.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, RestoreTask1.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_download_files_and_folders(self,
                                          body):
        """Does a POST request to /public/restore/downloadFilesAndFolders.

        Returns the created download Task information that downloads files and
        folders.

        Args:
            body (DownloadFilesAndFoldersParameters): Request to create a task
                for downloading list of files or folders.

        Returns:
            RestoreTask1: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_download_files_and_folders called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_download_files_and_folders.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_download_files_and_folders.')
            _url_path = '/public/restore/downloadFilesAndFolders'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_download_files_and_folders.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_download_files_and_folders.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_download_files_and_folders')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_download_files_and_folders.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, RestoreTask1.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_restore_files_task(self,
                                  body):
        """Does a POST request to /public/restore/files.

        Returns the created Restore Task that recovers files and folders.

        Args:
            body (RestoreTask): Request to create a Restore Task for
                recovering files or folders.

        Returns:
            RestoreTask1: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_restore_files_task called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_restore_files_task.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_restore_files_task.')
            _url_path = '/public/restore/files'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_restore_files_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_restore_files_task.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_restore_files_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_restore_files_task.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, RestoreTask1.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update_restore_task(self,
                            body):
        """Does a PUT request to /public/restore/recover.

        Updates an existing restore task with additional params which are
        needed for
        features like Hot-Standby.

        Args:
            body (UpdateRestoreTaskParams): TODO: type description here.
                Example:

        Returns:
            RestoreTask1: Response from the API. Specifies the response of the
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
            self.logger.info('Validating required parameters for update_restore_task.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_restore_task.')
            _url_path = '/public/restore/recover'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_restore_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_restore_task.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_restore_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_restore_task.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, RestoreTask1.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_applications_clone_task(self,
                                       body):
        """Does a POST request to /public/restore/applicationsClone.

        Returns the created Restore Task.

        Args:
            body (CreateApplicationsRestoreTaskRequest): Request to create a
                Restore Task for cloning Applications like SQL DB.

        Returns:
            RestoreTask1: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_applications_clone_task called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_applications_clone_task.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_applications_clone_task.')
            _url_path = '/public/restore/applicationsClone'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_applications_clone_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_applications_clone_task.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_applications_clone_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_applications_clone_task.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, RestoreTask1.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_applications_recover_task(self,
                                         body):
        """Does a POST request to /public/restore/applicationsRecover.

        Returns the created Restore Task.

        Args:
            body (CreateApplicationsRestoreTaskRequest): Request to create a
                Restore Task for recovering Applications like SQL DB. volumes
                to mount points.

        Returns:
            RestoreTask1: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_applications_recover_task called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_applications_recover_task.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_applications_recover_task.')
            _url_path = '/public/restore/applicationsRecover'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_applications_recover_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_applications_recover_task.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_applications_recover_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_applications_recover_task.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, RestoreTask1.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_clone_task(self,
                          body):
        """Does a POST request to /public/restore/clone.

        Returns the created Restore Task that clones VMs or a View.

        Args:
            body (CloneRestoreTaskRequest): Request to create a Restore Task
                for cloning VMs or a View.

        Returns:
            RestoreTask1: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_clone_task called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for create_clone_task.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_clone_task.')
            _url_path = '/public/restore/clone'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_clone_task.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_clone_task.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_clone_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_clone_task.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, RestoreTask1.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def destroy_clone_task(self,
                           id):
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
            self.logger.info('destroy_clone_task called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for destroy_clone_task.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for destroy_clone_task.')
            _url_path = '/public/restore/clone/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'id': id
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info('Preparing and executing request for destroy_clone_task.')
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'destroy_clone_task')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for destroy_clone_task.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
