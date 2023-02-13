# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.run_now_physical_parameters

class RunNowParameters(object):

    """Implementation of the 'RunNowParameters' model.

    Specifies the parameters of a Run Now operation. A Run Now operation
    will try to backup the a source and/or its databases instantly.

    Attributes:
        database_ids (list of long|int): Specifies the ids of the DB's to
            perform run now on.
        physical_params (RunNowPhysicalParameters): Specifies optional
            physical parameters for a specific source id.
        source_id (long|int): Specifies the source id of the Databases to
            perform the Run Now operation on.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "database_ids":'databaseIds',
        "physical_params":'physicalParams',
        "source_id":'sourceId'
    }

    def __init__(self,
                 database_ids=None,
                 physical_params=None,
                 source_id=None):
        """Constructor for the RunNowParameters class"""

        # Initialize members of the class
        self.database_ids = database_ids
        self.physical_params = physical_params
        self.source_id = source_id


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
        database_ids = dictionary.get('databaseIds')
        physical_params = cohesity_management_sdk.models.run_now_physical_parameters.RunNowPhysicalParameters.from_dictionary(dictionary.get('physicalParams')) if dictionary.get('physicalParams') else None
        source_id = dictionary.get('sourceId')

        # Return an object of this model
        return cls(database_ids,
                   physical_params,
                   source_id)


