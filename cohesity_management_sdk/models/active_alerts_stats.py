# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ActiveAlertsStats(object):

    """Implementation of the 'ActiveAlertsStats' model.

    Specifies the active alert statistics details.


    Attributes:

        num_critical_alerts (long|int): Specifies the count of active critical
            Alerts excluding alerts that belong to other bucket.
        num_critical_alerts_categories (long|int): Specifies the count of
            active critical alerts categories.
        num_data_service_alerts (long|int): Specifies the count of active
            service Alerts.
        num_data_service_critical_alerts (long|int): Specifies the count of
            active service critical Alerts.
        num_data_service_info_alerts (long|int): Specifies the count of active
            service info Alerts.
        num_data_service_warning_alerts (long|int): Specifies the count of
            active service warning Alerts.
        num_hardware_alerts (long|int): Specifies the count of active hardware
            Alerts.
        num_hardware_critical_alerts (long|int): Specifies the count of active
            hardware critical Alerts.
        num_hardware_info_alerts (long|int): Specifies the count of active
            hardware info Alerts.
        num_hardware_warning_alerts (long|int): Specifies the count of active
            hardware warning Alerts.
        num_info_alerts (long|int): Specifies the count of active info Alerts
            excluding alerts that belong to other bucket.
        num_info_alerts_categories (long|int): Specifies the count of active
            info alerts categories.
        num_maintenance_alerts (long|int): Specifies the count of active Alerts
            of maintenance bucket
        num_maintenance_critical_alerts (long|int): Specifies the count of
            active other critical Alerts.
        num_maintenance_info_alerts (long|int): Specifies the count of active
            other info Alerts.
        num_maintenance_warning_alerts (long|int): Specifies the count of
            active other warning Alerts.
        num_software_alerts (long|int): Specifies the count of active software
            Alerts.
        num_software_critical_alerts (long|int): Specifies the count of active
            software critical Alerts.
        num_software_info_alerts (long|int): Specifies the count of active
            software info Alerts.
        num_software_warning_alerts (long|int): Specifies the count of active
            software warning Alerts.
        num_warning_alerts (long|int): Specifies the count of active warning
            Alerts excluding alerts that belong to other bucket.
        num_warning_alerts_categories (long|int): Specifies the count of active
            warning alerts categories.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "num_critical_alerts":'numCriticalAlerts',
        "num_critical_alerts_categories":'numCriticalAlertsCategories',
        "num_data_service_alerts":'numDataServiceAlerts',
        "num_data_service_critical_alerts":'numDataServiceCriticalAlerts',
        "num_data_service_info_alerts":'numDataServiceInfoAlerts',
        "num_data_service_warning_alerts":'numDataServiceWarningAlerts',
        "num_hardware_alerts":'numHardwareAlerts',
        "num_hardware_critical_alerts":'numHardwareCriticalAlerts',
        "num_hardware_info_alerts":'numHardwareInfoAlerts',
        "num_hardware_warning_alerts":'numHardwareWarningAlerts',
        "num_info_alerts":'numInfoAlerts',
        "num_info_alerts_categories":'numInfoAlertsCategories',
        "num_maintenance_alerts":'numMaintenanceAlerts',
        "num_maintenance_critical_alerts":'numMaintenanceCriticalAlerts',
        "num_maintenance_info_alerts":'numMaintenanceInfoAlerts',
        "num_maintenance_warning_alerts":'numMaintenanceWarningAlerts',
        "num_software_alerts":'numSoftwareAlerts',
        "num_software_critical_alerts":'numSoftwareCriticalAlerts',
        "num_software_info_alerts":'numSoftwareInfoAlerts',
        "num_software_warning_alerts":'numSoftwareWarningAlerts',
        "num_warning_alerts":'numWarningAlerts',
        "num_warning_alerts_categories":'numWarningAlertsCategories',
    }
    def __init__(self,
                 num_critical_alerts=None,
                 num_critical_alerts_categories=None,
                 num_data_service_alerts=None,
                 num_data_service_critical_alerts=None,
                 num_data_service_info_alerts=None,
                 num_data_service_warning_alerts=None,
                 num_hardware_alerts=None,
                 num_hardware_critical_alerts=None,
                 num_hardware_info_alerts=None,
                 num_hardware_warning_alerts=None,
                 num_info_alerts=None,
                 num_info_alerts_categories=None,
                 num_maintenance_alerts=None,
                 num_maintenance_critical_alerts=None,
                 num_maintenance_info_alerts=None,
                 num_maintenance_warning_alerts=None,
                 num_software_alerts=None,
                 num_software_critical_alerts=None,
                 num_software_info_alerts=None,
                 num_software_warning_alerts=None,
                 num_warning_alerts=None,
                 num_warning_alerts_categories=None,
            ):

        """Constructor for the ActiveAlertsStats class"""

        # Initialize members of the class
        self.num_critical_alerts = num_critical_alerts
        self.num_critical_alerts_categories = num_critical_alerts_categories
        self.num_data_service_alerts = num_data_service_alerts
        self.num_data_service_critical_alerts = num_data_service_critical_alerts
        self.num_data_service_info_alerts = num_data_service_info_alerts
        self.num_data_service_warning_alerts = num_data_service_warning_alerts
        self.num_hardware_alerts = num_hardware_alerts
        self.num_hardware_critical_alerts = num_hardware_critical_alerts
        self.num_hardware_info_alerts = num_hardware_info_alerts
        self.num_hardware_warning_alerts = num_hardware_warning_alerts
        self.num_info_alerts = num_info_alerts
        self.num_info_alerts_categories = num_info_alerts_categories
        self.num_maintenance_alerts = num_maintenance_alerts
        self.num_maintenance_critical_alerts = num_maintenance_critical_alerts
        self.num_maintenance_info_alerts = num_maintenance_info_alerts
        self.num_maintenance_warning_alerts = num_maintenance_warning_alerts
        self.num_software_alerts = num_software_alerts
        self.num_software_critical_alerts = num_software_critical_alerts
        self.num_software_info_alerts = num_software_info_alerts
        self.num_software_warning_alerts = num_software_warning_alerts
        self.num_warning_alerts = num_warning_alerts
        self.num_warning_alerts_categories = num_warning_alerts_categories

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
        num_critical_alerts_categories = dictionary.get('numCriticalAlertsCategories')
        num_data_service_alerts = dictionary.get('numDataServiceAlerts')
        num_data_service_critical_alerts = dictionary.get('numDataServiceCriticalAlerts')
        num_data_service_info_alerts = dictionary.get('numDataServiceInfoAlerts')
        num_data_service_warning_alerts = dictionary.get('numDataServiceWarningAlerts')
        num_hardware_alerts = dictionary.get('numHardwareAlerts')
        num_hardware_critical_alerts = dictionary.get('numHardwareCriticalAlerts')
        num_hardware_info_alerts = dictionary.get('numHardwareInfoAlerts')
        num_hardware_warning_alerts = dictionary.get('numHardwareWarningAlerts')
        num_info_alerts = dictionary.get('numInfoAlerts')
        num_info_alerts_categories = dictionary.get('numInfoAlertsCategories')
        num_maintenance_alerts = dictionary.get('numMaintenanceAlerts')
        num_maintenance_critical_alerts = dictionary.get('numMaintenanceCriticalAlerts')
        num_maintenance_info_alerts = dictionary.get('numMaintenanceInfoAlerts')
        num_maintenance_warning_alerts = dictionary.get('numMaintenanceWarningAlerts')
        num_software_alerts = dictionary.get('numSoftwareAlerts')
        num_software_critical_alerts = dictionary.get('numSoftwareCriticalAlerts')
        num_software_info_alerts = dictionary.get('numSoftwareInfoAlerts')
        num_software_warning_alerts = dictionary.get('numSoftwareWarningAlerts')
        num_warning_alerts = dictionary.get('numWarningAlerts')
        num_warning_alerts_categories = dictionary.get('numWarningAlertsCategories')

        # Return an object of this model
        return cls(
            num_critical_alerts,
            num_critical_alerts_categories,
            num_data_service_alerts,
            num_data_service_critical_alerts,
            num_data_service_info_alerts,
            num_data_service_warning_alerts,
            num_hardware_alerts,
            num_hardware_critical_alerts,
            num_hardware_info_alerts,
            num_hardware_warning_alerts,
            num_info_alerts,
            num_info_alerts_categories,
            num_maintenance_alerts,
            num_maintenance_critical_alerts,
            num_maintenance_info_alerts,
            num_maintenance_warning_alerts,
            num_software_alerts,
            num_software_critical_alerts,
            num_software_info_alerts,
            num_software_warning_alerts,
            num_warning_alerts,
            num_warning_alerts_categories
)