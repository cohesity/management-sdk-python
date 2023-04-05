# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto


class DataTransferInfo_PrivateNetworkInfo(object):

    """Implementation of the 'DataTransferInfo_PrivateNetworkInfo' model.

    TODO: type description here.


    Attributes:

        location (string): Region/location of the virtual network.
        region (EntityProto): Proto of the region of the virtual network.
        subnet (EntityProto): Subnet in which we will create a private
            endpoint.
        vpn (EntityProto): Vitual network in which we will create a private
            endpoint.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "location":'location',
        "region":'region',
        "subnet":'subnet',
        "vpn":'vpn',
    }
    def __init__(self,
                 location=None,
                 region=None,
                 subnet=None,
                 vpn=None,
            ):

        """Constructor for the DataTransferInfo_PrivateNetworkInfo class"""

        # Initialize members of the class
        self.location = location
        self.region = region
        self.subnet = subnet
        self.vpn = vpn

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
        location = dictionary.get('location')
        region = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('region')) if dictionary.get('region') else None
        subnet = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('subnet')) if dictionary.get('subnet') else None
        vpn = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('vpn')) if dictionary.get('vpn') else None

        # Return an object of this model
        return cls(
            location,
            region,
            subnet,
            vpn
)