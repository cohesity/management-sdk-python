# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ApplicationParameters(object):

    """Implementation of the 'ApplicationParameters' model.

    TODO: type model description here.

    Attributes:
        truncate_exchange_log (bool): If true, after the Cohesity Cluster
            successfully captures a Snapshot during a Job Run, the Cluster
            truncates the Exchange transaction logs on a Microsoft Exchange
            Server. The default value is false.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "truncate_exchange_log":'truncateExchangeLog'
    }

    def __init__(self,
                 truncate_exchange_log=None):
        """Constructor for the ApplicationParameters class"""

        # Initialize members of the class
        self.truncate_exchange_log = truncate_exchange_log


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
        truncate_exchange_log = dictionary.get('truncateExchangeLog')

        # Return an object of this model
        return cls(truncate_exchange_log)


