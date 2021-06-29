# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.


class LifecycleConfigProto(object):

    """Implementation of the 'LifecycleConfigProto' model.

    Protobuf that describes the lifecycle configuration that is used to manage
    the lifecycle of objects in a bucket.

    """

    # Create a mapping from Model property names to API property names
    _names = {
    }

    def __init__(self):
        """Constructor for the LifecycleConfigProto class"""

        # Initialize members of the class
        pass


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

        # Return an object of this model
        return cls()


