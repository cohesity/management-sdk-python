# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IcapConnectionStatusResponse(object):

    """Implementation of the 'IcapConnectionStatusResponse' model.

    Specifies Icap server connection status response.

    Attributes:
        failed_connection_status (list of string): Specifies the failed
            connection status of Icap servers.
        succeeded_connection_status (list of string): Specifies the success
            connection status of Icap servers.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "failed_connection_status":'failedConnectionStatus',
        "succeeded_connection_status":'succeededConnectionStatus'
    }

    def __init__(self,
                 failed_connection_status=None,
                 succeeded_connection_status=None):
        """Constructor for the IcapConnectionStatusResponse class"""

        # Initialize members of the class
        self.failed_connection_status = failed_connection_status
        self.succeeded_connection_status = succeeded_connection_status


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
        failed_connection_status = dictionary.get('failedConnectionStatus')
        succeeded_connection_status = dictionary.get('succeededConnectionStatus')

        # Return an object of this model
        return cls(failed_connection_status,
                   succeeded_connection_status)


