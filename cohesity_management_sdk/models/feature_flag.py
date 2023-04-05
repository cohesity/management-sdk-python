# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FeatureFlag(object):

    """Implementation of the 'FeatureFlag' model.

    Specify feature flag override status.


    Attributes:

        is_approved (bool): Specifies the overridden approval status.
        is_ui_feature (bool): Specifies if it's a front-end(UI) or back-end
            feature.
        name (string, required): Specifies name of the feature.
        reason (string): Specifies the reason for override.
        timestamp (long|int): Specifies the timestamp of override.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_approved":'isApproved',
        "is_ui_feature":'isUiFeature',
        "name":'name',
        "reason":'reason',
        "timestamp":'timestamp',
    }
    def __init__(self,
                 is_approved=None,
                 is_ui_feature=None,
                 name=None,
                 reason=None,
                 timestamp=None,
            ):

        """Constructor for the FeatureFlag class"""

        # Initialize members of the class
        self.is_approved = is_approved
        self.is_ui_feature = is_ui_feature
        self.name = name
        self.reason = reason
        self.timestamp = timestamp

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
        is_approved = dictionary.get('isApproved')
        is_ui_feature = dictionary.get('isUiFeature')
        name = dictionary.get('name')
        reason = dictionary.get('reason')
        timestamp = dictionary.get('timestamp')

        # Return an object of this model
        return cls(
            is_approved,
            is_ui_feature,
            name,
            reason,
            timestamp
)