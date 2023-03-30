# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class BannerIdData(object):

    """Implementation of the 'BannerIdData' model.

    Specifies id of a banner.

    Attributes:
        banner_id (string): Specifies a banner_id which can uniquely identify
            a banner. This may be the cluster_id, or the tenant_id, or the
            group_id, or the user SID etc.
            If this field is nil, the it is assumed to be the cluster_id.
            The content is stored against this 'row' in Scribe.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "banner_id":'bannerId'
    }

    def __init__(self,
                 banner_id=None):
        """Constructor for the BannerIdData class"""

        # Initialize members of the class
        self.banner_id = banner_id


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
        banner_id = dictionary.get('bannerId')

        # Return an object of this model
        return cls(banner_id)


