# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.capacity_by_tier
import cohesity_management_sdk.models.chassis_info
import cohesity_management_sdk.models.count_by_tier
import cohesity_management_sdk.models.node_hardware_info
import cohesity_management_sdk.models.node_stats
import cohesity_management_sdk.models.node_system_disk_info

class Node(object):

    """Implementation of the 'Node' model.

    Node is the struct for a Node.

    Attributes:
        capacity_by_tier (list of CapacityByTier): CapacityByTier describes
            the capacity of each storage tier.
        chassis_info (ChassisInfo): ChassisInfo is the struct for the
            Chassis.
        cluster_partition_id (long|int): ClusterPartitionId is the Id of the
            cluster partition to which the Node belongs.
        cluster_partition_name (string): ClusterPartitionName is the name of
            the cluster to which the Node belongs.
        cohesity_node_serial (string): Cohesity Node Serial Number of the
            Node.
        disk_count (long|int): DiskCount is the number of disks in a node.
        disk_count_by_tier (list of CountByTier): DiskCountByTier describes
            the disk number of each storage tier.
        host_name (string): Host name of the node.
        id (long|int): Id is the Id of the Node.
        ip (string): Ip is the IP address of the Node.
        is_app_node (bool): Whether node is app node.
        is_marked_for_removal (bool): IsMarkedForRemoval specifies whether the
            node has been marked for removal.
        max_physical_capacity_bytes (long|int): MaxPhysicalCapacityBytes
            specifies the maximum physical capacity of the node in bytes.
        node_hardware_info (NodeHardwareInfo): NodeHardwareInfo provides the
            information regarding the hardware.
        node_incarnation_id (long|int): NodeIncarnationId is the incarnation
            id  of this node. The incarnation id is changed every time the
            data is wiped from the node. Various services on a node is only
            run if incarnation id of the node matches the incarnation id of
            the cluster. Whenever a mismatch is detected, Nexus will stop all
            services and clean the data from the node. After clean operation
            is completed, Nexus will set the node incarnation id to cluster
            incarnation id and start the services.
        node_software_version (string): NodeSoftwareVersion is the current
            version of Cohesity software installed on a node.
        node_type (string): Node type: StorageNode, AllFlashNode, RoboNode,
            AppNode, etc.
        offline_disk_count (long|int): OfflineDiskCount is the number of
            offline disks in a node.
        offline_mount_paths_of_disks (list of string):
            OfflineMountPathsOfDisks provides the corresponding mount paths
            for direct attached disks that are currently offline - access to
            these were detected to hang sometime in the past. After these
            disks have been fixed, their mount paths needs to be removed from
            the following list before these will be accessed again.
        product_model (string): Specifies the product model of the node.
        removal_reason (list of RemovalReasonNodeEnum): RemovalReason
            specifies the removal reason of the node. 'kAutoHealthCheck' means
            the entity health is bad. 'kUserGracefulRemoval' means user
            initiated a graceful removal. 'kUserAvoidAccess' means user
            initiated a mark offline. 'kUserGracefulNodeRemoval' mean users
            initiated graceful node removal. 'kUserRemoveDownNode' mean user
            initiated graceful removal of down node.
        removal_state (RemovalStateNodeEnum): RemovalState specifies the
            removal state of the node. 'kDontRemove' means the state of object
            is functional and it is not being removed. 'kMarkedForRemoval'
            means the object is being removed. 'kOkToRemove' means the object
            has been removed on the Cohesity Cluster and if the object is
            physical, it can be removed from the Cohesity Cluster.
        slot_number (int): Slot number occupied by this node within the
            chassis.
        stats (NodeStats): NodeStats provides various statistics for the
            node.
        system_disks (list of NodeSystemDiskInfo): SystemDisk describes the
            node system disks.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "capacity_by_tier":'capacityByTier',
        "chassis_info":'chassisInfo',
        "cluster_partition_id":'clusterPartitionId',
        "cluster_partition_name":'clusterPartitionName',
        "cohesity_node_serial":'cohesityNodeSerial',
        "disk_count":'diskCount',
        "disk_count_by_tier":'diskCountByTier',
        "host_name":'hostName',
        "id":'id',
        "ip":'ip',
        "is_app_node":'isAppNode',
        "is_marked_for_removal":'isMarkedForRemoval',
        "max_physical_capacity_bytes":'maxPhysicalCapacityBytes',
        "node_hardware_info":'nodeHardwareInfo',
        "node_incarnation_id":'nodeIncarnationId',
        "node_software_version":'nodeSoftwareVersion',
        "node_type":'nodeType',
        "offline_disk_count":'offlineDiskCount',
        "offline_mount_paths_of_disks":'offlineMountPathsOfDisks',
        "product_model":'productModel',
        "removal_reason":'removalReason',
        "removal_state":'removalState',
        "slot_number":'slotNumber',
        "stats":'stats',
        "system_disks":'systemDisks'
    }

    def __init__(self,
                 capacity_by_tier=None,
                 chassis_info=None,
                 cluster_partition_id=None,
                 cluster_partition_name=None,
                 cohesity_node_serial=None,
                 disk_count=None,
                 disk_count_by_tier=None,
                 host_name=None,
                 id=None,
                 ip=None,
                 is_app_node=None,
                 is_marked_for_removal=None,
                 max_physical_capacity_bytes=None,
                 node_hardware_info=None,
                 node_incarnation_id=None,
                 node_software_version=None,
                 node_type=None,
                 offline_disk_count=None,
                 offline_mount_paths_of_disks=None,
                 product_model=None,
                 removal_reason=None,
                 removal_state=None,
                 slot_number=None,
                 stats=None,
                 system_disks=None):
        """Constructor for the Node class"""

        # Initialize members of the class
        self.capacity_by_tier = capacity_by_tier
        self.chassis_info = chassis_info
        self.cluster_partition_id = cluster_partition_id
        self.cluster_partition_name = cluster_partition_name
        self.cohesity_node_serial = cohesity_node_serial
        self.disk_count = disk_count
        self.disk_count_by_tier = disk_count_by_tier
        self.host_name = host_name
        self.id = id
        self.ip = ip
        self.is_app_node = is_app_node
        self.is_marked_for_removal = is_marked_for_removal
        self.max_physical_capacity_bytes = max_physical_capacity_bytes
        self.node_hardware_info = node_hardware_info
        self.node_incarnation_id = node_incarnation_id
        self.node_software_version = node_software_version
        self.node_type = node_type
        self.offline_disk_count = offline_disk_count
        self.offline_mount_paths_of_disks = offline_mount_paths_of_disks
        self.product_model = product_model
        self.removal_reason = removal_reason
        self.removal_state = removal_state
        self.slot_number = slot_number
        self.stats = stats
        self.system_disks = system_disks


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
        capacity_by_tier = None
        if dictionary.get('capacityByTier') != None:
            capacity_by_tier = list()
            for structure in dictionary.get('capacityByTier'):
                capacity_by_tier.append(cohesity_management_sdk.models.capacity_by_tier.CapacityByTier.from_dictionary(structure))
        chassis_info = cohesity_management_sdk.models.chassis_info.ChassisInfo.from_dictionary(dictionary.get('chassisInfo')) if dictionary.get('chassisInfo') else None
        cluster_partition_id = dictionary.get('clusterPartitionId')
        cluster_partition_name = dictionary.get('clusterPartitionName')
        cohesity_node_serial = dictionary.get('cohesityNodeSerial')
        disk_count = dictionary.get('diskCount')
        disk_count_by_tier = None
        if dictionary.get('diskCountByTier') != None:
            disk_count_by_tier = list()
            for structure in dictionary.get('diskCountByTier'):
                disk_count_by_tier.append(cohesity_management_sdk.models.count_by_tier.CountByTier.from_dictionary(structure))
        host_name = dictionary.get('hostName')
        id = dictionary.get('id')
        ip = dictionary.get('ip')
        is_app_node = dictionary.get('isAppNode')
        is_marked_for_removal = dictionary.get('isMarkedForRemoval')
        max_physical_capacity_bytes = dictionary.get('maxPhysicalCapacityBytes')
        node_hardware_info = cohesity_management_sdk.models.node_hardware_info.NodeHardwareInfo.from_dictionary(dictionary.get('nodeHardwareInfo')) if dictionary.get('nodeHardwareInfo') else None
        node_incarnation_id = dictionary.get('nodeIncarnationId')
        node_software_version = dictionary.get('nodeSoftwareVersion')
        node_type = dictionary.get('nodeType')
        offline_disk_count = dictionary.get('offlineDiskCount')
        offline_mount_paths_of_disks = dictionary.get('offlineMountPathsOfDisks')
        product_model = dictionary.get('productModel')
        removal_reason = dictionary.get('removalReason')
        removal_state = dictionary.get('removalState')
        slot_number = dictionary.get('slotNumber')
        stats = cohesity_management_sdk.models.node_stats.NodeStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None
        system_disks = None
        if dictionary.get('systemDisks') != None:
            system_disks = list()
            for structure in dictionary.get('systemDisks'):
                system_disks.append(cohesity_management_sdk.models.node_system_disk_info.NodeSystemDiskInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(capacity_by_tier,
                   chassis_info,
                   cluster_partition_id,
                   cluster_partition_name,
                   cohesity_node_serial,
                   disk_count,
                   disk_count_by_tier,
                   host_name,
                   id,
                   ip,
                   is_app_node,
                   is_marked_for_removal,
                   max_physical_capacity_bytes,
                   node_hardware_info,
                   node_incarnation_id,
                   node_software_version,
                   node_type,
                   offline_disk_count,
                   offline_mount_paths_of_disks,
                   product_model,
                   removal_reason,
                   removal_state,
                   slot_number,
                   stats,
                   system_disks)


