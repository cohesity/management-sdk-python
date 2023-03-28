# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.uda_restore_object


class UdaRecoverParams(object):

    """Implementation of the 'UdaRecoverParams' model.

    TODO: type description here.


    Attributes:

        log_view_name (string): If the restore has logs to be replayed,
            'log_view_name' contains the name of log backup view to be mounted
            on the host.
        restore_objects (list of UdaRestoreObject): TODO: Type description
            here.
        view_box_id (long|int): The view box where log backed up data has been
            saved.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "log_view_name":'logViewName',
        "restore_objects":'restoreObjects',
        "view_box_id":'viewBoxId',
    }
    def __init__(self,
                 log_view_name=None,
                 restore_objects=None,
                 view_box_id=None,
            ):

        """Constructor for the UdaRecoverParams class"""

        # Initialize members of the class
        self.log_view_name = log_view_name
        self.restore_objects = restore_objects
        self.view_box_id = view_box_id

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
        log_view_name = dictionary.get('logViewName')
        restore_objects = None
        if dictionary.get('restoreObjects') != None:
            restore_objects = list()
            for structure in dictionary.get('restoreObjects'):
                restore_objects.append(cohesity_management_sdk.models.uda_restore_object.UdaRestoreObject.from_dictionary(structure))
        view_box_id = dictionary.get('viewBoxId')

        # Return an object of this model
        return cls(
            log_view_name,
            restore_objects,
            view_box_id
)