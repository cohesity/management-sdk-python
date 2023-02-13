# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class LegalHoldings(object):

    """Implementation of the 'LegalHoldings' model.

    Specifies the legal holding of a Protection Source.

    Attributes:
        hold_for_legal_purpose (bool): Specifies whether the source is put on
            legal hold or not.
        protection_source_id (long|int): Specifies an Protection Source Id in
            the snapshot.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hold_for_legal_purpose":'holdForLegalPurpose',
        "protection_source_id":'protectionSourceId'
    }

    def __init__(self,
                 hold_for_legal_purpose=None,
                 protection_source_id=None):
        """Constructor for the LegalHoldings class"""

        # Initialize members of the class
        self.hold_for_legal_purpose = hold_for_legal_purpose
        self.protection_source_id = protection_source_id


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
        hold_for_legal_purpose = dictionary.get('holdForLegalPurpose')
        protection_source_id = dictionary.get('protectionSourceId')

        # Return an object of this model
        return cls(hold_for_legal_purpose,
                   protection_source_id)


