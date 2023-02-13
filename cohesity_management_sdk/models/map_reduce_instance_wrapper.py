# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.map_reduce_instance

class MapReduceInstanceWrapper(object):

    """Implementation of the 'MapReduceInstanceWrapper' model.

    MapReduceInstanceWrapper is the struct containing the map reduce instance
    information along with the output file path information required to
    download the results set.

    Attributes:
        log_path (string): LogPath is the path of the log files for the MR
            instance run.
        mr_instance (MapReduceInstance): InstanceInfo is the information about
            the map reduce application instance.
        output_file_path_list (list of string): OutputFilePathList is the list
            containing the output files path suffix that Yoda uses to build
            the full path of the MR instance run output files.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "log_path":'logPath',
        "mr_instance":'mrInstance',
        "output_file_path_list":'outputFilePathList'
    }

    def __init__(self,
                 log_path=None,
                 mr_instance=None,
                 output_file_path_list=None):
        """Constructor for the MapReduceInstanceWrapper class"""

        # Initialize members of the class
        self.log_path = log_path
        self.mr_instance = mr_instance
        self.output_file_path_list = output_file_path_list


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
        log_path = dictionary.get('logPath')
        mr_instance = cohesity_management_sdk.models.map_reduce_instance.MapReduceInstance.from_dictionary(dictionary.get('mrInstance')) if dictionary.get('mrInstance') else None
        output_file_path_list = dictionary.get('outputFilePathList')

        # Return an object of this model
        return cls(log_path,
                   mr_instance,
                   output_file_path_list)


