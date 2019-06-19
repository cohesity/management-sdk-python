# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class AlertingConfig(object):

    """Implementation of the 'AlertingConfig' model.

    Specifies optional settings for alerting.

    Attributes:
        email_addresses (list of string): Specifies additional email addresses
            where alert notifications (configured in the AlertingPolicy) must
            be sent.
        raise_object_level_failure_alert (bool): Specifies the boolean to
            raise per object alert for failures.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email_addresses":'emailAddresses',
        "raise_object_level_failure_alert":'raiseObjectLevelFailureAlert'
    }

    def __init__(self,
                 email_addresses=None,
                 raise_object_level_failure_alert=None):
        """Constructor for the AlertingConfig class"""

        # Initialize members of the class
        self.email_addresses = email_addresses
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
        email_addresses = dictionary.get('emailAddresses')
        raise_object_level_failure_alert = dictionary.get('raiseObjectLevelFailureAlert')

        # Return an object of this model
        return cls(email_addresses,
                   raise_object_level_failure_alert)


