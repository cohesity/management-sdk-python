# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.upgrade_physical_agents_message import UpgradePhysicalAgentsMessage
from cohesity_management_sdk.models.protection_source_node import ProtectionSourceNode
from cohesity_management_sdk.models.registered_application_server import RegisteredApplicationServer
from cohesity_management_sdk.models.protection_source import ProtectionSource
from cohesity_management_sdk.models.protected_vm_info import ProtectedVmInfo
from cohesity_management_sdk.models.run_diagnostics_message import RunDiagnosticsMessage
from cohesity_management_sdk.models.get_registration_info_response import GetRegistrationInfoResponse
from cohesity_management_sdk.models.sql_aag_host_and_databases import SqlAagHostAndDatabases
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException
from cohesity_management_sdk.models.exchange_dag_hosts_response import ExchangeDagHostsResponse
from cohesity_management_sdk.models.download_cft_response import DownloadCftResponse


class ProtectionSourcesController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(ProtectionSourcesController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_download_physical_agent(self,
                                    host_type,
                                    host_os_type=None,
                                    pkg_type=None,
                                    agent_type=None):
        """Does a GET request to /public/physicalAgents/download.

        Host type could be Linux, Windows, AIX.

        Args:
            host_type (HostTypeDownloadPhysicalAgentEnum): Specifies the host
                type for which user wants to download the physical agent.
                'kLinux' indicates the Linux operating system. 'kWindows'
                indicates the Microsoft Windows operating system. 'kAix'
                indicates the IBM AIX operating system. 'kSolaris' indicates
                the Oracle Solaris operating system. 'kSapHana' indicates the
                Sap Hana database system developed by SAP SE. 'kOther'
                indicates the other types of operating system.
            host_os_type(HostOSTypeEnum, optional): Specifies the OS type for
                which user wants to download the physical agent/plugin.
            pkg_type (PkgTypeEnum, optional): Specifies the Linux installer
                package type applicable only to Linux OS and the value can be
                any of ("kScript","kRPM", "kSuseRPM", "kDEB") 'kScript'
                indicates a script based agent installer. 'kRPM' indicates a
                RPM agent installer. 'kSuseRPM' indicates a Open Suse RPM
                installer. 'kDEB' indicates a Debian agent installer.
            agent_type (AgentTypeEnum, optional): Specifies agent type. Can be
                "kGo" for go agent and "kJava" for java agent and "kCpp" for
                c++ agent. 'kCpp' indicates a c++ agent. 'kJava' indicates a
                java agent. 'kGo' indicates a go agent.

        Returns:
            list of int: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_download_physical_agent called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_download_physical_agent.'
            )
            self.validate_parameters(host_type=host_type)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_download_physical_agent.')
            _url_path = '/public/physicalAgents/download'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'hostType': host_type,
                'hostOSType': host_os_type,
                'pkgType': pkg_type,
                'agentType': agent_type
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_download_physical_agent.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_download_physical_agent.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_download_physical_agent')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_download_physical_agent.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_upgrade_physical_agents(self, body=None):
        """Does a POST request to /public/physicalAgents/upgrade.

        If the request is successful, the Cohesity agents on the specified
        Physical Servers are upgraded to the agent release
        currently available from this Cohesity Cluster.
        For example if the Cluster is upgraded from 3.7.1 to 4.0,
        the agents on the specified Physical Servers can be upgraded to 4.0
        using
        this POST operation.
        To get the agentIds to pass into this operation, call
        GET /public/protectionSources with the environment set to
        'KPhysical'.
        In addition this GET operation returns the agentUpgradability field,
        that
        indicates if an agent can be upgraded. Use the agentUpgradability
        field
        to determine which Physical Servers to upgrade using this
        POST /public/physicalAgents/upgrade operation.
        WARNING: Only agents at a particular Cohesity release can be
        upgraded using this operation.
        See the Cohesity online help for details.
        Returns the status of the upgrade initiation.

        Args:
            body (UpgradePhysicalServerAgents, optional): Request to upgrade
                agents on Physical Servers.

        Returns:
            UpgradePhysicalAgentsMessage: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_upgrade_physical_agents called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_upgrade_physical_agents.')
            _url_path = '/public/physicalAgents/upgrade'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_upgrade_physical_agents.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_upgrade_physical_agents.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_upgrade_physical_agents')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_upgrade_physical_agents.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                UpgradePhysicalAgentsMessage.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_protection_sources(self,
                                exclude_office_365_types=None,
                                get_teams_channels=None,
                                after_cursor_entity_id=None,
                                before_cursor_entity_id=None,
                                node_id=None,
                                page_size=None,
                                has_valid_mailbox=None,
                                has_valid_onedrive=None,
                                id=None,
                                num_levels=None,
                                exclude_types=None,
                                exclude_aws_types=None,
                                exclude_kubernetes_types=None,
                                include_datastores=None,
                                include_networks=None,
                                include_vm_folders=None,
                                include_system_v_apps=None,
                                environments=None,
                                environment=None,
                                include_entity_permission_info=None,
                                sids=None,
                                include_source_credentials=None,
                                encryption_key=None,
                                include_object_protection_info=None,
                                prune_non_critical_info=None,
                                request_initiator_type=None,
                                use_cached_data=None,
                                tenant_ids=None,
                                all_under_hierarchy=None):
        """Does a GET request to /public/protectionSources.

        If no parameters are specified, all Protection Sources that are
        registered
        on the Cohesity Cluster are returned.
        In addition, an Object subtree gathered from each Source is returned.
        For example, the Cohesity Cluster interrogates a Source VMware vCenter
        Server
        and creates an hierarchical Object subtree that mirrors the
        Inventory tree on vCenter Server.
        The contents of the Object tree are returned as a "nodes" hierarchy
        of "protectionSource"s.
        Specifying parameters can alter the results that are returned.


        Args:
            exclude_office_365_types (list of ExcludeOffice365TypesEnum, optional):
                Specifies the Object types to be filtered out for Office 365
                that match the passed in types such as 'kDomain', 'kOutlook',
                'kMailbox', etc.
                For example, set this parameter to 'kMailbox' to exclude
                Mailbox Objects from being returned.
            get_teams_channels (bool): Specifies whether to get the list of the
                channels for a given M365 Teams object. This should be set to true
                only when a single Id belonging to M365 Teams object is provided
                in the query params.
            after_cursor_entity_id (long|int, optional): Specifies the entity
                id starting from which the items are to be returned.
            before_cursor_entity_id (long|int, optional): Specifies the entity
                id upto which the items are to be returned.
            node_id (long|int, optional): Specifies the entity id for the Node
                at any level within the Source entity hierarchy whose children
                are to be paginated.
            page_size (long|int, optional): Specifies the maximum number of
                entities to be returned within the page.
            has_valid_mailbox (bool, optional): If set to true, users with
                valid mailbox will be returned.
            has_valid_onedrive (bool, optional): If set to true, users with
                valid onedrive will be returned.
            id (long|int, optional): Return the Object subtree for the passed
                in Protection Source id.
            num_levels (int, optional): Specifies the expected number of levels
                from the root node to be returned in the entity hierarchy
                response.
            exclude_types (list of ExcludeTypeEnum, optional): Filter out the
                Object types (and their subtrees) that match the passed in
                types such as 'kVCenter', 'kFolder', 'kDatacenter',
                'kComputeResource', 'kResourcePool', 'kDatastore',
                'kHostSystem', 'kVirtualMachine', etc. For example, set this
                parameter to 'kResourcePool' to exclude Resource Pool Objects
                from being returned.
            exclude_aws_types (list of ExcludeAwsTypesEnum, optional): Specifies
                the Object types to be filtered out for AWS that match the passed
                in types such as 'kEC2Instance', 'kRDSInstance' & 'kAuroraCluster'.
                For example, set this parameter to 'kEC2Instance' to exclude ec2
                instance from being returned.
            exclude_kubernetes_types (list of ExcludeKubernetesTypesEnum, optional):
                Specifies the Object types to be filtered out for Kubernetes
                that match the passed in types such as 'kService'.
                For example, set this parameter to 'kService' to exclude services
                from being returned.
            include_datastores (bool, optional): Set this parameter to true to
                also return kDatastore object types found in the Source in
                addition to their Object subtrees. By default, datastores are
                not returned.
            include_networks (bool, optional): Set this parameter to true to
                also return kNetwork object types found in the Source in
                addition to their Object subtrees. By default, network objects
                are not returned.
            include_vm_folders (bool, optional): Set this parameter to true to
                also return kVMFolder object types found in the Source in
                addition to their Object subtrees. By default, VM folder
                objects are not returned.
            include_system_v_apps (bool, optional): Set this parameter to true
                to also return system VApp object types found in the Source in
                addition to their Object subtrees. By default, VM folder
                objects are not returned.
            environments (list of EnvironmentListProtectionSourcesEnum,
                optional): Return only Protection Sources that match the
                passed in environment type such as 'kVMware', 'kSQL', 'kView'
                'kPhysical', 'kPuppeteer', 'kPure', 'kNetapp', 'kGenericNas',
                'kHyperV', 'kAcropolis', or 'kAzure'. For example, set this
                parameter to 'kVMware' to only return the Sources (and their
                Object subtrees) found in the 'kVMware' (VMware vCenter
                Server) environment.  NOTE: 'kPuppeteer' refers to Cohesity's
                Remote Adapter.
            environment (string, optional): This field is deprecated. Use
                environments instead. deprecated: true
            include_entity_permission_info (bool, optional): If specified,
                then a list of entites with permissions assigned to them are
                returned.
            sids (list of string, optional): Filter the object subtree for the
                sids given in the list.
            include_source_credentials (bool, optional): If specified, then
                crednetial for the registered sources will be included.
                Credential is first encrypted with internal key and then
                reencrypted with user supplied 'encryption_key'.
            encryption_key (string, optional): Key to be used to encrypt the
                source credential. If include_source_credentials is set to true
                this key must be specified.
            include_object_protection_info (bool): If specified, the object
                protection of entities(if any) will be returned.
            prune_non_critical_info (bool): Specifies whether to prune non
                critical info within entities. Incase of VMs, virtual disk
                information will be pruned. Incase of Office365, metadata about
                user entities will be pruned. This can be used to limit the size
                of the response by caller.
            request_initiator_type (string): Specifies the type of the request.
                Possible values are UIUser and UIAuto, which means the request
                is triggered by user or is an auto refresh request. Services
                like magneto will use this to determine the priority of the
                requests, so that it can more intelligently handle overload
                situations by prioritizing higher priority requests.
            use_cached_data (bool): Specifies whether we can serve the GET
                request to the read replica cache. setting this to true ensures
                that the API request is served to the read replica. setting this
                to false will serve the request to the master.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            list of ProtectionSourceNode: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_protection_sources called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for list_protection_sources.')
            _url_path = '/public/protectionSources'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'getTeamsChannels': get_teams_channels,
                'excludeOffice365Types': exclude_office_365_types,
                'afterCursorEntityId': after_cursor_entity_id,
                'beforeCursorEntityId': before_cursor_entity_id,
                'nodeId': node_id,
                'pageSize': page_size,
                'hasValidMailbox': has_valid_mailbox,
                'hasValidOnedrive': has_valid_onedrive,
                'id': id,
                'numLevels': num_levels,
                'excludeTypes': exclude_types,
                'excludeAwsTypes': exclude_aws_types,
                'excludeKubernetesTypes': exclude_kubernetes_types,
                'includeDatastores': include_datastores,
                'includeNetworks': include_networks,
                'includeVMFolders': include_vm_folders,
                'includeSystemVApps': include_system_v_apps,
                'environments': environments,
                'environment': environment,
                'includeEntityPermissionInfo': include_entity_permission_info,
                'sids': sids,
                'includeSourceCredentials': include_source_credentials,
                'encryptionKey': encryption_key,
                'includeObjectProtectionInfo': include_object_protection_info,
                'pruneNonCriticalInfo': prune_non_critical_info,
                'requestInitiatorType': request_initiator_type,
                'useCachedData': use_cached_data,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_protection_sources.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_protection_sources.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='list_protection_sources')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for list_protection_sources.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ProtectionSourceNode.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_application_servers(self,
                                 protection_sources_root_node_id=None,
                                 environment=None,
                                 protection_source_id=None,
                                 application=None):
        """Does a GET request to /public/protectionSources/applicationServers.

        Given the root node id of a Protection Source tree, returns the list
        of
        Application Servers registered under that tree based on the filters.

        Args:
            protection_sources_root_node_id (long|int, optional): Specifies
                the Protection Source Id of the root node of a Protection
                Sources tree. A root node represents a registered Source on
                the Cohesity Cluster, such as a vCenter Server.
            environment (EnvironmentListApplicationServersEnum, optional):
                Specifies the environment such as 'kPhysical' or 'kVMware' of
                the Protection Source tree. overrideDescription: true
                Supported environment types such as 'kView', 'kSQL',
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
                environment. 'kO365' indicates the Office 365 Protection Source
                environment. 'kO365Outlook' indicates Office 365 outlook
                Protection Source environment. 'kHyperFlex' indicates the Hyper
                Flex Protection Source environment. 'kGCPNative' indicates the
                GCP Native Protection Source environment. 'kAzureNative'
                indicates the Azure Native Protection Source environment.
                'kKubernetes' indicates a Kubernetes Protection Source
                environment. 'kElastifile' indicates Elastifile Protection
                Source environment. 'kAD' indicates Active Directory
                Protection Source environment. 'kRDSSnapshotManager'
                indicates AWS RDS Protection Source environment. 'kCassandra'
                indicates Cassandra Protection Source environment. 'kMongoDB'
                indicates MongoDB Protection Source environment. 'kCouchbase'
                indicates Couchbase Protection Source environment. 'kHdfs'
                indicates Hdfs Protection Source environment. 'kHive'
                indicates Hive Protection Source environment. 'kHBase'
                indicates HBase Protection Source environment. 'kUDA'
                indicates Universal Data Adapter Protection Source environment.
            protection_source_id (long|int, optional): Specifies the
                Protection Source Id of the 'kPhysical' or 'kVMware' entity in
                the Protection Source tree hosting the applications.
            application (ApplicationEnum, optional): Specifies the application
                such as 'kSQL', 'kExchange' running on the Protection Source.
                overrideDescription: true Supported environment types such as
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
                environment.'kUDA' indicates Universal Data Adapter Protection
                Source environment.

        Returns:
            list of RegisteredApplicationServer: Response from the API.
                Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_application_servers called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for list_application_servers.')
            _url_path = '/public/protectionSources/applicationServers'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'protectionSourcesRootNodeId': protection_sources_root_node_id,
                'environment': environment,
                'protectionSourceId': protection_source_id,
                'application': application
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_application_servers.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_application_servers.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='list_application_servers')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for list_application_servers.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                RegisteredApplicationServer.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_register_application_servers(self, body):
        """Does a POST request to /public/protectionSources/applicationServers.

        Registering Application Servers will help Cohesity Cluster such that
        any
        application specific data can be backed up.
        Returns the Protection Source registered upon success.

        Args:
            body (RegisterApplicationServersParameters): Request to register
                Application Servers in a Protection Source.

        Returns:
            ProtectionSource: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_register_application_servers called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_register_application_servers.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_register_application_servers.')
            _url_path = '/public/protectionSources/applicationServers'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_register_application_servers.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_register_application_servers.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_register_application_servers')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_register_application_servers.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionSource.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_application_servers(self, body):
        """Does a PUT request to /public/protectionSources/applicationServers.

        Returns the Protection Source whose registration parameters of its
        Application Servers are modified upon success.

        Args:
            body (UpdateApplicationServerParameters): Request to modify the
                Application Servers registration of a Protection Source.

        Returns:
            ProtectionSource: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_application_servers called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_application_servers.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_application_servers.')
            _url_path = '/public/protectionSources/applicationServers'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for update_application_servers.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_application_servers.'
            )
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_application_servers')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_application_servers.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionSource.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_unregister_application_servers(self, body, id):
        """Does a DELETE request to /public/protectionSources/applicationServers/{id}.

        Unregistering Application Servers will fail if the Protection Source
        is
        currently being backed up.
        Returns the Protection Source whose Application Servers are
        unregistered upon
        success.

        Args:
            body (UnRegisterApplicationServersParameters): Request to register
                a protection source.
            id (long|int): Specifies a unique id of the Protection Source to
                unregister the Application Servers. If the Protection Source
                is currently being backed up, unregister operation will fail.

        Returns:
            ProtectionSource: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_unregister_application_servers called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_unregister_application_servers.'
            )
            self.validate_parameters(body=body, id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for delete_unregister_application_servers.'
            )
            _url_path = '/public/protectionSources/applicationServers/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for delete_unregister_application_servers.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_unregister_application_servers.'
            )
            _request = self.http_client.delete(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='delete_unregister_application_servers')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for delete_unregister_application_servers.'
            )
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionSource.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_data_store_information(self, source_id):
        """Does a GET request to /public/protectionSources/datastores.

        Returns the datastore information in VMware environment.

        Args:
            source_id (long|int): Specifies the id of the virtual machine in
                vmware environment.

        Returns:
            list of ProtectionSource: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_data_store_information called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for list_data_store_information.'
            )
            self.validate_parameters(source_id=source_id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for list_data_store_information.')
            _url_path = '/public/protectionSources/datastores'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'sourceId': source_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for list_data_store_information.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_data_store_information.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='list_data_store_information')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for list_data_store_information.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionSource.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def run_diagnostics(self, id):
        """Does a POST request to /public/protectionSources/diagnostics/{id}

        If the request is successful, the diagnostics script is triggered on
        Cohesity
        agent which generates a tarball containing various diagnostics and
        uploads it
        to the Cohesity cluster. Host type could be Linux, Windows.

        Args:
            id (int): Specifies the entity id.

        Returns:
            RunDiagnosticsMessage: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('run_diagnostics called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for run_diagnostics.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL

            _url_path = '/public/protectionSources/diagnostics/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
            # Prepare headers
            self.logger.info(
                'Preparing headers for run_diagnostics.')
            _headers = {
                'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for run_diagnostics.'
            )
            _request = self.http_client.post(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='run_diagnostics')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for run_diagnostics.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              RunDiagnosticsMessage.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def download_cft_file(self, body=None):
        """Does a GET request to /public/protectionSources/downloadCftFile.

        TODO: Type description here.

        Args:
            body (DownloadCftParams): Specifies the request to download CFT.

        Returns:
            DownloadCftResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('download_cft_file called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for download_cft_file.')
            _url_path = '/public/protectionSources/downloadCftFile'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for download_cft_file.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for download_cft_file.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='download_cft_file')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for download_cft_file.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                DownloadCftResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_exchange_dag_hosts(self, endpoint=None, protection_source_id=None):
        """Does a GET request to /public/protectionSources/exchangeDagHosts.

        Returns information about all the exchange hosts that belong to an
        Exchange
        DAG.

        Args:
            endpoint (string, optional): Specifies the endpoint of Exchange
                DAG or a host which is member of Exchange DAG or a standalone
                exchange server.
            protection_source_id (int): Specifies the Protection Source Id of
                the Exchange DAG source.

        Returns:
            ExchangeDagHostsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_exchange_dag_hosts called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for list_exchange_dag_hosts.')
            _url_path = '/public/protectionSources/exchangeDagHosts'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'endpoint': endpoint, 'protectionSourceId': protection_source_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_exchange_dag_hosts.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_exchange_dag_hosts.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='list_exchange_dag_hosts')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for list_exchange_dag_hosts.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ExchangeDagHostsResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protection_sources_objects(self, object_ids=None):
        """Does a GET request to /public/protectionSources/objects.

        Returns the Protection Source objects corresponding to the specified
        ids.

        Args:
            object_ids (list of long|int, optional): Specifies the ids of the
                Protection Source objects to return.

        Returns:
            list of ProtectionSource: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_sources_objects called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_protection_sources_objects.')
            _url_path = '/public/protectionSources/objects'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {'objectIds': object_ids}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_protection_sources_objects.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protection_sources_objects.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_protection_sources_objects')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_protection_sources_objects.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionSource.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_protection_sources_object_by_id(self, id):
        """Does a GET request to /public/protectionSources/objects/{id}.

        Returns the Protection Source object corresponding to the specified
        id.

        Args:
            id (long|int): Specifies a unique id of the Protection Source to
                return.

        Returns:
            ProtectionSource: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protection_sources_object_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_protection_sources_object_by_id.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for get_protection_sources_object_by_id.')
            _url_path = '/public/protectionSources/objects/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for get_protection_sources_object_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_protection_sources_object_by_id.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='get_protection_sources_object_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for get_protection_sources_object_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionSource.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_protected_objects(self,
                               environment,
                               id,
                               all_under_hierarchy=None,
                               include_rpo_snapshots=None,
                               prune_protection_job_metadata=None):
        """Does a GET request to /public/protectionSources/protectedObjects.

        Returns the list of protected Objects in a registered Protection
        Source.

        Args:
            environment (EnvironmentListProtectedObjectsEnum): Specifies the
                environment type of the registered Protection Source such as
                'kVMware', 'kSQL', 'kView' 'kPhysical', 'kPuppeteer', 'kPure',
                'kNetapp', 'kGenericNas', 'kHyperV', 'kAcropolis', or
                'kAzure'. For example, set this parameter to 'kVMware' if the
                registered Protection Source is of 'kVMware' environment type.
                Supported environment types such as 'kView', 'kSQL',
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
                indicates Elastifile Protection Source environment. 'kAD'
                indicates Active Directory Protection Source environment.
                'kRDSSnapshotManager' indicates AWS RDS Protection Source
                environment. 'kCassandra' indicates Cassandra Protection
                Source environment. 'kMongoDB' indicates MongoDB Protection
                Source environment. 'kCouchbase' indicates Couchbase Protection
                Source environment. 'kHdfs' indicates Hdfs Protection Source
                environment. 'kHive' indicates Hive Protection Source
                environment. 'kHBase' indicates HBase Protection Source
                environment. 'kUDA' indicates Universal Data Adapter Protection
                Source environment. 'kO365Teams' indicates the Office365 Teams
                Protection Source environment. 'kO365Group' indicates the
                Office365 Groups Protection Source environment. 'kO365Exchange'
                indicates the Office365 Mailbox Protection Source environment.
                'kO365OneDrive' indicates the Office365 OneDrive Protection
                Source environment.'kO365Sharepoint' indicates the Office365
                SharePoint Protection Source environment.'kO365PublicFolders'
                indicates the Office365 PublicFolders Protection Source
                environment.
            id (long|int): Specifies the Id of a registered Protection Source
                of the type given in environment.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.
            include_rpo_snapshots (bool, optional): If true, then the
                Protected Objects protected by RPO policies will also be
                returned.
            prune_protection_job_metadata (bool, optional): Specifies whether
                the metadata about the protection job is to be pruned. If set
                to true, only ID, name & policy info will be returned. Info
                about indexing, entities within the job and other additional
                settings will be omitted.

        Returns:
            list of ProtectedVmInfo: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_protected_objects called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for list_protected_objects.')
            self.validate_parameters(environment=environment, id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for list_protected_objects.')
            _url_path = '/public/protectionSources/protectedObjects'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'environment': environment,
                'id': id,
                'allUnderHierarchy': all_under_hierarchy,
                'includeRpoSnapshots': include_rpo_snapshots,
                'pruneProtectionJobMetadata': prune_protection_job_metadata
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_protected_objects.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_protected_objects.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='list_protected_objects')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for list_protected_objects.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectedVmInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_refresh_protection_source_by_id(self, id):
        """Does a POST request to /public/protectionSources/refresh/{id}.

        Force an immediate refresh between the specified Protection Source
        tree
        on the Cohesity Cluster and the Inventory tree
        in the associated vCenter Server.

        For example if a new VM is added to the vCenter Server, after a
        refresh,
        a new Protection Source node for this VM is added to the Protection
        Sources
        tree.

        Success indicates the forced refresh has been completed. For larger
        sources it
        is possible for the operation to timeout before the force refresh has
        been
        completed. This timeout can be increased by modifying the
        'iris_post_timeout_msecs_to_magneto' gflag on the Iris service.

        Args:
            id (long|int): Id of the root node of the Protection Sources tree
                to refresh.  Force a refresh of the Object hierarchy for the
                passed in Protection Sources Id.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_refresh_protection_source_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_refresh_protection_source_by_id.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_refresh_protection_source_by_id.'
            )
            _url_path = '/public/protectionSources/refresh/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_refresh_protection_source_by_id.'
            )
            _request = self.http_client.post(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_refresh_protection_source_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_refresh_protection_source_by_id.'
            )
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_register_protection_source(self, body):
        """Does a POST request to /public/protectionSources/register.

        Register a Protection Source on the Cohesity Cluster.
        It could be the root node of a vCenter Server or a physical server.
        Returns the newly registered Protection Source upon success.

        Args:
            body (RegisterProtectionSourceParameters): Request to register a
                protection source.

        Returns:
            ProtectionSource: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_register_protection_source called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_register_protection_source.'
            )
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_register_protection_source.')
            _url_path = '/public/protectionSources/register'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for create_register_protection_source.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_register_protection_source.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='create_register_protection_source')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_register_protection_source.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionSource.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_protection_sources_registration_info(
        self,
        environments=None,
        ids=None,
        include_entity_permission_info=None,
        sids=None,
        include_source_credentials=None,
        encryption_key=None,
        include_applications_tree_info=None,
        tenant_ids=None,
        prune_non_critical_info=None,
        request_initiator_type=None,
        use_cached_data=None,
        all_under_hierarchy=None):
        """Does a GET request to /public/protectionSources/registrationInfo.

        Returns the registration and protection information of the registered
        Protection Sources.

        Args:
            environments (list of
                EnvironmentListProtectionSourcesRegistrationInfoEnum,
                optional): Return only Protection Sources that match the
                passed in environment type such as 'kVMware', 'kSQL', 'kView'
                'kPhysical', 'kPuppeteer', 'kPure', 'kNetapp', 'kGenericNas',
                'kHyperV', 'kAcropolis', or 'kAzure'. For example, set this
                parameter to 'kVMware' to only return the Sources (and their
                Object subtrees) found in the 'kVMware' (VMware vCenter
                Server) environment.  NOTE: 'kPuppeteer' refers to Cohesity's
                Remote Adapter.
            ids (list of long|int, optional): Return only the registered root
                nodes whose Ids are given in the list.
            include_entity_permission_info (bool, optional): If specified,
                then a list of entities with permissions assigned to them are
                returned.
            sids (list of string, optional): Filter the registered root nodes
                for the sids given in the list.
            include_source_credentials (bool, optional): If specified, then
                crednetial for the registered sources will be included.
                Credential is first encrypted with internal key and then
                    reencrypted with user supplied 'encryption_key'.
            encryption_key (string, optional): Key to be used to encrypt the
                source credential. If include_source_credentials is set to true
                this key must be specified.
            prune_non_critical_info (bool, optional): Specifies whether to
                prune non critical info within entities. Incase of VMs,
                virtual disk information will be pruned. Incase of
                Office365, metadata about user entities will be pruned. This
                can be used to limit the size of the response by caller.
            request_initiator_type (str, optional): Specifies the type of the
                request. Possible values are UIUser and UIAuto, which means the
                request is triggered by user or is an auto refresh request.
                Services like magneto will use this to determine the priority
                of the requests, so that it can more intelligently handle
                overload situations by prioritizing higher priority requests.
            use_cached_data (bool, optional): Specifies whether we can serve
                the GET request to the read replica cache. setting this to
                true ensures that the API request is served to the read
                replica. setting this to false will serve the request to the
                master.
            include_applications_tree_info (bool, optional): Specifies whether
                to return applications tree info or not.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            GetRegistrationInfoResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info(
                'list_protection_sources_registration_info called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for list_protection_sources_registration_info.'
            )
            _url_path = '/public/protectionSources/registrationInfo'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'environments': environments,
                'ids': ids,
                'includeEntityPermissionInfo': include_entity_permission_info,
                'sids': sids,
                'includeSourceCredentials': include_source_credentials,
                'encryptionKey': encryption_key,
                'includeApplicationsTreeInfo':include_applications_tree_info,
                'tenantIds': tenant_ids,
                'pruneNonCriticalInfo': prune_non_critical_info,
                'requestInitiatorType': request_initiator_type,
                'useCachedData': use_cached_data,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for list_protection_sources_registration_info.'
            )
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_protection_sources_registration_info.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='list_protection_sources_registration_info')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for list_protection_sources_registration_info.'
            )
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                GetRegistrationInfoResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_protection_sources_root_nodes(self,
                                           id=None,
                                           environments=None,
                                           environment=None):
        """Does a GET request to /public/protectionSources/rootNodes.

        Returns the root Protection Sources and the registration information
        for
        each of these Sources.

        Args:
            id (long|int, optional): Return the registration information for
                the Protection Source id.
            environments (list of
                EnvironmentListProtectionSourcesRootNodesEnum, optional):
                Return only the root Protection Sources that match the passed
                in environment type such as 'kVMware', 'kSQL', 'kView',
                'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp', 'kGenericNas',
                'kHyperV', 'kAcropolis' 'kAzure'. For example, set this
                parameter to 'kVMware' to only return the root Protection
                Sources found in the 'kVMware' (VMware vCenter) environment.
                In addition, the registration information for each Source is
                returned.  NOTE: 'kPuppeteer' refers to Cohesity's Remote
                Adapter.
            environment (string, optional): This field is deprecated. Use
                environments instead. deprecated: true

        Returns:
            list of ProtectionSourceNode: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_protection_sources_root_nodes called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for list_protection_sources_root_nodes.')
            _url_path = '/public/protectionSources/rootNodes'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'id': id,
                'environments': environments,
                'environment': environment
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for list_protection_sources_root_nodes.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_protection_sources_root_nodes.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='list_protection_sources_root_nodes')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for list_protection_sources_root_nodes.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ProtectionSourceNode.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_sql_aag_hosts_and_databases(self, sql_protection_source_ids):
        """Does a GET request to /public/protectionSources/sqlAagHostsAndDatabases.

        Given a list of Protection Source Ids registered as SQL servers,
        returns
        AAGs found and the databases in AAG(Always on Availablity Group).

        Args:
            sql_protection_source_ids (list of long|int): Specifies a list of
                Ids of Protection Sources registered as SQL servers. These
                sources may have one or more SQL databases in them. Some of
                them may be part of AAGs(Always on Availability Group).

        Returns:
            list of SqlAagHostAndDatabases: Response from the API. List SQL
                AAG hosts and databases response.
Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_sql_aag_hosts_and_databases called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for list_sql_aag_hosts_and_databases.'
            )
            self.validate_parameters(
                sql_protection_source_ids=sql_protection_source_ids)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for list_sql_aag_hosts_and_databases.')
            _url_path = '/public/protectionSources/sqlAagHostsAndDatabases'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'sqlProtectionSourceIds': sql_protection_source_ids
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                'Preparing headers for list_sql_aag_hosts_and_databases.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_sql_aag_hosts_and_databases.'
            )
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='list_sql_aag_hosts_and_databases')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for list_sql_aag_hosts_and_databases.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                SqlAagHostAndDatabases.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def list_virtual_machines(self,
                              v_center_id=None,
                              names=None,
                              uuids=None,
                              protected=None):
        """Does a GET request to /public/protectionSources/virtualMachines.

        Returns all Virtual Machines found in all the vCenter Servers
        registered
        on the Cohesity Cluster that match the filter criteria specified
        using
        parameters.
        If an id is specified, only VMs found in the specified vCenter Server
        are returned.
        Only VM Objects are returned.
        Other VMware Objects such as datacenters are not returned.

        Args:
            v_center_id (long|int, optional): Limit the VMs returned to the
                set of VMs found in a specific vCenter Server. Pass in the
                root Protection Source id for the vCenter Server to search for
                VMs.
            names (list of string, optional): Limit the returned VMs to those
                that exactly match the passed in VM name. To match multiple VM
                names, specify multiple "names" parameters that each specify a
                single VM name. The string must exactly match the passed in VM
                name and wild cards are not supported.
            uuids (list of string, optional): Limit the returned VMs to those
                that exactly match the passed in UUIDs.
            protected (bool, optional): Limit the returned VMs to those that
                have been protected by a Protection Job. By default, both
                protected and unprotected VMs are returned.

        Returns:
            list of ProtectionSource: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_virtual_machines called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for list_virtual_machines.')
            _url_path = '/public/protectionSources/virtualMachines'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'vCenterId': v_center_id,
                'names': names,
                'uuids': uuids,
                'protected': protected
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_virtual_machines.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for list_virtual_machines.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='list_virtual_machines')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for list_virtual_machines.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              ProtectionSource.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_unregister_protection_source(self, id):
        """Does a DELETE request to /public/protectionSources/{id}.

        Unregister a previously registered Protection Source.

        Args:
            id (long|int): Specifies a unique id of the Protection Source to
                unregister. If the Protection Source is currently being backed
                up, unregister operation will fail.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_unregister_protection_source called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_unregister_protection_source.'
            )
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for delete_unregister_protection_source.')
            _url_path = '/public/protectionSources/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_unregister_protection_source.'
            )
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(
                _request, name='delete_unregister_protection_source')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for delete_unregister_protection_source.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_protection_source(self, id, body=None):
        """Does a PATCH request to /public/protectionSources/{id}.

        Update a previously registered Protection Source with new details.

        Args:
            id (long|int): Specifies a unique id of the Protection Source to
                update.
            body (UpdateProtectionSourceParameters, optional): Request to
                update protection source.

        Returns:
            ProtectionSourceNode: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_protection_source called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_protection_source.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_protection_source.')
            _url_path = '/public/protectionSources/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_protection_source.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_protection_source.'
            )
            _request = self.http_client.patch(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_protection_source')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_protection_source.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body,
                ProtectionSourceNode.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
