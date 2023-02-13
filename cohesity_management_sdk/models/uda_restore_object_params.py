# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class UdaRestoreObjectParams(object):

    """Implementation of the 'UdaRestoreObjectParams' model.

    Attributes:
        new_object_name (string): The new name of the object, if it is going to
            be renamed.
        overwrite (bool): Whether to overwrite or keep the object if the
            object being recovered already exists in the destination.
        restore_time_secs (long|int): The point-in-time to which object needs
            to be restored. This allows for the granular recovery of Uda
            objects. If this is not set, the Uda object will be restored to
            full/incremental snapshot.


    """

    # Create a mapping from Model property names to API property names
    _names = {
        "new_object_name":'newObjectName',
        "overwrite":'overwrite',
        "restore_time_secs":'restoreTimeSecs'
    }

    def __init__(self,
                 new_object_name=None,
                 overwrite=None,
                 restore_time_secs=None):
        """Constructor for the UdaRestoreObjectParams class"""

        # Initialize members of the class
        self.new_object_name = new_object_name
        self.overwrite = overwrite
        self.restore_time_secs = restore_time_secs


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
        new_object_name = dictionary.get('newObjectName')
        overwrite =  dictionary.get('overwrite')
        restore_time_secs = dictionary.get('restoreTimeSecs')

        # Return an object of this model
        return cls(new_object_name,
                   overwrite,
                   restore_time_secs)


