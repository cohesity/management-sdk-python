# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.share

class GetViewsByShareNameResult(object):

    """Implementation of the 'GetViewsByShareNameResult' model.

    Specifies the list of Views and Aliases by share name that matched the
    specified filter criteria.

    Attributes:
        pagination_cookie (string): If set, i.e. there are more results to
            display, use this value to get the next set of results, by using
            this value in paginationCookie param for the next request to
            GetViewsByShare.
        shares_list (list of Share): Array of Views and Aliases by Share name.
            Specifies the list of Views returned in this response.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pagination_cookie":'paginationCookie',
        "shares_list":'sharesList'
    }

    def __init__(self,
                 pagination_cookie=None,
                 shares_list=None):
        """Constructor for the GetViewsByShareNameResult class"""

        # Initialize members of the class
        self.pagination_cookie = pagination_cookie
        self.shares_list = shares_list


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
        pagination_cookie = dictionary.get('paginationCookie')
        shares_list = None
        if dictionary.get('sharesList') != None:
            shares_list = list()
            for structure in dictionary.get('sharesList'):
                shares_list.append(cohesity_management_sdk.models.share.Share.from_dictionary(structure))

        # Return an object of this model
        return cls(pagination_cookie,
                   shares_list)


