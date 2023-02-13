# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.alert_resolution_details

class AlertResolution(object):

    """Implementation of the 'AlertResolution' model.

    Provides Resolution details and the list of Alerts resolved by a
    Resolution,
    which are specified by Alert Ids.

    Attributes:
        alert_id_list (list of string): Specifies list of Alerts resolved by a
            Resolution, which are specified by Alert Ids.
        resolution_details (AlertResolutionDetails): Specifies information
            about the Alert Resolution such as a summary, id assigned by the
            Cohesity Cluster, user who resolved the Alerts, etc.
        tenant_ids (list of string): Specifies unique tenantIds of the alert
            contained in this resolution.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alert_id_list":'alertIdList',
        "resolution_details":'resolutionDetails',
        "tenant_ids":'tenantIds'
    }

    def __init__(self,
                 alert_id_list=None,
                 resolution_details=None,
                 tenant_ids=None):
        """Constructor for the AlertResolution class"""

        # Initialize members of the class
        self.alert_id_list = alert_id_list
        self.resolution_details = resolution_details
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
        alert_id_list = dictionary.get('alertIdList')
        resolution_details = cohesity_management_sdk.models.alert_resolution_details.AlertResolutionDetails.from_dictionary(dictionary.get('resolutionDetails')) if dictionary.get('resolutionDetails') else None
        tenant_ids = dictionary.get('tenantIds')

        # Return an object of this model
        return cls(alert_id_list,
                   resolution_details,
                   tenant_ids)


