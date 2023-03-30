# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SiteContinuityInfo(object):

    """Implementation of the 'SiteContinuityInfo' model.

    SiteContinuityInfo holds information about the Site Continuity subscription
    such as if it is active or not.


    Attributes:

        end_date (string): Specifies the end date of the subscription.
        is_active (bool): Specifies whether the DRaaS subscription is active.
        is_free_trial (bool): Specifies whether the subscription is free trial.
        start_date (string): Specifies the start date of the subscription.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "end_date":'endDate',
        "is_active":'isActive',
        "is_free_trial":'isFreeTrial',
        "start_date":'startDate',
    }
    def __init__(self,
                 end_date=None,
                 is_active=None,
                 is_free_trial=None,
                 start_date=None,
            ):

        """Constructor for the SiteContinuityInfo class"""

        # Initialize members of the class
        self.end_date = end_date
        self.is_active = is_active
        self.is_free_trial = is_free_trial
        self.start_date = start_date

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
        end_date = dictionary.get('endDate')
        is_active = dictionary.get('isActive')
        is_free_trial = dictionary.get('isFreeTrial')
        start_date = dictionary.get('startDate')

        # Return an object of this model
        return cls(
            end_date,
            is_active,
            is_free_trial,
            start_date
)