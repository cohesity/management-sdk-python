# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SfdcRecoverJobParams(object):

    """Implementation of the 'SfdcRecoverJobParams' model.

    TODO: type description here.


    Attributes:

        overwrite (bool): Whether to overwrite or keep the object if the object
            being recovered already exists in the destination.
        restore_childs_object_vec (list of string): TODO: Type description
            here.
        restore_parent_object_vec (list of string): List of parent/child
            objects that need to be restored.
        run_start_time_usecs (long|int): The time when the corresponding backup
            run was started.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "overwrite":'overwrite',
        "restore_childs_object_vec":'restoreChildsObjectVec',
        "restore_parent_object_vec":'restoreParentObjectVec',
        "run_start_time_usecs":'runStartTimeUsecs',
    }
    def __init__(self,
                 overwrite=None,
                 restore_childs_object_vec=None,
                 restore_parent_object_vec=None,
                 run_start_time_usecs=None,
            ):

        """Constructor for the SfdcRecoverJobParams class"""

        # Initialize members of the class
        self.overwrite = overwrite
        self.restore_childs_object_vec = restore_childs_object_vec
        self.restore_parent_object_vec = restore_parent_object_vec
        self.run_start_time_usecs = run_start_time_usecs

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
        overwrite = dictionary.get('overwrite')
        restore_childs_object_vec = dictionary.get("restoreChildsObjectVec")
        restore_parent_object_vec = dictionary.get("restoreParentObjectVec")
        run_start_time_usecs = dictionary.get('runStartTimeUsecs')

        # Return an object of this model
        return cls(
            overwrite,
            restore_childs_object_vec,
            restore_parent_object_vec,
            run_start_time_usecs
)