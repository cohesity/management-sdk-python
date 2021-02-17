# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.


class ServiceStateResult(object):

    """Implementation of the 'ServiceStateResult' model.

    Specifies the result of querying the state of a specific service on
    the Cluster.

    Attributes:
        service (ServiceServiceStateResultEnum): Specifies the name of the
            service. 'kApollo' is a service for reclaiming freed disk sectors
            on Nodes in the SnapFS distributed file system. 'kBridge' is a
            service for managing the SnapFS distributed file system. 'kGenie'
            is a service that is responsible for monitoring hardware health on
            the Cluster. 'kGenieGofer' is a service that links the Genie
            service to other services on the Cluster. 'kMagneto' is the data
            protection service of the Cohesity Data Platform. 'kIris' is the
            service which serves REST API calls to the UI, CLI, and any
            scripts written by customers. 'kIrisProxy' is a service that links
            the Iris service to other services on the Cluster. 'kScribe' is
            the service responsible for storing filesystem metadata. 'kStats'
            is the service that is responsible for retrieving and aggregating
            disk metrics across the Cluster. 'kYoda' is an elastic search
            indexing service. 'kAlerts' is a publisher and subscribing service
            for alerts. 'kKeychain' is a service for managing disk encryption
            keys. 'kLogWatcher' is a service that scans the log directory and
            reduces the number of logs if required. 'kStatsCollector' is a
            service that periodically logs system stats. 'kGandalf' is a
            distributed lock service and coordination manager. 'kNexus'
            indicates the Nexus service. This is the service that is
            responsible for creation of Clusters and configuration of Nodes
            and networking. 'kNexusProxy' is a service that links the Nexus
            service to other services on the Cluster. 'kStorageProxy' is a
            service for accessing data on external entities. 'kTricorder' is a
            diagnostic health testing service for Clusters. 'kRtClient' is a
            reverse tunneling client service. 'kVaultProxy' is a service for
            managing external targets that Clusters can be backed up to.
            'kSmbProxy' is an SMB protocol service. 'kBridgeProxy' is the
            service that links the Bridge service to other services on the
            Cluster. 'kLibrarian' is an elastic search indexing service.
            'kGroot' is a service for managing replication of SQL databases
            across multiple nodes in a Cluster. 'kEagleAgent' is a service
            that is responsible for retrieving information on Cluster health.
            'kAthena' is a service for running distributed containerized
            applications on the Cohesity Data Platform. 'kBifrostBroker' is a
            service for communicating with the Cohesity proxies for
            multitenancy. 'kSmb2Proxy' is a new SMB protocol service. 'kOs'
            can be specified in order to do a full reboot. 'kPatch' is a
            service for downloading and applying patches.
           'kCompass' is a service for serving dns request for external and
            internal traffic.
        state (StateServiceStateResultEnum): Specifies the state of the
            service. 'kServiceStopped' indicates that the service has been
            stopped. 'kServiceRunning' indicates that the service is currently
            running. 'kServiceRestarting' indicates that the service is in the
            queue to be restarted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "service":'service',
        "state":'state'
    }

    def __init__(self,
                 service=None,
                 state=None):
        """Constructor for the ServiceStateResult class"""

        # Initialize members of the class
        self.service = service
        self.state = state


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
        service = dictionary.get('service')
        state = dictionary.get('state')

        # Return an object of this model
        return cls(service,
                   state)


