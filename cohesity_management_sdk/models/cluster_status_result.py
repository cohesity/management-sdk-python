# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.node_status_result
import cohesity_management_sdk.models.system_app_status_result


class ClusterStatusResult(object):

    """Implementation of the 'ClusterStatusResult' model.

    Specifies the result of getting the status of a Cluster.


    Attributes:

        cluster_id (long|int): Specifies the ID of the Cluster.
        cluster_incarnation_id (long|int): Specifies the incarnation ID of the
            Cluster.
        current_operation (CurrentOperationEnum): Specifies the current
            operation being run on the Cluster. 'kNone' indicates that there is
            no current operation taking place. 'kDestroy' indicates that the
            Cluster is currently being destroyed. 'kUpgrade' indicates that the
            Cluster is currently being upgraded. 'kClean' indicates that the
            Cluster is being cleaned. 'kRemoveNode' indicates that a Node is
            being removed from the Cluster. 'kRestartServices' indicates that
            the services on the Cluster are currently being restarted.
        message (string): Specifies an optional message describing details of
            the Cluster status.
        name (string): Specifies the name of the Cluster.
        node_statuses (list of NodeStatusResult): Specifies the status of each
            Node on the Cluster.
        removal_state (RemovalStateClusterStatusResultEnum): Specifies the
            current healing state of the Cluster. 'kNoRemoval' indicates that
            there are no removal operations currently happening on the Cluster.
            'kNodeRemoval' indicates that there is a Node being removed from
            the Cluster. 'kDiskRemoval' indicates that there is a Disk being
            removed from the Cluster. 'kNodeAndDiskRemoval' indicates that
            there is a Node and a Disk being removed from the Cluster.
        services_synced (bool): Specifies whether or not the services are
            synced with the list of stopped services.
        software_version (string): Specifies the software version of the
            Cluster.
        stopped_services (list of StoppedServicesEnum): Specifies the list of
            stopped services on the Cluster. 'kApollo' is a service for
            reclaiming freed disk sectors on Nodes in the SnapFS distributed
            file system. 'kBridge' is a service for managing the SnapFS
            distributed file system. 'kGenie' is a service that is responsible
            for monitoring hardware health on the Cluster. 'kGenieGofer' is a
            service that links the Genie service to other services on the
            Cluster. 'kMagneto' is the data protection service of the Cohesity
            Data Platform. 'kIris' is the service which serves REST API calls
            to the UI, CLI, and any scripts written by customers. 'kIrisProxy'
            is a service that links the Iris service to other services on the
            Cluster. 'kScribe' is the service responsible for storing
            filesystem metadata. 'kStats' is the service that is responsible
            for retrieving and aggregating disk metrics across the Cluster.
            'kYoda' is an elastic search indexing service. 'kAlerts' is a
            publisher and subscribing service for alerts. 'kKeychain' is a
            service for managing disk encryption keys. 'kLogWatcher' is a
            service that scans the log directory and reduces the number of logs
            if required. 'kStatsCollector' is a service that periodically logs
            system stats. 'kGandalf' is a distributed lock service and
            coordination manager. 'kNexus' indicates the Nexus service. This is
            the service that is responsible for creation of Clusters and
            configuration of Nodes and networking. 'kNexusProxy' is a service
            that links the Nexus service to other services on the Cluster.
            'kStorageProxy' is a service for accessing data on external
            entities. 'kRtClient' is a reverse tunneling client service.
            'kVaultProxy' is a service for managing external targets that
            Clusters can be backed up to. 'kSmbProxy' is an SMB protocol
            service. 'kBridgeProxy' is the service that links the Bridge
            service to other services on the Cluster. 'kLibrarian' is an
            elastic search indexing service. 'kGroot' is a service for managing
            replication of SQL databases across multiple nodes in a Cluster.
            'kEagleAgent' is a service that is responsible for retrieving
            information on Cluster health. 'kAthena' is a service for running
            distributed containerized applications on the Cohesity Data
            Platform. 'kBifrostBroker' is a service for communicating with the
            Cohesity proxies for multitenancy. 'kSmb2Proxy' is a new SMB
            protocol service. 'kOs' can be specified in order to do a full
            reboot. 'kAtom' is a service for receiving data for the Continuous
            Data Protection. 'kPatch' is a service for downloading and applying
            patches. 'kCompass' is a service for serving dns request for
            external and internal traffic. 'kEtlServer' is a service
            responsible for ETling data for globalsearch. 'kIcebox' is service
            that links Icebox service to other services on cluster. kScribe,
            kStats, kYoda, kAlerts, kKeychain, kLogWatcher, kStatsCollecter,
            kGandalf, kNexus, kNexusProxy, kStorageProxy, kRtClient,
            kVaultProxy, kSmbProxy, kBridgeProxy, kLibrarian, kGroot,
            kEagleAgent, kAthena, kBifrostBroker, kSmb2Proxy, kOs, kAtom,
            kIcebox
        system_app_status (list of SystemAppStatusResult): Specifies the status
            of each system app on the Cluster
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_id":'clusterId',
        "cluster_incarnation_id":'clusterIncarnationId',
        "current_operation":'currentOperation',
        "message":'message',
        "name":'name',
        "node_statuses":'nodeStatuses',
        "removal_state":'removalState',
        "services_synced":'servicesSynced',
        "software_version":'softwareVersion',
        "stopped_services":'stoppedServices',
        "system_app_status":'systemAppStatus',
    }
    def __init__(self,
                 cluster_id=None,
                 cluster_incarnation_id=None,
                 current_operation=None,
                 message=None,
                 name=None,
                 node_statuses=None,
                 removal_state=None,
                 services_synced=None,
                 software_version=None,
                 stopped_services=None,
                 system_app_status=None,
            ):

        """Constructor for the ClusterStatusResult class"""

        # Initialize members of the class
        self.cluster_id = cluster_id
        self.cluster_incarnation_id = cluster_incarnation_id
        self.current_operation = current_operation
        self.message = message
        self.name = name
        self.node_statuses = node_statuses
        self.removal_state = removal_state
        self.services_synced = services_synced
        self.software_version = software_version
        self.stopped_services = stopped_services
        self.system_app_status = system_app_status

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        cluster_id = dictionary.get('clusterId')
        cluster_incarnation_id = dictionary.get('clusterIncarnationId')
        current_operation = dictionary.get('currentOperation')
        message = dictionary.get('message')
        name = dictionary.get('name')
        node_statuses = None
        if dictionary.get('nodeStatuses') != None:
            node_statuses = list()
            for structure in dictionary.get('nodeStatuses'):
                node_statuses.append(cohesity_management_sdk.models.node_status_result.NodeStatusResult.from_dictionary(structure))
        removal_state = dictionary.get('removalState')
        services_synced = dictionary.get('servicesSynced')
        software_version = dictionary.get('softwareVersion')
        stopped_services = dictionary.get("stoppedServices")
        system_app_status = None
        if dictionary.get('systemAppStatus') != None:
            system_app_status = list()
            for structure in dictionary.get('systemAppStatus'):
                system_app_status.append(cohesity_management_sdk.models.system_app_status_result.SystemAppStatusResult.from_dictionary(structure))

        # Return an object of this model
        return cls(
            cluster_id,
            cluster_incarnation_id,
            current_operation,
            message,
            name,
            node_statuses,
            removal_state,
            services_synced,
            software_version,
            stopped_services,
            system_app_status
)