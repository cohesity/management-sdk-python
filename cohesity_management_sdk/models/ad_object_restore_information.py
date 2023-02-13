# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.attribute_restore_information

class AdObjectRestoreInformation(object):

    """Implementation of the 'AdObjectRestoreInformation' model.

    Represents the details about the restore of the AD object.

    Attributes:
        attribute_restore_info (list of AttributeRestoreInformation):
            Specifies the list of attributes of the AD object whose restore
            failed.
        error_message (string): Specifies the error message while restoring
            the AD Object.
        name (string): Specifies the name of the AD object.
        start_time_usecs (long|int): Specifies the start time of the restore
            of the AD object specified as a Unix epoch Timestamp(in
            microseconds).
        time_taken_msecs (int): Specifies the time taken for restore of AD
            Object and its attributes in milliseconds.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attribute_restore_info":'attributeRestoreInfo',
        "error_message":'errorMessage',
        "name":'name',
        "start_time_usecs":'startTimeUsecs',
        "time_taken_msecs":'timeTakenMsecs'
    }

    def __init__(self,
                 attribute_restore_info=None,
                 error_message=None,
                 name=None,
                 start_time_usecs=None,
                 time_taken_msecs=None):
        """Constructor for the AdObjectRestoreInformation class"""

        # Initialize members of the class
        self.attribute_restore_info = attribute_restore_info
        self.error_message = error_message
        self.name = name
        self.start_time_usecs = start_time_usecs
        self.time_taken_msecs = time_taken_msecs


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
        attribute_restore_info = None
        if dictionary.get('attributeRestoreInfo') != None:
            attribute_restore_info = list()
            for structure in dictionary.get('attributeRestoreInfo'):
                attribute_restore_info.append(cohesity_management_sdk.models.attribute_restore_information.AttributeRestoreInformation.from_dictionary(structure))
        error_message = dictionary.get('errorMessage')
        name = dictionary.get('name')
        start_time_usecs = dictionary.get('startTimeUsecs')
        time_taken_msecs = dictionary.get('timeTakenMsecs')

        # Return an object of this model
        return cls(attribute_restore_info,
                   error_message,
                   name,
                   start_time_usecs,
                   time_taken_msecs)


