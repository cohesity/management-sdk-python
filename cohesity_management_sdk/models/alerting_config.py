# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.email_delivery_target

class AlertingConfig(object):

    """Implementation of the 'AlertingConfig' model.

    Specifies optional settings for alerting.

    Attributes:
        email_addresses (list of string): Exists to maintain backwards
            compatibility with versions before eff8198.
        email_delivery_targets (list of EmailDeliveryTarget): Specifies
            additional email addresses where alert notifications (configured
            in the AlertingPolicy) must be sent.
        raise_object_level_failure_alert (bool): Specifies the boolean to
            raise per object alert for failures.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email_addresses":'emailAddresses',
        "email_delivery_targets":'emailDeliveryTargets',
        "raise_object_level_failure_alert":'raiseObjectLevelFailureAlert'
    }

    def __init__(self,
                 email_addresses=None,
                 email_delivery_targets=None,
                 raise_object_level_failure_alert=None):
        """Constructor for the AlertingConfig class"""

        # Initialize members of the class
        self.email_addresses = email_addresses
        self.email_delivery_targets = email_delivery_targets
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
        email_delivery_targets = None
        email_addresses = dictionary.get('emailAddresses')
        if dictionary.get('emailDeliveryTargets') != None:
            email_delivery_targets = list()
            for structure in dictionary.get('emailDeliveryTargets'):
                email_delivery_targets.append(cohesity_management_sdk.models.email_delivery_target.EmailDeliveryTarget.from_dictionary(structure))
        raise_object_level_failure_alert = dictionary.get('raiseObjectLevelFailureAlert')

        # Return an object of this model
        return cls(email_addresses,
                   email_delivery_targets,
                   raise_object_level_failure_alert)


