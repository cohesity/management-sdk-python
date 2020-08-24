# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class OracleEnvJobParameters(object):

    """Implementation of the 'OracleEnvJobParameters' model.

    Specifies job parameters applicable for all 'kOracle' Environment type
    Protection Sources in a Protection Job.

    Attributes:
    persist_mountpoints (bool): Specifies whether the mountpoints created while
        backing up Oracle DBs should be persisted.
        Note: This parameter is for the entire Job. For overriding persistence
        of mountpoints for a subset of Oracle hosts within the job, refer
        OracleSourceParams.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "persist_mountpoints": 'persistMountpoints'
    }

    def __init__(self,
                 persist_mountpoints=None):
        """Constructor for the OracleEnvJobParameters class"""

        # Initialize members of the class
        self.persist_mountpoints = persist_mountpoints


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
        persist_mountpoints = dictionary.get('persistMountpoints')

        # Return an object of this model
        return cls(persist_mountpoints)


