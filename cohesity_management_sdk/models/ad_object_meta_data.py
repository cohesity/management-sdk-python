# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class AdObjectMetaData(object):

    """Implementation of the 'AdObjectMetaData' model.

    Specifies details about the AD objects.

    Attributes:
        guid (string): Specifies the Guid of the AD object.
        name (string): Specifies the name of the AD object.
        sam_account_name (string): Specifies the sam account name of the AD
            object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "guid":'guid',
        "name":'name',
        "sam_account_name":'samAccountName'
    }

    def __init__(self,
                 guid=None,
                 name=None,
                 sam_account_name=None):
        """Constructor for the AdObjectMetaData class"""

        # Initialize members of the class
        self.guid = guid
        self.name = name
        self.sam_account_name = sam_account_name


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
        guid = dictionary.get('guid')
        name = dictionary.get('name')
        sam_account_name = dictionary.get('samAccountName')

        # Return an object of this model
        return cls(guid,
                   name,
                   sam_account_name)


