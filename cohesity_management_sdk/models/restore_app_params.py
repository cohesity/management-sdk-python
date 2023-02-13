# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.credentials
import cohesity_management_sdk.models.app_owner_restore_info
import cohesity_management_sdk.models.restore_app_object

class RestoreAppParams(object):

    """Implementation of the 'RestoreAppParams' model.

    This message captures all the necessary arguments specified by the user
    to
    restore an application.

    Attributes:
        credentials (Credentials): Specifies credentials to access a target
            source.
        owner_restore_info (AppOwnerRestoreInfo): TODO: type description
            here.
        restore_app_object_vec (list of RestoreAppObject): The application
            level objects that needs to be restored. If this vector is
            populated with exactly one object without its 'app_entity', all
            the application objects of the owner will be restored. If multiple
            objects are being restored, the 'app_entity' field must be
            specified for all of them.
        mtype (int): The application environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "credentials":'credentials',
        "owner_restore_info":'ownerRestoreInfo',
        "restore_app_object_vec":'restoreAppObjectVec',
        "mtype":'type'
    }

    def __init__(self,
                 credentials=None,
                 owner_restore_info=None,
                 restore_app_object_vec=None,
                 mtype=None):
        """Constructor for the RestoreAppParams class"""

        # Initialize members of the class
        self.credentials = credentials
        self.owner_restore_info = owner_restore_info
        self.restore_app_object_vec = restore_app_object_vec
        self.mtype = mtype


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
        credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('credentials')) if dictionary.get('credentials') else None
        owner_restore_info = cohesity_management_sdk.models.app_owner_restore_info.AppOwnerRestoreInfo.from_dictionary(dictionary.get('ownerRestoreInfo')) if dictionary.get('ownerRestoreInfo') else None
        restore_app_object_vec = None
        if dictionary.get('restoreAppObjectVec') != None:
            restore_app_object_vec = list()
            for structure in dictionary.get('restoreAppObjectVec'):
                restore_app_object_vec.append(cohesity_management_sdk.models.restore_app_object.RestoreAppObject.from_dictionary(structure))
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(credentials,
                   owner_restore_info,
                   restore_app_object_vec,
                   mtype)


