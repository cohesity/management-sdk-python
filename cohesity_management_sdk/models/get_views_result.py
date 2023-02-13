# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.view

class GetViewsResult(object):

    """Implementation of the 'GetViewsResult' model.

    Specifies the list of Views returned that matched the specified filter
    criteria.

    Attributes:
        last_result (bool): If false, more Views are available to return. If
            the number of Views to return exceeds the number of Views
            specified in maxCount (default of 1000) of the original GET
            /public/views request, the first set of Views are returned and
            this field returns false. To get the next set of Views, in the
            next GET /public/views request send the last id from the previous
            viewList.
        views (list of View): Array of Views.  Specifies the list of Views
            returned in this response. The list is sorted by decreasing View
            ids.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_result":'lastResult',
        "views":'views'
    }

    def __init__(self,
                 last_result=None,
                 views=None):
        """Constructor for the GetViewsResult class"""

        # Initialize members of the class
        self.last_result = last_result
        self.views = views


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
        last_result = dictionary.get('lastResult')
        views = None
        if dictionary.get('views') != None:
            views = list()
            for structure in dictionary.get('views'):
                views.append(cohesity_management_sdk.models.view.View.from_dictionary(structure))

        # Return an object of this model
        return cls(last_result,
                   views)


