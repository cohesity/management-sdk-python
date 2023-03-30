# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

from cohesity_management_sdk.decorators import lazy_property
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.controllers.access_tokens_controller import AccessTokensController
from cohesity_management_sdk.controllers.active_directory_controller import ActiveDirectoryController
from cohesity_management_sdk.controllers.alerts_controller import AlertsController
from cohesity_management_sdk.controllers.analytics_controller import AnalyticsController
from cohesity_management_sdk.controllers.antivirus_service_group_controller import AntivirusServiceGroupController
from cohesity_management_sdk.controllers.app_controller import AppController
from cohesity_management_sdk.controllers.app_instance_controller import AppInstanceController
from cohesity_management_sdk.controllers.audit_controller import AuditController
from cohesity_management_sdk.controllers.banner_controller import BannerController
from cohesity_management_sdk.controllers.cluster_controller import ClusterController
from cohesity_management_sdk.controllers.certificates_controller import CertificatesController
from cohesity_management_sdk.controllers.clusters_controller import ClustersController
from cohesity_management_sdk.controllers.cluster_partitions_controller import ClusterPartitionsController
from cohesity_management_sdk.controllers.dashboard_controller import DashboardController
from cohesity_management_sdk.controllers.nodes_controller import NodesController
from cohesity_management_sdk.controllers.groups_controller import GroupsController
from cohesity_management_sdk.controllers.idps_controller import IdpsController
from cohesity_management_sdk.controllers.interface_controller import InterfaceController
from cohesity_management_sdk.controllers.interface_group_controller import InterfaceGroupController
from cohesity_management_sdk.controllers.ip_controller import IpController
from cohesity_management_sdk.controllers.kms_configuration_controller import KmsConfigurationController
from cohesity_management_sdk.controllers.ldap_provider_controller import LdapProviderController
from cohesity_management_sdk.controllers.license_controller import LicenseController
from cohesity_management_sdk.controllers.monitoring_controller import MonitoringController
from cohesity_management_sdk.controllers.network_controller import NetworkController
from cohesity_management_sdk.controllers.reports_controller import ReportsController
from cohesity_management_sdk.controllers.scheduler_controller import SchedulerController
from cohesity_management_sdk.controllers.tags_controller import TagsController
from cohesity_management_sdk.controllers.views_controller import ViewsController
from cohesity_management_sdk.controllers.packages_controller import PackagesController
from cohesity_management_sdk.controllers.protection_sources_controller import ProtectionSourcesController
from cohesity_management_sdk.controllers.custom_reporting_controller import CustomReportingController
from cohesity_management_sdk.controllers.principals_controller import PrincipalsController
from cohesity_management_sdk.controllers.privileges_controller import PrivilegesController
from cohesity_management_sdk.controllers.protection_jobs_controller import ProtectionJobsController
from cohesity_management_sdk.controllers.protection_objects_controller import ProtectionObjectsController
from cohesity_management_sdk.controllers.protection_policies_controller import ProtectionPoliciesController
from cohesity_management_sdk.controllers.protection_runs_controller import ProtectionRunsController
from cohesity_management_sdk.controllers.remote_cluster_controller import RemoteClusterController
from cohesity_management_sdk.controllers.remote_restore_controller import RemoteRestoreController
from cohesity_management_sdk.controllers.restore_tasks_controller import RestoreTasksController
from cohesity_management_sdk.controllers.clone_refresh_tasks_controller import CloneRefreshTasksController
from cohesity_management_sdk.controllers.roles_controller import RolesController
from cohesity_management_sdk.controllers.routes_controller import RoutesController
from cohesity_management_sdk.controllers.search_controller import SearchController
from cohesity_management_sdk.controllers.notifications_controller import NotificationsController
from cohesity_management_sdk.controllers.preferences_controller import PreferencesController
from cohesity_management_sdk.controllers.smb_file_opens_controller import SMBFileOpensController
from cohesity_management_sdk.controllers.statistics_controller import StatisticsController
from cohesity_management_sdk.controllers.stats_controller import StatsController
from cohesity_management_sdk.controllers.tenant_controller import TenantController
from cohesity_management_sdk.controllers.vaults_controller import VaultsController
from cohesity_management_sdk.controllers.view_boxes_controller import ViewBoxesController
from cohesity_management_sdk.controllers.vlan_controller import VlanController


