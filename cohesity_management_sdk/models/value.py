# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.value_data

class Value(object):

    """Implementation of the 'Value' model.

    Specifies a data type and data field used to store data.

    Attributes:
        data (ValueData): Specifies the fields to store data of a given type.
            Specify data in the appropriate field for the current data type.
        mtype (int): Specifies the type of value. 0 specifies a data point of
            type Int64. 1 specifies a data point of type Double. 2 specifies a
            data point of type String. 3 specifies a data point of type
            Bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data":'data',
        "mtype":'type'
    }

    def __init__(self,
                 data=None,
                 mtype=None):
        """Constructor for the Value class"""

        # Initialize members of the class
        self.data = data
        self.mtype = mtype


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
        data = cohesity_management_sdk.models.value_data.ValueData.from_dictionary(dictionary.get('data')) if dictionary.get('data') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(data,
                   mtype)


