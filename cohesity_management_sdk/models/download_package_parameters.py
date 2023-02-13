# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DownloadPackageParameters(object):

    """Implementation of the 'DownloadPackageParameters' model.

    Specifies the parameters needed for a request to download a new software
    package to a Cluster.

    Attributes:
        url (string): Specifies a URL from which the package can be downloaded
            to the Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url":'url'
    }

    def __init__(self,
                 url=None):
        """Constructor for the DownloadPackageParameters class"""

        # Initialize members of the class
        self.url = url


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
        url = dictionary.get('url')

        # Return an object of this model
        return cls(url)


