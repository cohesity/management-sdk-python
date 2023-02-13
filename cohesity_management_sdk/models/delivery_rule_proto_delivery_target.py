# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DeliveryRuleProtoDeliveryTarget(object):

    """Implementation of the 'DeliveryRuleProto_DeliveryTarget' model.

    Delivery targets for the notifications. For now only email delivery is
    supported. In future, we can potentially add other delivery targets such
    as paging, SMS, etc.

    Attributes:
        email_address (string): List of email addresses to send
            notifications.
        email_recipient_type (int): TODO: Type description here.
        external_api_curl_options (string): Specifies the curl options used to
            invoke above rest external api.
        external_api_url (string): Specifies the external api to be invoked
            when an alert matching this rule is raised.
        locale (string): Locale for the delivery target.
        snmp_notification (bool): Need to send snmp notification for matched
            alerts.
        syslog_notification (bool): Need to write syslog for matched alerts.
        tenant_id (string): Tenant who has been assigned this target. This
            field is not populated within AlertsDataProto persisted in
            Gandalf. This is a convenience field and is populated on the fly
            by the Alerts component for delivery targets in the
            delivery_target_list within AlertProto. This field is utilized by
            NotificationDeliveryHelper to group delivery targets so that we
            could send out a single email to all the email addresses
            registered with the same locale by a given tenant or by the SP
            admin. Another approach could have been to use an internal object,
            but since the AlertProto contains a list of type DeliveryTarget,
            this field has been added to make it convenient to pass around an
            AlertProto object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email_address":'emailAddress',
        "email_recipient_type":'emailRecipientType',
        "external_api_curl_options":'externalApiCurlOptions',
        "external_api_url":'externalApiUrl',
        "locale":'locale',
        "snmp_notification":'snmpNotification',
        "syslog_notification":'syslogNotification',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 email_address=None,
                 email_recipient_type=None,
                 external_api_curl_options=None,
                 external_api_url=None,
                 locale=None,
                 snmp_notification=None,
                 syslog_notification=None,
                 tenant_id=None):
        """Constructor for the DeliveryRuleProtoDeliveryTarget class"""

        # Initialize members of the class
        self.email_address = email_address
        self.email_recipient_type = email_recipient_type
        self.external_api_curl_options = external_api_curl_options
        self.external_api_url = external_api_url
        self.locale = locale
        self.snmp_notification = snmp_notification
        self.syslog_notification = syslog_notification
        self.tenant_id = tenant_id


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
        email_address = dictionary.get('emailAddress')
        email_recipient_type = dictionary.get('emailRecipientType')
        external_api_curl_options = dictionary.get('externalApiCurlOptions')
        external_api_url = dictionary.get('externalApiUrl')
        locale = dictionary.get('locale')
        snmp_notification = dictionary.get('snmpNotification', None)
        syslog_notification = dictionary.get('syslogNotification', None)
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(email_address,
                   email_recipient_type,
                   external_api_curl_options,
                   external_api_url,
                   locale,
                   snmp_notification,
                   syslog_notification,
                   tenant_id)


