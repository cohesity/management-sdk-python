# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.alert_document

class AlertMetadata(object):

    """Implementation of the 'AlertMetadata' model.

    AlertMetadata specifies metadata for a given alert type. All the alerts of
    a
    given alert type share the same metadata.

    Attributes:
        alert_document_list (list of AlertDocument): Specifies alert
            documentation one per each language supported.
        alert_type_bucket (AlertTypeBucketEnum): Specifies the Alert type
            bucket. Specifies the Alert type bucket. kSoftware - Alerts which
            are related to Cohesity services. kHardware - Alerts related to
            hardware on which Cohesity software is running. kService - Alerts
            related to other external services. kOther - Alerts not of one of
            above categories.
        alert_type_id (int): Specifies unique id for the alert type.
        category (CategoryAlertMetadataEnum): Specifies category of the alert
            type. Specifies the category of an Alert. kDisk - Alerts that are
            related to Disk. kNode - Alerts that are related to Node. kCluster
            - Alerts that are related to Cluster. kNodeHealth - Alerts that
            are related to Node Health. kClusterHealth - Alerts that are
            related to Cluster Health. kBackupRestore - Alerts that are
            related to Backup/Restore. kEncryption - Alerts that are related
            to Encryption. kArchivalRestore - Alerts that are related to
            Archival/Restore. kRemoteReplication - Alerts that are related to
            Remote Replication. kQuota - Alerts that are related to Quota.
            kLicense - Alerts that are related to License.
            kHeliosProActiveWellness - Alerts that are related to Helios
            ProActive Wellness. kHeliosAnalyticsJobs - Alerts that are related
            to Helios Analytics Jobs. kHeliosSignatureJobs - Alerts that are
            related to Helios Signature Jobs. kSecurity - Alerts that are
            related to Security. kAppsInfra - Alerts that are related to
            applications infra. kAntivirus - Alerts that are related to
            antivirus. kArchivalCopy - Alerts that are related to archival
            copies.
        dedup_interval_seconds (int): Specifies dedup interval in seconds. If
            the same alert is raised multiple times by any client in this
            duration, only one of them will be reported.
        dedup_until_resolved (bool): Specifies if the alerts are to be deduped
            until the current one (if any) is resolved.
        hide_alert_from_user (bool): Specifies whether to show the alert in
            the iris UI and CLI.
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
        syslog_notification (bool): Specifies whether an syslog notification
            is sent when an alert is raised.
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
        "version":'version'
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
                 version=None):
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
        primary_key_list = dictionary.get('primaryKeyList')
        property_list = dictionary.get('propertyList')
        send_support_notification = dictionary.get('sendSupportNotification')
        snmp_notification = dictionary.get('snmpNotification')
        syslog_notification = dictionary.get('syslogNotification')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(alert_document_list,
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
                   version)


