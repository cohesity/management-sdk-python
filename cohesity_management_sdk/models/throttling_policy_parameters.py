# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.latency_thresholds
import cohesity_management_sdk.models.nas_source_throttling_params

class ThrottlingPolicyParameters(object):

    """Implementation of the 'ThrottlingPolicyParameters' model.

    Specifies the throttling policy for a registered Protection Source.

    Attributes:
        enforce_max_streams (bool): Specifies whether datastore streams are
            configured for all datastores that are part of the registered
            entity. If set to true, number of streams from Cohesity cluster to
            the registered entity will be limited to the value set for
            maxConcurrentStreams. If not set or set to false, there is no max
            limit for the number of concurrent streams.
        enforce_registered_source_max_backups (bool): Specifies whether no. of
            backups are configured for the registered entity. If set to true,
            number of backups made by Cohesity cluster in the registered
            entity will be limited to the value set for
            RegisteredSourceMaxConcurrentBackups. If not set or set to false,
            there is no max limit for the number of concurrent backups.
        is_enabled (bool): Indicates whether read operations to the
            datastores, which are part of the registered Protection Source,
            are throttled.
        latency_thresholds (LatencyThresholds): Specifies latency thresholds
            that trigger throttling for all datastores found in the registered
            Protection Source or specific to one datastore.
        max_concurrent_streams (int): Specifies the limit on the number of
            streams Cohesity cluster will make concurrently to the datastores
            of the registered entity. This limit is enforced only when the
            flag enforceMaxStreams is set to true.
        nas_source_params (NasSourceThrottlingParams): Specifies the NAS
            specific source throttling parameters during source registration
            of the source.
        registered_source_max_concurrent_backups (int): Specifies the limit on
            the number of backups Cohesity cluster will make concurrently to
            the registered entity. This limit is enforced only when the flag
            enforceRegisteredSourceMaxBackups is set to true.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enforce_max_streams":'enforceMaxStreams',
        "enforce_registered_source_max_backups":'enforceRegisteredSourceMaxBackups',
        "is_enabled":'isEnabled',
        "latency_thresholds":'latencyThresholds',
        "max_concurrent_streams":'maxConcurrentStreams',
        "nas_source_params":'nasSourceParams',
        "registered_source_max_concurrent_backups":'registeredSourceMaxConcurrentBackups'
    }

    def __init__(self,
                 enforce_max_streams=None,
                 enforce_registered_source_max_backups=None,
                 is_enabled=None,
                 latency_thresholds=None,
                 max_concurrent_streams=None,
                 nas_source_params=None,
                 registered_source_max_concurrent_backups=None):
        """Constructor for the ThrottlingPolicyParameters class"""

        # Initialize members of the class
        self.enforce_max_streams = enforce_max_streams
        self.enforce_registered_source_max_backups = enforce_registered_source_max_backups
        self.is_enabled = is_enabled
        self.latency_thresholds = latency_thresholds
        self.max_concurrent_streams = max_concurrent_streams
        self.nas_source_params = nas_source_params
        self.registered_source_max_concurrent_backups = registered_source_max_concurrent_backups


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
        enforce_max_streams = dictionary.get('enforceMaxStreams')
        enforce_registered_source_max_backups = dictionary.get('enforceRegisteredSourceMaxBackups')
        is_enabled = dictionary.get('isEnabled')
        latency_thresholds = cohesity_management_sdk.models.latency_thresholds.LatencyThresholds.from_dictionary(dictionary.get('latencyThresholds')) if dictionary.get('latencyThresholds') else None
        max_concurrent_streams = dictionary.get('maxConcurrentStreams')
        nas_source_params = cohesity_management_sdk.models.nas_source_throttling_params.NasSourceThrottlingParams.from_dictionary(dictionary.get('nasSourceParams')) if dictionary.get('nasSourceParams') else None
        registered_source_max_concurrent_backups = dictionary.get('registeredSourceMaxConcurrentBackups')

        # Return an object of this model
        return cls(enforce_max_streams,
                   enforce_registered_source_max_backups,
                   is_enabled,
                   latency_thresholds,
                   max_concurrent_streams,
                   nas_source_params,
                   registered_source_max_concurrent_backups)


