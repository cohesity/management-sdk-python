# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.map_reduce_instance_input_param
import cohesity_management_sdk.models.input_spec
import cohesity_management_sdk.models.output_spec

class RunMapReduceParams(object):

    """Implementation of the 'RunMapReduceParams' model.

     RunMapReduceParams specifies the input params to run a map reduce
    instance.

    Attributes:
        app_id (int):ApplicationId is the Id of the map reduce application to
            run.
        input_params (list of MapReduceInstanceInputParam): InputParams
            specifies optional list of key=value input params specified for
            running the map reduce instance.
        mr_input (InputSpec):InputSpecification specifies the input
            information to run the specific map reduce instance.
        mr_output (OutputSpec): OutputSpecification specifies the output
            information to run the specific map reduce instance.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_id":'appId',
        "input_params":'inputParams',
        "mr_input":'mrInput',
        "mr_output":'mrOutput'
    }

    def __init__(self,
                 app_id=None,
                 input_params=None,
                 mr_input=None,
                 mr_output=None):
        """Constructor for the RunMapReduceParams class"""

        # Initialize members of the class
        self.app_id = app_id
        self.input_params = input_params
        self.mr_input = mr_input
        self.mr_output = mr_output


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
        input_params = None
        if dictionary.get('inputParams', None) != None:
            input_params = list()
            for params in dictionary.get('inputParams'):
                input_params.append(cohesity_management_sdk.models.map_reduce_instance_input_param.MapReduceInstanceInputParam.from_dictionary(params))
        mr_input = cohesity_management_sdk.models.input_spec.InputSpec.from_dictionary(dictionary.get('mrInput')) if  dictionary.get('mrInput') else None
        mr_output = cohesity_management_sdk.models.output_spec.OutputSpec.from_dictionary(dictionary.get('mrOutput')) if dictionary.get('mrOutput') else None

        # Return an object of this model
        return cls(app_id,
                   input_params,
                   mr_input,
                   mr_output)


