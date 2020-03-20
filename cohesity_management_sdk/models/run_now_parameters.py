# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class RunNowParameters(object):

    """Implementation of the 'RunNowParameters' model.

    Specifies the parameters of a Run Now operation. A Run Now operation
    will try to backup the a source and/or its databases instantly.

    Attributes:
        database_ids (list of long|int): Specifies the ids of the DB's to
            perform run now on.
        source_id (long|int): Specifies the source id of the Databases to
            perform the Run Now operation on.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "database_ids":'databaseIds',
        "source_id":'sourceId'
    }

    def __init__(self,
                 database_ids=None,
                 source_id=None):
        """Constructor for the RunNowParameters class"""

        # Initialize members of the class
        self.database_ids = database_ids
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
        source_id = dictionary.get('sourceId')

        # Return an object of this model
        return cls(database_ids,
                   source_id)


