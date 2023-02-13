# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TapeMediaInformation(object):

    """Implementation of the 'TapeMediaInformation' model.

    Provides information about a single tape media in a QStar Archive Vault.

    Attributes:
        barcode (string): Specifies a unique identifier for the media.
        location (string): Specifies the location of the offline media as
            recorded by the backup administrator using media management
            software.
        online (bool): Specifies a flag that indicates if the media is online
            or offline. Offline media must be manually loaded into the media
            library before a recovery can occur.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "barcode":'barcode',
        "location":'location',
        "online":'online'
    }

    def __init__(self,
                 barcode=None,
                 location=None,
                 online=None):
        """Constructor for the TapeMediaInformation class"""

        # Initialize members of the class
        self.barcode = barcode
        self.location = location
        self.online = online


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
        barcode = dictionary.get('barcode')
        location = dictionary.get('location')
        online = dictionary.get('online')

        # Return an object of this model
        return cls(barcode,
                   location,
                   online)


