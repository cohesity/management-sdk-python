# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.exchange_restore_view_parameters

class ExchangeRestoreParameters(object):

    """Implementation of the 'ExchangeRestoreParameters' model.

    Specifies the exchange restore parameters.

    Attributes:
        mtype (TypeExchangeRestoreParametersEnum):Specifies the Exchange
            restore type.
            Specifies the type of Exchange restore.

            'kNone' specifies no special behaviour.
            'kView' specifies the option to create a view which cann be used
            by the external tools like Kroll to perform mailbox or mail-item
            recovery.
            'kDatabase' specifies the option to restore an Exchange database.
        view_parameters (ExchangeRestoreViewParameters): Specifies the
            parameters for the restore of type kView.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "view_parameters": 'viewParameters'
    }

    def __init__(self,
                 mtype=None,
                 view_parameters=None):
        """Constructor for the ExchangeRestoreParameters class"""

        # Initialize members of the class
        self.mtype = mtype
        self.view_parameters = view_parameters


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
        mtype = dictionary.get('type')
        view_parameters = cohesity_management_sdk.models.exchange_restore_view_parameters.ExchangeRestoreViewParameters.from_dictionary(dictionary.get('viewParameters')) if dictionary.get('viewParameters') else None

        # Return an object of this model
        return cls(mtype,
                   view_parameters)


