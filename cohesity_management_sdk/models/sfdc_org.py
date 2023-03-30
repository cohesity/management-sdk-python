# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SfdcOrg(object):

    """Implementation of the 'SfdcOrg' model.

    Specifies an Object containing information about a Salesforce Org.


    Attributes:

        org_id (string): String id of the organization to which Sfdc user
            belongs.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "org_id":'orgId',
    }
    def __init__(self,
                 org_id=None,
            ):

        """Constructor for the SfdcOrg class"""

        # Initialize members of the class
        self.org_id = org_id

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
        org_id = dictionary.get('orgId')

        # Return an object of this model
        return cls(
            org_id
)