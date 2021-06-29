# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

from cohesity_management_sdk.api_helper import APIHelper
import cohesity_management_sdk.exceptions.api_exception

class RequestErrorErrorException(cohesity_management_sdk.exceptions.api_exception.APIException):
    def __init__(self, reason, context):
        """Constructor for the RequestErrorErrorException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            context (HttpContext):  The HttpContext of the API call.

        """
        super(RequestErrorErrorException, self).__init__(reason, context)
        dictionary = APIHelper.json_deserialize(self.context.response.raw_body)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.error_code = dictionary.get('errorCode')
        self.message = dictionary.get('message')
