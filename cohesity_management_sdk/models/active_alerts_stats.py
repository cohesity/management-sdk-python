# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class ActiveAlertsStats(object):

    """Implementation of the 'ActiveAlertsStats' model.

    Specifies the active alert statistics details.

    Attributes:
        num_critical_alerts (long|int): Specifies the count of active critical
            Alerts.
        num_hardware_alerts (long|int): Specifies the count of active hardware
            Alerts.
        num_hardware_critical_alerts (long|int): Specifies the count of active
            hardware critical Alerts.
        num_hardware_info_alerts (long|int): Specifies the count of active
            hardware info Alerts.
        num_hardware_warning_alerts (long|int): Specifies the count of active
            hardware warning Alerts.
        num_info_alerts (long|int): Specifies the count of active info
            Alerts.
        num_service_alerts (long|int): Specifies the count of active service
            Alerts.
        num_service_critical_alerts (long|int): Specifies the count of active
            service critical Alerts.
        num_service_info_alerts (long|int): Specifies the count of active
            service info Alerts.
        num_service_warning_alerts (long|int): Specifies the count of active
            service warning Alerts.
        num_software_alerts (long|int): Specifies the count of active software
            Alerts.
        num_software_critical_alerts (long|int): Specifies the count of active
            software critical Alerts.
        num_software_info_alerts (long|int): Specifies the count of active
            software info Alerts.
        num_software_warning_alerts (long|int): Specifies the count of active
            software warning Alerts.
        num_warning_alerts (long|int): Specifies the count of active warning
            Alerts.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_critical_alerts":'numCriticalAlerts',
        "num_hardware_alerts":'numHardwareAlerts',
        "num_hardware_critical_alerts":'numHardwareCriticalAlerts',
        "num_hardware_info_alerts":'numHardwareInfoAlerts',
        "num_hardware_warning_alerts":'numHardwareWarningAlerts',
        "num_info_alerts":'numInfoAlerts',
        "num_service_alerts":'numServiceAlerts',
        "num_service_critical_alerts":'numServiceCriticalAlerts',
        "num_service_info_alerts":'numServiceInfoAlerts',
        "num_service_warning_alerts":'numServiceWarningAlerts',
        "num_software_alerts":'numSoftwareAlerts',
        "num_software_critical_alerts":'numSoftwareCriticalAlerts',
        "num_software_info_alerts":'numSoftwareInfoAlerts',
        "num_software_warning_alerts":'numSoftwareWarningAlerts',
        "num_warning_alerts":'numWarningAlerts'
    }

    def __init__(self,
                 num_critical_alerts=None,
                 num_hardware_alerts=None,
                 num_hardware_critical_alerts=None,
                 num_hardware_info_alerts=None,
                 num_hardware_warning_alerts=None,
                 num_info_alerts=None,
                 num_service_alerts=None,
                 num_service_critical_alerts=None,
                 num_service_info_alerts=None,
                 num_service_warning_alerts=None,
                 num_software_alerts=None,
                 num_software_critical_alerts=None,
                 num_software_info_alerts=None,
                 num_software_warning_alerts=None,
                 num_warning_alerts=None):
        """Constructor for the ActiveAlertsStats class"""

        # Initialize members of the class
        self.num_critical_alerts = num_critical_alerts
        self.num_hardware_alerts = num_hardware_alerts
        self.num_hardware_critical_alerts = num_hardware_critical_alerts
        self.num_hardware_info_alerts = num_hardware_info_alerts
        self.num_hardware_warning_alerts = num_hardware_warning_alerts
        self.num_info_alerts = num_info_alerts
        self.num_service_alerts = num_service_alerts
        self.num_service_critical_alerts = num_service_critical_alerts
        self.num_service_info_alerts = num_service_info_alerts
        self.num_service_warning_alerts = num_service_warning_alerts
        self.num_software_alerts = num_software_alerts
        self.num_software_critical_alerts = num_software_critical_alerts
        self.num_software_info_alerts = num_software_info_alerts
        self.num_software_warning_alerts = num_software_warning_alerts
        self.num_warning_alerts = num_warning_alerts


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
        num_critical_alerts = dictionary.get('numCriticalAlerts')
        num_hardware_alerts = dictionary.get('numHardwareAlerts')
        num_hardware_critical_alerts = dictionary.get('numHardwareCriticalAlerts')
        num_hardware_info_alerts = dictionary.get('numHardwareInfoAlerts')
        num_hardware_warning_alerts = dictionary.get('numHardwareWarningAlerts')
        num_info_alerts = dictionary.get('numInfoAlerts')
        num_service_alerts = dictionary.get('numServiceAlerts')
        num_service_critical_alerts = dictionary.get('numServiceCriticalAlerts')
        num_service_info_alerts = dictionary.get('numServiceInfoAlerts')
        num_service_warning_alerts = dictionary.get('numServiceWarningAlerts')
        num_software_alerts = dictionary.get('numSoftwareAlerts')
        num_software_critical_alerts = dictionary.get('numSoftwareCriticalAlerts')
        num_software_info_alerts = dictionary.get('numSoftwareInfoAlerts')
        num_software_warning_alerts = dictionary.get('numSoftwareWarningAlerts')
        num_warning_alerts = dictionary.get('numWarningAlerts')

        # Return an object of this model
        return cls(num_critical_alerts,
                   num_hardware_alerts,
                   num_hardware_critical_alerts,
                   num_hardware_info_alerts,
                   num_hardware_warning_alerts,
                   num_info_alerts,
                   num_service_alerts,
                   num_service_critical_alerts,
                   num_service_info_alerts,
                   num_service_warning_alerts,
                   num_software_alerts,
                   num_software_critical_alerts,
                   num_software_info_alerts,
                   num_software_warning_alerts,
                   num_warning_alerts)


