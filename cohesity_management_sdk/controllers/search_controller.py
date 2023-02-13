# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.protection_run_response import ProtectionRunResponse
from cohesity_management_sdk.models.protection_source_response import ProtectionSourceResponse
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class SearchController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(SearchController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def search_protection_runs(self, uuid):
        """Does a GET request to /public/search/protectionRuns.

        Returns the information of latest snapshot of a particular object
        across
        all snapshot target locations.

        Args:
            uuid (string): Specifies the unique id of the Protection Source.

        Returns:
            ProtectionRunResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('search_protection_runs called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for search_protection_runs.')
            self.validate_parameters(uuid=uuid)

            # Prepare query URL
            self.logger.info('Preparing query URL for search_protection_runs.')
            _url_path = '/public/search/protectionRuns'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'uuid': uuid}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for search_protection_runs.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for search_protection_runs.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='search_protection_runs')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for search_protection_runs.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ProtectionRunResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def search_protection_sources(self,
                                  office_365_protection_source_types=None,
                                  department_list=None,
                                  title_list=None,
                                  country_list=None,
                                  search_string=None,
                                  protection_status=None,
                                  environments=None,
                                  last_protection_job_run_status=None,
                                  physical_server_host_types=None,
                                  registered_source_uuids=None,
                                  start_index=None,
                                  page_count=None):
        """Does a GET request to /public/search/protectionSources.

        Returns list of all the objects along with the protection status
        information.

        Args:
            office_365_protection_source_types (
                Office365ProtectionSourceTypesEnum, optional): Specifies the
                Array of Office365 source types. Specifies the type of Office
                365 entity
            department_list (list of string, optional): Specifies the list of
                departments to which an Office365 user may belong.
            title_list (list of string, optional): Specifies the list of
                titles/desgination applicable to Office365 users.
            country_list (list of string, optional): Specifies the list of
                countries to which Office365 user belongs.
            search_string (string, optional): Specifies the search string to
                query the name of the Protection Source or the name of the job
                protecting a Protection Source.
            protection_status (list of string, optional): Specifies the
                protection status of the object. If specified, the objects are
                filtered based on current protection status of that object on
                the cluster. Possible values that can be passed are
                "protected", "unprotected" or both. If not specified, all the
                objects are returned irrespective of protection status of the
                object.
            environments (list of EnvironmentSearchProtectionSourcesEnum,
                optional): Specifies the environment type by which Protection
                Sources will be filtered. Supported environment types such as
                'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer' refers to
                Cohesity's Remote Adapter. 'kVMware' indicates the VMware
                Protection Source environment. 'kHyperV' indicates the HyperV
                Protection Source environment. 'kSQL' indicates the SQL
                Protection Source environment. 'kView' indicates the View
                Protection Source environment. 'kPuppeteer' indicates the
                Cohesity's Remote Adapter. 'kPhysical' indicates the physical
                Protection Source environment. 'kPure' indicates the Pure
                Storage Protection Source environment. 'kNimble' indicates the
                Nimble Storage Protection Source environment. 'kAzure'
                indicates the Microsoft's Azure Protection Source environment.
                'kNetapp' indicates the Netapp Protection Source environment.
                'kAgent' indicates the Agent Protection Source environment.
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
                environment. 'kO365' indicates the Office 365 Protection Source
                environment. 'kO365Outlook' indicates Office 365 outlook
                Protection Source environment. 'kHyperFlex' indicates the Hyper
                Flex Protection Source environment. 'kGCPNative' indicates the
                GCP Native Protection Source environment. 'kAzureNative'
                indicates the Azure Native Protection Source environment.
                'kKubernetes' indicates a Kubernetes Protection Source
                environment. 'kElastifile' indicates Elastifile Protection
                Source environment. 'kAD' indicates Active Directory Protection
                Source environment. 'kRDSSnapshotManager' indicates AWS RDS
                Protection Source environment. 'kCassandra' indicates Cassandra
                Protection Source environment. 'kMongoDB' indicates MongoDB
                Protection Source environment. 'kCouchbase' indicates Couchbase
                Protection Source environment. 'kHdfs' indicates Hdfs
                Protection Source environment. 'kHive' indicates Hive
                Protection Source environment. 'kHBase' indicates HBase
                Protection Source environment. 'kUDA' indicates Universal Data
                Adapter Protection Source environment.
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
            last_protection_job_run_status (list of int, optional): Specifies
                the last Protection Job run status of the object. If
                specified, objects will be filtered based on last job run
                status.
            physical_server_host_types (list of PhysicalServerHostTypeEnum,
                optional): Specifies physical server host OS type. If
                specified, the physical server objects will be filtered
                based on OS type of the server.
                'kLinux' indicates the Linux operating system.
                'kWindows' indicates the Microsoft Windows operating system.
                'kAix' indicates the IBM AIX operating system.
                'kSolaris' indicates the Oracle Solaris operating system.
                'kSapHana' indicates the Sap Hana database system developed by
                SAP SE.
                'kSapOracle' indicates the Sap Oracle database system
                developed by SAP SE.
                'kCockroachDB' indicates the CockroachDB database system.
                'kMySQL' indicates the MySQL database system.
                'kOther' indicates the other types of operating system.

            registered_source_uuids (list of string, optional): Specifies the
                list of Registered Sources Uuids. Only items from the listed
                Registered Sources are returned.
            start_index (int, optional): Specifies an index number that can be
                used to return subsets of items in multiple requests. Break up
                the items to return into multiple requests by setting
                pageCount and using startIndex to return a subsets of items.
                For example, set startIndex to 0 to get the first set of items
                for the first request. Increment startIndex by pageCount to
                get the next set of items for a next request.
            page_count (int, optional): Specifies the number of items to
                return in the response for pagination purposes. Default the
                pageCount to MaxSearchResponseSize if this is unspecified.

        Returns:
            list of ProtectionSourceResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('search_protection_sources called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for search_protection_sources.')
            _url_path = '/public/search/protectionSources'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'office365ProtectionSourceTypes': office_365_protection_source_types,
                'departmentList': department_list,
                'titleList': title_list,
                'countryList': country_list,
                'searchString': search_string,
                'protectionStatus': protection_status,
                'environments': environments,
                'lastProtectionJobRunStatus': last_protection_job_run_status,
                'physicalServerHostTypes': physical_server_host_types,
                'registeredSourceUuids': registered_source_uuids,
                'startIndex': start_index,
                'pageCount': page_count
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for search_protection_sources.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for search_protection_sources.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='search_protection_sources')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for search_protection_sources.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ProtectionSourceResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
