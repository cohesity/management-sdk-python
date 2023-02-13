# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NetappClusterInfo(object):

    """Implementation of the 'NetappClusterInfo' model.

    Specifies information about a NetApp Cluster Protection Source.

    Attributes:
        contact_info (string): Specifies information about the contact for the
            NetApp cluster such as a name, phone number, and email address.
        location (string): Specifies where this NetApp cluster is located.
            This location identification string is configured by the NetApp
            system administrator. This field does not contain the NetApp
            cluster hostname or IP address.
        serial_number (string): Specifies the serial number of the NetApp
            cluster in the format: x-xx-xxxxxx.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "contact_info":'contactInfo',
        "location":'location',
        "serial_number":'serialNumber'
    }

    def __init__(self,
                 contact_info=None,
                 location=None,
                 serial_number=None):
        """Constructor for the NetappClusterInfo class"""

        # Initialize members of the class
        self.contact_info = contact_info
        self.location = location
        self.serial_number = serial_number


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
        contact_info = dictionary.get('contactInfo')
        location = dictionary.get('location')
        serial_number = dictionary.get('serialNumber')

        # Return an object of this model
        return cls(contact_info,
                   location,
                   serial_number)


