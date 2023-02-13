# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AdObjectMetaData(object):

    """Implementation of the 'AdObjectMetaData' model.

    Specifies details about the AD objects.

    Attributes:
        distinguished_name (string): Specifies the Distinguished name of the
            AD object.
        domain (string): Domain of the AD object.
        email (string): Specifies the email of the AD object of type user or
            group.
        guid (string): Specifies the Guid of the AD object.
        name (string): Specifies the name of the AD object.
        object_type (string): Specifies the type of the AD Object. The type
            may be user, computer, group or ou.
        sam_account_name (string): Specifies the sam account name of the AD
            object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "distinguished_name":'distinguishedName',
        "domain":'domain',
        "email":'email',
        "guid":'guid',
        "name":'name',
        "object_type":'objectType',
        "sam_account_name":'samAccountName'
    }

    def __init__(self,
                 distinguished_name=None,
                 domain=None,
                 email=None,
                 guid=None,
                 name=None,
                 object_type=None,
                 sam_account_name=None):
        """Constructor for the AdObjectMetaData class"""

        # Initialize members of the class
        self.distinguished_name = distinguished_name
        self.domain = domain
        self.email = email
        self.guid = guid
        self.name = name
        self.object_type = object_type
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
        distinguished_name = dictionary.get('distinguishedName')
        domain = dictionary.get('domain')
        email = dictionary.get('email')
        guid = dictionary.get('guid')
        name = dictionary.get('name')
        object_type = dictionary.get('objectType')
        sam_account_name = dictionary.get('samAccountName')

        # Return an object of this model
        return cls(distinguished_name,
                   domain,
                   email,
                   guid,
                   name,
                   object_type,
                   sam_account_name)


