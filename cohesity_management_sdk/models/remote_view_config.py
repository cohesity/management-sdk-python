# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RemoteViewConfig(object):

    """Implementation of the 'RemoteViewConfig' model.

    Specifies the remote view config for a view protected in a view job. This
    field is only used when the view job has a replication policy.

    Attributes:
        source_view_id (long|int): Specifies the view Id of the view protected by the
            view protection job.
        use_same_view_name (bool): Specifies if the remote view name is same
            as the source view name. If this field is true, viewName is
            ignored as the remote view name is same as the source view name.
        view_name (string): Specifies the remote view name of the view
            protected by a view protection job. If UseSameViewName is set to
            false, this field provides the remote view name to be used in the
            remote cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "source_view_id":'sourceViewId',
        "use_same_view_name":'useSameViewName',
        "view_name":'viewName'
    }

    def __init__(self,
                 source_view_id=None,
                 use_same_view_name=None,
                 view_name=None):
        """Constructor for the RemoteViewConfig class"""

        # Initialize members of the class
        self.source_view_id = source_view_id
        self.use_same_view_name = use_same_view_name
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
        source_view_id = dictionary.get('sourceViewId')
        use_same_view_name = dictionary.get('useSameViewName')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(source_view_id,
                   use_same_view_name,
                   view_name)


