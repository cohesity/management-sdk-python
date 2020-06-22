# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.email_delivery_target
import cohesity_management_sdk.models.web_hook_delivery_target

class NotificationRule(object):

    """Implementation of the 'NotificationRule' model.

    Specifies a rule to notify delivery targets such as sending emails,
    invoking an external api etc based on the alert type, category and
    severity of the generated alert.

    Attributes:
        alert_type_list (list of int): Specifies alert types this rule is
            applicable to.
        categories (list of CategoryNotificationRuleEnum): Specifies alert
            categories this rule is applicable to. Specifies the category of
            an Alert. kDisk - Alerts that are related to Disk. kNode - Alerts
            that are related to Node. kCluster - Alerts that are related to
            Cluster. kNodeHealth - Alerts that are related to Node Health.
            kClusterHealth - Alerts that are related to Cluster Health.
            kBackupRestore - Alerts that are related to Backup/Restore.
            kEncryption - Alerts that are related to Encryption.
            kArchivalRestore - Alerts that are related to Archival/Restore.
            kRemoteReplication - Alerts that are related to Remote
            Replication. kQuota - Alerts that are related to Quota. kLicense -
            Alerts that are related to License. kHeliosProActiveWellness -
            Alerts that are related to Helios ProActive Wellness.
            kHeliosAnalyticsJobs - Alerts that are related to Helios Analytics
            Jobs. kHeliosSignatureJobs - Alerts that are related to Helios
            Signature Jobs. kSecurity - Alerts that are related to Security.
        email_delivery_targets (list of EmailDeliveryTarget): Specifies email
            addresses to be notified when an alert matching this rule is
            generated.
        rule_id (long|int): Specifies id of the alert delivery rule.
        rule_name (string): Specifies name of the alert delivery rule.
        severities (list of SeverityNotificationRuleEnum): Specifies alert
            severity types this rule is applicable to. Specifies the severity
            level of an Alert. kCritical - Alerts whose severity type is
            Critical. kWarning - Alerts whose severity type is Warning. kInfo
            - Alerts whose severity type is Info.
        snmp_enabled (bool): Specifies whether SNMP notification to be invoked
            when an alert matching this rule is generated.
        syslog_enabled (bool): Specifies whether syslog notification to be
            invoked when an alert matching this rule is generated.
        tenant_id (string): Specifies tenant id this rule is applicable to.
        web_hook_delivery_targets (list of WebHookDeliveryTarget): Specifies
            external api urls to be invoked when an alert matching this rule
            is generated.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alert_type_list":'alertTypeList',
        "categories":'categories',
        "email_delivery_targets":'emailDeliveryTargets',
        "rule_id":'ruleId',
        "rule_name":'ruleName',
        "severities":'severities',
        "snmp_enabled":'snmpEnabled',
        "syslog_enabled":'syslogEnabled',
        "tenant_id":'tenantId',
        "web_hook_delivery_targets":'webHookDeliveryTargets'
    }

    def __init__(self,
                 alert_type_list=None,
                 categories=None,
                 email_delivery_targets=None,
                 rule_id=None,
                 rule_name=None,
                 severities=None,
                 snmp_enabled=None,
                 syslog_enabled=None,
                 tenant_id=None,
                 web_hook_delivery_targets=None):
        """Constructor for the NotificationRule class"""

        # Initialize members of the class
        self.alert_type_list = alert_type_list
        self.categories = categories
        self.email_delivery_targets = email_delivery_targets
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.severities = severities
        self.snmp_enabled = snmp_enabled
        self.syslog_enabled = syslog_enabled
        self.tenant_id = tenant_id
        self.web_hook_delivery_targets = web_hook_delivery_targets


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
        alert_type_list = dictionary.get('alertTypeList')
        categories = dictionary.get('categories')
        email_delivery_targets = None
        if dictionary.get('emailDeliveryTargets') != None:
            email_delivery_targets = list()
            for structure in dictionary.get('emailDeliveryTargets'):
                email_delivery_targets.append(cohesity_management_sdk.models.email_delivery_target.EmailDeliveryTarget.from_dictionary(structure))
        rule_id = dictionary.get('ruleId')
        rule_name = dictionary.get('ruleName')
        severities = dictionary.get('severities')
        snmp_enabled = dictionary.get('snmpEnabled')
        syslog_enabled = dictionary.get('syslogEnabled')
        tenant_id = dictionary.get('tenantId')
        web_hook_delivery_targets = None
        if dictionary.get('webHookDeliveryTargets') != None:
            web_hook_delivery_targets = list()
            for structure in dictionary.get('webHookDeliveryTargets'):
                web_hook_delivery_targets.append(cohesity_management_sdk.models.web_hook_delivery_target.WebHookDeliveryTarget.from_dictionary(structure))

        # Return an object of this model
        return cls(alert_type_list,
                   categories,
                   email_delivery_targets,
                   rule_id,
                   rule_name,
                   severities,
                   snmp_enabled,
                   syslog_enabled,
                   tenant_id,
                   web_hook_delivery_targets)


