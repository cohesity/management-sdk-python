# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.application_restore_object
import cohesity_management_sdk.models.restore_object_details

class ProtectionSourceAndApplicationRestoreObjects(object):

    """Implementation of the 'ProtectionSourceAndApplicationRestoreObjects'
    model.

    Specifies the details about the protection source and snapshot from where
    the application objects must be restored. It also provides information
    about the application objects which have to be restored and target host to
    which the application objects must be restored.

    Attributes:
        application_restore_objects (list of ApplicationRestoreObject):
            Specifies the Application Server objects whose data should be
            restored and the restore parameters for each of them.
        hosting_protection_source (RestoreObjectDetails): Specifies the
            restore information for the Protection Source object that
            and hosts the Application Servers. This provides the registered
            snapshot details from which the applications should be restored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_restore_objects": 'applicationRestoreObjects',
        "hosting_protection_source": 'hostingProtectionSource'
    }

    def __init__(self,
                 application_restore_objects=None,
                 hosting_protection_source=None):
        """Constructor for the ProtectionSourceAndApplicationRestoreObjects class"""

        # Initialize members of the class
        self.application_restore_objects = application_restore_objects
        self.hosting_protection_source = hosting_protection_source


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
        application_restore_objects = None
        if  dictionary.get('applicationRestoreObjects') != None:
            application_restore_objects = list()
            for structure in dictionary.get('applicationRestoreObjects'):
                application_restore_objects.append(cohesity_management_sdk.models.application_restore_object.ApplicationRestoreObject.from_dictionary(structure))
        hosting_protection_source = cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(dictionary.get('hostingProtectionSource')) if dictionary.get('hostingProtectionSource') else None

        # Return an object of this model
        return cls(application_restore_objects,
                   hosting_protection_source)