class CohesityClient(object):

    @lazy_property
    def access_tokens(self):
        return AccessTokensController(self.config)

    @lazy_property
    def active_directory(self):
        return ActiveDirectoryController(self.config)

    @lazy_property
    def app(self):
        return AppController(self.config)

    @lazy_property
    def app_instance(self):
        return AppInstanceController(self.config)

    @lazy_property
    def analytics(self):
        return AnalyticsController(self.config)

    @lazy_property
    def alerts(self):
        return AlertsController(self.config)

    @lazy_property
    def antivirus_service_group(self):
        return AntivirusServiceGroupController(self.config)

    @lazy_property
    def audit(self):
        return AuditController(self.config)

    @lazy_property
    def banner(self):
        return BannerController(self.config) 

    @lazy_property
    def cluster(self):
        return ClusterController(self.config)

    @lazy_property
    def certificates(self):
        return CertificatesController(self.config)

    @lazy_property
    def clusters(self):
        return ClustersController(self.config)

    @lazy_property
    def cluster_partitions(self):
        return ClusterPartitionsController(self.config)

    @lazy_property
    def dashboard(self):
        return DashboardController(self.config)

    @lazy_property
    def nodes(self):
        return NodesController(self.config)

    @lazy_property
    def groups(self):
        return GroupsController(self.config)

    @lazy_property
    def idps(self):
        return IdpsController(self.config)

    @lazy_property
    def interface(self):
        return InterfaceController(self.config)

    @lazy_property
    def interface_group(self):
        return InterfaceGroupController(self.config)

    @lazy_property
    def ip(self):
        return IpController(self.config)

    @lazy_property
    def license(self):
        return LicenseController(self.config)

    @lazy_property
    def kms_configuration(self):
        return KmsConfigurationController(self.config)

    @lazy_property
    def ldap_provider(self):
        return LdapProviderController(self.config)

    @lazy_property
    def monitoring(self):
        return MonitoringController(self.config)

    @lazy_property
    def network(self):
        return NetworkController(self.config)

    @lazy_property
    def views(self):
        return ViewsController(self.config)

    @lazy_property
    def packages(self):
        return PackagesController(self.config)

    @lazy_property
    def protection_sources(self):
        return ProtectionSourcesController(self.config)

    @lazy_property
    def custom_reporting(self):
        return CustomReportingController(self.config)

    @lazy_property
    def principals(self):
        return PrincipalsController(self.config)

    @lazy_property
    def privileges(self):
        return PrivilegesController(self.config)

    @lazy_property
    def protection_jobs(self):
        return ProtectionJobsController(self.config)

    @lazy_property
    def protection_objects(self):
        return ProtectionObjectsController(self.config)

    @lazy_property
    def protection_policies(self):
        return ProtectionPoliciesController(self.config)

    @lazy_property
    def protection_runs(self):
        return ProtectionRunsController(self.config)

    @lazy_property
    def remote_cluster(self):
        return RemoteClusterController(self.config)

    @lazy_property
    def remote_restore(self):
        return RemoteRestoreController(self.config)

    @lazy_property
    def restore_tasks(self):
        return RestoreTasksController(self.config)

    @lazy_property
    def clone_refresh_tasks(self):
        return CloneRefreshTasksController(self.config)

    @lazy_property
    def roles(self):
        return RolesController(self.config)

    @lazy_property
    def routes(self):
        return RoutesController(self.config)

    @lazy_property
    def scheduler(self):
        return SchedulerController(self.config)

    @lazy_property
    def search(self):
        return SearchController(self.config)

    @lazy_property
    def notifications(self):
        return NotificationsController(self.config)

    @lazy_property
    def preferences(self):
        return PreferencesController(self.config)

    @lazy_property
    def reports(self):
        return ReportsController(self.config)
    @lazy_property
    def smb_file_opens(self):
        return SMBFileOpensController(self.config)

    @lazy_property
    def statistics(self):
        return StatisticsController(self.config)

    @lazy_property
    def stats(self):
        return StatsController(self.config)

    @lazy_property
    def tags(self):
        return TagsController(self.config)

    @lazy_property
    def tenant(self):
        return TenantController(self.config)

    @lazy_property
    def vaults(self):
        return VaultsController(self.config)

    @lazy_property
    def view_boxes(self):
        return ViewBoxesController(self.config)

    @lazy_property
    def vlan(self):
        return VlanController(self.config)


    def __init__(self,
                 cluster_vip=None,
                 username=None,
                 password=None,
                 domain=None,
                 auth_token=None,
                 api_key=None,
                 open_id_token=None,
                 session_id=None,
                 otp_code=None,
                 otp_type=None):

        self.auth = AuthManager()
        self.config = Configuration()

        if cluster_vip is None:
            raise Exception("Specify cluster VIP")
        if auth_token is not None:
            self.config.auth_token = auth_token
        if username is not None:
            self.config.username = username
        if password is not None:
            self.config.password = password
            self.config.auth_token = None  # Flushing existing token.
        if domain is not None:
            self.config.domain = domain
        if open_id_token is not None:
            self.config.open_id_token = open_id_token
        if session_id is not None:
            self.config.session_id = session_id
        if api_key is not None:
            self.config.api_key = api_key
        if otp_code is not None:
            self.config.otp_code = otp_code
        if otp_type is not None:
            self.config.otp_type = otp_type
        self.config.cluster_vip = cluster_vip
