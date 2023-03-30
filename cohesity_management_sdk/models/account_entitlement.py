# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AccountEntitlement(object):

    """Implementation of the 'AccountEntitlement' model.

    Specifies the account entitlement for a Salesforce account.

    Attributes:
        d_maas_free_trial__c (bool): Specifies whether DMaaS free trail is
            active.
        end_date (string): Specifies the end date for the entitlement.
        id (bool): Specifies the entitlement ID.
        name (bool): Specifies the name of the entitlement.
        sku__c (long|int): Specifies the stock keeping unit.
        start_date (string): Specifies the start date for the entitlement.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "d_maas_free_trial__c":'DMaaS_Free_Trial__c',
        "end_date":'EndDate',
        "id":'Id',
        "name":'Name',
        "sku__c":'SKU__c',
        "start_date":'StartDate'
    }

    def __init__(self,
                 d_maas_free_trial__c=None,
                 end_date=None,
                 id=None,
                 name=None,
                 sku__c=None,
                 start_date=None):
        """Constructor for the AccountEntitlement class"""

        # Initialize members of the class
        self.d_maas_free_trial__c = d_maas_free_trial__c
        self.end_date = end_date
        self.id = id
        self.name = name
        self.sku__c = sku__c
        self.start_date = start_date


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
        d_maas_free_trial__c = dictionary.get('DMaaS_Free_Trial__c')
        end_date = dictionary.get('EndDate')
        id = dictionary.get('Id')
        name = dictionary.get('Name')
        sku__c = dictionary.get('SKU__c')
        start_date = dictionary.get('StartDate')

        # Return an object of this model
        return cls(d_maas_free_trial__c,
                   end_date,
                   id,
                   name,
                   sku__c,
                   start_date)


