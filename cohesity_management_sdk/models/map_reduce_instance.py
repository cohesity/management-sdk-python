# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.map_reduce_instance_input_param
import cohesity_management_sdk.models.input_selector_selects_the_files_to_map_over
import cohesity_management_sdk.models.output_specification_for_the_mapreduce
import cohesity_management_sdk.models.stores_the_progress_of_run_of_this_instance

class MapReduceInstance(object):

    """Implementation of the 'Map Reduce Instance.' model.

    Information about a Map reduce instance. An instance can be run only
    once.

    Attributes:
        id (long|int): System generated ID of map reduce instance.
        input_params (list of MapReduceInstanceInputParam): TODO: type
            description here.
        input_spec (InputSelectorSelectsTheFilesToMapOver): TODO: type
            description here.
        map_reduce_info_id (long|int): ID of Map reduce info.
        output_spec (OutputSpecificationForTheMapreduce): TODO: type
            description here.
        run_info (StoresTheProgressOfRunOfThisInstance): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "input_params":'inputParams',
        "input_spec":'inputSpec',
        "map_reduce_info_id":'mapReduceInfoId',
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
        input_spec = cohesity_management_sdk.models.input_selector_selects_the_files_to_map_over.InputSelectorSelectsTheFilesToMapOver.from_dictionary(dictionary.get('inputSpec')) if dictionary.get('inputSpec') else None
        map_reduce_info_id = dictionary.get('mapReduceInfoId')
        output_spec = cohesity_management_sdk.models.output_specification_for_the_mapreduce.OutputSpecificationForTheMapreduce.from_dictionary(dictionary.get('outputSpec')) if dictionary.get('outputSpec') else None
        run_info = cohesity_management_sdk.models.stores_the_progress_of_run_of_this_instance.StoresTheProgressOfRunOfThisInstance.from_dictionary(dictionary.get('runInfo')) if dictionary.get('runInfo') else None

        # Return an object of this model
        return cls(id,
                   input_params,
                   input_spec,
                   map_reduce_info_id,
                   output_spec,
                   run_info)


