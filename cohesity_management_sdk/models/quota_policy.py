# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class QuotaPolicy(object):

    """Implementation of the 'QuotaPolicy' model.

    Specifies a quota limit that can be optionally applied to Views and
    View Boxes.
    At the View level, this quota defines a logical limit for usage on the
    View.
    At the View Box level, this quota defines a physical limit or
    a default logical View limit.
    If a physical quota is specified for View Box, this quota defines a
    physical
    limit for the usage on the View Box.
    If a default logical View quota is specified for View Box, this limit
    is inherited by all the Views in that View Box.
    However, this inherited quota can be overwritten at the View level.
    A new write is not allowed if the resource will exceed the specified
    quota.
    However, it takes time for the Cohesity Cluster to calculate
    the usage across Nodes, so the limit may be exceeded by a small amount.
    In addition, if the limit is increased or data is removed,
    there may be a delay before the Cohesity Cluster allows more data
    to be written to the resource, as the Cluster calculates the usage
    across Nodes.

    Attributes:
        alert_limit_bytes (long|int): Specifies if an alert should be
            triggered when the usage of this resource exceeds this quota
            limit. This limit is optional and is specified in bytes. If no
            value is specified, there is no limit.
        alert_threshold_percentage (long|int): Supported only for user quota
            policy. Specifies when the usage goes above an alert threshold
            percentage which is: HardLimitBytes * AlertThresholdPercentage,
            eg: 80% of HardLimitBytes Can only be set if HardLimitBytes is
            set. Cannot be set if AlertLimitBytes is already set.
        hard_limit_bytes (long|int): Specifies an optional quota limit on the
            usage allowed for this resource. This limit is specified in bytes.
            If no value is specified, there is no limit.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alert_limit_bytes":'alertLimitBytes',
        "alert_threshold_percentage":'alertThresholdPercentage',
        "hard_limit_bytes":'hardLimitBytes'
    }

    def __init__(self,
                 alert_limit_bytes=None,
                 alert_threshold_percentage=None,
                 hard_limit_bytes=None):
        """Constructor for the QuotaPolicy class"""

        # Initialize members of the class
        self.alert_limit_bytes = alert_limit_bytes
        self.alert_threshold_percentage = alert_threshold_percentage
        self.hard_limit_bytes = hard_limit_bytes


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
        alert_limit_bytes = dictionary.get('alertLimitBytes')
        alert_threshold_percentage = dictionary.get('alertThresholdPercentage')
        hard_limit_bytes = dictionary.get('hardLimitBytes')

        # Return an object of this model
        return cls(alert_limit_bytes,
                   alert_threshold_percentage,
                   hard_limit_bytes)


