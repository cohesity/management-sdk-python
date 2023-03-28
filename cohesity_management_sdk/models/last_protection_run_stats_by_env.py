# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class LastProtectionRunStatsByEnv(object):

    """Implementation of the 'LastProtectionRunStatsByEnv' model.

    Specifies the last Protection Run stats by env.


    Attributes:

        environment (EnvironmentLastProtectionRunStatsByEnvEnum): Specifies the
            environment.
        num_objects_failed (long|int): Specifies the count of objects that
            failed last Protection Run.
        num_objects_failed_sla (long|int): Specifies the count of objects that
            failed sla in the last Run.
        num_objects_met_sla (long|int): Specifies the count of objects that met
            sla in the last Run.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "environment":'environment',
        "num_objects_failed":'numObjectsFailed',
        "num_objects_failed_sla":'numObjectsFailedSla',
        "num_objects_met_sla":'numObjectsMetSla',
    }
    def __init__(self,
                 environment=None,
                 num_objects_failed=None,
                 num_objects_failed_sla=None,
                 num_objects_met_sla=None,
            ):

        """Constructor for the LastProtectionRunStatsByEnv class"""

        # Initialize members of the class
        self.environment = environment
        self.num_objects_failed = num_objects_failed
        self.num_objects_failed_sla = num_objects_failed_sla
        self.num_objects_met_sla = num_objects_met_sla

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
        environment = dictionary.get('environment')
        num_objects_failed = dictionary.get('numObjectsFailed')
        num_objects_failed_sla = dictionary.get('numObjectsFailedSla')
        num_objects_met_sla = dictionary.get('numObjectsMetSla')

        # Return an object of this model
        return cls(
            environment,
            num_objects_failed,
            num_objects_failed_sla,
            num_objects_met_sla
)