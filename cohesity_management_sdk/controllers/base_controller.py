# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.
import json
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.http.http_context import HttpContext
from cohesity_management_sdk.http.requests_client import RequestsClient
from cohesity_management_sdk.exceptions.api_exception import APIException, ExpiredTokenException


class BaseController(object):
    """All controllers inherit from this base class.

    Attributes:
        http_client (HttpClient): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an HttpRequest.
        global_headers (dict): The global headers of the API which are sent with
            every request.

    """

    http_client = RequestsClient()

    http_call_back = None


    global_headers = {'user-agent': 'cohesity-python/1.9.2'}

    def __init__(self, config=None, client=None, call_back=None):
        if client != None:
            self.http_client = client
        if call_back != None:
            self.http_call_back = call_back

    def validate_parameters(self, **kwargs):
        """Validates required parameters of an endpoint.

        Args:
            kwargs (dict): A dictionary of the required parameters.

        """
        for name, value in kwargs.items():
            if value is None:
                raise ValueError(
                    "Required parameter {} cannot be None.".format(name))

    def execute_request(self, request, binary=False, name=None):
        """Executes an HttpRequest.

        Args:
            request (HttpRequest): The HttpRequest to execute.
            binary (bool): A flag which should be set to True if
                a binary response is expected.

        Returns:
            HttpContext: The HttpContext of the request. It contains,
                both, the request itself and the HttpResponse object.

        """
        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.logger.info(
                "Calling the on_before_request method of http_call_back for {}."
                .format(name))
            self.http_call_back.on_before_request(request)

        # Add global headers to request
        self.logger.info(
            "Merging global headers with endpoint headers for {}.".format(
                name))
        request.headers = APIHelper.merge_dicts(self.global_headers,
                                                request.headers)

        # Invoke the API call to fetch the response.
        self.logger.debug("Raw request for {} is: {}".format(
            name, vars(request)))
        func = self.http_client.execute_as_binary if binary else self.http_client.execute_as_string
        response = func(request)
        self.logger.debug("Raw response for {} is: {}".format(
            name, vars(response)))
        self.logger.info(
            "Wrapping request and response in a context object for {}.".format(
                name))
        context = HttpContext(request, response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.logger.info(
                "Calling on_after_response method of http_call_back for {}.".
                format(name))
            self.http_call_back.on_after_response(context)

        return context

    def validate_response(self, context):
        """Validates an HTTP response by checking for global errors.

        Args:
            context (HttpContext): The HttpContext of the API call.

        """
        #CohesityPatch
        if (context.response.status_code < 200) or (
                context.response.status_code > 208):  # [200,208] = HTTP OK
            status = context.response.status_code
            message = json.loads(context.response.raw_body)['message']
            raise_except = APIException(
                'Response status code: %s, Response message: %s' %
                (status, message), context)
            if context.response.status_code == 401 and \
                    json.loads(context.response.raw_body)['errorCode'] == 'KStatusUnauthorized' and \
                    json.loads(context.response.raw_body)['message'] == "The access token is invalid.":
                raise_except = ExpiredTokenException(
                    'Response status code: %s, Response message: %s' %
                    (status, message), context)
            raise raise_except
