# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PodInfo_PodSpec_VolumeInfo_Flocker(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_Flocker' model.

    Flocker Volumes.

    Attributes:
        dataset_name (string): TODO: Type description here.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dataset_name":'datasetName'
    }

    def __init__(self,
                 dataset_name=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_Flocker class"""

        # Initialize members of the class
        self.dataset_name = dataset_name


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
        dataset_name = dictionary.get('datasetName')

        # Return an object of this model
        return cls(dataset_name)


