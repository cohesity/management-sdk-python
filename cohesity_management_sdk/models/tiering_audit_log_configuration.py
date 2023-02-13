# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TieringAuditLogConfiguration(object):

    """Implementation of the 'TieringAuditLogConfiguration' model.

    Specifies the settings of the tiering audit log configuration.

    Attributes:
        enabled (bool): Specifies if tiering audit logging is enabled on the
            Cohesity Cluster.
            If 'true', NAS tiering audit logging is enabled. Otherwise, it is
            disabled.
        retention_period_days (int): Specifies the number of days to keep
            (retain) the tiering audit logs. Audit logs generated before the
            period of time specified by retentionPeriodDays are removed from
            the Cohesity Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": 'enabled',
        "retention_period_days": 'retentionPeriodDays'
    }

    def __init__(self,
                 enabled=None,
                 retention_period_days=None):
        """Constructor for the TieringAuditLogConfiguration class"""

        # Initialize members of the class
        self.enabled = enabled
        self.retention_period_days = retention_period_days


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
        enabled = dictionary.get('enabled', None)
        retention_period_days = dictionary.get('retentionPeriodDays', None)

        # Return an object of this model
        return cls(enabled,
                   retention_period_days)


