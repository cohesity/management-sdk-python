# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CdpIoFilterState(object):

    """Implementation of the 'CdpIoFilterState' model.

    CdpIoFilterState specifies the current state of the CDP IO Filter for a
    single Protection Source.

    Attributes:
        error_message (string): Specifies the message of the error, which was
            encountered duing the last upgrade. If this is specified, then it
            means that the last upgrade failed.
        filter_status (string): Specifies the current status of the IO Filter.
          See magneto/base/entities.proto > IgrOFilterState > FilterStatus
        upgradability (string): Specifies the current upgradability status of
            the IO Filter.
            See magneto/base/common.proto > Upgradability
        version (string): Specifies the current version of the IO filter.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_message":'errorMessage',
        "filter_status":'filterStatus',
        "upgradability":'upgradability',
        "version":'version'
    }

    def __init__(self,
                 error_message=None,
                 filter_status=None,
                 upgradability=None,
                 version=None):
        """Constructor for the CdpIoFilterState class"""

        # Initialize members of the class
        self.error_message = error_message
        self.filter_status = filter_status
        self.upgradability = upgradability
        self.version = version


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
        error_message = dictionary.get('errorMessage')
        filter_status = dictionary.get('filterStatus')
        upgradability = dictionary.get('upgradability')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(error_message,
                   filter_status,
                   upgradability,
                   version)


