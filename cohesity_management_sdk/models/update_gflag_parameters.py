# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.gflag


class UpdateGflagParameters(object):

    """Implementation of the 'UpdateGflagParameters' model.

    Specifies the parameters for updating service gflags.


    Attributes:

        effective_now (bool): Specifies whether to apply the change
            immediately. If set to true, the gflag change will work without
            restarting the service.
        gflags (list of Gflag): Specifies a list of gflags. These will be added
            to the existing flags for the service. The values will be
            overwritten if required. If no value for gflag is specified, this
            gflag will be reset to default value. If no gflag is specified, all
            gflags for this service will be reset to default value.
        reason (string): Specifies the reason for clearing gflags.
        service_name (ServiceNameEnum, required): Specifies the service name.
            'kApollo' is a service for reclaiming freed disk sectors on Nodes
            in the SnapFS distributed file system. 'kBridge' is a service for
            managing the SnapFS distributed file system. 'kGenie' is a service
            that is responsible for monitoring hardware health on the Cluster.
            'kGenieGofer' is a service that links the Genie service to other
            services on the Cluster. 'kMagneto' is the data protection service
            of the Cohesity Data Platform. 'kIris' is the service which serves
            REST API calls to the UI, CLI, and any scripts written by
            customers. 'kIrisProxy' is a service that links the Iris service to
            other services on the Cluster. 'kScribe' is the service responsible
            for storing filesystem metadata. 'kStats' is the service that is
            responsible for retrieving and aggregating disk metrics across the
            Cluster. 'kYoda' is an elastic search indexing service. 'kAlerts'
            is a publisher and subscribing service for alerts. 'kKeychain' is a
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
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "effective_now":'effectiveNow',
        "gflags":'gflags',
        "reason":'reason',
        "service_name":'serviceName',
    }
    def __init__(self,
                 effective_now=None,
                 gflags=None,
                 reason=None,
                 service_name=None,
            ):

        """Constructor for the UpdateGflagParameters class"""

        # Initialize members of the class
        self.effective_now = effective_now
        self.gflags = gflags
        self.reason = reason
        self.service_name = service_name

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
        effective_now = dictionary.get('effectiveNow')
        gflags = None
        if dictionary.get('gflags') != None:
            gflags = list()
            for structure in dictionary.get('gflags'):
                gflags.append(cohesity_management_sdk.models.gflag.Gflag.from_dictionary(structure))
        reason = dictionary.get('reason')
        service_name = dictionary.get('serviceName')

        # Return an object of this model
        return cls(
            effective_now,
            gflags,
            reason,
            service_name
)