# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.delivery_rule_proto_delivery_target

class AlertingPolicyProto(object):

    """Implementation of the 'AlertingPolicyProto' model.

    TODO: type model description here.

    Attributes:
        delivery_target_vec (list of DeliveryRuleProtoDeliveryTarget): The
            delivery targets to be alerted.
        emails (list of string): The email addresses to send alerts to. This
            field has been deprecated in favor of the field
            delivery_target_vec. The clients should take care to ensure that
            the emails stored in here are migrated to that field, or else
            utilise both the fields when trying to obtain the complete list of
            delivery targets.
        policy (int): 'policy' is declared as int32 because ORing the enums
            will generate values which are invalid as enums. Protobuf doesn't
            allow those invalid enums to be set.
        raise_object_level_failure_alert (bool): Raise per object alert for
            failures.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delivery_target_vec":'deliveryTargetVec',
        "emails":'emails',
        "policy":'policy',
        "raise_object_level_failure_alert":'raiseObjectLevelFailureAlert'
    }

    def __init__(self,
                 delivery_target_vec=None,
                 emails=None,
                 policy=None,
                 raise_object_level_failure_alert=None):
        """Constructor for the AlertingPolicyProto class"""

        # Initialize members of the class
        self.delivery_target_vec = delivery_target_vec
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
        delivery_target_vec = None
        if dictionary.get('deliveryTargetVec') != None:
            delivery_target_vec = list()
            for structure in dictionary.get('deliveryTargetVec'):
                delivery_target_vec.append(cohesity_management_sdk.models.delivery_rule_proto_delivery_target.DeliveryRuleProtoDeliveryTarget.from_dictionary(structure))
        emails = dictionary.get('emails')
        policy = dictionary.get('policy')
        raise_object_level_failure_alert = dictionary.get('raiseObjectLevelFailureAlert')

        # Return an object of this model
        return cls(delivery_target_vec,
                   emails,
                   policy,
                   raise_object_level_failure_alert)


