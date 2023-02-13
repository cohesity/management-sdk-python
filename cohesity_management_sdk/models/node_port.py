# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NodePort(object):

    """Implementation of the 'NodePort' model.

    VmInfo specifies information of a NodePort per service and port
    combination within an application instance.

    Attributes:
        is_ui_port (bool): TODO: type description here.
        port (int): TODO: type description here.
        tag (TagEnum): Specifies use of the nodeport kDefault - No specific
            service. kHttp - HTTP server. kHttps -  Secure HTTP server. kSsh -
            Secure shell server.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_ui_port":'isUiPort',
        "port":'port',
        "tag":'tag'
    }

    def __init__(self,
                 is_ui_port=None,
                 port=None,
                 tag=None):
        """Constructor for the NodePort class"""

        # Initialize members of the class
        self.is_ui_port = is_ui_port
        self.port = port
        self.tag = tag


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
        is_ui_port = dictionary.get('isUiPort')
        port = dictionary.get('port')
        tag = dictionary.get('tag')

        # Return an object of this model
        return cls(is_ui_port,
                   port,
                   tag)


