# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.map_reduce_instance_input_param
import cohesity_management_sdk.models.input_spec
import cohesity_management_sdk.models.output_spec
import cohesity_management_sdk.models.map_reduce_instance_run_info

class MapReduceInstance(object):

    """Implementation of the 'MapReduceInstance' model.

    Information about a Map reduce instance. An instance can be run only
    once.

    Attributes:
        id (int|long): System generated ID of map reduce instance.
        input_params (list of MapReduceInstance_InputParam): TODO:
            Add description here.
        input_spec (InputSpec): Input spec for the MR.
        map_reduce_info_id (int): ID of Map reduce info.
        output_spec (OutputSpec): Output spec for the MR.
        run_info (MapReduceInstance_RunInfo): Information about run of this
            instance. All fields of RunInfo will be populated b
             yoda/analytics components.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "input_params": 'inputParams',
        "input_spec": 'inputSpec',
        "map_reduce_info_id": 'mapReduceInfoId',
        "output_spec":'outputSpec',
        "run_info":'runInfo'
    }

    def __init__(self,
                 id=None,
                 input_params=None,
                 input_spec=None,
                 map_reduce_info_id=None,
                 output_spec=None,
                 run_info=None):
        """Constructor for the MapReduceInstance class"""

        # Initialize members of the class
        self.id = id
        self.input_params = input_params
        self.input_spec = input_spec
        self.map_reduce_info_id = map_reduce_info_id
        self.output_spec = output_spec
        self.run_info = run_info

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
        id = dictionary.get('id')
        input_params = None
        if dictionary.get('inputParams') != None:
            input_params = list()
            for structure in dictionary.get('inputParams'):
                input_params.append(cohesity_management_sdk.models.map_reduce_instance_input_param.MapReduceInstanceInputParam.from_dictionary(structure))
        input_spec = cohesity_management_sdk.models.input_spec.InputSpec.from_dictionary(dictionary.get('inputSpec')) if dictionary.get('inputSpec') else None
        map_reduce_info_id = dictionary.get('mapReduceInfoId')
        output_spec = cohesity_management_sdk.models.output_spec.OutputSpec.from_dictionary(dictionary.get('outputSpec')) if dictionary.get('outputSpec') else None
        run_info = cohesity_management_sdk.map_reduce_instance_run_info.MapReduceInstance_RunInfo.from_dictionary(dictionary.get('runInfo')) if dictionary.get('runInfo') else None

        # Return an object of this model
        return cls(id,
                   input_params,
                   input_spec,
                   map_reduce_info_id,
                   output_spec,
                   run_info)


