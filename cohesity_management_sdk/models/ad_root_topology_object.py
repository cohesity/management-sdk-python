# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AdRootTopologyObject(object):

    """Implementation of the 'AdRootTopologyObject' model.

    Represents a node in AD Topology tree.

    Attributes:
        child_objects (list of object): Specifies the array of children of
            this object.
        description (string): Specifies the 'description' of an object.
        dest_guid (string): Specifies the guid of matching 'source_guid' from
            production AD. This is looked up  based on source_guid or
            distinguishedName attribute value.
        display_name (string): Specifies the display name of the object in AD
            Topology tree.
        distinguished_name (string): Specifies the distinguished name of the
            object in AD Topology tree. Eg: CN=Jone
            Doe,OU=Users,DC=corp,DC=cohesity,DC=com
        error_message (string): Specifies the AD error while fetching the
            ADRootTopologyObject.
        object_class (string): Specifies the LDAP class name such as
            'user','computer', 'organizationalUnit'.
        source_guid (string): Specifies the guid string of the object in AD
            snapshot database.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "child_objects":'childObjects',
        "description":'description',
        "dest_guid":'destGuid',
        "display_name":'displayName',
        "distinguished_name":'distinguishedName',
        "error_message":'errorMessage',
        "object_class":'objectClass',
        "source_guid":'sourceGuid'
    }

    def __init__(self,
                 child_objects=None,
                 description=None,
                 dest_guid=None,
                 display_name=None,
                 distinguished_name=None,
                 error_message=None,
                 object_class=None,
                 source_guid=None):
        """Constructor for the AdRootTopologyObject class"""

        # Initialize members of the class
        self.child_objects = child_objects
        self.description = description
        self.dest_guid = dest_guid
        self.display_name = display_name
        self.distinguished_name = distinguished_name
        self.error_message = error_message
        self.object_class = object_class
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
        child_objects = dictionary.get('childObjects')
        description = dictionary.get('description')
        dest_guid = dictionary.get('destGuid')
        display_name = dictionary.get('displayName')
        distinguished_name = dictionary.get('distinguishedName')
        error_message = dictionary.get('errorMessage')
        object_class = dictionary.get('objectClass')
        source_guid = dictionary.get('sourceGuid')

        # Return an object of this model
        return cls(child_objects,
                   description,
                   dest_guid,
                   display_name,
                   distinguished_name,
                   error_message,
                   object_class,
                   source_guid)


