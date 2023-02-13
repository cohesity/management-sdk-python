# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_exchange_params_database_options
import cohesity_management_sdk.models.restore_exchange_params_view_options

class RestoreExchangeParams(object):

    """Implementation of the 'RestoreExchangeParams' model.

    Params specific to restoring an Exchange application.

    Attributes:
        database_options (RestoreExchangeParams_DatabaseOptions): Only
            applicable when ExchangeRestoreType.Type=kDatabase.
        mtype (int): Restore type.
        view_options (RestoreExchangeParams_ViewOptions): Only applicable
            when ExchangeRestoreType.Type=kView.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "database_options":'databaseOptions',
        "mtype":'type',
        "view_options":'viewOptions'
    }

    def __init__(self,
                 database_options=None,
                 mtype=None,
                 view_options=None):
        """Constructor for the RestoreExchangeParams class"""

        # Initialize members of the class
        self.database_options = database_options
        self.mtype = mtype
        self.view_options = view_options


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
        database_options = cohesity_management_sdk.models.restore_exchange_params_database_options.RestoreExchangeParams_DatabaseOptions.from_dictionary(dictionary.get('databaseOptions')) if dictionary.get('databaseOptions') else None
        mtype = dictionary.get('type')
        view_options = cohesity_management_sdk.models.restore_exchange_params_view_options.RestoreExchangeParams_ViewOptions.from_dictionary(dictionary.get('viewOptions')) if dictionary.get('viewOptions') else None

        # Return an object of this model
        return cls(database_options,
                   mtype,
                   view_options)


