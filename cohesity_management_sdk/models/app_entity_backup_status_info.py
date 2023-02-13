# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AppEntityBackupStatusInfo(object):

    """Implementation of the 'AppEntityBackupStatusInfo' model.

    Specifies the app level backup status and information.

    Attributes:
        app_id (long|int): Specifies the Id of the App entity. This is
            typically a database entity in case of SQL, Oracle jobs etc.
        error (string): Specifies if an error occurred (if any) while
            running this task. This field is populated when the status is
            equal to 'kFailure'.
        name (string): Specifies the name of the app entity.
        owner_id (string): Specifies the owner id of the the app. Owner is the
            host under which the app is located. Example: SQL DB entities can
            be hosted by Physical host or virtual machine.
        status (StatusAppEntityBackupStatusInfoEnum): Specifies the backup
            status for this app entity.
        warnings (list of string): Specifies the warnings that
            occurred (if any) while running this task.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_id": 'appId',
        "error": 'error',
        "name": 'name',
        "owner_id": 'ownerId',
        "status":'status',
        "warnings":'warnings'
    }

    def __init__(self,
                 app_id=None,
                 error=None,
                 name=None,
                 owner_id=None,
                 status=None,
                 warnings=None):
        """Constructor for the AppEntityBackupStatusInfo class"""

        # Initialize members of the class
        self.app_id = app_id
        self.error = error
        self.name = name
        self.owner_id = owner_id
        self.status = status
        self.warnings = warnings

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
        app_id = dictionary.get('appId')
        error = dictionary.get('error')
        name = dictionary.get('name')
        owner_id = dictionary.get('ownerId')
        status = dictionary.get('status')
        warnings = dictionary.get('warnings')

        # Return an object of this model
        return cls(app_id,
                   error,
                   name,
                   owner_id,
                   status,
                   warnings)


