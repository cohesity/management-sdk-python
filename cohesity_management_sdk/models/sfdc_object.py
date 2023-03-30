# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SfdcObject(object):

    """Implementation of the 'SfdcObject' model.

    Specifies an Object containing information about a Salseforce object.


    Attributes:

        object_type (ObjectTypeEnum): Type of this object Specifies the type of
            an Universal Data Adapter source entity. 'kStandard' indicates a
            Universal Data Adapter source, possibly distributed over several
            physical nodes. 'kCustom' indicates a generic object within the UDA
            environment.
        record_count (long|int): Number of records in this object.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "object_type":'objectType',
        "record_count":'recordCount',
    }
    def __init__(self,
                 object_type=None,
                 record_count=None,
            ):

        """Constructor for the SfdcObject class"""

        # Initialize members of the class
        self.object_type = object_type
        self.record_count = record_count

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
        object_type = dictionary.get('objectType')
        record_count = dictionary.get('recordCount')

        # Return an object of this model
        return cls(
            object_type,
            record_count
)