# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class HiveConnectParams(object):

    """Implementation of the 'HiveConnectParams' model.

    Specifies an Object containing information about a registered Hive
    source.

    Attributes:
        metastore (string): Specifies the Hive metastore host.
        thrift_port (int): Specifies the Hive metastore thrift Port

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metastore": 'metastore',
        "thrift_port": 'thriftPort'
    }

    def __init__(self,
                 metastore=None,
                 thrift_port=None):
        """Constructor for the HiveConnectParams class"""

        # Initialize members of the class
        self.metastore = metastore
        self.thrift_port = thrift_port


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
        metastore = dictionary.get('metastore', None)
        thrift_port = dictionary.get('thriftPort', None)

        # Return an object of this model
        return cls(metastore,
                   thrift_port)


