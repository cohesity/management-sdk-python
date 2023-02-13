# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.alerting_config
import cohesity_management_sdk.models.environment_type_job_parameters
import cohesity_management_sdk.models.indexing_policy

class RpoPolicySettings(object):

    """Implementation of the 'RpoPolicySettings' model.

    Specifies all the additional settings that are applicable only
    to an RPO policy. This can include storage domain, settings of different
    environments, etc.

    Attributes:
        alerting_config (AlertingConfig): Specifies optional settings for
            alerting.
        alerting_policy (list of AlertingPolicyEnum): Array of Job Events.
            During Job Runs, the following Job Events are generated: 1) Job
            succeeds 2) Job fails 3) Job violates the SLA These Job Events can
            cause Alerts to be generated. 'kSuccess' means the Protection Job
            succeeded. 'kFailure' means the Protection Job failed.
            'kSlaViolation' means the Protection Job took longer than the time
            period specified in the SLA.
        environment_type_job_params (EnvironmentTypeJobParameters): Specifies
            additional parameters that are common to all Protection Sources in
            a Protection Job created for a particular environment type.
        indexing_policy (IndexingPolicy): Specifies settings for indexing
            files found in an Object (such as a VM) so these files can be
            searched and recovered. This also specifies inclusion and
            exclusion rules that determine the directories to index.
        qos_type (QosTypeRpoPolicySettingsEnum): Specifies the QoS policy type
            to use. 'kBackupHDD' indicates the Cohesity Cluster writes data
            directly to the HDD tier for this Protection Job. This is the
            recommended setting. 'kBackupSSD' indicates the Cohesity Cluster
            writes data directly to the SSD tier for this Protection Job. Only
            specify this policy if you need fast ingest speed for a small
            number of Protection Jobs.
        storage_domain_id (long|int): Specifies the Storage Domain to which
            data will be written.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alerting_config":'alertingConfig',
        "alerting_policy":'alertingPolicy',
        "environment_type_job_params":'environmentTypeJobParams',
        "indexing_policy":'indexingPolicy',
        "qos_type":'qosType',
        "storage_domain_id":'storageDomainId'
    }

    def __init__(self,
                 alerting_config=None,
                 alerting_policy=None,
                 environment_type_job_params=None,
                 indexing_policy=None,
                 qos_type=None,
                 storage_domain_id=None):
        """Constructor for the RpoPolicySettings class"""

        # Initialize members of the class
        self.alerting_config = alerting_config
        self.alerting_policy = alerting_policy
        self.environment_type_job_params = environment_type_job_params
        self.indexing_policy = indexing_policy
        self.qos_type = qos_type
        self.storage_domain_id = storage_domain_id


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
        alerting_config = cohesity_management_sdk.models.alerting_config.AlertingConfig.from_dictionary(dictionary.get('alertingConfig')) if dictionary.get('alertingConfig') else None
        alerting_policy = dictionary.get('alertingPolicy')
        environment_type_job_params = cohesity_management_sdk.models.environment_type_job_parameters.EnvironmentTypeJobParameters.from_dictionary(dictionary.get('environmentTypeJobParams')) if dictionary.get('environmentTypeJobParams') else None
        indexing_policy = cohesity_management_sdk.models.indexing_policy.IndexingPolicy.from_dictionary(dictionary.get('indexingPolicy')) if dictionary.get('indexingPolicy') else None
        qos_type = dictionary.get('qosType')
        storage_domain_id = dictionary.get('storageDomainId')

        # Return an object of this model
        return cls(alerting_config,
                   alerting_policy,
                   environment_type_job_params,
                   indexing_policy,
                   qos_type,
                   storage_domain_id)


