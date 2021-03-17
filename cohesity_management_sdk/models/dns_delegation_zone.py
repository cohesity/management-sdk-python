# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.


class DnsDelegationZone(object):

    """Implementation of the 'DnsDelegationZone' model.

    IP Range for range of vip address addition.

    Attributes:
        dns_zone_name (string): Specifies the dns zone name.
        dns_zone_vips (list of string): Specifies list of vips part of dns
            delegation zone.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dns_zone_name": 'dnsZoneName',
        "dns_zone_vips": 'dnsZoneVips'
    }

    def __init__(self,
                 dns_zone_name=None,
                 dns_zone_vips=None):
        """Constructor for the DnsDelegationZone class"""

        # Initialize members of the class
        self.dns_zone_name = dns_zone_name
        self.dns_zone_vips = dns_zone_vips


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
        dns_zone_name = dictionary.get('dnsZoneName', None)
        dns_zone_vips = dictionary.get('dnsZoneVips', None)

        # Return an object of this model
        return cls(dns_zone_name,
                   dns_zone_vips)


