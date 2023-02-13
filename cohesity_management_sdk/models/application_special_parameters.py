# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ApplicationSpecialParameters(object):

    """Implementation of the 'ApplicationSpecialParameters' model.

    Specifies additional special settings applicable for a Protection Source
    of 'kSQL'/'kOracle' type in a Protection Job.

    Attributes:
        application_entity_ids (list of long|int): Array of Ids of Application
            Entities like SQL/Oracle instances, and databases that should be
            protected in a Protection Source.  Specifies the subset of
            application entities like SQL/Oracle instances, and databases to
            protect in a Protection Source of type 'kSQL'/'kOracle'. If not
            specified, all application entities on the Protection Source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_entity_ids":'applicationEntityIds'
    }

    def __init__(self,
                 application_entity_ids=None):
        """Constructor for the ApplicationSpecialParameters class"""

        # Initialize members of the class
        self.application_entity_ids = application_entity_ids


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
        application_entity_ids = dictionary.get('applicationEntityIds')

        # Return an object of this model
        return cls(application_entity_ids)


