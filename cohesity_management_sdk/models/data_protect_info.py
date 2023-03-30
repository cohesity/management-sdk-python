# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.tiering_info


class DataProtectInfo(object):

    """Implementation of the 'DataProtectInfo' model.

    DMaaSSubscriptionInfo holds information about the Data Protect subscription
    such as if it is active or not.


    Attributes:

        end_date (string): Specifies the end date of the subscription.
        is_active (bool): Specifies whether the dmaas subscription is active.
        is_aws_subscription (bool): Specifies whether the subscription is AWS
            Subscription.
        is_cohesity_subscription (bool): Specifies whether the subscription is
            a Cohesity Paid subscription.
        is_free_trial (bool): Specifies whether the subscription is free trial.
        quantity (long|int): Specifies the quantity of the subscription.
        start_date (string): Specifies the start date of the subscription.
        tiering (TieringInfo): Specifies the Tiering information for the Data
            Protect subscription
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "end_date":'endDate',
        "is_active":'isActive',
        "is_aws_subscription":'isAwsSubscription',
        "is_cohesity_subscription":'isCohesitySubscription',
        "is_free_trial":'isFreeTrial',
        "quantity":'quantity',
        "start_date":'startDate',
        "tiering":'tiering',
    }
    def __init__(self,
                 end_date=None,
                 is_active=None,
                 is_aws_subscription=None,
                 is_cohesity_subscription=None,
                 is_free_trial=None,
                 quantity=None,
                 start_date=None,
                 tiering=None,
            ):

        """Constructor for the DataProtectInfo class"""

        # Initialize members of the class
        self.end_date = end_date
        self.is_active = is_active
        self.is_aws_subscription = is_aws_subscription
        self.is_cohesity_subscription = is_cohesity_subscription
        self.is_free_trial = is_free_trial
        self.quantity = quantity
        self.start_date = start_date
        self.tiering = tiering

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
        is_aws_subscription = dictionary.get('isAwsSubscription')
        is_cohesity_subscription = dictionary.get('isCohesitySubscription')
        is_free_trial = dictionary.get('isFreeTrial')
        quantity = dictionary.get('quantity')
        start_date = dictionary.get('startDate')
        tiering = cohesity_management_sdk.models.tiering_info.TieringInfo.from_dictionary(dictionary.get('tiering')) if dictionary.get('tiering') else None

        # Return an object of this model
        return cls(
            end_date,
            is_active,
            is_aws_subscription,
            is_cohesity_subscription,
            is_free_trial,
            quantity,
            start_date,
            tiering
)