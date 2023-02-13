# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ExchangeRestoreViewParameters(object):

    """Implementation of the 'ExchangeRestoreViewParameters' model.


    Attributes:
        endpoint (bool): Specifies whether we should white-list the restore
            view for all the IP addresses. If this parameter is set to false,
            then only the machine on which the view is mounted will be
            white-listed.
        mount_point (string): Specifies the path of the SMB share.
        view_name (string): Specifies the view to which the files of an
            Exchange database has to be cloned.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "endpoint":'endpoint',
        "mount_point":'mountPoint',
        "view_name":'viewName'
    }

    def __init__(self,
                 endpoint=None,
                 mount_point=None,
                 view_name=None):
        """Constructor for the ExchangeRestoreViewParameters class"""

        # Initialize members of the class
        self.endpoint = endpoint
        self.mount_point = mount_point
        self.view_name = view_name


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
        endpoint = dictionary.get('endpoint')
        mount_point = dictionary.get('mountPoint')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(endpoint,
                   mount_point,
                   view_name)


