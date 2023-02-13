# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.label_selector_match_labels_entry

class LabelSelector(object):

    """Implementation of the 'LabelSelector' model.

    Attributes:
        match_labels (list of LabelSelector_MatchLabelsEntry): This field is
            an object which consists of key-value pairs
            of all labels that must be matched by the selector
        name (string): Select all objects which have a label with
            key : "name" and value specified by this field.
        service_name (string): Select all objects which have a label with.
            key: "serviceName" and value as specified by this field.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "match_labels":'matchLabels',
        "name":'name',
        "service_name":'serviceName'
    }

    def __init__(self,
                 match_labels=None,
                 name=None,
                 service_name=None):
        """Constructor for the LabelSelector class"""

        # Initialize members of the class
        self.match_labels = match_labels
        self.name = name
        self.service_name = service_name


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
        match_labels = None
        if dictionary.get('matchLabels'):
            match_labels = list()
            for structure in dictionary.get('matchLabels'):
                match_labels.append(cohesity_management_sdk.models.label_selector_match_labels_entry.LabelSelector_MatchLabelsEntry.from_dictionary(structure))
        name = dictionary.get('name')
        service_name = dictionary.get('serviceName')

        # Return an object of this model
        return cls(match_labels,
                   name,
                   service_name)


