# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_object_restore_information


class AdObjectsRestoreStatus(object):

    """Implementation of the 'AdObjectsRestoreStatus' model.

    Represents the details about the status of restore of the AD objects. It
    also has details about the number of objects whose restore is successfull,
    failure or in progress.


    Attributes:

        ad_objects_restore_info (list of AdObjectRestoreInformation): Specifies
            the status of all the AD Objects which were requested to be
            restored.
        num_objects_failed (int): Specifies the number of AD Objects whose
            restore has failed.
        num_objects_running (int): Specifies the number of AD Objects whose
            restore is in progress.
        num_objects_succeeded (int): Specifies the number of AD Objects whose
            restore is successfull.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "ad_objects_restore_info":'adObjectsRestoreInfo',
        "num_objects_failed":'numObjectsFailed',
        "num_objects_running":'numObjectsRunning',
        "num_objects_succeeded":'numObjectsSucceeded',
    }
    def __init__(self,
                 ad_objects_restore_info=None,
                 num_objects_failed=None,
                 num_objects_running=None,
                 num_objects_succeeded=None,
            ):

        """Constructor for the AdObjectsRestoreStatus class"""

        # Initialize members of the class
        self.ad_objects_restore_info = ad_objects_restore_info
        self.num_objects_failed = num_objects_failed
        self.num_objects_running = num_objects_running
        self.num_objects_succeeded = num_objects_succeeded

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
        ad_objects_restore_info = None
        if dictionary.get('adObjectsRestoreInfo') != None:
            ad_objects_restore_info = list()
            for structure in dictionary.get('adObjectsRestoreInfo'):
                ad_objects_restore_info.append(cohesity_management_sdk.models.ad_object_restore_information.AdObjectRestoreInformation.from_dictionary(structure))
        num_objects_failed = dictionary.get('numObjectsFailed')
        num_objects_running = dictionary.get('numObjectsRunning')
        num_objects_succeeded = dictionary.get('numObjectsSucceeded')

        # Return an object of this model
        return cls(
            ad_objects_restore_info,
            num_objects_failed,
            num_objects_running,
            num_objects_succeeded
)