# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

class APIException(Exception):

    """Class that handles HTTP Exceptions when fetching API Endpoints.

    Attributes:
        response_code (int): The status code of the response.
        context (HttpContext): The HttpContext of the API call.

    """

    def __init__(self,
                 reason,
                 context):
        """Constructor for the APIException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            context (HttpContext): The HttpContext of the API call.

        """
        super(APIException, self).__init__(reason)
        self.context = context
        self.response_code = context.response.status_code

#CohesityPatch
class ExpiredTokenException(APIException):
    pass
