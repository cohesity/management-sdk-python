# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class EmailDeliveryTarget(object):

    """Implementation of the 'EmailDeliveryTarget' model.

    EmailDeliveryTarget
    Specifies the email address and the locale setting for it.

    Attributes:
        email_address (string): TODO: type description here.
        locale (string): Specifies the language in which the emails sent to
            the above defined mail address should be in.
        recipient_type (int): Specifies the recipient type on how the emails
            are to received.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email_address":'emailAddress',
        "locale":'locale',
        "recipient_type":'recipientType'
    }

    def __init__(self,
                 email_address=None,
                 locale=None,
                 recipient_type=None):
        """Constructor for the EmailDeliveryTarget class"""

        # Initialize members of the class
        self.email_address = email_address
        self.locale = locale
        self.recipient_type = recipient_type


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
        email_address = dictionary.get('emailAddress')
        locale = dictionary.get('locale')
        recipient_type = dictionary.get('recipientType')

        # Return an object of this model
        return cls(email_address,
                   locale,
                   recipient_type)


