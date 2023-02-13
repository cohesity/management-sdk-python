# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ADObject(object):

    """Implementation of the 'ADObject' model.

    Represents the details about an AD object.

    Attributes:
        description (string): Specifies the 'description' of an AD object.
        destination_guid (string): Specifies the guid of object in the
            Production AD which is equivalent to the object in the Snapshot
            AD.
        display_name (string): Specifies the display name of the AD object.
        distinguished_name (string): Specifies the distinguished name of the
            AD object. Eg: CN=Jone Doe,OU=Users,DC=corp,DC=cohesity,DC=com
        error_message (string): Specifies the error message while fetching the
            AD object.
        object_class (string): Specifies the class name of an AD Object such
            as 'user','computer', 'organizationalUnit'.
        search_result_flags (list of SearchResultFlagEnum): Specifies the
            SearchResultFlags of the AD object. 'kEqual' indicates the AD
            Object from Snapshot and Production AD are equal. 'kNotEqual'
            indicates the AD Object from snapshot and production AD are not
            equal. 'kRestorePasswordRequired' indicates when restoring this AD
            Object from Snapshot AD to Production AD, a password is required.
            'kMovedOnDestination' indicates the object has moved to another
            container or OU in Production AD compared to  Snapshot AD.
            'kDisableSupported' indicates the enable and disable is supported
            on the AD Object. AD Objects of type 'User' and 'Computers'
            support this operation.
        source_guid (string): Specifies the guid of the AD object in Snapshot
            AD.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "destination_guid":'destinationGuid',
        "display_name":'displayName',
        "distinguished_name":'distinguishedName',
        "error_message":'errorMessage',
        "object_class":'objectClass',
        "search_result_flags":'searchResultFlags',
        "source_guid":'sourceGuid'
    }

    def __init__(self,
                 description=None,
                 destination_guid=None,
                 display_name=None,
                 distinguished_name=None,
                 error_message=None,
                 object_class=None,
                 search_result_flags=None,
                 source_guid=None):
        """Constructor for the ADObject class"""

        # Initialize members of the class
        self.description = description
        self.destination_guid = destination_guid
        self.display_name = display_name
        self.distinguished_name = distinguished_name
        self.error_message = error_message
        self.object_class = object_class
        self.search_result_flags = search_result_flags
        self.source_guid = source_guid


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
        description = dictionary.get('description')
        destination_guid = dictionary.get('destinationGuid')
        display_name = dictionary.get('displayName')
        distinguished_name = dictionary.get('distinguishedName')
        error_message = dictionary.get('errorMessage')
        object_class = dictionary.get('objectClass')
        search_result_flags = dictionary.get('searchResultFlags')
        source_guid = dictionary.get('sourceGuid')

        # Return an object of this model
        return cls(description,
                   destination_guid,
                   display_name,
                   distinguished_name,
                   error_message,
                   object_class,
                   search_result_flags,
                   source_guid)


