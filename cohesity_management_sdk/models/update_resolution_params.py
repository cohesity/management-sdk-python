# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpdateResolutionParams(object):

    """Implementation of the 'UpdateResolutionParams' model.

    Apply an existing Resolution to a new list of Alerts, which are specified
    by
    Alert Ids.

    Attributes:
        alert_id_list (list of string): Specifies the Alerts to resolve, which
            are specified by Alert Ids.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alert_id_list":'alertIdList'
    }

    def __init__(self,
                 alert_id_list=None):
        """Constructor for the UpdateResolutionParams class"""

        # Initialize members of the class
        self.alert_id_list = alert_id_list


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
        alert_id_list = dictionary.get('alertIdList')

        # Return an object of this model
        return cls(alert_id_list)


