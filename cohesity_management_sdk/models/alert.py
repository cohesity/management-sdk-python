# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.alert_document
import cohesity_management_sdk.models.alert_property
import cohesity_management_sdk.models.alert_resolution_details


class Alert(object):

    """Implementation of the 'Alert' model.

    Specifies information about an Alert such as the type, id assigned by the
    Cohesity Cluster, number of duplicates, severity, etc.


    Attributes:

        alert_category (AlertCategoryEnum): Specifies the category of an Alert.
            kDisk - Alert associated with the disk. kNode - Alert associated
            with general hardware on a specific node. kCluster - Alert
            associated with general hardware in cluster level. kChassis - Alert
            associated with the Chassis. kPowerSupply - Alert associated with
            the power supply. kCPU - Alert associated with the CPU usage.
            kMemory - Alert associated with the RAM/Memory. kTemperature -
            Alert associated with the temperature. kFan - Alert associated with
            the fan. kNIC - Alert associated with network chips and interfaces.
            kFirmware - Alert associated with the firmware. kNodeHealth - Alert
            associated with node health status. kOperatingSystem - Alert
            associated with operating systems. kDataPath - Alert associated
            with data management in the cluster. kMetadata - Alert associated
            with metadata management. kIndexing - Alert associated with
            indexing services. kHelios - Alert associated with Helios.
            kAppMarketPlace - Alert associated with App MarketPlace.
            kSystemService -Alert associated with System service apps. kLicense
            - Alert associated with licensing. kSecurity - Alert associated
            with security. kUpgrade - Alert associated with upgrade activities.
            kClusterManagement - Alert associated with cluster management
            activities. kAuditLog - Alert associated with audit log events.
            kNetworking - Alert associated with networking issue.
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
        alert_code (string): Specifies a unique code that categorizes the
            Alert, for example: CE00200014, where CE stands for Cohesity Error,
            the alert state next 3 digits is the id of the Alert Category (e.g.
            002 for 'kNode') and the last 5 digits is the id of the Alert Type
            (e.g. 00014 for 'kNodeHighCpuUsage').
        alert_document (AlertDocument): Specifies documentation about the Alert
            such as name, description, cause and how to resolve the Alert.
        alert_state (AlertStateEnum): Specifies the current state of the Alert.
            kAlertNote - Alerts that are just for note. kAlertOpen - Alerts
            that are unresolved. kAlertResolved - Alerts that are already
            marked as resolved. kAlertSuppressed - Alerts that are suppressed
            due to snooze settings.
        alert_type (int): Specifies a 5 digit unique digital id for the Alert
            Type, such as 00014 for 'kNodeHighCpuUsage'. This id is used in
            alertCode.
        alert_type_bucket (AlertTypeBucketEnum): Specifies the Alert type
            bucket. Specifies the Alert type bucket. kHardware - Alerts related
            to hardware on which Cohesity software is running. kSoftware -
            Alerts which are related to software components. kDataService -
            Alerts related to data services. kMaintenance - Alerts relates to
            maintenance activities.
        cluster_id (long|int): Specifies id of the cluster where the alert was
            raised.
        cluster_name (string): Specifies name of the cluster where the alert
            was raised.
        dedup_count (int): Specifies total count of duplicated Alerts even if
            there are more than 25 occurrences.
        dedup_timestamps (list of long|int): Specifies Unix epoch Timestamps
            (in microseconds) for the last 25 occurrences of duplicated Alerts
            that are stored with the original/primary Alert. Alerts are grouped
            into one Alert if the Alerts are the same type, are reporting on
            the same Object and occur within one hour. 'dedupCount' always
            reports the total count of duplicated Alerts even if there are more
            than 25 occurrences. For example, if there are 100 occurrences of
            this Alert, dedupTimestamps stores the timestamps of the last 25
            occurrences and dedupCount equals 100.
        event_source (string): Specifies source where the event occurred.
        first_timestamp_usecs (long|int): Specifies Unix epoch Timestamp (in
            microseconds) of the first occurrence of the Alert.
        id (string): Specifies unique id of this Alert.
        latest_timestamp_usecs (long|int): Specifies Unix epoch Timestamp (in
            microseconds) of the most recent occurrence of the Alert.
        property_list (list of AlertProperty): Specifies array of key-value
            pairs associated with the Alert. The Cohesity Cluster may
            autogenerate properties depending on the Alert type. This list
            includes both autogenerated and specified properties.
        region_id (string): Specifies the region id of the cluster.
        resolution_details (AlertResolutionDetails): Specifies information
            about the Alert Resolution such as a summary, id assigned by the
            Cohesity Cluster, user who resolved the Alerts, etc.
        resolved_timestamp_usecs (long|int): Specifies Unix epoch Timestamps in
            microseconds when alert is resolved.
        severity (SeverityEnum): Specifies the severity level of an Alert.
            kCritical - Alerts whose severity type is Critical. kWarning -
            Alerts whose severity type is Warning. kInfo - Alerts whose
            severity type is Info.
        suppression_id (long|int): Specifies unique id generated when the Alert
            is suppressed by the admin.
        tenant_ids (list of string): Specifies the tenants for which this alert
            has been raised.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "alert_category":'alertCategory',
        "alert_code":'alertCode',
        "alert_document":'alertDocument',
        "alert_state":'alertState',
        "alert_type":'alertType',
        "alert_type_bucket":'alertTypeBucket',
        "cluster_id":'clusterId',
        "cluster_name":'clusterName',
        "dedup_count":'dedupCount',
        "dedup_timestamps":'dedupTimestamps',
        "event_source":'eventSource',
        "first_timestamp_usecs":'firstTimestampUsecs',
        "id":'id',
        "latest_timestamp_usecs":'latestTimestampUsecs',
        "property_list":'propertyList',
        "region_id":'regionId',
        "resolution_details":'resolutionDetails',
        "resolved_timestamp_usecs":'resolvedTimestampUsecs',
        "severity":'severity',
        "suppression_id":'suppressionId',
        "tenant_ids":'tenantIds',
    }
    def __init__(self,
                 alert_category=None,
                 alert_code=None,
                 alert_document=None,
                 alert_state=None,
                 alert_type=None,
                 alert_type_bucket=None,
                 cluster_id=None,
                 cluster_name=None,
                 dedup_count=None,
                 dedup_timestamps=None,
                 event_source=None,
                 first_timestamp_usecs=None,
                 id=None,
                 latest_timestamp_usecs=None,
                 property_list=None,
                 region_id=None,
                 resolution_details=None,
                 resolved_timestamp_usecs=None,
                 severity=None,
                 suppression_id=None,
                 tenant_ids=None,
            ):

        """Constructor for the Alert class"""

        # Initialize members of the class
        self.alert_category = alert_category
        self.alert_code = alert_code
        self.alert_document = alert_document
        self.alert_state = alert_state
        self.alert_type = alert_type
        self.alert_type_bucket = alert_type_bucket
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.dedup_count = dedup_count
        self.dedup_timestamps = dedup_timestamps
        self.event_source = event_source
        self.first_timestamp_usecs = first_timestamp_usecs
        self.id = id
        self.latest_timestamp_usecs = latest_timestamp_usecs
        self.property_list = property_list
        self.region_id = region_id
        self.resolution_details = resolution_details
        self.resolved_timestamp_usecs = resolved_timestamp_usecs
        self.severity = severity
        self.suppression_id = suppression_id
        self.tenant_ids = tenant_ids

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
        alert_category = dictionary.get('alertCategory')
        alert_code = dictionary.get('alertCode')
        alert_document = cohesity_management_sdk.models.alert_document.AlertDocument.from_dictionary(dictionary.get('alertDocument')) if dictionary.get('alertDocument') else None
        alert_state = dictionary.get('alertState')
        alert_type = dictionary.get('alertType')
        alert_type_bucket = dictionary.get('alertTypeBucket')
        cluster_id = dictionary.get('clusterId')
        cluster_name = dictionary.get('clusterName')
        dedup_count = dictionary.get('dedupCount')
        dedup_timestamps = dictionary.get("dedupTimestamps")
        event_source = dictionary.get('eventSource')
        first_timestamp_usecs = dictionary.get('firstTimestampUsecs')
        id = dictionary.get('id')
        latest_timestamp_usecs = dictionary.get('latestTimestampUsecs')
        property_list = None
        if dictionary.get('propertyList') != None:
            property_list = list()
            for structure in dictionary.get('propertyList'):
                property_list.append(cohesity_management_sdk.models.alert_property.AlertProperty.from_dictionary(structure))
        region_id = dictionary.get('regionId')
        resolution_details = cohesity_management_sdk.models.alert_resolution_details.AlertResolutionDetails.from_dictionary(dictionary.get('resolutionDetails')) if dictionary.get('resolutionDetails') else None
        resolved_timestamp_usecs = dictionary.get('resolvedTimestampUsecs')
        severity = dictionary.get('severity')
        suppression_id = dictionary.get('suppressionId')
        tenant_ids = dictionary.get("tenantIds")

        # Return an object of this model
        return cls(
            alert_category,
            alert_code,
            alert_document,
            alert_state,
            alert_type,
            alert_type_bucket,
            cluster_id,
            cluster_name,
            dedup_count,
            dedup_timestamps,
            event_source,
            first_timestamp_usecs,
            id,
            latest_timestamp_usecs,
            property_list,
            region_id,
            resolution_details,
            resolved_timestamp_usecs,
            severity,
            suppression_id,
            tenant_ids
)