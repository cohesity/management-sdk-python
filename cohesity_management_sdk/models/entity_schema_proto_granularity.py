# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class EntitySchemaProto_Granularity(object):

    """Implementation of the 'EntitySchemaProto_Granularity' model.

    Rolling up or Down sampling is performed on timeseries data to reduce
    space usage by timeseries. Rollup Granularity is defined per entity
    schema but rollup function is not defined. Instead we create rolledup
    values for all the rollup functions.

    Attributes:
        rollup_interval_secs (int): Defines the rollup interval or a bucket
            size. All data points within one time bucket are rolled up to one
            summary data point using the defined rollup function. For example,
            say, raw metric is published at ~30 secs granularity. To generate
            a hourly or a daily summary time series, client can define rolled
            up metrics having interval 3600 secs and 86400 secs respectively.
        time_to_live_secs (int): Defines the duration for which the rolled up
            data is to be stored. Once the lifespan has elapsed, expired data
            is garbage collected.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rollup_interval_secs":'rollupIntervalSecs',
        "time_to_live_secs":'timeToLiveSecs'
    }

    def __init__(self,
                 rollup_interval_secs=None,
                 time_to_live_secs=None):
        """Constructor for the EntitySchemaProto_Granularity class"""

        # Initialize members of the class
        self.rollup_interval_secs = rollup_interval_secs
        self.time_to_live_secs = time_to_live_secs


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
        rollup_interval_secs = dictionary.get('rollupIntervalSecs', None)
        time_to_live_secs = dictionary.get('timeToLiveSecs', None)
        # Return an object of this model
        return cls(rollup_interval_secs,
                   time_to_live_secs)


