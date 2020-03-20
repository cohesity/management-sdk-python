# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.restore_source_summary_by_object_type_element import RestoreSourceSummaryByObjectTypeElement
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class ReportsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(ReportsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_restore_summary_by_object_type_report(self,
                                                  start_time_usecs=None,
                                                  end_time_usecs=None,
                                                  mtype=None,
                                                  user_name=None,
                                                  recovered_from=None,
                                                  recover_task_name=None,
                                                  status=None,
                                                  output_format=None):
        """Does a GET request to /public/reports/restoreSummaryByObjectType.

        TODO: type endpoint description here.

        Args:
            start_time_usecs (long|int, optional): Filter by a start time
                specified as a Unix epoch Timestamp (in microseconds).
            end_time_usecs (long|int, optional): Filter by an end time
                specified as a Unix epoch Timestamp (in microseconds).
            mtype (TypeGetRestoreSummaryByObjectTypeReportEnum, optional):
                Specify the object type to filter with. Specifies the type of
                Restore Task.  'kRecoverVMs' specifies a Restore Task that
                recovers VMs. 'kCloneVMs' specifies a Restore Task that clones
                VMs. 'kCloneView' specifies a Restore Task that clones a View.
                'kMountVolumes' specifies a Restore Task that mounts volumes.
                'kRestoreFiles' specifies a Restore Task that recovers files
                and folders. 'kRecoverApp' specifies a Restore Task that
                recovers app. 'kCloneApp' specifies a Restore Task that clone
                app. 'kRecoverSanVolume' specifies a Restore Task that
                recovers SAN volumes. 'kConvertAndDeployVMs' specifies a
                Restore Task that converts and deploy VMs to a target
                environment. 'kMountFileVolume' specifies a Restore Task that
                mounts a file volume. 'kSystem' specifies a Restore Task that
                recovers a system. 'kRecoverVolumes' specifies a Restore Task
                that recovers volumes via the physical agent. 'kDeployVolumes'
                specifies a Restore Task that deployes volumes to a target
                environment. 'kDownloadFiles' specifies a Restore Task that
                downloads the requested files and folders in zip format.
                'kRecoverEmails' specifies a Restore Task that recovers the
                mailbox/email items. 'kRecoverDisks' specifies a Restore Task
                that recovers the virtual disks.
            user_name (string, optional): Specify the user name to filter
                with.
            recovered_from (list of string, optional): Specifies the targets
                from which the recovery happend.
            recover_task_name (string, optional): Specifies the recover task
                name.
            status (StatusGetRestoreSummaryByObjectTypeReportEnum, optional):
                Specifies the overall status of the Restore Task to filter.
                'kReadyToSchedule' indicates the Restore Task is waiting to be
                scheduled. 'kProgressMonitorCreated' indicates the progress
                monitor for the Restore Task has been created.
                'kRetrievedFromArchive' indicates that the objects to restore
                have been retrieved from the specified archive. A Task will
                only ever transition to this state if a retrieval is
                necessary. 'kAdmitted' indicates the task has been admitted.
                After a task has been admitted, its status does not move back
                to 'kReadyToSchedule' state even if it is rescheduled.
                'kInProgress' indicates that the Restore Task is in progress.
                'kFinishingProgressMonitor' indicates that the Restore Task is
                finishing its progress monitoring. 'kFinished' indicates that
                the Restore Task has finished. The status indicating success
                or failure is found in the error code that is stored with the
                Restore Task. 'kInternalViewCreated' indicates that internal
                view for the task has been created. 'kZipFileRequested'
                indicates that request has been sent to create zip files for
                the files to be downloaded. This state is only going to be
                present for kDownloadFiles Task. 'kCancelled' indicates that
                task or jb has been cancelled.
            output_format (string, optional): Specifies the format for the
                output such as 'csv' or 'json'. If not specified, the json
                format is returned. If 'csv' is specified, a comma-separated
                list with a heading row is returned.

        Returns:
            list of RestoreSourceSummaryByObjectTypeElement: Response from the
                API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info(
                'get_restore_summary_by_object_type_report called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_restore_summary_by_object_type_report.'
            )
            _url_path = '/public/reports/restoreSummaryByObjectType'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'startTimeUsecs': start_time_usecs,
                'endTimeUsecs': end_time_usecs,
                'type': mtype,
                'userName': user_name,
                'recoveredFrom': recovered_from,
                'recoverTaskName': recover_task_name,
                'status': status,
                'outputFormat': output_format
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_restore_summary_by_object_type_report.'
            )
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_restore_summary_by_object_type_report.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_restore_summary_by_object_type_report')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_restore_summary_by_object_type_report.'
            )
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                RestoreSourceSummaryByObjectTypeElement.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
