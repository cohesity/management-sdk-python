# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ProtectedObjectPrivileges(object):

    """Implementation of the 'ProtectedObjectPrivileges' model.

    ProtectedObjectPrivileges specifies which protected objects are allowed
    to
    be accessed by an app instance.

    Attributes:
        protected_objectsprivileges_type (ProtectedObjectsprivilegesTypeEnum):
            Specifies if all, none or specific protected objects are allowed
            to be accessed. Specifies if all, none or specific protected
            objects are allowed to be accessed. kNone - None of the protected
            objects have access. kAll - All the protected objects have access.
            kSpecific - Only specific protected objects have access.
        protection_source_ids (list of long|int): Specifies the ids of the
            protection sources which are allowed to be accessed in case the
            privilege type is kSpecific.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protected_objectsprivileges_type":'protectedObjectsprivilegesType',
        "protection_source_ids":'protectionSourceIds'
    }

    def __init__(self,
                 protected_objectsprivileges_type=None,
                 protection_source_ids=None):
        """Constructor for the ProtectedObjectPrivileges class"""

        # Initialize members of the class
        self.protected_objectsprivileges_type = protected_objectsprivileges_type
        self.protection_source_ids = protection_source_ids


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
        protected_objectsprivileges_type = dictionary.get('protectedObjectsprivilegesType')
        protection_source_ids = dictionary.get('protectionSourceIds')

        # Return an object of this model
        return cls(protected_objectsprivileges_type,
                   protection_source_ids)


