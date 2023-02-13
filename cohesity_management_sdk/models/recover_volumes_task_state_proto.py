# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.recover_volumes_params
import cohesity_management_sdk.models.recover_volumes_task_state_proto_task_result

class RecoverVolumesTaskStateProto(object):

    """Implementation of the 'RecoverVolumesTaskStateProto' model.

    TODO: type model description here.

    Attributes:
        params (RecoverVolumesParams): TODO: type description here.
        task_result_vec (list of RecoverVolumesTaskStateProtoTaskResult):
            Contains high-level per-volume information. This data is here
            because Iris cannot see into protobuf extensions yet needs to
            display per-subtask progress.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "params":'params',
        "task_result_vec":'taskResultVec'
    }

    def __init__(self,
                 params=None,
                 task_result_vec=None):
        """Constructor for the RecoverVolumesTaskStateProto class"""

        # Initialize members of the class
        self.params = params
        self.task_result_vec = task_result_vec


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
        params = cohesity_management_sdk.models.recover_volumes_params.RecoverVolumesParams.from_dictionary(dictionary.get('params')) if dictionary.get('params') else None
        task_result_vec = None
        if dictionary.get('taskResultVec') != None:
            task_result_vec = list()
            for structure in dictionary.get('taskResultVec'):
                task_result_vec.append(cohesity_management_sdk.models.recover_volumes_task_state_proto_task_result.RecoverVolumesTaskStateProtoTaskResult.from_dictionary(structure))

        # Return an object of this model
        return cls(params,
                   task_result_vec)


