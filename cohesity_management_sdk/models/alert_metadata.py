# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.alert_document


class AlertMetadata(object):

    """Implementation of the 'AlertMetadata' model.

    AlertMetadata specifies metadata for a given alert type. All the alerts of
    a given alert type share the same metadata.


    Attributes:

        alert_document_list (list of AlertDocument): Specifies alert
            documentation one per each language supported.
        alert_type_bucket (AlertTypeBucketEnum): Specifies the Alert type
            bucket. Specifies the Alert type bucket. kHardware - Alerts related
            to hardware on which Cohesity software is running. kSoftware -
            Alerts which are related to software components. kDataService -
            Alerts related to data services. kMaintenance - Alerts relates to
            maintenance activities.
        alert_type_id (int): Specifies unique id for the alert type.
        category (CategoryAlertMetadataEnum): Specifies category of the alert
            type. Specifies the category of an Alert. kDisk - Alert associated
            with the disk. kNode - Alert associated with general hardware on a
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
            MarketPlace. kSystemService -Alert associated with System service
            apps. kLicense - Alert associated with licensing. kSecurity - Alert
            associated with security. kUpgrade - Alert associated with upgrade
            activities. kClusterManagement - Alert associated with cluster
            management activities. kAuditLog - Alert associated with audit log
            events. kNetworking - Alert associated with networking issue.
            kConfiguration - Alert associated with cluster or system
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
        dedup_interval_seconds (int): Specifies dedup interval in seconds. If
            the same alert is raised multiple times by any client in this
            duration, only one of them will be reported.
        dedup_until_resolved (bool): Specifies if the alerts are to be deduped
            until the current one (if any) is resolved.
        hide_alert_from_user (bool): Specifies whether to show the alert in the
            iris UI and CLI.
        ignore_duplicate_occurrences (bool): Specifies whether to ignore
            duplicate occurrences completely.
        primary_key_list (list of string): Specifies properties that serve as
            primary keys.
        property_list (list of string): Specifies list of properties that the
            client is supposed to provide when alert of this type is raised.
        send_support_notification (bool): Specifies whether to send support
            notification for the alert.
        snmp_notification (bool): Specifies whether an SNMP notification is
            sent when an alert is raised.
        syslog_notification (bool): Specifies whether an syslog notification is
            sent when an alert is raised.
        version (int): Specifies version of the metadata.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "alert_document_list":'alertDocumentList',
        "alert_type_bucket":'alertTypeBucket',
        "alert_type_id":'alertTypeId',
        "category":'category',
        "dedup_interval_seconds":'dedupIntervalSeconds',
        "dedup_until_resolved":'dedupUntilResolved',
        "hide_alert_from_user":'hideAlertFromUser',
        "ignore_duplicate_occurrences":'ignoreDuplicateOccurrences',
        "primary_key_list":'primaryKeyList',
        "property_list":'propertyList',
        "send_support_notification":'sendSupportNotification',
        "snmp_notification":'snmpNotification',
        "syslog_notification":'syslogNotification',
        "version":'version',
    }
    def __init__(self,
                 alert_document_list=None,
                 alert_type_bucket=None,
                 alert_type_id=None,
                 category=None,
                 dedup_interval_seconds=None,
                 dedup_until_resolved=None,
                 hide_alert_from_user=None,
                 ignore_duplicate_occurrences=None,
                 primary_key_list=None,
                 property_list=None,
                 send_support_notification=None,
                 snmp_notification=None,
                 syslog_notification=None,
                 version=None,
            ):

        """Constructor for the AlertMetadata class"""

        # Initialize members of the class
        self.alert_document_list = alert_document_list
        self.alert_type_bucket = alert_type_bucket
        self.alert_type_id = alert_type_id
        self.category = category
        self.dedup_interval_seconds = dedup_interval_seconds
        self.dedup_until_resolved = dedup_until_resolved
        self.hide_alert_from_user = hide_alert_from_user
        self.ignore_duplicate_occurrences = ignore_duplicate_occurrences
        self.primary_key_list = primary_key_list
        self.property_list = property_list
        self.send_support_notification = send_support_notification
        self.snmp_notification = snmp_notification
        self.syslog_notification = syslog_notification
        self.version = version

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
        alert_document_list = None
        if dictionary.get('alertDocumentList') != None:
            alert_document_list = list()
            for structure in dictionary.get('alertDocumentList'):
                alert_document_list.append(cohesity_management_sdk.models.alert_document.AlertDocument.from_dictionary(structure))
        alert_type_bucket = dictionary.get('alertTypeBucket')
        alert_type_id = dictionary.get('alertTypeId')
        category = dictionary.get('category')
        dedup_interval_seconds = dictionary.get('dedupIntervalSeconds')
        dedup_until_resolved = dictionary.get('dedupUntilResolved')
        hide_alert_from_user = dictionary.get('hideAlertFromUser')
        ignore_duplicate_occurrences = dictionary.get('ignoreDuplicateOccurrences')
        primary_key_list = dictionary.get("primaryKeyList")
        property_list = dictionary.get("propertyList")
        send_support_notification = dictionary.get('sendSupportNotification')
        snmp_notification = dictionary.get('snmpNotification')
        syslog_notification = dictionary.get('syslogNotification')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(
            alert_document_list,
            alert_type_bucket,
            alert_type_id,
            category,
            dedup_interval_seconds,
            dedup_until_resolved,
            hide_alert_from_user,
            ignore_duplicate_occurrences,
            primary_key_list,
            property_list,
            send_support_notification,
            snmp_notification,
            syslog_notification,
            version
)