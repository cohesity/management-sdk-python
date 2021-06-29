# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

class HttpContext(object):

    """An HTTP Context that contains both the original HttpRequest
    object that intitiated the call and the HttpResponse object that
    is the result of the call.

    Attributes:
        request (HttpRequest): The original request object.
        response (HttpResponse): The returned response object after
            executing the request. Note that this may be None
            depending on if and when an error occurred.

    """

    def __init__(self,
                 request,
                 response):
        """Constructor for the HttpContext class

        Args:
            request (HttpRequest): The HTTP Request.
            response (HttpResponse): The HTTP Response.

        """
        self.request = request
        self.response = response
