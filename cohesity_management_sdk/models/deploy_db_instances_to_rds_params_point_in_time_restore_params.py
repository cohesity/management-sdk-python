# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DeployDBInstancesToRDSParamsPointInTimeRestoreParams(object):

    """Implementation of the 'DeployDBInstancesToRDSParams_PointInTimeRestoreParams' model.

    Message to capture details of a point in time that the DB needs to be
    restored to.

    Attributes:
        timestamp_msecs (long|int): Time in milliseconds since epoch that the
            DB needs to be restored to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "timestamp_msecs":'timestampMsecs'
    }

    def __init__(self,
                 timestamp_msecs=None):
        """Constructor for the DeployDBInstancesToRDSParamsPointInTimeRestoreParams class"""

        # Initialize members of the class
        self.timestamp_msecs = timestamp_msecs


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
        timestamp_msecs = dictionary.get('timestampMsecs')

        # Return an object of this model
        return cls(timestamp_msecs)


