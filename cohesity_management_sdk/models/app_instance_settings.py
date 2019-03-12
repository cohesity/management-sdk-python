# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.view_privileges

class AppInstanceSettings(object):

    """Implementation of the 'App instance settings.' model.

    AppInstanceSettings provides settings used while launching an app
    instance.
    Current settings include QoSTier to be used for the instance and views
    allowed to be accessed by the instance.

    Attributes:
        qos_tier (QosTierEnum): Specifies QoSTier of the app instance.
            Specifies QoS Tier for an app instance. App instances are
            allocated resources such as memory, CPU and IO based on their QoS
            Tier. kLow - Low QoS Tier. kMedium - Medium QoS Tier. kHigh - High
            QoS Tier.
        read_view_privileges (ViewPrivileges): ViewPrivileges specifies which
            views are allowed to be accessed by an app instance.
        read_write_view_privileges (ViewPrivileges): ViewPrivileges specifies
            which views are allowed to be accessed by an app instance.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "qos_tier":'qosTier',
        "read_view_privileges":'readViewPrivileges',
        "read_write_view_privileges":'readWriteViewPrivileges'
    }

    def __init__(self,
                 qos_tier=None,
                 read_view_privileges=None,
                 read_write_view_privileges=None):
        """Constructor for the AppInstanceSettings class"""

        # Initialize members of the class
        self.qos_tier = qos_tier
        self.read_view_privileges = read_view_privileges
        self.read_write_view_privileges = read_write_view_privileges


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
        qos_tier = dictionary.get('qosTier')
        read_view_privileges = cohesity_management_sdk.models.view_privileges.ViewPrivileges.from_dictionary(dictionary.get('readViewPrivileges')) if dictionary.get('readViewPrivileges') else None
        read_write_view_privileges = cohesity_management_sdk.models.view_privileges.ViewPrivileges.from_dictionary(dictionary.get('readWriteViewPrivileges')) if dictionary.get('readWriteViewPrivileges') else None

        # Return an object of this model
        return cls(qos_tier,
                   read_view_privileges,
                   read_write_view_privileges)


