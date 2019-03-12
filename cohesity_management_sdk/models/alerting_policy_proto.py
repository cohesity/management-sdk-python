# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class AlertingPolicyProto(object):

    """Implementation of the 'AlertingPolicyProto' model.

    TODO: type model description here.

    Attributes:
        emails (list of string): The email addresses to send alerts to.
        policy (int): 'policy' is declared as int32 because ORing the enums
            will generate values which are invalid as enums. Protobuf doesn't
            allow those invalid enums to be set.
        raise_object_level_failure_alert (bool): Raise per object alert for
            failures.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "emails":'emails',
        "policy":'policy',
        "raise_object_level_failure_alert":'raiseObjectLevelFailureAlert'
    }

    def __init__(self,
                 emails=None,
                 policy=None,
                 raise_object_level_failure_alert=None):
        """Constructor for the AlertingPolicyProto class"""

        # Initialize members of the class
        self.emails = emails
        self.policy = policy
        self.raise_object_level_failure_alert = raise_object_level_failure_alert


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
        emails = dictionary.get('emails')
        policy = dictionary.get('policy')
        raise_object_level_failure_alert = dictionary.get('raiseObjectLevelFailureAlert')

        # Return an object of this model
        return cls(emails,
                   policy,
                   raise_object_level_failure_alert)


