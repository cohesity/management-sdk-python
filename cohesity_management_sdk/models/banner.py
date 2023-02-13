# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Banner(object):

    """Implementation of the 'Banner' model.

    Banner is used for storing the banner content in scribe and also for
    transferring it over the wire.

    Attributes:
        banner_id (string): Specifies a banner_id which can uniquely identify
            a banner. This may be the cluster_id, or the tenant_id, or the
            group_id, or the user SID etc.
            If this field is nil, the it is assumed to be the cluster_id.
            The content is stored against this 'row' in Scribe.
        content (string): Specifies the content of the banner.
        created_time_msecs (int|long): createdTimeMsecs field is deprecated.
            Timestamp at which banner was created.
        description (string): description field is deprecated. Specifies the
            description of this banner.
        last_updated_time_msecs (int|long): lastUpdatedTimeMsecs field is
            deprecated. Timestamp at which banner was last updated.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "banner_id": 'bannerId',
        "content": 'content',
        "created_time_msecs": 'createdTimeMsecs',
        "description": 'description',
        "last_updated_time_msecs":'lastUpdatedTimeMsecs'
    }

    def __init__(self,
                 banner_id=None,
                 content=None,
                 created_time_msecs=None,
                 description=None,
                 last_updated_time_msecs=None):
        """Constructor for the Banner class"""

        # Initialize members of the class
        self.banner_id = banner_id
        self.content = content
        self.created_time_msecs = created_time_msecs
        self.description = description
        self.last_updated_time_msecs = last_updated_time_msecs

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
        content = dictionary.get('content')
        created_time_msecs = dictionary.get('createdTimeMsecs')
        description = dictionary.get('description')
        last_updated_time_msecs = dictionary.get('lastUpdatedTimeMsecs')

        # Return an object of this model
        return cls(banner_id,
                   content,
                   created_time_msecs,
                   description,
                   last_updated_time_msecs)


