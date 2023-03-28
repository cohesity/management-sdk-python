# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.date_time


class GranularityBucket_ExactDatesInfo(object):

    """Implementation of the 'GranularityBucket_ExactDatesInfo' model.

    TODO: type description here.


    Attributes:

        dates_vec (list of DateTime): TODO: Type description here.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "dates_vec":'datesVec',
    }
    def __init__(self,
                 dates_vec=None,
            ):

        """Constructor for the GranularityBucket_ExactDatesInfo class"""

        # Initialize members of the class
        self.dates_vec = dates_vec

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
        dates_vec = None
        if dictionary.get('datesVec') != None:
            dates_vec = list()
            for structure in dictionary.get('datesVec'):
                dates_vec.append(cohesity_management_sdk.models.date_time.DateTime.from_dictionary(structure))

        # Return an object of this model
        return cls(
            dates_vec
)