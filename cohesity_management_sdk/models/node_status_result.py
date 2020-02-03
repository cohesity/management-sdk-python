# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.service_process_entry

class NodeStatusResult(object):

    """Implementation of the 'NodeStatusResult' model.

    Specifies the current status of a Node in the cluster.

    Attributes:
        active_operation (ActiveOperationEnum): Specifies the active operation
            on the Node if there is one. 'kNone' specifies that there is no
            active operation on the Node. 'kDestroyCluster' specifies that the
            Cluster which the Node is a part of is currently being destroyed.
            'kUpgradeCluster' specifies that the Cluster which the Node is a
            part of is currently being upgraded to a new software package.
            'kRestartCluster' specifies that the Cluster which the Node is a
            part of is currently being restarted. 'kCreateCluster' specifies
            that the Node is currently being used to create a new Cluster.
            'kExpandCluster' specifies that the Node is currently being added
            to a Cluster or being used to assist in adding another Node to a
            Cluster. 'kUpgradeNode' specifies that the Node is currently being
            upgraded to a new software package. 'kRemoveNode' specifies that
            the Node is currently being removed from a Cluster or that it is
            assisting in removing another Node from a Cluster. 'kAddDisks'
            specifies that the Node is being used to assist in adding disks to
            the Cluster. 'kMarkDiskOffline' specifies that the Node is being
            use to assist in marking a disk in the Cluster as offline.
        cluster_id (long|int): Specifies the Cluster ID if the Node is part of
            a Cluster.
        id (long|int): Specifies the ID of the Node.
        in_cluster (bool): Specifies whether or not the Node is part of a
            Cluster.
        incarnation_id (long|int): Specifies the Incarnation ID if the Node is
            part of a Cluster.
        ip (string): Specifies the IP address of the Node.
        last_upgrade_time_secs (long|int): Specifies the time of the last
            upgrade in seconds since the epoch.
        marked_for_removal (bool): Specifies whether or not this node is
            marked for removal.
        message (string): Specifies an optional message describing the current
            state of the Node.
        removal_reason (RemovalReasonEnum): Specifies the reason for the
            removal operation if there is a removal operation going on.
            'kUnknown' specifies that the removal reason is not known.
            'kAutoHealthCheck' specifies that an internal health check found
            problems with the Node. 'kUserGracefulRemoval' specifies that the
            user requested a graceful removal. 'kUserAvoidAccess' specifies
            that the user requested to avoid access to this Node.
            'kUserGracefulNodeRemoval' specifies that the user requested a
            graceful removal for all of the disks in this Node.
            'kUserRemoveDownNode' specifies that the user requested a graceful
            removal of the Node while it is down.
        services (list of ServiceProcessEntry): Specifies the list of services
            running on the cluster and their process Ids.
        software_version (string): Specifies the version of the software
            running on the Node.
        uptime (string): Uptime of node.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "active_operation":'activeOperation',
        "cluster_id":'clusterId',
        "id":'id',
        "in_cluster":'inCluster',
        "incarnation_id":'incarnationId',
        "ip":'ip',
        "last_upgrade_time_secs":'lastUpgradeTimeSecs',
        "marked_for_removal":'markedForRemoval',
        "message":'message',
        "removal_reason":'removalReason',
        "services":'services',
        "software_version":'softwareVersion',
        "uptime":'uptime'
    }

    def __init__(self,
                 active_operation=None,
                 cluster_id=None,
                 id=None,
                 in_cluster=None,
                 incarnation_id=None,
                 ip=None,
                 last_upgrade_time_secs=None,
                 marked_for_removal=None,
                 message=None,
                 removal_reason=None,
                 services=None,
                 software_version=None,
                 uptime=None):
        """Constructor for the NodeStatusResult class"""

        # Initialize members of the class
        self.active_operation = active_operation
        self.cluster_id = cluster_id
        self.id = id
        self.in_cluster = in_cluster
        self.incarnation_id = incarnation_id
        self.ip = ip
        self.last_upgrade_time_secs = last_upgrade_time_secs
        self.marked_for_removal = marked_for_removal
        self.message = message
        self.removal_reason = removal_reason
        self.services = services
        self.software_version = software_version
        self.uptime = uptime


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
        active_operation = dictionary.get('activeOperation')
        cluster_id = dictionary.get('clusterId')
        id = dictionary.get('id')
        in_cluster = dictionary.get('inCluster')
        incarnation_id = dictionary.get('incarnationId')
        ip = dictionary.get('ip')
        last_upgrade_time_secs = dictionary.get('lastUpgradeTimeSecs')
        marked_for_removal = dictionary.get('markedForRemoval')
        message = dictionary.get('message')
        removal_reason = dictionary.get('removalReason')
        services = None
        if dictionary.get('services') != None:
            services = list()
            for structure in dictionary.get('services'):
                services.append(cohesity_management_sdk.models.service_process_entry.ServiceProcessEntry.from_dictionary(structure))
        software_version = dictionary.get('softwareVersion')
        uptime = dictionary.get('uptime')

        # Return an object of this model
        return cls(active_operation,
                   cluster_id,
                   id,
                   in_cluster,
                   incarnation_id,
                   ip,
                   last_upgrade_time_secs,
                   marked_for_removal,
                   message,
                   removal_reason,
                   services,
                   software_version,
                   uptime)


