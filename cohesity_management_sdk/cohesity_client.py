# Copyright 2019 Cohesity Inc.

# -*- coding: utf-8 -*-

from cohesity_management_sdk.decorators import lazy_property
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.controllers.alerts import Alerts
from cohesity_management_sdk.controllers.active_directory import ActiveDirectory
from cohesity_management_sdk.controllers.tenant import Tenant
from cohesity_management_sdk.controllers.static_route import StaticRoute
from cohesity_management_sdk.controllers.preferences import Preferences
from cohesity_management_sdk.controllers.notifications import Notifications
from cohesity_management_sdk.controllers.principals import Principals
from cohesity_management_sdk.controllers.routes import Routes
from cohesity_management_sdk.controllers.remote_cluster import RemoteCluster
from cohesity_management_sdk.controllers.nodes import Nodes
from cohesity_management_sdk.controllers.interface_group import InterfaceGroup
from cohesity_management_sdk.controllers.clusters import Clusters
from cohesity_management_sdk.controllers.certificates import Certificates
from cohesity_management_sdk.controllers.app import App
from cohesity_management_sdk.controllers.app_instance import AppInstance
from cohesity_management_sdk.controllers.vlan import Vlan
from cohesity_management_sdk.controllers.views import Views
from cohesity_management_sdk.controllers.view_boxes import ViewBoxes
from cohesity_management_sdk.controllers.restore_tasks import RestoreTasks
from cohesity_management_sdk.controllers.vaults import Vaults
from cohesity_management_sdk.controllers.tenants import Tenants
from cohesity_management_sdk.controllers.statistics import Statistics
from cohesity_management_sdk.controllers.smb_file_opens import SMBFileOpens
from cohesity_management_sdk.controllers.search import Search
from cohesity_management_sdk.controllers.roles import Roles
from cohesity_management_sdk.controllers.remote_restore import RemoteRestore
from cohesity_management_sdk.controllers.protection_sources import ProtectionSources
from cohesity_management_sdk.controllers.protection_runs import ProtectionRuns
from cohesity_management_sdk.controllers.protection_policies import ProtectionPolicies
from cohesity_management_sdk.controllers.protection_jobs import ProtectionJobs
from cohesity_management_sdk.controllers.audit import Audit
from cohesity_management_sdk.controllers.kms_configuration import KmsConfiguration
from cohesity_management_sdk.controllers.privileges import Privileges
from cohesity_management_sdk.controllers.ldap_provider import LdapProvider
from cohesity_management_sdk.controllers.mimport import Import
from cohesity_management_sdk.controllers.idps import Idps
from cohesity_management_sdk.controllers.groups import Groups
from cohesity_management_sdk.controllers.dashboard import Dashboard
from cohesity_management_sdk.controllers.cluster_partitions import ClusterPartitions
from cohesity_management_sdk.controllers.export import Export
from cohesity_management_sdk.controllers.cluster import Cluster
from cohesity_management_sdk.controllers.access_tokens import AccessTokens


class CohesityClient(object):

    auth = AuthManager
    config = Configuration

    @lazy_property
    def alerts(self):
        return Alerts()

    @lazy_property
    def active_directory(self):
        return ActiveDirectory()

    @lazy_property
    def tenant(self):
        return Tenant()

    @lazy_property
    def static_route(self):
        return StaticRoute()

    @lazy_property
    def preferences(self):
        return Preferences()

    @lazy_property
    def notifications(self):
        return Notifications()

    @lazy_property
    def principals(self):
        return Principals()

    @lazy_property
    def routes(self):
        return Routes()

    @lazy_property
    def remote_cluster(self):
        return RemoteCluster()

    @lazy_property
    def nodes(self):
        return Nodes()

    @lazy_property
    def interface_group(self):
        return InterfaceGroup()

    @lazy_property
    def clusters(self):
        return Clusters()

    @lazy_property
    def certificates(self):
        return Certificates()

    @lazy_property
    def app(self):
        return App()

    @lazy_property
    def app_instance(self):
        return AppInstance()

    @lazy_property
    def vlan(self):
        return Vlan()

    @lazy_property
    def views(self):
        return Views()

    @lazy_property
    def view_boxes(self):
        return ViewBoxes()

    @lazy_property
    def restore_tasks(self):
        return RestoreTasks()

    @lazy_property
    def vaults(self):
        return Vaults()

    @lazy_property
    def tenants(self):
        return Tenants()

    @lazy_property
    def statistics(self):
        return Statistics()

    @lazy_property
    def smb_file_opens(self):
        return SMBFileOpens()

    @lazy_property
    def search(self):
        return Search()

    @lazy_property
    def roles(self):
        return Roles()

    @lazy_property
    def remote_restore(self):
        return RemoteRestore()

    @lazy_property
    def protection_sources(self):
        return ProtectionSources()

    @lazy_property
    def protection_runs(self):
        return ProtectionRuns()

    @lazy_property
    def protection_policies(self):
        return ProtectionPolicies()

    @lazy_property
    def protection_jobs(self):
        return ProtectionJobs()

    @lazy_property
    def audit(self):
        return Audit()

    @lazy_property
    def kms_configuration(self):
        return KmsConfiguration()

    @lazy_property
    def privileges(self):
        return Privileges()

    @lazy_property
    def ldap_provider(self):
        return LdapProvider()

    @lazy_property
    def mimport(self):
        return Import()

    @lazy_property
    def idps(self):
        return Idps()

    @lazy_property
    def groups(self):
        return Groups()

    @lazy_property
    def dashboard(self):
        return Dashboard()

    @lazy_property
    def cluster_partitions(self):
        return ClusterPartitions()

    @lazy_property
    def export(self):
        return Export()

    @lazy_property
    def cluster(self):
        return Cluster()

    @lazy_property
    def access_tokens(self):
        return AccessTokens()

    def __init__(self,
                 cluster_vip=None,
                 username=None,
                 password=None,
                 domain=None,
                 auth_token=None):
        #CohesityPatch
        if cluster_vip == None:
            raise Exception("Specify cluster VIP")
        if auth_token != None:
            Configuration.auth_token = auth_token
        if username != None:
            Configuration.username = username
        if password != None:
            Configuration.password = password
            Configuration.auth_token = None  # Flushing existing token.
        if domain != None:
            Configuration.domain = domain
        Configuration.cluster_vip = cluster_vip


