# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AlertCategoryName(object):

    """Implementation of the 'AlertCategoryName' model.

    AlertCategoryName returns alert category and its public facing string.


    Attributes:

        category (CategoryAlertCategoryNameEnum): Specifies alert category.
            Specifies the category of an Alert. kDisk - Alert associated with
            the disk. kNode - Alert associated with general hardware on a
            specific node. kCluster - Alert associated with general hardware in
            cluster level. kChassis - Alert associated with the Chassis.
            kPowerSupply - Alert associated with the power supply. kCPU - Alert
            associated with the CPU usage. kMemory - Alert associated with the
            RAM/Memory. kTemperature - Alert associated with the temperature.
            kFan - Alert associated with the fan. kNIC - Alert associated with
            network chips and interfaces. kFirmware - Alert associated with the
            firmware. kNodeHealth - Alert associated with node health status.
            kOperatingSystem - Alert associated with operating systems.
            kDataPath - Alert associated with data management in the cluster.
            kMetadata - Alert associated with metadata management. kIndexing -
            Alert associated with indexing services. kHelios - Alert associated
            with Helios. kAppMarketPlace - Alert associated with App
            MarketPlace. kLicense - Alert associated with licensing. kSecurity
            - Alert associated with security. kUpgrade - Alert associated with
            upgrade activities. kClusterManagement - Alert associated with
            cluster management activities. kAuditLog - Alert associated with
            audit log events. kNetworking - Alert associated with networking
            issue. kConfiguration - Alert associated with cluster or system
            configurations. kStorageUsage - Alert associated with the
            disk/domain/cluster storage usage. kFaultTolerance - Alert
            associated with the fault tolerance in different levels.
            kBackupRestore - Alert associated with Backup-Restore job.
            kArchivalRestore - Alert associated with Archival-Restore job.
            kRemoteReplication - Alert associated with Replication job. kQuota
            - Alert associated with Quotas. kCDP - Alert associated with
            Continuous Data Protection. kViewFailover - Alert associated with
            view Failover. kDisasterRecovery - Alert associated with Disaster
            Recovery.
        name (string): Specifies public facing string for alert enums.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "category":'category',
        "name":'name',
    }
    def __init__(self,
                 category=None,
                 name=None,
            ):

        """Constructor for the AlertCategoryName class"""

        # Initialize members of the class
        self.category = category
        self.name = name

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
        category = dictionary.get('category')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(
            category,
            name
)