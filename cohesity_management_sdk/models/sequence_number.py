# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SequenceNumber(object):

    """Implementation of the 'SequenceNumber' model.

    Sequence Number for each change for MongoDB Entity.

    Attributes:
        timestamp (long|int): Timestamp field of the change event.
            Mongodb associates each change with a timestamp type which is a 64
            bit value where:
            The most significant 32 bits are a time_t value (seconds since the
            Unix epoch), the least significant 32 bits are an incrementing
            ordinal for operations within a given second. Note that the
            timestamps of events are not consecutive numbers and also we can
            have multiple colocated changes entries for same timestamp.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "timestamp":'timestamp'
    }

    def __init__(self,
                 timestamp=None):
        """Constructor for the SequenceNumber class"""

        # Initialize members of the class
        self.timestamp = timestamp


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
        timestamp = dictionary.get('timestamp')

        # Return an object of this model
        return cls(timestamp)


